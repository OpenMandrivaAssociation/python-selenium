%define module	selenium

Summary:	Python bindings for Selenium



Name:		python-%{module}
Version:	3.141.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/ed/9c/9030520bf6ff0b4c98988448a93c04fcbd5b13cd9520074d8ed53569ccfe/selenium-3.141.0.tar.gz
License:	Apache License
Group:		Development/Python
Url:		https://pypi.python.org/pypi/selenium
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




