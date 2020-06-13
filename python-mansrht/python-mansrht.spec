
%global srcname mansrht

Name:           python-%{srcname}
Version:        0.14.9
Release:        1%{?dist}
Summary:        User manual for Sourcehut

License:        AGPL
URL:            https://git.sr.ht/~sircmpwn/man.sr.ht/
Source0:        https://git.sr.ht/~sircmpwn/man.sr.ht/archive/%{version}.tar.gz

BuildArch:      noarch

%description
User manual for Sourcehut

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel, python3-srht, sassc, npm, git
Requires: python3-celery, python3-packaging
%description -n python3-%{srcname}
User manual for Sourcehut

%prep
%autosetup -n man.sr.ht-%{version}
%build
%py3_build

%install
%py3_install

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/
%{_bindir}/mansrht-initdb
%{_bindir}/mansrht-migrate
