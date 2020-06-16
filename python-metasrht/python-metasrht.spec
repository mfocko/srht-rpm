%global srcname metasrht

Name:           python-%{srcname}
Version:        0.44.4
Release:        7%{?dist}
Summary:        Metadata service for Sourcehut

License:        AGPL
URL:            https://git.sr.ht/~sircmpwn/meta.sr.ht/
Source0:        https://git.sr.ht/~sircmpwn/meta.sr.ht/archive/%{version}.tar.gz

BuildArch:      noarch

%description
Metadata service for Sourcehut

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel, python3-srht, sassc, node, npm, git
Requires: python3-celery, python3-packaging

%description -n python3-%{srcname}
Core Python library for Sourcehut

%prep
%autosetup -n meta.sr.ht-%{version}

%build
%py3_build

%install
%py3_install

## These are autoinstalled, but should be packaged by sourcehut-meta.
## The two packages could conceivably be combined into a single Specfile.
rm %{buildroot}/%{_bindir}/metasrht-*

%check
%{python3} setup.py test

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/
