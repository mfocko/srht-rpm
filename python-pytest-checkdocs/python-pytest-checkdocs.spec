# Created by pyp2rpm-3.3.4
%global pypi_name pytest-checkdocs

Name:           python-%{pypi_name}
Version:        2.1.1
Release:        1%{?dist}
Summary:        check the README when running tests

License:        None
URL:            https://github.com/jaraco/pytest-checkdocs
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(docutils) >= 0.15
BuildRequires:  python3dist(importlib-metadata) >= 0.21
BuildRequires:  python3dist(jaraco.packaging) >= 3.2
BuildRequires:  python3dist(more-itertools)
BuildRequires:  (python3dist(pytest) >= 3.5 with (python3dist(pytest) < 3.7.3 or python3dist(pytest) > 3.7.3))
BuildRequires:  python3dist(pytest-black) >= 0.3.7
BuildRequires:  python3dist(pytest-checkdocs) >= 1.2.3
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-flake8)
BuildRequires:  python3dist(pytest-mypy)
BuildRequires:  python3dist(rst.linker) >= 1.9
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm) >= 3.4.1
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx)

%description
 :target: PyPI link_ :target: PyPI link_.. _PyPI link: .. image::

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(docutils) >= 0.15
Requires:       python3dist(importlib-metadata) >= 0.21
Requires:       python3dist(jaraco.packaging) >= 3.2
Requires:       python3dist(more-itertools)
Requires:       (python3dist(pytest) >= 3.5 with (python3dist(pytest) < 3.7.3 or python3dist(pytest) > 3.7.3))
Requires:       python3dist(pytest-black) >= 0.3.7
Requires:       python3dist(pytest-checkdocs) >= 1.2.3
Requires:       python3dist(pytest-cov)
Requires:       python3dist(pytest-flake8)
Requires:       python3dist(pytest-mypy)
Requires:       python3dist(rst.linker) >= 1.9
Requires:       python3dist(setuptools)
Requires:       python3dist(sphinx)
%description -n python3-%{pypi_name}
 :target: PyPI link_ :target: PyPI link_.. _PyPI link: .. image::

%package -n python-%{pypi_name}-doc
Summary:        pytest-checkdocs documentation
%description -n python-%{pypi_name}-doc
Documentation for pytest-checkdocs

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
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/pytest_checkdocs.py
%{python3_sitelib}/pytest_checkdocs-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Mon Jun 15 2020 Tyler Griffiths <t@tyjgr.com> - 2.1.1-1
- Initial package.
