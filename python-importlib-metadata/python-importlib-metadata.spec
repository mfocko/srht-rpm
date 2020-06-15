# Created by pyp2rpm-3.3.4
%global pypi_name importlib_metadata

Name:           python-%{pypi_name}
Version:        1.6.1
Release:        1%{?dist}
Summary:        Read metadata from Python packages

License:        Apache Software License
URL:            http://importlib-metadata.readthedocs.io/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(configparser) >= 3.5
BuildRequires:  python3dist(contextlib2)
BuildRequires:  python3dist(importlib-resources) >= 1.3
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pathlib2)
BuildRequires:  python3dist(pep517)
BuildRequires:  python3dist(rst.linker)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(zipp) >= 0.5
BuildRequires:  python3dist(sphinx)

%description
 importlib_metadata importlib_metadata is a library to access the metadata for
a Python package. It is intended to be ported to Python 3.8.See the online
documentation < for usage details.Finder authors < can also add support for
custom package installers. See the above documentation for details.This project
primarily supports third-party packages installed by PyPA tools (or other
conforming...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(configparser) >= 3.5
Requires:       python3dist(contextlib2)
Requires:       python3dist(importlib-resources) >= 1.3
Requires:       python3dist(packaging)
Requires:       python3dist(pathlib2)
Requires:       python3dist(pep517)
Requires:       python3dist(rst.linker)
Requires:       python3dist(sphinx)
Requires:       python3dist(zipp) >= 0.5
%description -n python3-%{pypi_name}
 importlib_metadata importlib_metadata is a library to access the metadata for
a Python package. It is intended to be ported to Python 3.8.See the online
documentation < for usage details.Finder authors < can also add support for
custom package installers. See the above documentation for details.This project
primarily supports third-party packages installed by PyPA tools (or other
conforming...

%package -n python-%{pypi_name}-doc
Summary:        importlib_metadata documentation
%description -n python-%{pypi_name}-doc
Documentation for importlib_metadata

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 importlib_metadata/docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Mon Jun 15 2020 Tyler Griffiths <t@tyjgr.com> - 1.6.1-1
- Initial package.
