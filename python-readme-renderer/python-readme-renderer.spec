# Created by pyp2rpm-3.3.4
%global pypi_name readme-renderer

Name:           python-%{pypi_name}
Version:        26.0
Release:        1%{?dist}
Summary:        readme_renderer is a library for rendering "readme" descriptions for Warehouse

License:        Apache License, Version 2.0
URL:            https://github.com/pypa/readme_renderer
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/readme_renderer-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(bleach) >= 2.1
BuildRequires:  python3dist(cmarkgfm) >= 0.2
BuildRequires:  python3dist(docutils) >= 0.13.1
BuildRequires:  python3dist(pygments) >= 2.5.1
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)

%description
Readme Renderer Readme Renderer is a library that will safely render arbitrary
README files into HTML. It is designed to be used in Warehouse_ to render the
long_description for packages. It can handle Markdown, reStructuredText (.rst),
and plain text... _Warehouse: Check Description Locally -To locally check
whether your long descriptions will render on PyPI, first build your
distributions,...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(bleach) >= 2.1
Requires:       python3dist(cmarkgfm) >= 0.2
Requires:       python3dist(docutils) >= 0.13.1
Requires:       python3dist(pygments) >= 2.5.1
Requires:       python3dist(setuptools)
Requires:       python3dist(six)
%description -n python3-%{pypi_name}
Readme Renderer Readme Renderer is a library that will safely render arbitrary
README files into HTML. It is designed to be used in Warehouse_ to render the
long_description for packages. It can handle Markdown, reStructuredText (.rst),
and plain text... _Warehouse: Check Description Locally -To locally check
whether your long descriptions will render on PyPI, first build your
distributions,...


%prep
%autosetup -n readme_renderer-%{version}
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
%{python3_sitelib}/readme_renderer
%{python3_sitelib}/readme_renderer-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Jun 15 2020 Tyler Griffiths <t@tyjgr.com> - 26.0-1
- Initial package.
