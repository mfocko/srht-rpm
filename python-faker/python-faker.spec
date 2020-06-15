# Created by pyp2rpm-3.3.4
%global pypi_name faker

Name:           python-%{pypi_name}
Version:        4.1.0
Release:        1%{?dist}
Summary:        Faker is a Python package that generates fake data for you

License:        MIT License
URL:            https://github.com/joke2k/faker
Source0:        https://files.pythonhosted.org/packages/source/f/%{pypi_name}/Faker-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(python-dateutil) >= 2.4
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(text-unidecode) = 1.3

%description
*Faker* is a Python package that generates fake data for you. Whether you need
to bootstrap your database, create good-looking XML documents, fill-in your
persistence to stress test it, or anonymize data taken from a production
service, Faker is for you.Faker is heavily inspired by PHP Faker_, Perl Faker_,
and by Ruby Faker_.-:: _|_|_|_| _| _| _|_|_| _| _| _|_| _| _|_| _|_|_| _| _|
_|_|...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(python-dateutil) >= 2.4
Requires:       python3dist(setuptools)
Requires:       python3dist(text-unidecode) = 1.3
%description -n python3-%{pypi_name}
*Faker* is a Python package that generates fake data for you. Whether you need
to bootstrap your database, create good-looking XML documents, fill-in your
persistence to stress test it, or anonymize data taken from a production
service, Faker is for you.Faker is heavily inspired by PHP Faker_, Perl Faker_,
and by Ruby Faker_.-:: _|_|_|_| _| _| _|_|_| _| _| _|_| _| _|_| _|_|_| _| _|
_|_|...


%prep
%autosetup -n Faker-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install


%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{_bindir}/faker
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Jun 15 2020 Tyler Griffiths <t@tyjgr.com> - 4.1.0-1
- Initial package.
