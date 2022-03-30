# TODO: finish docs
#
# Conditional build:
%bcond_with	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (need rust configured)

Summary:	Setuptools plugin to build Rust Python extensions
Summary(pl.UTF-8):	Wtyczka setuptools do budowania rozszerzeń pythonowych w języku Rust
Name:		python3-setuptools_rust
Version:	0.12.1
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/setuptools-rust/
Source0:	https://pypi.debian.net/setuptools_rust/setuptools-rust-%{version}.tar.gz
# Source0-md5:	33c3fd3bcde2877483ab782353bee54c
URL:		https://rusthub.com/msabramo/setuptools-rust
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools >= 1:46.1
BuildRequires:	python3-setuptools_scm >= 3.4.3
BuildRequires:	python3-toml >= 0.9.0
%if %{with tests}
BuildRequires:	rust-core
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-m2r2
BuildRequires:	python3-sphinx_autodoc_typehints
BuildRequires:	python3-sphinx_rtd_theme
BuildRequires:	sphinx-pdg-3
%endif
Requires:	cargo
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Compile and distribute Python extensions written in Rust as easily as
if they were written in C.

%description -l pl.UTF-8
Kompilownie i dystrybuowanie napisanych w języku Rust rozszerzeń
Pythona tak łatwo, jakby były napisane w C.

%prep
%setup -q -n setuptools-rust-%{version}

%build
%py3_build %{?with_tests:test}

%if %{with doc}
%{__make} -C docs html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%{py3_sitescriptdir}/setuptools_rust
%{py3_sitescriptdir}/setuptools_rust-%{version}-py*.egg-info
