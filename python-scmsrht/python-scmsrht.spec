%global srcname scmsrht

Name:           python-%{srcname}
Version:        0.19.9
Release:        1%{?dist}
Summary:        Scm service for Sourcehut

License:        AGPL
URL:            https://git.sr.ht/~sircmpwn/scm.sr.ht/
Source0:        https://git.sr.ht/~sircmpwn/scm.sr.ht/archive/%{version}.tar.gz

BuildArch:      noarch

%description
Scmdata service for Sourcehut

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel, python3-srht, sassc, node, npm, git
Requires: python3-srht, python3-packaging

%description -n python3-%{srcname}
Scm service for Sourcehut

%prep
%autosetup -n scm.sr.ht-%{version}

%build
%py3_build

%install
%py3_install


#%check
#%{python3} setup.py test

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}
%license LICENSE
%{python3_sitelib}/%{srcname}-*.egg-info
%{python3_sitelib}/%{srcname}/
