Name:           sourcehut-hg
Version:        0.26.6
Release:        5%{?dist}
Summary:        Hg services for Sourcehut

License:        AGPL
URL:            https://hg.sr.ht/~sircmpwn/hg.sr.ht/
Source0:        https://hg.sr.ht/~sircmpwn/hg.sr.ht/archive/%{version}.tar.gz
Source1:        sourcehut-hg.service
Source2:        hg-srht.conf
Source3:        hg-gunicorn-run.py
Source4:        hg.ini
Source5:        sourcehut-hg.timer
BuildRequires:  python3-scmsrht, python3-devel, python3-hgsrht, sourcehut-core, sourcehut-meta, sassc, node, npm, hg, golang, git
Requires:       python3-scmsrht, python3-hgsrht, python3-hglib, python3-minio, python3-unidiff, sourcehut-core, sourcehut-meta, python3-gunicorn, golang, hg, git

%global debug_package %{nil}

%description
Hg services for Sourcehut


%prep
%autosetup -n hg.sr.ht-%{version}


%build
%py3_build

cd hgsrht-keys/
go build 
cd ..



%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/share/srht/hg/html
mkdir -p %{buildroot}/%{_sysconfdir}/sr.ht
mkdir -p %{buildroot}/%{_sysconfdir}/systemd/system
mkdir -p %{buildroot}/%{_sysconfdir}/httpd/conf.d
mkdir -p %{buildroot}/%{_bindir}

cp -r static %{buildroot}/usr/share/srht/hg/html/static

install -m 0755 hgsrht-clonebundles %{buildroot}/%{_bindir}/hgsrht-clonebundles
install -m 0755 hgsrht-hook-changegroup %{buildroot}/%{_bindir}/hgsrht-hook-changegroup
install -m 0755 hgsrht-initdb %{buildroot}/%{_bindir}/hgsrht-initdb
install -m 0755 hgsrht-install-ext %{buildroot}/%{_bindir}/hgsrht-install-ext
install -m 0755 hgsrht-keys/hgsrht-keys %{buildroot}/%{_bindir}/hgsrht-keys
install -m 0755 hgsrht-migrate %{buildroot}/%{_bindir}/hgsrht-migrate
install -m 0755 hgsrht-periodic %{buildroot}/%{_bindir}/hgsrht-periodic
install -m 0755 hgsrht-shell %{buildroot}/%{_bindir}/hgsrht-shell
install -m 0755 hgsrht-upgraderepos %{buildroot}/%{_bindir}/hgsrht-upgraderepos
install -m 0755 run.py %{buildroot}/usr/share/srht/hg/run.py

cp %{SOURCE1} %{buildroot}/%{_sysconfdir}/systemd/system/sourcehut-hg.service
cp %{SOURCE5} %{buildroot}/%{_sysconfdir}/systemd/system/sourcehut-hg.timer
cp %{SOURCE2} %{buildroot}/%{_sysconfdir}/httpd/conf.d/hg-srht.conf
install -m 0755 %{SOURCE3} %{buildroot}/usr/share/srht/hg/gunicorn-run.py
cp %{SOURCE4} %{buildroot}/%{_sysconfdir}/sr.ht/hg.ini



%files
%doc README.md
%license LICENSE
%{_sysconfdir}/sr.ht/hg.ini
%{_sysconfdir}/systemd/system/sourcehut-hg.service
%{_sysconfdir}/systemd/system/sourcehut-hg.timer
%{_sysconfdir}/httpd/conf.d/hg-srht.conf
/usr/share/srht/hg/run.py
/usr/share/srht/hg/gunicorn-run.py
/usr/share/srht/hg/html

%{_bindir}/hgsrht-clonebundles
%{_bindir}/hgsrht-hook-changegroup
%{_bindir}/hgsrht-initdb
%{_bindir}/hgsrht-install-ext
%{_bindir}/hgsrht-keys
%{_bindir}/hgsrht-migrate
%{_bindir}/hgsrht-periodic
%{_bindir}/hgsrht-shell
%{_bindir}/hgsrht-upgraderepos
/usr/share/srht/hg/run.py



%changelog
* Sun Jun 14 2020 Tyler Griffiths <t@tyjgr.com>
- 
