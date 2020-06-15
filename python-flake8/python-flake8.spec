# Created by pyp2rpm-3.3.4
%global pypi_name flake8

Name:           python-%{pypi_name}
Version:        3.8.3
Release:        1%{?dist}
Summary:        the modular source code checker: pep8 pyflakes and co

License:        MIT
URL:            https://gitlab.com/pycqa/flake8
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(configparser)
BuildRequires:  python3dist(enum34)
BuildRequires:  python3dist(functools32)
BuildRequires:  python3dist(importlib-metadata)
BuildRequires:  (python3dist(mccabe) >= 0.6 with python3dist(mccabe) < 0.7)
BuildRequires:  (python3dist(pycodestyle) >= 2.6~a1 with python3dist(pycodestyle) < 2.7)
BuildRequires:  (python3dist(pyflakes) >= 2.2 with python3dist(pyflakes) < 2.3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(typing)
BuildRequires:  python3dist(sphinx)

%description
 Flake8 Flake8 is a wrapper around these tools:- PyFlakes - pycodestyle - Ned
Batchelder's McCabe scriptFlake8 runs all the tools by launching the single
flake8 command. It displays the warnings in a per-file, merged output.It also
adds a few features:- files that contain this line are skipped:: flake8: noqa-
lines that contain a noqa comment at the end will not issue warnings. - you
can...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(configparser)
Requires:       python3dist(enum34)
Requires:       python3dist(functools32)
Requires:       python3dist(importlib-metadata)
Requires:       (python3dist(mccabe) >= 0.6 with python3dist(mccabe) < 0.7)
Requires:       (python3dist(pycodestyle) >= 2.6~a1 with python3dist(pycodestyle) < 2.7)
Requires:       (python3dist(pyflakes) >= 2.2 with python3dist(pyflakes) < 2.3)
Requires:       python3dist(setuptools)
Requires:       python3dist(typing)
%description -n python3-%{pypi_name}
 Flake8 Flake8 is a wrapper around these tools:- PyFlakes - pycodestyle - Ned
Batchelder's McCabe scriptFlake8 runs all the tools by launching the single
flake8 command. It displays the warnings in a per-file, merged output.It also
adds a few features:- files that contain this line are skipped:: flake8: noqa-
lines that contain a noqa comment at the end will not issue warnings. - you
can...

%package -n python-%{pypi_name}-doc
Summary:        flake8 documentation
%description -n python-%{pypi_name}-doc
Documentation for flake8

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst tests/fixtures/config_files/README.rst
%{_bindir}/flake8
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Mon Jun 15 2020 Tyler Griffiths <t@tyjgr.com> - 3.8.3-1
- Initial package.
