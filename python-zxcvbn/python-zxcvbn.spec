# Created by pyp2rpm-3.3.4
%global pypi_name zxcvbn

Name:           python-%{pypi_name}
Version:        4.4.28
Release:        2%{?dist}
Summary:        A realistic password strength estimator

License:        MIT
URL:            https://github.com/dwolfhub/zxcvbn-python
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
|Build Status|zxcvbn A realistic password strength estimator.This is a Python
implementation of the library created by the team at Dropbox. The original
library, written for JavaScript, can be found here < there may be other Python
ports available, this one is the most up to date and is recommended by the
original developers of zxcvbn at thisFeatures- **Tested in Python versions 2.7,
3.3-3.6**...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
|Build Status|zxcvbn A realistic password strength estimator.This is a Python
implementation of the library created by the team at Dropbox. The original
library, written for JavaScript, can be found here < there may be other Python
ports available, this one is the most up to date and is recommended by the
original developers of zxcvbn at thisFeatures- **Tested in Python versions 2.7,
3.3-3.6**...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%{_bindir}/zxcvbn
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Sat Jun 13 2020 Tyler Griffiths <t@tyjgr.com> - 4.4.28-1
- Initial package.
