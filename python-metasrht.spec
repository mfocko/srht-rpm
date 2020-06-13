%global srcname metasrht

Name:           python-%{srcname}
Version:        0.44.2
Release:        1%{?dist}
Summary:        Metadata service for Sourcehut

License:        BSD
URL:            https://git.sr.ht/~sircmpwn/meta.sr.ht/
Source0:        https://git.sr.ht/~sircmpwn/meta.sr.ht/archive/%{version}.tar.gz

BuildArch:      noarch

%description
Metadata service for Sourcehut

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel, python3-srht, sassc, node, npm, git

%description -n python3-%{srcname}
Core Python library for Sourcehut

%prep
%autosetup -n meta.sr.ht-%{version}
%build
%py3_build

%install
%py3_install

%check
%{python3} setup.py test

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}
#%{python3_sitelib}/%{srcname}-*.egg-info/
#%{python3_sitelib}/%{srcname}/
#%{_bindir}/sample-exec
#%doc /usr/share/doc/python3-srht/README.md
#%license /usr/share/licenses/python3-srht/LICENSE
#/usr/lib/python3.8/site-packages/srht-0.0.0-py3.8.egg-info
#/usr/lib/python3.8/site-packages/srht
#%{_bindir}/srht-migrate
#%{_bindir}/srht-update-profiles
#%{_bindir}/srht-keygen
