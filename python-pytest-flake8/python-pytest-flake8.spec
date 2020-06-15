# Created by pyp2rpm-3.3.4
%global pypi_name pytest-flake8

Name:           python-%{pypi_name}
Version:        1.0.6
Release:        1%{?dist}
Summary:        pytest plugin to check FLAKE8 requirements

License:        BSD License
URL:            https://github.com/tholo/pytest-flake8
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(flake8) >= 3.5
BuildRequires:  python3dist(pytest) >= 3.5
BuildRequires:  python3dist(setuptools)

%description
pytest plugin for efficiently checking PEP8 compliance .. image::

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(flake8) >= 3.5
Requires:       python3dist(pytest) >= 3.5
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
pytest plugin for efficiently checking PEP8 compliance .. image::


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/pytest_flake8.py
%{python3_sitelib}/pytest_flake8-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Jun 15 2020 Tyler Griffiths <t@tyjgr.com> - 1.0.6-1
- Initial package.
