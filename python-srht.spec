%global srcname srht

Name:           python-%{srcname}
Version:        0.62.3
Release:        1%{?dist}
Summary:        Core Python library for Sourcehut

License:        BSD
URL:            https://git.sr.ht/~sircmpwn/core.sr.ht/
Source0:        https://git.sr.ht/~sircmpwn/core.sr.ht/archive/%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand: Core Python library for Sourcehut}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{python3} setup.py test

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}
%license COPYING
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/
%{_bindir}/sample-exec

