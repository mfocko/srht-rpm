%global srcname pastesrht

Name:           python-%{srcname}
Version:        0.10.3
Release:        2%{?dist}
Summary:        Pastebin for Sourcehut

License:        AGPL
URL:            https://git.sr.ht/~sircmpwn/paste.sr.ht/
Source0:        https://git.sr.ht/~sircmpwn/paste.sr.ht/archive/%{version}.tar.gz
BuildArch:      noarch

%description
Pastebin for Sourcehut

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel, python3-srht, python3-packaging, sassc, node, npm, git
Requires:       python3-srht, python3-packaging

%description -n python3-%{srcname}
Pastebin for Sourcehut

%prep
%autosetup -n paste.sr.ht-%{version}

%build
%py3_build

%install
%py3_install
rm %{buildroot}/%{_bindir}/pastesrht-*

#%check
#%{python3} setup.py test

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}
%license LICENSE
/usr/lib/python3.8/site-packages/pastesrht-0.0.0-py3.8.egg-info
/usr/lib/python3.8/site-packages/pastesrht
