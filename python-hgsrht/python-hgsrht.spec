%global srcname hgsrht

Name:           python-%{srcname}
Version:        0.26.6
Release:        1%{?dist}
Summary:        Hg service for Sourcehut

License:        AGPL
URL:            https://hg.sr.ht/~sircmpwn/hg.sr.ht/
Source0:        https://hg.sr.ht/~sircmpwn/hg.sr.ht/archive/%{version}.tar.gz

BuildArch:      noarch

%description
Hg service for Sourcehut

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel, python3-srht, sassc, node, npm, git
Requires: python3-celery, python3-packaging

%description -n python3-%{srcname}
Hg service for Sourcehut

%prep
%autosetup -n hg.sr.ht-%{version}

%build
%py3_build

%install
%py3_install

## These are autoinstalled, but should be packaged by sourcehut-hg.
## The two packages could conceivably be combined into a single Specfile.
rm %{buildroot}/%{_bindir}/hgsrht-*

#%check
#%{python3} setup.py test

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{srcname}-*.egg-info
%{python3_sitelib}/%{srcname}/
