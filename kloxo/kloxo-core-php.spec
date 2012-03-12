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

%define kloxo /usr/local/lxlabs/ext/php
%define productname kloxo-core
%define packagename php
%define sourcename %{packagename}

Name: %{productname}-%{packagename}
Version: 5.2.17
Release: 1%{?dist}
Summary: Kloxo Core PHP package
Group: System Environment/Base
License: PHP License
URL: http://www.php.net

Source0: %{packagename}-%{version}.tar.bz2
Source1: lxphp.ini
# All backported patches and security fixes.
Patch1: http://php52-backports.googlecode.com/files/php52-backports-20120216.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: bzip2-devel, curl-devel >= 7.10, db4-devel, expat-devel
BuildRequires: gmp-devel, aspell-devel >= 0.60.0
BuildRequires: libjpeg-devel, libpng-devel, pam-devel
BuildRequires: libstdc++-devel, openssl-devel, sqlite-devel >= 3.3.6
BuildRequires: zlib-devel, pcre-devel >= 8.02, smtpdaemon, readline-devel
BuildRequires: bzip2, perl, libtool >= 1.4.3, gcc-c++
BuildRequires: gdbm-devel
Obsoletes: lxphp
Provides: kloxo

%description
PHP 5 is a powerful apache module that adds scripting and database connection
capabilities to the apache server. This version includes the "php_cgi" binary
for suExec and stand alone php scripts too.

PHP 5.2.17 is not maintained anymore (EOL) at php.net, the site
http://php52-backports.googlecode.com/ still provides fixes and
backported code.

%prep

%setup -q -n %{packagename}-%{version}
# Use F switch to set fuzzy lines (usefull when compiling at CentOS 6)
%patch1 -p 1 -b .patched -F 2

%build

./configure \
	--prefix=%{kloxo} \
	--with-config-file-path=%{kloxo}/etc \
	--with-libdir=%{_lib} \
	--with-jpeg-dir=%{_prefix} \
	--with-gd=shared \
	--with-imap=shared --with-imap-ssl=shared \
	--with-kerberos \
	--with-gdbm \
	--with-zlib \
	--with-gmp=shared \
	--with-mysql=shared,/usr \
	--with-pgsql=shared \
	--with-iconv=shared \
	--with-curl=/usr \
	--with-kerberos \
	--with-mhash \
	--with-mcrypt \
	--with-layout=GNU \
	--with-pcre-regex \
	--with-dom-exslt=/usr \
	--with-dom-xslt=/usr \
	--with-dom=shared,/usr \
	--with-expat-dir=/usr \
	--with-regex=system \
	--with-openssl \
	--enable-pdo \
    --with-pdo-mysql \
    --enable-sqlite \
    --with-sqlite \
    --with-pdo-sqlite \
	--with-pdo \
	--with-gettext \
	--with-db4=shared,/usr \
	--without-oci8 \
	--disable-rpath \
	--disable-debug \
	--enable-force-cgi-redirect \
	--enable-fastcgi \
	--enable-mbstring=shared --enable-mbstr-enc-trans \
	--enable-pic \
	--enable-inline-optimization \
	--enable-posix \
	--enable-simplexml \
	--enable-track-vars \
    --enable-discard-path \
	--enable-sysvshm \
	--enable-soap=/usr \
	--enable-sysvsem \
	--enable-sockets \
	--enable-safe-mode \
	--enable-magic-quotes \
	--enable-ftp \
	--enable-exif \
	--enable-bcmath \
	--enable-trans-sid \
	--enable-pcntl \
	--enable-mbregex=shared \
	--enable-dio \
	--enable-shmop \
	--enable-bcmath \
	--enable-memory-limit

%{__make} %{_smp_mflags}

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
install -D -m 755 modules/gd.so $RPM_BUILD_ROOT%{kloxo}/lib/gd.so
install -D -m 755 modules/imap.so $RPM_BUILD_ROOT%{kloxo}/lib/imap.so
install -D -m 755 modules/mbstring.so $RPM_BUILD_ROOT%{kloxo}/lib/mbstring.so
install -D -m 755 modules/mysql.so $RPM_BUILD_ROOT%{kloxo}/lib/mysql.so
install -D -m 755 modules/gmp.so $RPM_BUILD_ROOT%{kloxo}/lib/gmp.so
install -D -m 755 modules/pgsql.so $RPM_BUILD_ROOT%{kloxo}/lib/pgsql.so
install -D -m 755 modules/iconv.so $RPM_BUILD_ROOT%{kloxo}/lib/iconv.so
install -D -m 755 modules/pdo_mysql.so $RPM_BUILD_ROOT%{kloxo}/lib/pdo_mysql.so
install -D -m 755 modules/sqlite.so $RPM_BUILD_ROOT%{kloxo}/lib/sqlite.so
# If we need xdebug then we have to do the proper way.
#install -D -m 755 /root/xdebug-2.1.0/modules/xdebug.so $RPM_BUILD_ROOT%{kloxo}/lib/xdebug.so
# Doc
install -D -m 755 sapi/cli/php.1 $RPM_BUILD_ROOT%{kloxo}/man/man1/php.1
# Binary
install -D -m 755 sapi/cli/php $RPM_BUILD_ROOT%{kloxo}/php
install -D -m 755 sapi/cli/php $RPM_BUILD_ROOT%{kloxo}/bin/php
install -D -m 755 sapi/cgi/php-cgi $RPM_BUILD_ROOT%{kloxo}/bin/php_cgi
# php.ini
install -D -m 755 $RPM_SOURCE_DIR/%{SOURCE1} $RPM_BUILD_ROOT%{kloxo}php.ini

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
# Modules
%{kloxo}/lib
# Manuals
%{kloxo}/man
# Binary
%{kloxo}/php
%{kloxo}/bin
# Conf
%{kloxo}/etc
%config(noreplace) %{kloxo}/etc/php.ini
# Docs
%doc CODING_STANDARDS CREDITS INSTALL LICENSE NEWS
%doc Zend/ZEND_* 

%changelog
* Mon Mar 12 2012 Danny Terweij <d.terweij@lxcenter.org> 5.2.17-1
- Refactored SPEC file
- Use backported code from http://php52-backports.googlecode.com/

* Tue Feb 22 2011 Danny Terweij <d.terweij@lxcenter.org> 5.2.17-0.lxcenter.3
- Added sqlite and pdo_mysql modules
- Using lxphp.ini as source for php.ini

* Mon Feb 21 2011 Danny Terweij <d.terweij@lxcenter.org> 5.2.17-0.lxcenter.2
- Upgrade to PHP 5.2.17
- Added xdebug module for debugging with PHPStorm IDE
 
* Thu Jan 04 2011 Danny Terweij <d.terweij@lxcenter.org> 5.2.16-0.lxcenter.1
- Repackaged at build system 
- Upgrade to PHP 5.2.16

* Thu Nov 25 2010 Angel Guzman <angel.guzman@lxcenter.org> 5.2.14-0lxcenter3
- Upgrade to PHP 5.2.14 

