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

%define kloxo /usr/local/lxlabs/kloxo/httpdocs/thirdparty
%define productname kloxo-core
%define packagename sshterm-applet

Name: %{productname}-%{packagename}
Summary: SSHTerm SSH access for webpages
Version: 0.0.1
Release: 1%{?dist}
License: GPL
URL: http://lxcenter.org/
Group: Applications/Internet
Source0: %{packagename}-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Requires: kloxo-core-lighttpd
Provides: sshterm

%description
SSHTerm provides web based SSH access console (java applet)

%prep
%setup -q -n %{packagename}-%{version}

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p -m0755 $RPM_BUILD_ROOT%{kloxo}/%{packagename}
%{__cp} -rp * $RPM_BUILD_ROOT%{kloxo}/%{packagename}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(644,lxlabs,lxlabs,755)
%{kloxo}/%{packagename}

%changelog
* Sun Mar 11 2012 Danny Terweij <contact@lxcenter.org> - 0.0.1-1
- Initial start of this SPEC
- Source is unknown just packed current dir and set version to 0.0.1
