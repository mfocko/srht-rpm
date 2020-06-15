# Created by pyp2rpm-3.3.4
%global pypi_name pytest-black-multipy

Name:           python-%{pypi_name}
Version:        1.0.0
Release:        1%{?dist}
Summary:        Allow '--black' on older Pythons

License:        None
URL:            https://github.com/jaraco/skeleton
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm) >= 1.15
BuildRequires:  python3dist(sphinx)

%description
.. .. .. .. :target:

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(jaraco.packaging) >= 3.2
Requires:       (python3dist(pytest) >= 3.5 with (python3dist(pytest) < 3.7.3 or python3dist(pytest) > 3.7.3))
Requires:       python3dist(pytest-black)
Requires:       python3dist(pytest-checkdocs)
Requires:       python3dist(pytest-flake8)
Requires:       python3dist(rst.linker) >= 1.9
Requires:       python3dist(setuptools)
Requires:       python3dist(sphinx)
%description -n python3-%{pypi_name}
.. .. .. .. :target:

%package -n python-%{pypi_name}-doc
Summary:        pytest-black-multipy documentation
%description -n python-%{pypi_name}-doc
Documentation for pytest-black-multipy

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
%{python3_sitelib}/pytest_black_multipy
%{python3_sitelib}/pytest_black_multipy-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Mon Jun 15 2020 Tyler Griffiths <t@tyjgr.com> - 1.0.0-1
- Initial package.
