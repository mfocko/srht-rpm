%global goipath         git.sr.ht/~sircmpwn/aerc/
Version:                0.4.0

%gometa

%global common_description %{expand:
aerc is a mail client.}

%global golicenses    MIT

Name:           %{goname}
Release:        1%{?dist}
Summary:        A TUI mail client
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/davecgh/go-spew/spew)
BuildRequires: golang(github.com/pmezard/go-difflib/difflib)
BuildRequires: golang(github.com/stretchr/objx)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%check
%gochecks

%gopkgfiles


%changelog
* Thu Mar 21 22:20:22 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.2-1
- First package for Fedora
