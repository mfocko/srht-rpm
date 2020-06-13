# Created by pyp2rpm-3.3.4
%global pypi_name pytest-mock

Name:           python-%{pypi_name}
Version:        3.1.1
Release:        2%{?dist}
Summary:        Thin-wrapper around the mock package for easier use with pytest

License:        MIT
URL:            https://github.com/pytest-dev/pytest-mock/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pre-commit)
BuildRequires:  python3dist(pytest) >= 2.7
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(tox)

%description
 pytest-mock This plugin provides a mocker fixture which is a thin-wrapper
around the patching API provided by the mock package < code-block:: python
import os class UnixFS: @staticmethod def rm(filename): os.remove(filename) def
test_unix_fs(mocker): mocker.patch('os.remove') UnixFS.rm('file')
os.remove.assert_called_once_with('file') Besides undoing the mocking
automatically after the end of...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(pytest) >= 2.7
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
 pytest-mock This plugin provides a mocker fixture which is a thin-wrapper
around the patching API provided by the mock package < code-block:: python
import os class UnixFS: @staticmethod def rm(filename): os.remove(filename) def
test_unix_fs(mocker): mocker.patch('os.remove') UnixFS.rm('file')
os.remove.assert_called_once_with('file') Besides undoing the mocking
automatically after the end of...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

# %check
# %{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/pytest_mock
%{python3_sitelib}/pytest_mock-%{version}-py%{python3_version}.egg-info

%changelog
* Sat Jun 13 2020 Tyler Griffiths <t@tyjgr.com> - 3.1.1-1
- Initial package.
