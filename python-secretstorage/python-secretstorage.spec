# Created by pyp2rpm-3.3.4
%global pypi_name secretstorage

Name:           python-%{pypi_name}
Version:        3.1.2
Release:        1%{?dist}
Summary:        Python bindings to FreeDesktop.org Secret Service API

License:        BSD 3-Clause License
URL:            https://github.com/mitya57/secretstorage
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/SecretStorage-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(jeepney) >= 0.4.2
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
 Module description This module provides a way for securely storing passwords
and other secrets.It uses D-Bus Secret Service_ API that is supported by GNOME
Keyring

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(cryptography)
Requires:       python3dist(jeepney) >= 0.4.2
%description -n python3-%{pypi_name}
 Module description This module provides a way for securely storing passwords
and other secrets.It uses D-Bus Secret Service_ API that is supported by GNOME
Keyring

%package -n python-%{pypi_name}-doc
Summary:        secretstorage documentation
%description -n python-%{pypi_name}-doc
Documentation for secretstorage

%prep
%autosetup -n SecretStorage-%{version}
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

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Mon Jun 15 2020 Tyler Griffiths <t@tyjgr.com> - 3.1.2-1
- Initial package.
