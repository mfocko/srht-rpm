Name:           aerc
Version:        0.4.0
Release:        1%{?dist}
Summary:        A mail client

License:        MIT
URL:            https://aerc-mail.org
Source0:        https://git.sr.ht/~sircmpwn/aerc/archive/0.4.0.tar.gz

BuildRequires:  golang, scdoc, git
Requires:       golang, scdoc

%global debug_package %{nil}

%description
A mail client

%prep
%autosetup


%build
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%license LICENSE
%doc README.md
/usr/local/bin/aerc
/usr/local/share/aerc/accounts.conf
/usr/local/share/aerc/aerc.conf
/usr/local/share/aerc/binds.conf
/usr/local/share/aerc/filters/hldiff
/usr/local/share/aerc/filters/html
/usr/local/share/aerc/filters/plaintext
/usr/local/share/aerc/templates/forward_as_body
/usr/local/share/aerc/templates/quoted_reply
/usr/local/share/man/man1/aerc-search.1
/usr/local/share/man/man1/aerc.1
/usr/local/share/man/man5/aerc-config.5
/usr/local/share/man/man5/aerc-imap.5
/usr/local/share/man/man5/aerc-maildir.5
/usr/local/share/man/man5/aerc-notmuch.5
/usr/local/share/man/man5/aerc-sendmail.5
/usr/local/share/man/man5/aerc-smtp.5
/usr/local/share/man/man7/aerc-templates.7
/usr/local/share/man/man7/aerc-tutorial.7

%changelog
* Sun Jun 14 2020 Tyler Griffiths <t@tyjgr.com>
- 
