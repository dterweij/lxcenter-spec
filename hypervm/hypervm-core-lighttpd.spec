%define name    hypervm-core-lighttpd
%define packagename lighttpd
%define version 1.4.43
%define release 1%{?dist}

Name: %{name}
Version: %{version}
Release: %{release}


Summary: Webserver for LxCenter products (based on lighttpd)
License: BSD
Group: System Environment/Daemons
URL: http://www.lxcenter.org

SOURCE0: %{packagename}-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{packagename}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires(pre): /usr/sbin/useradd
Provides: webserver

BuildRequires: openssl-devel, pcre-devel, bzip2-devel, zlib-devel, spawn-fcgi
BuildRequires: /usr/bin/awk
BuildRequires: lua-devel

%if 0%{?rhel} <= 5
BuildRequires: readline-devel
%endif

Obsoletes: lxlighttpd

%description
This is the Core GUI webserver for LxCenter products (based on lighttpd)

%prep
%setup -q -n %{packagename}-%{version}

%build
%configure \
	--program-prefix= \
	--prefix=/usr/local/lxlabs/ext/lxlighttpd/ \
	--exec-prefix=/usr/local/lxlabs/ext/lxlighttpd/ \
	--bindir=/usr/local/lxlabs/ext/lxlighttpd/bin \
	--sbindir=/usr/local/lxlabs/ext/lxlighttpd/sbin/ \
	--libdir=/usr/local/lxlabs/ext/lxlighttpd/lib/ \
	--mandir=/usr/local/lxlabs/ext/lxlighttpd/share/man/ \
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
echo "Info: LxCenter Package for Own Usage at Home. Dont use it in production environment!"

/usr/sbin/useradd -s /sbin/nologin -M -r -d /home/lxlabs/ \
    -c "lighttpd web server" lxlabs &>/dev/null || :

%files
%defattr(-,root,root,-)
%dir %attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd"
%dir %attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_access.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_access.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_accesslog.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_accesslog.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_alias.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_alias.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_auth.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_auth.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_cgi.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_cgi.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_cml.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_cml.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_compress.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_compress.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_dirlisting.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_dirlisting.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_evasive.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_evasive.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_evhost.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_evhost.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_expire.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_expire.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_extforward.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_extforward.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_fastcgi.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_fastcgi.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_flv_streaming.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_flv_streaming.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_indexfile.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_indexfile.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_magnet.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_magnet.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_mysql_vhost.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_mysql_vhost.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_proxy.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_proxy.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_redirect.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_redirect.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_rewrite.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_rewrite.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_rrdtool.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_rrdtool.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_scgi.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_scgi.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_secdownload.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_secdownload.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_setenv.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_setenv.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_simple_vhost.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_simple_vhost.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_ssi.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_ssi.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_staticfile.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_staticfile.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_status.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_status.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_trigger_b4_dl.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_trigger_b4_dl.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_userdir.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_userdir.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_usertrack.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_usertrack.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_webdav.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_webdav.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_authn_file.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_authn_file.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_authn_mysql.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_authn_mysql.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_deflate.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_deflate.so"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_uploadprogress.la"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/lib/mod_uploadprogress.so"

