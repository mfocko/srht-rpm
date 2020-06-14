%global srcname srht

Name:           python-%{srcname}
Version:        0.62.3
Release:        3%{?dist}
Summary:        Core Python library for Sourcehut

License:        BSD
URL:            https://git.sr.ht/~sircmpwn/core.sr.ht/
Source0:        https://git.sr.ht/~sircmpwn/core.sr.ht/archive/%{version}.tar.gz
Source1:        https://github.com/twbs/bootstrap/archive/v4.5.0.tar.gz
BuildArch:      noarch

%description
Core Python library for Sourcehut

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel, npm, gcc, libpq-devel, git
Requires:       python3-packaging

%description -n python3-%{srcname}
Core Python library for Sourcehut

%prep
%autosetup -n core.sr.ht-%{version}
cp %{SOURCE1} ./
tar xf ./v4.5.0.tar.gz

%build
%py3_build

%install
%py3_install

rm %{buildroot}/%{_bindir}/srht-*

cp -r ./bootstrap-4.5.0 $RPM_BUILD_ROOT/usr/lib/python3.8/site-packages/%{srcname}/scss/bootstrap

# %check
# %{python3} setup.py test

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}
%doc README.md
%license LICENSE
/usr/lib/python3.8/site-packages/srht-0.0.0-py3.8.egg-info
/usr/lib/python3.8/site-packages/srht
