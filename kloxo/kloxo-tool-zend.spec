#
#    LxCenter RPM packages
#
#    Copyright (C) 2000-2009    LxLabs
#    Copyright (C) 2009-2012    LxCenter
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
%define packagename zend


%global         php_extdir %(php-config --extension-dir 2>/dev/null || echo "undefined")

Name:           %{productname}-%{packagename}
Version:        3.3.9
Release:        1%{?dist}
Summary:        PHP ZendOptimizer Loader
Group:          Development/Languages
License:        Other
URL:            http://www.zend.com/products/guard/zend-optimizer

%ifarch x86_64
Source0:        ZendOptimizer-3.3.9-linux-glibc23-x86_64.tar.gz
%define kloxo /usr/lib64/kloxophp/zend/lib/Optimizer-3.2.8/php-5.2.x/
%else
Source0:        ZendOptimizer-3.3.9-linux-glibc23-i386.tar.gz
%define kloxo /usr/lib/kloxophp/zend/lib/Optimizer-3.2.8/php-5.2.x/
%endif

# To be sure both ate packaged inside the SRPM
Source88:        ZendOptimizer-3.3.9-linux-glibc23-x86_64.tar.gz
Source99:        ZendOptimizer-3.3.9-linux-glibc23-i386.tar.gz


BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: php, php-devel
BuildRequires: autoconf, automake, libtool
Requires: php(zend-abi) = %{php_zend_api}
Requires: php(api) = %{php_core_api}
Provides: zend

%description
ZendOptimizer Loader for PHP (LxCenter Package for Kloxo)


%prep
%ifarch x86_64
%setup -q -n ZendOptimizer-3.3.9-linux-glibc23-x86_64
%else
%setup -q -n ZendOptimizer-3.3.9-linux-glibc23-i386
%endif


%build


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{kloxo}
%{__install} -m 644 data/5_2_x_comp/ZendOptimizer.so %{buildroot}%{kloxo}/ZendOptimizer.so


%clean
%{__rm} -rf %{buildroot}


%preun


%files
%defattr(-,root,root,-)
%doc EULA-ZendOptimizer LICENSE README-ZendOptimizer
%{kloxo}/ZendOptimizer.so


%changelog
* Sat Feb 18 2012 Danny Terweij <contact@lxcenter.org> - 3.3.9-1
- Initial RPM release.
- Replaces the so file in current Kloxo installation path so no need to change the ini file!
