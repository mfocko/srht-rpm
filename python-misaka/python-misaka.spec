%global srcname misaka

Name:           python-%{srcname}
Version:        2.1.1
Release:        2%{?dist}
Summary:        Example python module

License:        BSD
URL:            https://pypi.org/project/%{srcname}/
Source0:        %{pypi_source}

BuildArch:      x86_64

%global _description %{expand:
A CFFI binding for Hoedown (version 3), a markdown parsing library.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel, gcc, python3-cffi

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install 

# %check
# %{python3} setup.py test

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}
%doc README.rst
%{_bindir}/%{srcname}
/usr/lib64/python3.8/site-packages/%{srcname}-*.egg-info/
/usr/lib64/python3.8/site-packages/%{srcname}/
