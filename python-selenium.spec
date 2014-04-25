%define module	selenium

Summary:	Python bindings for Selenium

Name:		python-%{module}
Version:	2.41.0
Release:	1
Source0:	http://pypi.python.org/packages/source/s/selenium/selenium-%{version}.tar.gz
License:	Apache License
Group:		Development/Python
Url:		http://pypi.python.org/pypi/selenium
BuildRequires:	python-devel, python-setuptools

%description
Selenium Python Client Driver is a Python language binding for
Selenium Remote Control (version 1.0 and 2.0).

Currently the remote protocol, Firefox and Chrome for Selenium 2.0 are
supported, as well as the Selenium 1.0 bindings.

%prep
%setup -q -n %{module}-%{version}

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install \
        --root=%{buildroot} \
	--install-lib=%{py_platsitedir} \
	--install-data=%{py_platsitedir}

# Fix for x86_64 described in 
# http://code.google.com/p/selenium/issues/detail?id=2852
pushd %{buildroot}%{py_platsitedir}/selenium/webdriver/firefox
cp -f x86/x_ignore_nofocus.so amd64/x_ignore_nofocus.so
popd

%clean

%files 
%{py_platsitedir}/*


