%define module	selenium
%define name	python-%{module}
%define version 2.14.0
%define release %mkrel 1

Summary:	Python bindings for Selenium
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/s/%{module}/%{module}-%{version}.tar.gz
License:	Apache License
Group:		Development/Python
Url:		http://pypi.python.org/pypi/selenium
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	python-rdflib >= 3.1.0
BuildRequires:	python-setuptools

%description
Selenium Python Client Driver is a Python language binding for
Selenium Remote Control (version 1.0 and 2.0).

Currently the remote protocol, Firefox and Chrome for Selenium 2.0 are
supported, as well as the Selenium 1.0 bindings.

%prep
%setup -q -n %{module}-%{version}

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc COPYING CREDITS.txt
