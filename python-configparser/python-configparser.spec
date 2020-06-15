# Created by pyp2rpm-3.3.4
%global pypi_name configparser

Name:           python-%{pypi_name}
Version:        5.0.0
Release:        1%{?dist}
Summary:        Updated configparser from Python 3.8 for Python 2.6+

License:        None
URL:            https://github.com/jaraco/configparser/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(jaraco.packaging) >= 3.2
BuildRequires:  (python3dist(pytest) >= 3.5 with (python3dist(pytest) < 3.7.3 or python3dist(pytest) > 3.7.3))
BuildRequires:  python3dist(rst.linker) >= 1.9
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm) >= 3.4.1
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx)

%description
 :target: PyPI link_ :target: PyPI link_.. _PyPI link: :target:

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(jaraco.packaging) >= 3.2
Requires:       (python3dist(pytest) >= 3.5 with (python3dist(pytest) < 3.7.3 or python3dist(pytest) > 3.7.3))
Requires:       python3dist(pytest-black-multipy)
Requires:       python3dist(pytest-checkdocs) >= 1.2.3
Requires:       python3dist(pytest-cov)
Requires:       python3dist(pytest-flake8)
Requires:       python3dist(rst.linker) >= 1.9
Requires:       python3dist(sphinx)
%description -n python3-%{pypi_name}
 :target: PyPI link_ :target: PyPI link_.. _PyPI link: :target:

%package -n python-%{pypi_name}-doc
Summary:        configparser documentation
%description -n python-%{pypi_name}-doc
Documentation for configparser

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
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/backports
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Mon Jun 15 2020 Tyler Griffiths <t@tyjgr.com> - 5.0.0-1
- Initial package.
