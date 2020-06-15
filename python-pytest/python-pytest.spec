# Created by pyp2rpm-3.3.4
%global pypi_name pytest

Name:           python-%{pypi_name}
Version:        5.4.3
Release:        1%{?dist}
Summary:        pytest: simple powerful testing with Python

License:        MIT license
URL:            https://docs.pytest.org/en/latest/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(argcomplete)
BuildRequires:  python3dist(atomicwrites) >= 1
BuildRequires:  python3dist(attrs) >= 17.4
BuildRequires:  python3dist(colorama)
BuildRequires:  python3dist(hypothesis) >= 3.56
BuildRequires:  python3dist(importlib-metadata) >= 0.12
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(more-itertools) >= 4
BuildRequires:  python3dist(mypy) = 0.761
BuildRequires:  python3dist(nose)
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pathlib2) >= 2.2
BuildRequires:  (python3dist(pluggy) >= 0.12 with python3dist(pluggy) < 1)
BuildRequires:  python3dist(py) >= 1.5
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools) >= 40
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(wcwidth)
BuildRequires:  python3dist(xmlschema)
BuildRequires:  python3dist(sphinx)

%description
 :alt: Code coverage Status

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(argcomplete)
Requires:       python3dist(atomicwrites) >= 1
Requires:       python3dist(attrs) >= 17.4
Requires:       python3dist(colorama)
Requires:       python3dist(hypothesis) >= 3.56
Requires:       python3dist(importlib-metadata) >= 0.12
Requires:       python3dist(mock)
Requires:       python3dist(more-itertools) >= 4
Requires:       python3dist(mypy) = 0.761
Requires:       python3dist(nose)
Requires:       python3dist(packaging)
Requires:       python3dist(pathlib2) >= 2.2
Requires:       (python3dist(pluggy) >= 0.12 with python3dist(pluggy) < 1)
Requires:       python3dist(py) >= 1.5
Requires:       python3dist(requests)
Requires:       python3dist(setuptools)
Requires:       python3dist(wcwidth)
Requires:       python3dist(xmlschema)
%description -n python3-%{pypi_name}
 :alt: Code coverage Status

%package -n python-%{pypi_name}-doc
Summary:        pytest documentation
%description -n python-%{pypi_name}-doc
Documentation for pytest

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 doc/en html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE doc/en/_themes/LICENSE doc/en/license.rst
%doc README.rst changelog/README.rst testing/example_scripts/README.rst
%{_bindir}/py.test
%{_bindir}/pytest
%{python3_sitelib}/_pytest
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE doc/en/_themes/LICENSE doc/en/license.rst

%changelog
* Mon Jun 15 2020 Tyler Griffiths <t@tyjgr.com> - 5.4.3-1
- Initial package.
