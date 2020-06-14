%global srcname hubsrht

Name:           python-%{srcname}
Version:        0.4.0
Release:        4%{?dist}
Summary:        Project hub for Sourcehut

License:        AGPL
URL:            https://git.sr.ht/~sircmpwn/hub.sr.ht/
Source0:        https://git.sr.ht/~sircmpwn/hub.sr.ht/archive/%{version}.tar.gz

BuildArch:      noarch

%description
Project hub for Sourcehut

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  sourcehut-core
Requires: sourcehut-core, python3-gunicorn

%description -n python3-%{srcname}
Project hub for Sourcehut

%prep
%autosetup -n hub.sr.ht-%{version}

%build
%py3_build
cat /var/tmp/rpm-tmp.*

%install
%py3_install

## These are autoinstalled, but should be packaged by sourcehut-meta.
## The two packages could conceivably be combined into a single Specfile.
rm %{buildroot}/%{_bindir}/hubsrht-*

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{srcname}-*.egg-info
%{python3_sitelib}/%{srcname}/
