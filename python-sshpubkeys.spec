# Created by pyp2rpm-3.3.4
%global pypi_name sshpubkeys

Name:           python-%{pypi_name}
Version:        3.1.0
Release:        2%{?dist}
Summary:        SSH public key parser

License:        BSD
URL:            https://github.com/ojarva/python-sshpubkeys
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(cryptography) >= 2.1.4
BuildRequires:  python3dist(ecdsa) >= 0.13
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(twine)
BuildRequires:  python3dist(wheel)

%description
OpenSSH Public Key Parser for Python Major changes between versions 2 and 3
Dropped support for Python 2.6 and 3.3 - Even in loose mode, DSA keys must be
1024, 2048, or 3072 bits (earlier this was looser) - The interface (API) is
exactly the same--Native implementation for validating OpenSSH public
keys.Currently ssh-rsa, ssh-dss (DSA), ssh-ed25519 and ecdsa keys with NIST
curves are...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(cryptography) >= 2.1.4
Requires:       python3dist(ecdsa) >= 0.13
%description -n python3-%{pypi_name}
OpenSSH Public Key Parser for Python Major changes between versions 2 and 3
Dropped support for Python 2.6 and 3.3 - Even in loose mode, DSA keys must be
1024, 2048, or 3072 bits (earlier this was looser) - The interface (API) is
exactly the same--Native implementation for validating OpenSSH public
keys.Currently ssh-rsa, ssh-dss (DSA), ssh-ed25519 and ecdsa keys with NIST
curves are...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

# %check
# %{__python3} setup.py test

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Sat Jun 13 2020 Tyler Griffiths <t@tyjgr.com> - 3.1.0-1
- Initial package.
