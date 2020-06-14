%global srcname todosrht

Name:           python-%{srcname}
Version:        0.58.4
Release:        2%{?dist}
Summary:        Ticketing for Sourcehut

License:        AGPL
URL:            https://git.sr.ht/~sircmpwn/todo.sr.ht/
Source0:        https://git.sr.ht/~sircmpwn/todo.sr.ht/archive/%{version}.tar.gz
BuildArch:      noarch

%description
Ticketing for Sourcehut

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-srht, sassc, node, npm, sourcehut-core, python3-packaging
Requires:       sourcehut-core, python3-packaging

%description -n python3-%{srcname}
Ticketing for Sourcehut

%prep
%autosetup -n todo.sr.ht-%{version}

%build
%py3_build

%install
%py3_install
#rm %{buildroot}/%{_bindir}/todosrht-*

# %check
# %{python3} setup.py test

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}
%doc README.md
%license LICENSE
/usr/lib/python3.8/site-packages/todosrht-0.0.0-py3.8.egg-info
/usr/lib/python3.8/site-packages/todosrht
