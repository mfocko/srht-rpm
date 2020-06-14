# Created by pyp2rpm-3.3.4
%global pypi_name minio

Name:           python-%{pypi_name}
Version:        5.0.10
Release:        1%{?dist}
Summary:        MinIO Python Library for Amazon S3 Compatible Cloud Storage for Python

License:        Apache License 2.0
URL:            https://github.com/minio/minio-py
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(certifi)
BuildRequires:  python3dist(configparser)
BuildRequires:  python3dist(faker)
BuildRequires:  python3dist(future)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(nose)
BuildRequires:  python3dist(python-dateutil)
BuildRequires:  python3dist(pytz)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(urllib3)

%description
 MinIO Python Library for Amazon S3 Compatible Cloud Storage [![Slack]( MinIO
Python Client SDK provides simple APIs to access any Amazon S3 compatible
object storage server.This quickstart guide will show you how to install the
client SDK and execute an example python program. For a complete list of APIs
and examples, please take a look at the [Python Client API Reference](
documentation.This...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(certifi)
Requires:       python3dist(configparser)
Requires:       python3dist(future)
Requires:       python3dist(python-dateutil)
Requires:       python3dist(pytz)
Requires:       python3dist(urllib3)
%description -n python3-%{pypi_name}
 MinIO Python Library for Amazon S3 Compatible Cloud Storage [![Slack]( MinIO
Python Client SDK provides simple APIs to access any Amazon S3 compatible
object storage server.This quickstart guide will show you how to install the
client SDK and execute an example python program. For a complete list of APIs
and examples, please take a look at the [Python Client API Reference](
documentation.This...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md README_zh_CN.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Sun Jun 14 2020 Tyler Griffiths <t@tyjgr.com> - 5.0.10-1
- Initial package.
