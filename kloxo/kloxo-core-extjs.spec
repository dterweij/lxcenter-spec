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

%define kloxo /usr/local/lxlabs/kloxo/httpdocs/htmllib
%define productname kloxo-core
%define packagename extjs
%define sourcename ext

Name: %{productname}-%{packagename}
Summary: Javascript Framework
Version: 1.1
Release: 1%{?dist}
License: GPL
URL: http://www.extjs.com/
Group: Applications/Internet

# Where to get old versions
# http://www.sencha.com/learn/legacy/Ext_Version_Archives 
# Repacked to tar.gz
Source0: %{sourcename}-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Requires: kloxo-core-lighttpd, kloxo-core-php >= 5.2.17
Provides: kloxo

%description
JavaScript Framework for HTML

%prep
%setup -q -n %{sourcename}-%{version}

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p -m0755 $RPM_BUILD_ROOT%{kloxo}/%{packagename}
%{__cp} -rp * $RPM_BUILD_ROOT%{kloxo}/%{packagename}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(644,lxlabs,lxlabs,755)
%doc INCLUDE_ORDER.txt license.txt
%{kloxo}/%{packagename}

%changelog
* Sun Feb 19 2012 Danny Terweij <contact@lxcenter.org> - 1.1-1
- Initial start of this SPEC
