#
#    LxCenter RPM packages
#
#    Copyright (C) 2000-2009    LxLabs
#    Copyright (C) 2009-2013    LxCenter
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

%define productname kloxo-tool
%define packagename ioncube

Name:           %{productname}-%{packagename}
Version:        4.0.14
Release:        1%{?dist}
Summary:        PHP IonCube Loader
Group:          Development/Languages
License:        Other
URL:            http://www.ioncube.com/loaders.php

%ifarch x86_64
Source0:        ioncube_loaders_lin_x86-64.tar.gz
%define kloxo /usr/lib64/kloxophp/%{packagename}/
%else
Source0:        ioncube_loaders_lin_x86.tar.gz
%define kloxo /usr/lib/kloxophp/%{packagename}/
%endif

# To be sure both are packaged inside the SRPM
Source88:        ioncube_loaders_lin_x86-64.tar.gz
Source99:        ioncube_loaders_lin_x86.tar.gz


BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: php, php-devel
BuildRequires: autoconf, automake, libtool
Requires: php(zend-abi) = %{php_zend_api}
Requires: php(api) = %{php_core_api}
Provides: ioncube

%description
IonCube Loader for PHP (LxCenter Package for Kloxo)


%prep
%setup -q -n %{packagename}


%build


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{kloxo}
%{__install} -m 644 loader-wizard.php %{buildroot}%{kloxo}/loader-wizard.php
%{__cp} -rp  *.so %{buildroot}%{kloxo}


%clean
%{__rm} -rf %{buildroot}


%preun


%files
%defattr(-,root,root,-)
%doc LICENSE.txt README.txt
%{kloxo}/loader-wizard.php
%{kloxo}/


%changelog
* Sun Mar 11 2012 Danny Terweij <contact@lxcenter.org> - 4.0.14-1
- Version 4.0.14

* Sun Feb 19 2012 Danny Terweij <contact@lxcenter.org> - 4.0.12-1
- Initial RPM release.
