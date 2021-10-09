#
# Conditional build:
%bcond_with	tests	# unit tests (need rust configured)
%bcond_with	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Setuptools plugin to build Rust Python extensions
Summary(pl.UTF-8):	Wtyczka setuptools do budowania rozszerzeń pythonowych Rust
Name:		python3-setuptools_rust
Version:	0.12.1
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/setuptools-rust/
Source0:	https://pypi.debian.net/setuptools_rust/setuptools-rust-%{version}.tar.gz
# Source0-md5:	33c3fd3bcde2877483ab782353bee54c
URL:		https://rusthub.com/msabramo/setuptools-rust
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools >= 1:46.0
BuildRequires:	python3-setuptools_scm
%endif
%if %{with tests}
BuildRequires:	rust-core
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	cargo
Requires:	python3-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Compile and distribute Python extensions written in Rust as easily as if they were written in C.

%prep
%setup -q -n setuptools-rust-%{version}

%build
%py3_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md
%{py3_sitescriptdir}/setuptools_rust
%{py3_sitescriptdir}/setuptools_rust-%{version}-py*.egg-info