%dir %attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/sbin"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/sbin/lighttpd"
%attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/sbin/lighttpd-angel"
%dir %attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/share"
%dir %attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/share/man"
%dir %attr(0755 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/share/man/man8"
%attr(0644 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/share/man/man8/lighttpd.8"
%attr(0644 lxlabs lxlabs) "/usr/local/lxlabs/ext/lxlighttpd/share/man/man8/lighttpd-angel.8"

%changelog
* Mon Dec 05 2016 Danny Terweij <danny@terweij.nl> 1.4.43-1
- Update to 1.4.43
- Own usage at home
- set packagename to hypervm-core-lighttpd

* Fri Jan 29 2016 Danny Terweij <danny@terweij.nl> 1.4.39-1
- Update to 1.4.39
- Own usage at home

* Tue Nov 17 2015 Danny Terweij <danny@terweij.nl> 1.4.37-1
- Update to 1.4.37
- Own usage at home

* Sun Aug 30 2015 Danny Terweij <danny@terweij.nl> 1.4.36-1
- Update to 1.4.36
- Own usage at home

* Mon Dec 17 2012 Danny Terweij <contact@lxcenter.org> 1.4.32-1
- Update to 1.4.32

* Thu Jan 26 2012 Danny Terweij <contact@lxcenter.org> 1.4.30-0
- Update to 1.4.30

* Sun Aug 21 2011 Danny Terweij <contact@lxcenter.org> 1.4.29-0
- Update to 1.4.29
- Added patch for RHEL/CentOS 6 systems (OpenSSL patents)
  See http://redmine.lighttpd.net/issues/2335 for details and patch

* Mon Feb 08 2010 Denis Frolov <d.frolov81@mail.ru> 1.4.26-1
- Update to 1.4.26

* Mon Nov 23 2009 Denis Frolov <d.frolov81@mail.ru> 1.4.25-1
- Update to 1.4.25

* Mon Oct 26 2009 Denis Frolov <d.frolov81@mail.ru> 1.4.24-1
- Update to 1.4.24

* Thu Sep 24 2009 Denis Frolov <d.frolov81@mail.ru> 1.4.23-1
- Rebuild for CentOS 5

* Thu Sep 3 2009 Matthias Saou <http://freshrpms.net/> 1.4.23-1
- Update to 1.4.23.
- Update defaultconf and mod_geoip patches.
- Remove no longer shipped spawn-fcgi, it's a separate source package now.
- Remove unused patch to the init script.

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.4.22-5
- rebuilt with new openssl

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr 12 2009 Matthias Saou <http://freshrpms.net/> 1.4.22-3
- Update init script to new style.
- No longer include a sysconfig file, though one can be set to override the
  default configuration file location.

* Mon Mar 30 2009 Matthias Saou <http://freshrpms.net/> 1.4.22-2
- Update to 1.4.22.
- Add missing defattr for the spawn-fcgi package.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Matthias Saou <http://freshrpms.net/> 1.4.21-1
- Update to 1.4.21.

* Sat Jan 24 2009 Caolán McNamara <caolanm@redhat.com> 1.4.20-7
- rebuild for dependencies

* Wed Dec 24 2008 Matthias Saou <http://freshrpms.net/> 1.4.20-6
- Partially revert last change by creating a "spawn-fastcgi" symlink, so that
  nothing breaks currently (especially for EL).
- Install empty poweredby image on RHEL since the symlink's target is missing.
- Split spawn-fcgi off in its own sub-package, have fastcgi package require it
  to provide backwards compatibility.

* Mon Dec 22 2008 Matthias Saou <http://freshrpms.net/> 1.4.20-3
- Rename spawn-fastcgi to lighttpd-spawn-fastcgi to avoid clash with other
  packages providing it for their own needs (#472749). It's not used as-is
  by lighttpd, so it shouldn't be a problem... at worst, some custom scripts
  will need to be updated.

* Mon Dec 22 2008 Matthias Saou <http://freshrpms.net/> 1.4.20-2
- Include conf.d/*.conf configuration snippets (#444953).
- Mark the default index.html in order to not loose changes upon upgrade if it
  was edited or replaced with a different file (#438564).
- Include patch to add the INIT INFO block to the init script (#246973).

* Mon Oct 13 2008 Matthias Saou <http://freshrpms.net/> 1.4.20-1
- Update to 1.4.20 final.

* Mon Sep 22 2008 Matthias Saou <http://freshrpms.net/> 1.4.20-0.1.r2303
- Update to 1.4.20 r2303 pre-release.

* Mon Sep 22 2008 Matthias Saou <http://freshrpms.net/> 1.4.19-5
- Include memory leak patch (changeset #2305 from ticket #1774).

* Thu Apr 24 2008 Matthias Saou <http://freshrpms.net/> 1.4.19-4
- Merge in second changest from upstream fix for upstream bug #285.

* Thu Mar 27 2008 Matthias Saou <http://freshrpms.net/> 1.4.19-3
- Include sslshutdown patch, upstream fix to upstream bug #285 (#439066).

* Sat Mar 22 2008 Matthias Saou <http://freshrpms.net/> 1.4.19-2
- Provide "webserver" (#437884).

* Wed Mar 12 2008 Matthias Saou <http://freshrpms.net/> 1.4.19-1
- Update to 1.4.19, which includes all previous security fixes + bugfixes.

* Tue Mar 4 2008 Matthias Saou <http://freshrpms.net/> 1.4.18-6
- Include patch for CVE-2008-0983 (crash when low on file descriptors).
- Include patch for CVE-2008-1111 (cgi source disclosure).

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org>
- Autorebuild for GCC 4.3

* Wed Dec 05 2007 Release Engineering <rel-eng at fedoraproject dot org>
 - Rebuild for deps

* Wed Oct 31 2007 Matthias Saou <http://freshrpms.net/> 1.4.18-3
- Update mod_geoip source to fix segfault upon stopping lighttpd.

* Mon Oct 22 2007 Matthias Saou <http://freshrpms.net/> 1.4.18-2
- Include mod_geoip additional source, make it an optional sub-package.
- Reorder sub-packages alphabetically in spec file.
- Make sub-packages require exact release, just in case.
- Change default webroot back from /srv to /var.

* Mon Sep 10 2007 Matthias Saou <http://freshrpms.net/> 1.4.18-1
- Update to 1.4.18.
- Include newly installed lighttpd-angel ("angel" process meant to always run
  as root and restart lighttpd when it crashes, spawn processes on SIGHUP), but
  it's in testing stage and must be run with -D for now.

* Wed Sep  5 2007 Matthias Saou <http://freshrpms.net/> 1.4.17-1
- Update to 1.4.17.
- Update defaultconf patch to match new example configuration.
- Include patch to fix log file rotation with max-workers set (trac #902).
- Add /var/run/lighttpd/ directory where to put fastcgi sockets.

* Thu Aug 23 2007 Matthias Saou <http://freshrpms.net/> 1.4.16-3
- Add /usr/bin/awk build requirement, used to get LIGHTTPD_VERSION_ID.

* Wed Aug 22 2007 Matthias Saou <http://freshrpms.net/> 1.4.16-2
- Rebuild to fix wrong execmem requirement on ppc32.

* Thu Jul 26 2007 Matthias Saou <http://freshrpms.net/> 1.4.16-1
- Update to 1.4.16 security fix release.

* Mon Apr 16 2007 Matthias Saou <http://freshrpms.net/> 1.4.15-1
- Update to 1.4.15.
- Remove now included previous patch.
- Switch to using the bz2 source.
- Add optional --with-webdav-locks support.

* Fri Feb 16 2007 Matthias Saou <http://freshrpms.net/> 1.4.13-6
- Include patch to fix 99% cpu bug when client connection is dropped.

* Fri Feb  2 2007 Matthias Saou <http://freshrpms.net/> 1.4.13-5
- Update defaultconf patch to change php binary to /usr/bin/php-cgi (#219723).
- Noticed %%{?_smp_mflags} was missing, so add it as it works fine.

* Mon Jan 29 2007 Matthias Saou <http://freshrpms.net/> 1.4.13-4
- Remove readline-devel build req, added by lua but since fixed (#213895).

* Mon Nov  6 2006 Matthias Saou <http://freshrpms.net/> 1.4.13-3
- Switch to using killall for log rotation to fix it when using workers.

* Mon Oct 16 2006 Matthias Saou <http://freshrpms.net/> 1.4.13-2
- Remove gcc-c++ build req, it's part of the defaults.
- Add readline-devel build req, needed on RHEL4.

* Wed Oct 11 2006 Matthias Saou <http://freshrpms.net/> 1.4.13-1
- Update to 1.4.13, which contains the previous fix.

* Tue Oct  3 2006 Matthias Saou <http://freshrpms.net/> 1.4.12-3
- Include fix for segfaults (lighttpd bug #876, changeset 1352).

* Mon Sep 25 2006 Matthias Saou <http://freshrpms.net/> 1.4.12-1
- Update to 1.4.12 final.

* Fri Sep 22 2006 Matthias Saou <http://freshrpms.net/> 1.4.12-0.1.r1332
- Update to latest 1.4.12 pre-release, fixes SSL issues and other bugs.
- Update powered_by_fedora.png to the new logo.

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 1.4.11-2
- FC6 rebuild.

* Thu Mar  9 2006 Matthias Saou <http://freshrpms.net/> 1.4.11-1
- Update to 1.4.11.

* Mon Mar  6 2006 Matthias Saou <http://freshrpms.net/> 1.4.10-2
- FC5 rebuild.

* Wed Feb  8 2006 Matthias Saou <http://freshrpms.net/> 1.4.10-1
- Update to 1.4.10.
- Remove now included fix.

* Wed Jan 25 2006 Matthias Saou <http://freshrpms.net/> 1.4.9-2
- Add mod_fastcgi-fix patch to fix crash on backend overload.

* Mon Jan 16 2006 Matthias Saou <http://freshrpms.net/> 1.4.9-1
- Update to 1.4.9.

* Wed Nov 23 2005 Matthias Saou <http://freshrpms.net/> 1.4.8-1
- Update to 1.4.8.

* Fri Nov  4 2005 Matthias Saou <http://freshrpms.net/> 1.4.7-1
- Update to 1.4.7.

* Wed Oct 12 2005 Matthias Saou <http://freshrpms.net/> 1.4.6-1
- Update to 1.4.6.

* Mon Oct  3 2005 Matthias Saou <http://freshrpms.net/> 1.4.5-1
- Update to 1.4.5.
- Disable gamin/fam support for now, it does not work.

* Tue Sep 27 2005 Matthias Saou <http://freshrpms.net/> 1.4.4-3
- Update to current SVN to check if it fixes the remaining load problems.

* Wed Sep 21 2005 Matthias Saou <http://freshrpms.net/> 1.4.4-2
- Patch to SVN 722 revision : Fixes a crash in mod_mysql_vhost and a problem
  with keepalive and certain browsers.

* Mon Sep 19 2005 Matthias Saou <http://freshrpms.net/> 1.4.4-1
- Update to 1.4.4 final.
- Enable ldap auth, gdbm and gamin/fam support by default.

* Thu Sep 15 2005 Matthias Saou <http://freshrpms.net/> 1.4.4-0
- Update to 1.4.4 pre-release (fixes another fastcgi memleak).
- Enable lua (cml module) by default.
- Add --with-webdav-props conditional option.

* Tue Sep 13 2005 Matthias Saou <http://freshrpms.net/> 1.4.3-2
- Include lighttpd-1.4.3-stat_cache.patch to fix memleak.

* Fri Sep  2 2005 Matthias Saou <http://freshrpms.net/> 1.4.3-1.1
- Rearrange the included index.html to include the new logo, button and
  favicon from lighttpd.net.

* Fri Sep  2 2005 Matthias Saou <http://freshrpms.net/> 1.4.3-1
- Update to 1.4.3.
- No longer override libdir at make install stage, use DESTDIR instead, as
  the resulting binary would now have referenced to %%{buildroot} :-(

* Tue Aug 30 2005 Matthias Saou <http://freshrpms.net/> 1.4.2-1
- Update to 1.4.2.

* Mon Aug 22 2005 Matthias Saou <http://freshrpms.net/> 1.4.1-1
- Update to 1.4.1.

* Sun Aug 21 2005 Matthias Saou <http://freshrpms.net/> 1.4.0-1
- Update to 1.4.0.
- Add conditional of gamin, gdbm, memcache and lua options.

* Mon Aug  1 2005 Matthias Saou <http://freshrpms.net/> 1.3.16-2
- Update to 1.3.16, rebuild.

* Mon Jul 18 2005 Matthias Saou <http://freshrpms.net/> 1.3.15-1
- Update to 1.3.15.

* Mon Jun 20 2005 Matthias Saou <http://freshrpms.net/> 1.3.14-1
- Update to 1.3.14.

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.3.13-5
- rebuild on all arches

* Mon Apr  4 2005 Matthias Saou <http://freshrpms.net/> 1.3.13-4
- Change signal sent from the logrotate script from USR1 to HUP, as that's the
  correct one.

* Fri Apr  1 2005 Michael Schwendt <mschwendt[AT]users.sf.net> 1.3.13-2
- Include /etc/lighttpd directory.

* Sun Mar  6 2005 Matthias Saou <http://freshrpms.net/> 1.3.13-1
- Update to 1.3.13.

* Wed Mar  2 2005 Matthias Saou <http://freshrpms.net/> 1.3.12-1
- Update to 1.3.12.
- Remove obsolete empty_cgi_handler patch.

* Tue Mar  1 2005 Matthias Saou <http://freshrpms.net/> 1.3.11-2
- Add missing defattr to sub-packages (#150018).

* Mon Feb 21 2005 Matthias Saou <http://freshrpms.net/> 1.3.11-0
- Update to 1.3.11.
- Remove cleanconf and init.d patches (merged upstream).
- Add empty_cgi_handler patch.

* Fri Feb 18 2005 Matthias Saou <http://freshrpms.net/> 1.3.10-0
- Split off -fastcgi sub-package.
- Include php.d entry to set sane FastCGI defaults.

* Wed Feb 16 2005 Matthias Saou <http://freshrpms.net/> 1.3.10-0
- Spec file cleanup for freshrpms.net/Extras.
- Compile OpenSSL support unconditionally.
- Put modules in a subdirectory of libdir.
- Don't include all of libdir's content to avoid debuginfo content.
- Add optional LDAP support.
- Add patch to change the default configuration.
- Add dedicated lighttpd user/group creation.
- Add logrotate entry.
- Include a nice little default page for the default setup.
- Split off mod_mysql_vhost sub-package, get dep only there.
- Use webroot in /srv by default.
- Exclude .la files, I doubt anyone will need them.

* Thu Sep 30 2004 <jan@kneschke.de> 1.3.1
- upgraded to 1.3.1

* Tue Jun 29 2004 <jan@kneschke.de> 1.2.3
- rpmlint'ed the package
- added URL
- added (noreplace) to start-script
- change group to Networking/Daemon (like apache)

* Sun Feb 23 2003 <jan@kneschke.de>
- initial version

