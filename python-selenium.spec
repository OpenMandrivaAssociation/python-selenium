%undefine _debugsource_packages
%define module	selenium
# oname required for vendoring script
%define oname	selenium

# NOTE	Run create_vendored_crate_archive.sh script to create vendor archive-
# NOTE	when you update this package, submit archive to to abf and update-
# NOTE	Source1 & yml.

Name:		python-selenium
Version:	4.31.0
Release:	2
Summary:	Python language bindings for Selenium WebDriver
License:	Apache-2.0
Group:		Development/Python
URL:		https://pypi.org/project/selenium/
Source0:	https://files.pythonhosted.org/packages/source/s/selenium/%{oname}-%{version}.tar.gz
Source1:	%{oname}-%{version}-vendor.tar.xz
BuildSystem: python

BuildRequires:	python
BuildRequires:  pkgconfig(python3)
BuildRequires:	python%{pyver}dist(certifi)
BuildRequires:	python%{pyver}dist(maturin)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(setuptools-rust)
BuildRequires:	python%{pyver}dist(trio)
BuildRequires:	python%{pyver}dist(trio-websocket)
BuildRequires:	python%{pyver}dist(typing-extensions)
BuildRequires:	python%{pyver}dist(urllib3)
BuildRequires:	python%{pyver}dist(websockets)
BuildRequires:	python%{pyver}dist(websocket-client)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	cargo
BuildRequires:	rust-packaging

Requires:	python%{pyver}dist(certifi) >= 2021.10.8
Requires:	python%{pyver}dist(trio) >= 0.17
Requires:	python%{pyver}dist(trio-websocket) >= 0.9
Requires:	python%{pyver}dist(typing-extensions) >= 4.9
Requires:	python%{pyver}dist(urllib3) >= 1.26
Requires:	python%{pyver}dist(websocket-client) >= 1.8


%description
Python language bindings for Selenium WebDriver.

The selenium package is used to automate web browser interaction from Python.

%prep
%autosetup -n %{oname}-%{version} -p1 -a1
%cargo_prep -v vendor

cat >>.cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

EOF

%build
%py_build

%install
%py3_install

%files
%{_bindir}/%{module}.webdriver.common.%{module}-manager
%{python3_sitearch}/%{module}
%{python3_sitearch}/%{module}-%{version}.dist-info
%license LICENSE
%doc README.rst





