%define module	selenium
%define name	python-%{module}
%define version 2.25.0
%define release 1

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

# Fix for x86_64 described in 
# http://code.google.com/p/selenium/issues/detail?id=2852
pushd %{buildroot}%{py_platsitedir}/selenium/webdriver/firefox
cp -f x86/x_ignore_nofocus.so amd64/x_ignore_nofocus.so
popd

%clean
%__rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc COPYING CREDITS.txt
%py_platsitedir


%changelog
* Tue Jul 31 2012 Lev Givon <lev@mandriva.org> 2.25.0-1
+ Revision: 811502
- Update to 2.25.0.

* Fri Jun 22 2012 Lev Givon <lev@mandriva.org> 2.24.0-1
+ Revision: 806709
- Update to 2.24.0.
  Add fix for Firefox load problem on x86_64.

* Fri Dec 09 2011 Lev Givon <lev@mandriva.org> 2.15.0-2
+ Revision: 739555
- Shouldn't be noarch.

* Fri Dec 09 2011 Lev Givon <lev@mandriva.org> 2.15.0-1
+ Revision: 739229
- Update to 2.15.0.

* Wed Nov 30 2011 Lev Givon <lev@mandriva.org> 2.14.0-1
+ Revision: 735508
- Update to 2.14.0.

* Tue Nov 15 2011 Lev Givon <lev@mandriva.org> 2.12.1-1
+ Revision: 730726
- Update to 2.12.1.

* Sun Oct 30 2011 Lev Givon <lev@mandriva.org> 2.11.1-1
+ Revision: 707860
- Update to 2.11.1.

* Tue Oct 25 2011 Lev Givon <lev@mandriva.org> 2.9.0-1
+ Revision: 707147
- Update to 2.9.0.

* Thu Oct 06 2011 Lev Givon <lev@mandriva.org> 2.8.1-1
+ Revision: 703356
- Update to 2.8.1.

* Mon Sep 26 2011 Lev Givon <lev@mandriva.org> 2.7.0-1
+ Revision: 701372
- Update to 2.7.0.

* Tue Sep 13 2011 Lev Givon <lev@mandriva.org> 2.6.0-1
+ Revision: 699688
- Update to 2.6.0.

* Sun Aug 28 2011 Lev Givon <lev@mandriva.org> 2.5.0-1
+ Revision: 697259
- Update to 2.5.0.

* Thu Aug 11 2011 Lev Givon <lev@mandriva.org> 2.4.0-1
+ Revision: 694042
- Update to 2.4.0.

* Wed Aug 10 2011 Lev Givon <lev@mandriva.org> 2.3.0-2
+ Revision: 693802
- Require python-rdflib.

* Tue Aug 02 2011 Lev Givon <lev@mandriva.org> 2.3.0-1
+ Revision: 692712
- Update to 2.3.0.

* Fri Jul 29 2011 Lev Givon <lev@mandriva.org> 2.2.0-1
+ Revision: 692159
- import python-selenium


