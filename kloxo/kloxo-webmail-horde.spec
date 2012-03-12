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

%define kloxo /home/kloxo/httpd/webmail
%define productname kloxo-webmail
%define packagename horde

Name: %{productname}-%{packagename}
Summary: Horde webmail client
Version: 1.2.11
Release: 1%{?dist}
License: GPL
URL: http://www.horde.org/
Group: Applications/Internet

Source0: ftp://ftp.horde.org/pub/horde-webmail/%{packagename}-webmail-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Requires: php >= 5.2.17, php-mbstring
Provides: horde

%description
Horde Groupware Webmail Edition is a free, enterprise ready, browser
based collaboration suite. Users can manage and share calendars,
contacts, tasks and notes with the standards compliant components from
the Horde Project.

The Horde Project writes web applications in PHP and releases them
under the GNU Public License. For more information (including help
with Webmail) please visit <http://www.horde.org/>.

%prep
%setup -q -n %{packagename}-webmail-%{version}

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p -m0755 $RPM_BUILD_ROOT%{kloxo}/%{packagename}
%{__cp} -rp * $RPM_BUILD_ROOT%{kloxo}/%{packagename}

# Do not install this file
%{__rm} -f $RPM_BUILD_ROOT%{kloxo}/%{packagename}/test.php

# Move 2 files into docs
%{__mv} -f COPYING $RPM_BUILD_ROOT%{kloxo}/%{packagename}/docs/
%{__mv} -f README $RPM_BUILD_ROOT%{kloxo}/%{packagename}/docs/

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(644,lxlabs,lxlabs,755)
%doc docs/*
%{kloxo}/%{packagename}

%changelog
* Sun Feb 19 2012 Danny Terweij <contact@lxcenter.org> - 1.2.11-1
- Initial start of this SPEC
