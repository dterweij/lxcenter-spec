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

%define kloxo /usr/local/lxlabs/kloxo/httpdocs/htmllib
%define productname kloxo-core
%define packagename yui-dragdrop
%define sourcename %{packagename}

Name: %{productname}-%{packagename}
Summary: Javascript Framework HTML 
Version: 2.2.2
Release: 1%{?dist}
License: GPL
URL: http://yuilibrary.com/yui/docs/dd/
Group: Applications/Internet

Source0: %{sourcename}-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Requires: kloxo-core-lighttpd
Provides: kloxo

%description
The Drag and Drop Utility allows you to create a draggable interface efficiently, 
buffering you from browser-level abnormalities and enabling you to focus on the 
interesting logic surrounding your particular implementation. This component enables 
you to create a variety of standard draggable objects with just a few lines of code and 
then, using its extensive API, add your own specific implementation logic.

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
%doc README
%{kloxo}/%{packagename}

%changelog
* Sun Feb 19 2012 Danny Terweij <contact@lxcenter.org> - 2.2.2-1
- Initial start of this SPEC
