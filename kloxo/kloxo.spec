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

%define productname kloxo
%define destination /usr/local/lxlabs/%{productname}

Name: %{productname}
Summary: Kloxo - Hosting Control Panel
Version: 6.1.11
Release: 1%{?dist}
License: AGPLV3
URL: http://www.lxcenter.org/
Group: Applications/Internet

Source0: %{name}-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

# Stop installing if those are found
Conflicts: postfix, sendmail, sendmail-cf, exim, vsftpd, dovecot
# Not wanted packages
Obsoletes: lxzend

# Defaults
Requires: php >= 5.2.17, lxphp
Requires: php-mysql, php-mbstring, php-imap, php-pear, php-gd
Requires: lxcenter-release
Requires: bind, bind-chroot, bind-utils
Requires: mysql, mysql-server
Requires: httpd, mod_ssl
Requires: openssl
Requires: vpopmail, courier-imap-toaster, courier-authlib-toaster, qmail
Requires: ezmlm-toaster, spamassassin, autorespond-toaster
Requires: ucspi-tcp-toaster, daemontools-toaster, libsrs2-toaster
Requires: simscan-toaster, maildrop-toaster, ripmime-toaster
Requires: clamav-toaster
Requires: pure-ftpd
Requires: wget, yum, zip, unzip, tar, safecat, which, yum-protectbase
Requires: apr, apr-util, rrdtool, pcre, t1lib
Requires: lxjailshell

# NEW kloxo=*
# Core
Requires: kloxo-core-ckeditor, kloxo-core-extjs, kloxo-core-lighttpd
Requires: kloxo-core-php, kloxo-core-phpMyAdmin, kloxo-core-sshterm-applet
Requires: kloxo-core-yui-dragdrop
# Tool
Requires: kloxo-tool-awstats, kloxo-tool-ioncube, kloxo-tool-zend
# Webmail
Requires: kloxo-webmail-horde, kloxo-webmail-roundcube

Provides: %{name}

%description
Scriptable, distributed and object oriented Hosting Platform.
Manage Clients, Resellers, Domains, Backups, Stats, Mails and Databases. Manage everything!

%prep
%setup -q -n %{name}-%{version}

%build

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p -m0755 %{buildroot}%{destination}
%{__cp} -rp * %{buildroot}%{destination}

%clean
%{__rm} -rf %{buildroot}
%files
%defattr(644,lxlabs,lxlabs,755)
%{destination}

%changelog
* Thu Mar 01 2012 Danny Terweij <contact@lxcenter.org> - 6.1.11-1
- Initial start of this SPEC
