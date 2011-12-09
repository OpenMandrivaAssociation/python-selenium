%define module	selenium
%define name	python-%{module}
%define version 2.15.0
%define release %mkrel 2

Summary:	Python bindings for Selenium
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/s/%{module}/%{module}-%{version}.tar.gz
License:	Apache License
Group:		Development/Python
Url:		http://pypi.python.org/pypi/selenium
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	python-rdflib >= 3.1.0
BuildRequires:	python-devel, python-setuptools

%description
Selenium Python Client Driver is a Python language binding for
Selenium Remote Control (version 1.0 and 2.0).

Currently the remote protocol, Firefox and Chrome for Selenium 2.0 are
supported, as well as the Selenium 1.0 bindings.

%prep
%setup -q -n %{module}-%{version}

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install \
        --root=%{buildroot} \
		--install-lib=%{python_sitearch} \
		--install-data=%{python_sitearch}

%if "%{_lib}" == "lib64"
rm -f %{buildroot}%py_platsitedir/selenium/webdriver/firefox/x86/x_ignore_nofocus.so
%else
rm -f %{buildroot}%py_platsitedir/selenium/webdriver/firefox/amd64/x_ignore_nofocus.so
%endif

%clean
%__rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc COPYING CREDITS.txt
%py_platsitedir
