Name:           sourcehut-hub
Version:        0.4.0
Release:        4%{?dist}
Summary:        Project hub for Sourcehut

License:        AGPL
URL:            https://git.sr.ht/~sircmpwn/hub.sr.ht/
Source0:        https://git.sr.ht/~sircmpwn/hub.sr.ht/archive/%{version}.tar.gz
Source1:        sourcehut-hub.service
Source2:        hub-srht.conf
Source3:        hub-gunicorn-run.py
Source4:        hub.ini
BuildRequires:  python3-hubsrht, sourcehut-core, python3-packaging
Requires:       python3-hubsrht, sourcehut-core

%global debug_package %{nil}

%description
Project hub for Sourcehut


%prep
%autosetup -n hub.sr.ht-%{version}


%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/share/srht/hub/html
mkdir -p %{buildroot}/%{_sysconfdir}/sr.ht
mkdir -p %{buildroot}/%{_sysconfdir}/systemd/system
mkdir -p %{buildroot}/%{_sysconfdir}/httpd/conf.d
mkdir -p %{buildroot}/%{_bindir}

cp -r static %{buildroot}/usr/share/srht/hub/html/static

install -m 0755 hubsrht-initdb %{buildroot}/%{_bindir}/hubsrht-initdb
install -m 0755 hubsrht-migrate %{buildroot}/%{_bindir}/hubsrht-migrate
install -m 0755 run.py %{buildroot}/usr/share/srht/hub/run.py

cp %{SOURCE1} %{buildroot}/%{_sysconfdir}/systemd/system/sourcehut-hub.service
cp %{SOURCE2} %{buildroot}/%{_sysconfdir}/httpd/conf.d/hub-srht.conf
install -m 0755 %{SOURCE3} %{buildroot}/usr/share/srht/hub/gunicorn-run.py
cp %{SOURCE4} %{buildroot}/%{_sysconfdir}/sr.ht/hub.ini



%files
%doc README.md
%license LICENSE
%{_sysconfdir}/sr.ht/hub.ini
%{_sysconfdir}/systemd/system/sourcehut-hub.service
%{_sysconfdir}/httpd/conf.d/hub-srht.conf
%{_bindir}/hubsrht-initdb
%{_bindir}/hubsrht-migrate
/usr/share/srht/hub/run.py
/usr/share/srht/hub/gunicorn-run.py
/usr/share/srht/hub/html


%changelog
* Sun Jun 14 2020 Tyler Griffiths <t@tyjgr.com>
- 
