Name:           sourcehut-meta
Version:        0.44.2
Release:        15%{?dist}
Summary:        Profile and credential storage for Sourcehut

License:        AGPL
URL:            https://git.sr.ht/~sircmpwn/meta.sr.ht/
Source0:        https://git.sr.ht/~sircmpwn/meta.sr.ht/archive/%{version}.tar.gz
Source1:        meta.ini
Source2:        sourcehut-meta.service
Source3:        meta-srht.conf
Source4:        meta-gunicorn-run.py
Source5:        sourcehut-meta-api.service
Source6:        sourcehut-meta.timer
BuildRequires:  python3-srht, python3-metasrht, sassc, sourcehut-core, golang, git
Requires:       python3-metasrht, sassc, python3-gunicorn, sourcehut-core, golang, git

%description

%global debug_package %{nil}

%prep
%autosetup -n meta.sr.ht-%{version}

%build
rm static
cp -rL _static static
sassc scss/main.scss -I /usr/lib/python3.8/site-packages/srht/scss/ > static/main.css

cd api
go build
cd ..



%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/share/srht/meta/html/
mkdir -p %{buildroot}/%{_sysconfdir}/sr.ht
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_sysconfdir}/systemd/system
mkdir -p %{buildroot}/%{_sysconfdir}/httpd/conf.d/

cp -r static %{buildroot}/usr/share/srht/meta/html/static

install -m 0755 run.py %{buildroot}/usr/share/srht/meta/run.py


install -m 0755 metasrht-createuser %{buildroot}%{_bindir}/metasrht-createuser
install -m 0755 metasrht-daily %{buildroot}%{_bindir}/metasrht-daily
install -m 0755 metasrht-initdb %{buildroot}%{_bindir}/metasrht-initdb
install -m 0755 metasrht-invoicestats %{buildroot}%{_bindir}/metasrht-invoicestats
install -m 0755 metasrht-migrate %{buildroot}%{_bindir}/metasrht-migrate
install -m 0755 scripts/revoke-expired-tokens %{buildroot}%{_bindir}/metasrht-revoke-expired-tokens

install -m 0755 api/api %{buildroot}/%{_bindir}/metasrht-api

cp %{SOURCE1} %{buildroot}/%{_sysconfdir}/sr.ht/meta.ini
cp %{SOURCE2} %{buildroot}/%{_sysconfdir}/systemd/system/
cp %{SOURCE3} %{buildroot}/%{_sysconfdir}/httpd/conf.d/meta-srht.conf
cp %{SOURCE4} %{buildroot}/usr/share/srht/meta/gunicorn-run.py
cp %{SOURCE5} %{buildroot}/%{_sysconfdir}/systemd/system/
cp %{SOURCE6} %{buildroot}/%{_sysconfdir}/systemd/system/

chmod a+xr -R %{buildroot}/usr/share/srht/

%files
%license LICENSE
%doc README.md
%{_bindir}/metasrht-createuser
%{_bindir}/metasrht-daily
%{_bindir}/metasrht-initdb
%{_bindir}/metasrht-invoicestats
%{_bindir}/metasrht-migrate
%{_bindir}/metasrht-revoke-expired-tokens
%{_bindir}/metasrht-api

%config %{_sysconfdir}/sr.ht/meta.ini
%config %{_sysconfdir}/httpd/conf.d/meta-srht.conf
%{_sysconfdir}/systemd/system/sourcehut-meta.service
%{_sysconfdir}/systemd/system/sourcehut-meta-api.service
%{_sysconfdir}/systemd/system/sourcehut-meta.timer

/usr/share/srht/meta/



%changelog
* Fri Jun 12 2020 Tyler Griffiths <t@tyjgr.com>
- 
