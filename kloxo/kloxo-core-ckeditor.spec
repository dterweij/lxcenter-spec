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
%define packagename ckeditor
%define sourcename %{packagename}

Name: %{productname}-%{packagename}
Summary: Javascript WYSIWYG Editor 
Version: 3.6.2
Release: 1%{?dist}
License: GPL
URL: http://ckeditor.com/
Group: Applications/Internet

Source0: %{sourcename}-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Requires: kloxo-core-lighttpd, kloxo-core-php >= 5.2.17
Conflicts: kloxo-core-fckeditor
Provides: kloxo

%description
CKEditor is a text editor to be used inside web pages. It's a WYSIWYG editor, which 
means that the text being edited on it looks as similar as possible to the results 
users have when publishing it. It brings to the web common editing features found on 
desktop editing applications like Microsoft Word and OpenOffice.


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
%doc CHANGES.html INSTALL.html LICENSE.html
%{kloxo}/%{packagename}

%changelog
* Sun Feb 19 2012 Danny Terweij <contact@lxcenter.org> - 3.6.2-1
- Initial start of this SPEC
