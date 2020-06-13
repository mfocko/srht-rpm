%global srcname pgpy

Name:           python-%{srcname}
Version:        0.5.2
Release:        2%{?dist}
Summary:        Example python module

License:        BSD
URL:            https://pypi.org/project/PGPy/
Source0:        https://files.pythonhosted.org/packages/source/P/PGPy/PGPy-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
A library for implementing Pretty Good Privacy into Python programs, conforming to the OpenPGP specification per RFC 4880}

%description %_description

%package -n python3-pgpy
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{srcname} %_description

%prep
%autosetup -n PGPy-%{version}

%build
%py3_build

%install
%py3_install

# %check
# %{python3} setup.py test

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}
%doc README.rst
%{python3_sitelib}/PGPy-*.egg-info/
%{python3_sitelib}/%{srcname}/
