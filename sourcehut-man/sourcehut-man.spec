Name:           sourcehut-man
Version:        0.14.9
Release:        1%{?dist}
Summary:        User manual for Sourcehut

License:        AGPL
URL:            https://git.sr.ht/~sircmpwn/man.sr.ht/
Source0:        https://git.sr.ht/~sircmpwn/man.sr.ht/archive/%{version}.tar.gz
Source2:        sourcehut-man.service
Source3:        man-srht.conf
BuildRequires:  python3-srht, python3-mansrht, sassc
Requires:       python3-srht, python3-mansrht, sassc

%description

%global debug_package %{nil}

%prep
%autosetup -n man.sr.ht-%{version}

%build
#rm static
#cp -rL _static static
#sassc scss/main.scss -I /usr/lib/python3.8/site-packages/srht/scss/ > static/main.css

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/share/srht/man/html/
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_sysconfdir}/systemd/system
mkdir -p %{buildroot}/%{_sysconfdir}/httpd/conf.d/

#cp -r static %{buildroot}/usr/share/srht/man/html/static

install -m 0755 run.py %{buildroot}/usr/share/srht/man/run.py

cp %{SOURCE2} %{buildroot}/%{_sysconfdir}/systemd/system/
cp %{SOURCE3} %{buildroot}/%{_sysconfdir}/httpd/conf.d/man-srht.conf

chmod a+xr -R %{buildroot}/usr/share/srht/

%files
%license LICENSE
%doc README.md

%config %{_sysconfdir}/httpd/conf.d/man-srht.conf
%{_sysconfdir}/systemd/system/sourcehut-man.service

/usr/share/srht/man/





%changelog
* Fri Jun 12 2020 Tyler Griffiths <t@tyjgr.com>
- 
