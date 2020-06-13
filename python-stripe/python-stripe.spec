# Created by pyp2rpm-3.3.4
%global pypi_name stripe

Name:           python-%{pypi_name}
Version:        2.48.0
Release:        2%{?dist}
Summary:        Python bindings for the Stripe API

License:        MIT
URL:            https://github.com/stripe/stripe-python
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
#BuildRequires:  (python3dist(coverage) >= 4.5.3 with python3dist(coverage) < 5)
BuildRequires:  (python3dist(pytest) >= 4.6.2 with python3dist(pytest) < 4.7)
BuildRequires:  python3dist(pytest-cov) >= 2.8.1
BuildRequires:  python3dist(pytest-mock) >= 2
BuildRequires:  python3dist(pytest-xdist) >= 1.31
BuildRequires:  python3dist(requests) >= 2.20
BuildRequires:  python3dist(requests) >= 2.20
BuildRequires:  python3dist(setuptools)

%description
Official Stripe Bindings for Python A Python library for Stripe's API.--You can
install this package by using the pip tool and installing: $ pip install
stripeOr: $ easy_install stripe Setting up a Stripe Account Sign up for Stripe
at the Stripe API --Documentation for the python bindings can be found
alongside Stripe's other bindings here:- - the standard documentation (the
first link), most...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(requests) >= 2.20
Requires:       python3dist(requests) >= 2.20
%description -n python3-%{pypi_name}
Official Stripe Bindings for Python A Python library for Stripe's API.--You can
install this package by using the pip tool and installing: $ pip install
stripeOr: $ easy_install stripe Setting up a Stripe Account Sign up for Stripe
at the Stripe API --Documentation for the python bindings can be found
alongside Stripe's other bindings here:- - the standard documentation (the
first link), most...


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
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Sat Jun 13 2020 Tyler Griffiths <t@tyjgr.com> - 2.48.0-1
- Initial package.
