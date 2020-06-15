Name:           sourcehut-paste
Version:        0.10.5
Release:        3%{?dist}
Summary:        Pastebin for Sourcehut

License:        AGPL
URL:            https://git.sr.ht/~sircmpwn/paste.sr.ht/
Source0:        https://git.sr.ht/~sircmpwn/paste.sr.ht/archive/%{version}.tar.gz
Source1:        sourcehut-paste.service
Source2:        paste-srht.conf
Source3:        paste-gunicorn-run.py
Source4:        paste.ini
BuildRequires:  python3-devel, python3-pastesrht, sourcehut-core, sourcehut-meta, sassc, node, npm, git
Requires:       python3-pastesrht, sourcehut-core, sourcehut-meta, python3-gunicorn


%global debug_package %{nil}

%description
Pastebin for Sourcehut


%prep
%autosetup -n paste.sr.ht-%{version}


%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/share/srht/paste/html
mkdir -p %{buildroot}/%{_sysconfdir}/sr.ht
mkdir -p %{buildroot}/%{_sysconfdir}/systemd/system
mkdir -p %{buildroot}/%{_sysconfdir}/httpd/conf.d
mkdir -p %{buildroot}/%{_bindir}

cp -r static %{buildroot}/usr/share/srht/paste/html/static

install -m 0755 pastesrht-initdb %{buildroot}/%{_bindir}/pastesrht-initdb
install -m 0755 pastesrht-migrate %{buildroot}/%{_bindir}/pastesrht-migrate
install -m 0755 run.py %{buildroot}/usr/share/srht/paste/run.py

cp %{SOURCE1} %{buildroot}/%{_sysconfdir}/systemd/system/sourcehut-paste.service
cp %{SOURCE2} %{buildroot}/%{_sysconfdir}/httpd/conf.d/paste-srht.conf
install -m 0755 %{SOURCE3} %{buildroot}/usr/share/srht/paste/gunicorn-run.py
cp %{SOURCE4} %{buildroot}/%{_sysconfdir}/sr.ht/paste.ini



%files
%license LICENSE
%{_sysconfdir}/sr.ht/paste.ini
%{_sysconfdir}/systemd/system/sourcehut-paste.service
%{_sysconfdir}/httpd/conf.d/paste-srht.conf
%{_bindir}/pastesrht-initdb
%{_bindir}/pastesrht-migrate
/usr/share/srht/paste/run.py
/usr/share/srht/paste/gunicorn-run.py
/usr/share/srht/paste/html


%changelog
* Sun Jun 14 2020 Tyler Griffiths <t@tyjgr.com>
- 
