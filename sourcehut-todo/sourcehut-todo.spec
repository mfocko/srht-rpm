Name:           sourcehut-todo
Version:        0.58.4
Release:        1%{?dist}
Summary:        Ticketing for Sourcehut

License:        AGPL
URL:            https://git.sr.ht/~sircmpwn/todo.sr.ht/
Source0:        https://git.sr.ht/~sircmpwn/todo.sr.ht/archive/%{version}.tar.gz
Source1:        sourcehut-todo.service
Source2:        todo-srht.conf
Source3:        todo-gunicorn-run.py
Source4:        todo.ini
BuildRequires:  python3-todosrht
Requires:       python3-todosrht

%global debug_package %{nil}

%description
Ticketing for Sourcehut


%prep
%autosetup -n todo.sr.ht-%{version}


%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/share/srht/todo/html
mkdir -p %{buildroot}/%{_sysconfdir}/sr.ht
mkdir -p %{buildroot}/%{_sysconfdir}/systemd/system
mkdir -p %{buildroot}/%{_sysconfdir}/httpd/conf.d
mkdir -p %{buildroot}/%{_bindir}

cp -r static %{buildroot}/usr/share/srht/todo/html/static

install -m 0755 todosrht-initdb %{buildroot}/%{_bindir}/todosrht-initdb
install -m 0755 todosrht-migrate %{buildroot}/%{_bindir}/todosrht-migrate
install -m 0755 run.py %{buildroot}/usr/share/srht/todo/run.py

cp %{SOURCE1} %{buildroot}/%{_sysconfdir}/systemd/system/sourcehut-todo.service
cp %{SOURCE2} %{buildroot}/%{_sysconfdir}/httpd/conf.d/todo-srht.conf
install -m 0755 %{SOURCE3} %{buildroot}/usr/share/srht/todo/gunicorn-run.py
cp %{SOURCE4} %{buildroot}/%{_sysconfdir}/sr.ht/todo.ini



%files
%doc README.md
%license LICENSE
%{_sysconfdir}/sr.ht/todo.ini
%{_sysconfdir}/systemd/system/sourcehut-todo.service
%{_sysconfdir}/httpd/conf.d/todo-srht.conf
%{_bindir}/todosrht-initdb
%{_bindir}/todosrht-migrate
/usr/share/srht/todo/run.py
/usr/share/srht/todo/gunicorn-run.py
/usr/share/srht/todo/html


%changelog
* Sun Jun 14 2020 Tyler Griffiths <t@tyjgr.com>
- 
