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

%define kloxo /usr/local/lxlabs/ext/lxlighttpd
%define productname kloxo-core
%define packagename lighttpd
%define sourcename %{packagename}

Name: %{productname}-%{packagename}
Summary: Webserver for LxCenter products (based on lighttpd)
Version: 1.4.30
Release: 1%{?dist}
License: BSD
Group: System Environment/Daemons
URL: http://www.lxcenter.org

Source0: %{packagename}-%{version}.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: openssl-devel, pcre-devel, bzip2-devel, zlib-devel, spawn-fcgi
BuildRequires: gawk, lua-devel
Requires(pre): shadow-utils
Obsoletes: lxlighttpd
Provides: kloxo

%description
This is the Core GUI webserver for LxCenter products (based on lighttpd)

%prep
%setup -q -n %{packagename}-%{version}

%build
%configure \
    --program-prefix= \
    --prefix=%{kloxo}/ \
    --exec-prefix=%{kloxo}/ \
    --bindir=%{kloxo}/bin \
    --sbindir=%{kloxo}/sbin/ \
    --libdir=%{kloxo}/lib/ \
    --mandir=%{kloxo}/share/man/ \
    --with-gdbm \
    --with-mysql \
    --with-openssl \
    --with-lua
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%pre
/usr/sbin/useradd -s /sbin/nologin -M -r -d /home/lxlabs/ \
    -c "lighttpd web server" lxlabs &>/dev/null || :

%files
%defattr(644,root,root,755)
%{kloxo}

%changelog
* Mon Mar 12 2012 Danny Terweij <contact@lxcenter.org> 1.4.30-1
- Refactored spec file
