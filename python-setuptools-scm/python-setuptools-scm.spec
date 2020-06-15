# Created by pyp2rpm-3.3.4
%global pypi_name setuptools-scm

Name:           python-%{pypi_name}
Version:        4.1.2
Release:        1%{?dist}
Summary:        the blessed package to manage your versions by scm tags

License:        MIT
URL:            https://github.com/pypa/setuptools_scm/
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/setuptools_scm-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(toml)

%description
setuptools_scm setuptools_scm handles managing your Python package versions in
SCM metadata instead of declaring them as the version argument or in a SCM
managed file.Additionally setuptools_scm provides setuptools with a list of
files that are managed by the SCM (i.e. it automatically adds all of the SCM-
managed files to the sdist). Unwanted files must be excluded by discarding them
via...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(setuptools)
Requires:       python3dist(toml)
%description -n python3-%{pypi_name}
setuptools_scm setuptools_scm handles managing your Python package versions in
SCM metadata instead of declaring them as the version argument or in a SCM
managed file.Additionally setuptools_scm provides setuptools with a list of
files that are managed by the SCM (i.e. it automatically adds all of the SCM-
managed files to the sdist). Unwanted files must be excluded by discarding them
via...


%prep
%autosetup -n setuptools_scm-%{version}
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
%doc README.rst
%{python3_sitelib}/setuptools_scm
%{python3_sitelib}/setuptools_scm-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Jun 15 2020 Tyler Griffiths <t@tyjgr.com> - 4.1.2-1
- Initial package.
