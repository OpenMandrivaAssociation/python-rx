# what it's called on pypi
%global srcname Rx
# what it's imported as
%global libname rx
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{libname}

%global _description \
Rx is a library for composing asynchronous and event-based programs using\
observable collections and LINQ-style query operators in Python.

%bcond_without tests


Name:           python-%{pkgname}
Version:        3.1.1
Release:        2
Summary:        Reactive Extensions (Rx) for Python
License:        ASL 2.0
URL:            https://github.com/ReactiveX/RxPY
# PyPI tarball doesn't have tests
Source0:        %{url}/archive/v%{version}/RxPY-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-coverage
BuildRequires:  python-devel
BuildRequires:  python-pytest
BuildRequires:  python-pytest-asyncio
BuildRequires:  python-pytest-runner
BuildRequires:  python-setuptools
%{?python_provide:%python_provide python-%{pkgname}}

%description %{_description}

%prep
%autosetup -n RxPY-%{version}
rm -rf %{eggname}.egg-info

%build
%py_build

%install
%py_install



%files
%license LICENSE
%doc README.rst authors.txt changes.md
%{python_sitelib}/%{libname}
%{python_sitelib}/%{eggname}-%{version}-py%{python_version}.egg-info
