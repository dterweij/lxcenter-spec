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

%define kloxo /home/kloxo/httpd
%define productname kloxo-tool
%define packagename awstats

Name: %{productname}-%{packagename}
Summary: AWStats logfile analyzer
Version: 7.0
Release: 1%{?dist}
License: GPL
URL: http://awstats.sourceforge.net/
Group: Applications/Internet
Source0: http://prdownloads.sourceforge.net/awstats/%{packagename}-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Requires: webserver, php >= 5.2.17, php-mbstring
Provides: awstats

%description
AWStats is a free powerful and featureful tool that generates advanced 
web, streaming, ftp or mail server statistics, graphically. This log 
analyzer works as a CGI or from command line and shows you all possible 
information your log contains, in few graphical web pages. It uses a 
partial information file to be able to process large log files, often 
and quickly. It can analyze log files from all major server tools like 
Apache log files (NCSA combined/XLF/ELF log format or common/CLF log 
format), WebStar, IIS (W3C log format) and a lot of other web, proxy, 
wap, streaming servers, mail servers and some ftp servers.

AWStats is a free software distributed under the GNU General Public 
License. You can have a look at this license chart to know what you 
can/can't do.

As AWStats works from the command line but also as a CGI, it can work 
with all web hosting providers which allow Perl, CGI and log access.

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
%doc docs/*
%{kloxo}/%{packagename}

%changelog
* Sun Mar 11 2012 Danny Terweij <contact@lxcenter.org> - 7.0-1
- Initial start of this SPEC
