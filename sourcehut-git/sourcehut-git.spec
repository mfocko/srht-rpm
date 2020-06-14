Name:           sourcehut-git
Version:        0.54.1
Release:        1%{?dist}
Summary:        Git services for Sourcehut

License:        AGPL
URL:            https://git.sr.ht/~sircmpwn/git.sr.ht/
Source0:        https://git.sr.ht/~sircmpwn/git.sr.ht/archive/%{version}.tar.gz
Source1:        sourcehut-git.service
Source2:        git-srht.conf
Source3:        git-gunicorn-run.py
Source4:        git.ini
BuildRequires:  python3-scmsrht, python3-devel, python3-gitsrht, sourcehut-core, sourcehut-meta, sassc, node, npm, git
Requires:       python3-scmsrht, python3-gitsrht, sourcehut-core, sourcehut-meta, python3-gunicorn

%global debug_package %{nil}

%description
Git services for Sourcehut


%prep
%autosetup -n git.sr.ht-%{version}


%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/share/srht/git/html
mkdir -p %{buildroot}/%{_sysconfdir}/sr.ht
mkdir -p %{buildroot}/%{_sysconfdir}/systemd/system
mkdir -p %{buildroot}/%{_sysconfdir}/httpd/conf.d
mkdir -p %{buildroot}/%{_bindir}

cp -r static %{buildroot}/usr/share/srht/git/html/static

install -m 0755 gitsrht-initdb %{buildroot}/%{_bindir}/gitsrht-initdb
install -m 0755 gitsrht-migrate %{buildroot}/%{_bindir}/gitsrht-migrate
install -m 0755 run.py %{buildroot}/usr/share/srht/git/run.py

cp %{SOURCE1} %{buildroot}/%{_sysconfdir}/systemd/system/sourcehut-git.service
cp %{SOURCE2} %{buildroot}/%{_sysconfdir}/httpd/conf.d/git-srht.conf
install -m 0755 %{SOURCE3} %{buildroot}/usr/share/srht/git/gunicorn-run.py
cp %{SOURCE4} %{buildroot}/%{_sysconfdir}/sr.ht/git.ini



%files
%doc README.md
%license LICENSE
%{_sysconfdir}/sr.ht/git.ini
%{_sysconfdir}/systemd/system/sourcehut-git.service
%{_sysconfdir}/httpd/conf.d/git-srht.conf
%{_bindir}/gitsrht-initdb
%{_bindir}/gitsrht-migrate
/usr/share/srht/git/run.py
/usr/share/srht/git/gunicorn-run.py
/usr/share/srht/git/html


%changelog
* Sun Jun 14 2020 Tyler Griffiths <t@tyjgr.com>
- 
