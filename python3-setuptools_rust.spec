# TODO: finish docs
#
# Conditional build:
%bcond_with	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (need rust configured)

Summary:	Setuptools plugin to build Rust Python extensions
Summary(pl.UTF-8):	Wtyczka setuptools do budowania rozszerzeń pythonowych w języku Rust
Name:		python3-setuptools_rust
Version:	1.11.1
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/setuptools-rust/
Source0:	https://pypi.debian.net/setuptools_rust/setuptools_rust-%{version}.tar.gz
# Source0-md5:	cc5c2cf6828af473951295d9f33bcf33
URL:		https://rusthub.com/msabramo/setuptools-rust
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	python3-setuptools >= 1:62.4
BuildRequires:	python3-setuptools_scm >= 3.4.3
%if %{with tests}
BuildRequires:	rust-core
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-furo >= 2024
BuildRequires:	python3-myst_parser >= 4
BuildRequires:	python3-sphinx_autodoc_typehints >= 3.1.0
BuildRequires:	sphinx-pdg-3 >= 8.2.3
%endif
Requires:	cargo
Requires:	python3-modules >= 1:3.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Compile and distribute Python extensions written in Rust as easily as
if they were written in C.

%description -l pl.UTF-8
Kompilownie i dystrybuowanie napisanych w języku Rust rozszerzeń
Pythona tak łatwo, jakby były napisane w C.

%prep
%setup -q -n setuptools_rust-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%if %{with doc}
%{__make} -C docs html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%{py3_sitescriptdir}/setuptools_rust
%{py3_sitescriptdir}/setuptools_rust-%{version}.dist-info
