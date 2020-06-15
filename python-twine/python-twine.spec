# Created by pyp2rpm-3.3.4
%global pypi_name twine

Name:           python-%{pypi_name}
Version:        3.1.1
Release:        1%{?dist}
Summary:        Collection of utilities for publishing packages on PyPI

License:        None
URL:            https://twine.readthedocs.io/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(importlib-metadata)
BuildRequires:  python3dist(keyring) >= 15.1
BuildRequires:  python3dist(pkginfo) >= 1.4.2
BuildRequires:  python3dist(readme-renderer) >= 21
BuildRequires:  python3dist(requests) >= 2.20
BuildRequires:  (python3dist(requests-toolbelt) >= 0.8 with (python3dist(requests-toolbelt) < 0.9 or python3dist(requests-toolbelt) > 0.9))
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools) >= 0.7
BuildRequires:  python3dist(setuptools-scm) >= 1.15
BuildRequires:  python3dist(tqdm) >= 4.14
BuildRequires:  python3dist(sphinx)

%description
 twine .. rtd-inclusion-marker-do-not-removeTwine is a utility_ for publishing_
Python packages on PyPI_.It provides build system independent uploads of source
and binary

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(importlib-metadata)
Requires:       python3dist(keyring) >= 15.1
Requires:       python3dist(pkginfo) >= 1.4.2
Requires:       python3dist(readme-renderer) >= 21
Requires:       python3dist(requests) >= 2.20
Requires:       (python3dist(requests-toolbelt) >= 0.8 with (python3dist(requests-toolbelt) < 0.9 or python3dist(requests-toolbelt) > 0.9))
Requires:       python3dist(setuptools)
Requires:       python3dist(setuptools) >= 0.7
Requires:       python3dist(tqdm) >= 4.14
%description -n python3-%{pypi_name}
 twine .. rtd-inclusion-marker-do-not-removeTwine is a utility_ for publishing_
Python packages on PyPI_.It provides build system independent uploads of source
and binary

%package -n python-%{pypi_name}-doc
Summary:        twine documentation
%description -n python-%{pypi_name}-doc
Documentation for twine

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/twine
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Mon Jun 15 2020 Tyler Griffiths <t@tyjgr.com> - 3.1.1-1
- Initial package.
