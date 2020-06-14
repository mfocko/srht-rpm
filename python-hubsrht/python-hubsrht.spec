%global srcname hubsrht

Name:           python-%{srcname}
Version:        0.4.0
Release:        1%{?dist}
Summary:        Project hub for Sourcehut

License:        BSD
URL:            https://git.sr.ht/~sircmpwn/hub.sr.ht/
Source0:        https://git.sr.ht/~sircmpwn/hub.sr.ht/archive/%{version}.tar.gz
BuildArch:      noarch

%description
Project hub for Sourcehut

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-srht, sassc, node, npm
Requires:       python3-srht

%description -n python3-%{srcname}
Project hub for Sourcehut

%prep
%autosetup -n hub.sr.ht-%{version}

%build
%py3_build

%install
%py3_install
rm %{buildroot}/%{_bindir}/hubsrht-*

# %check
# %{python3} setup.py test

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}
%doc README.md
%license LICENSE
/usr/lib/python3.8/site-packages/hubsrht-0.0.0-py3.8.egg-info
/usr/lib/python3.8/site-packages/hubsrht
