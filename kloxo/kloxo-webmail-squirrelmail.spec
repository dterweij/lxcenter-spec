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

%define kloxo /home/kloxo/httpd/webmail
%define productname kloxo-webmail
%define packagename squirrelmail

Name: %{productname}-%{packagename}
Summary: SquirrelMail webmail client
Version: 1.4.22
Release: 1%{?dist}
License: GPL
URL: http://www.squirrelmail.org/
Group: Applications/Internet
Source0: http://prdownloads.sourceforge.net/squirrelmail/%{packagename}-webmail-%{version}.tar.bz2
Source4: http://prdownloads.sourceforge.net/squirrelmail/all_locales-1.4.18-20090526.tar.bz2

# Added settings for courier-imapd
Source5: config_local.php

BuildRoot: %{_tmppath}/%{packagename}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
BuildRequires: gettext, findutils, tar
Requires: php >= 5.2.17, php-mbstring, perl, tmpwatch >= 2.8, aspell, perl
Provides: squirrelmail

%description
SquirrelMail is a standards-based webmail package written in PHP4. It
includes built-in pure PHP support for the IMAP and SMTP protocols, and
all pages render in pure HTML 4.0 (with no Javascript) for maximum
compatibility across browsers.  It has very few requirements and is very
easy to configure and install. SquirrelMail has all the functionality
you would want from an email client, including strong MIME support,
address books, and folder manipulation.

%prep
%setup -q -n squirrelmail-webmail-%{version}

mkdir locale_tempdir
cd locale_tempdir
tar xfj %SOURCE4

%build
rm -f plugins/make_archive.pl

# Clean up .orig files
find -name '*.orig' -exec rm -f \{\} \;

# Rearrange the documentation
for f in `find plugins -name "README*" -or -name INSTALL \
		   -or -name CHANGES -or -name HISTORY`; do
    mkdir -p doc/`dirname $f`
    mv $f $_
done
mv doc/plugins/squirrelspell/doc/README doc/plugins/squirrelspell
rmdir doc/plugins/squirrelspell/doc
mv plugins/squirrelspell/doc/* doc/plugins/squirrelspell
rm -f doc/plugins/squirrelspell/index.php
rmdir plugins/squirrelspell/doc
%{__perl} -pi -e "s{\.\./}{}g" doc/index.html

# Fixup various files
echo "left_refresh=300" >> data/default_pref
for f in contrib/RPM/squirrelmail.cron contrib/RPM/config.php.redhat; do
    perl -pi -e "s|__ATTDIR__|%{kloxo}/squirrelmail/attach/|g;"\
	 -e "s|__PREFSDIR__|%{kloxo}/squirrelmail/prefs/|g;" $f
done

# Fix the version
%{__perl} -pi -e "s|^(\s*\\\$version\s*=\s*'[^']+)'|\1-%{release}'|g"\
    functions/strings.php

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p -m0755 $RPM_BUILD_ROOT%{kloxo}/squirrelmail
mkdir -p -m0755 $RPM_BUILD_ROOT%{kloxo}/squirrelmail/prefs
mkdir -p -m0755 $RPM_BUILD_ROOT%{kloxo}/squirrelmail/attach
mkdir -p -m0755 $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily

# install default_pref
install -m 0644 data/default_pref \
    $RPM_BUILD_ROOT%{kloxo}/squirrelmail/
ln -s %{kloxo}/squirrelmail/default_pref \
    $RPM_BUILD_ROOT%{kloxo}/squirrelmail/prefs/default_pref

# install the config files
mkdir -p -m0755 $RPM_BUILD_ROOT%{kloxo}/squirrelmail/config
install -m 0644 config/*.php $RPM_BUILD_ROOT%{kloxo}/squirrelmail/config/
rm -f $RPM_BUILD_ROOT%{kloxo}/squirrelmail/config/config_local.php
install -m 0644 %{SOURCE5} \
    $RPM_BUILD_ROOT%{kloxo}/squirrelmail/config_local.php
ln -s %{kloxo}/squirrelmail/config_local.php \
    $RPM_BUILD_ROOT%{kloxo}/squirrelmail/config/config_local.php
install -m 0644 contrib/RPM/config.php.redhat \
    $RPM_BUILD_ROOT%{kloxo}/squirrelmail/config.php
ln -s %{kloxo}/squirrelmail/config.php \
    $RPM_BUILD_ROOT%{kloxo}/squirrelmail/config/config.php
install -m 0755 config/*.pl $RPM_BUILD_ROOT%{kloxo}/squirrelmail/config/

# install index.php
install -m 0644 index.php $RPM_BUILD_ROOT%{kloxo}/squirrelmail/

# copy over the rest
for d in class functions help images include locale plugins src themes; do
    cp -rp $d $RPM_BUILD_ROOT%{kloxo}/squirrelmail/
done

# install the cron script
install -m 0755 contrib/RPM/squirrelmail.cron \
    $RPM_BUILD_ROOT/%{_sysconfdir}/cron.daily/

# move sqspell plugin config to /etc
rm -f $RPM_BUILD_ROOT%{kloxo}/squirrelmail/plugins/squirrelspell/sqspell_config.php
install -m 0644 plugins/squirrelspell/sqspell_config.php \
    $RPM_BUILD_ROOT%{kloxo}/squirrelmail/sqspell_config.php
ln -s %{kloxo}/squirrelmail/sqspell_config.php \
    $RPM_BUILD_ROOT%{kloxo}/squirrelmail/plugins/squirrelspell/sqspell_config.php

cd locale_tempdir
cp -r locale/* $RPM_BUILD_ROOT%{kloxo}/squirrelmail/locale/
cp -r images/* $RPM_BUILD_ROOT%{kloxo}/squirrelmail/images/
cp -r help/* $RPM_BUILD_ROOT%{kloxo}/squirrelmail/help/
cd ..
rm $RPM_BUILD_ROOT%{kloxo}/squirrelmail/locale/README.locales

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,lxlabs,lxlabs)
%config %dir %{kloxo}/squirrelmail
%attr(640,root,apache) %config(noreplace) %{kloxo}/squirrelmail/*.php
%attr(640,root,apache) %config(noreplace) %{kloxo}/squirrelmail/default_pref
%doc doc/*
%dir %{kloxo}/squirrelmail
%{kloxo}/squirrelmail/class
%{kloxo}/squirrelmail/config
%{kloxo}/squirrelmail/functions
%{kloxo}/squirrelmail/help
%{kloxo}/squirrelmail/images
%{kloxo}/squirrelmail/include
%{kloxo}/squirrelmail/locale
%{kloxo}/squirrelmail/plugins
%{kloxo}/squirrelmail/src
%{kloxo}/squirrelmail/themes
%{kloxo}/squirrelmail/index.php
%attr(0700, apache, apache) %dir %{kloxo}/squirrelmail/prefs
%attr(0700, apache, apache) %dir %{kloxo}/squirrelmail/attach
%{kloxo}/squirrelmail/prefs/default_pref
%{_sysconfdir}/cron.daily/squirrelmail.cron

%changelog
* Sat Feb 18 2012 Danny Terweij <contact@lxcenter.org> - 1.4.22-1
- Refactored specfile
- Make use of courier-imapd because Kloxo uses it.
- Updated locales package
- Updated to 1.4.22

* Tue Oct 27 2009 Karanbir Singh <kbsingh@centos.org> - 1.4.8-5.el5.centos.10
- Remove upstream branding

* Mon Oct 05 2009 Michal Hlavinka <mhlavink@redhat.com> - 1.4.8-5.10
- fix: CVE-2009-2964 : CSRF issues in all forms - extend to all forms

* Tue Sep 29 2009 Michal Hlavinka <mhlavink@redhat.com> - 1.4.8-5.9
- fix: CVE-2009-2964 : CSRF issues in all forms - add missing parts

* Tue Sep 15 2009 Michal Hlavinka <mhlavink@redhat.com> - 1.4.8-5.8
- fix: CVE-2009-2964 : CSRF issues in all forms

* Thu May 21 2009 Michal Hlavinka <mhlavink@redhat.com> - 1.4.8-5.7
- fix broken patch for CVE-2009-1579

* Wed May 20 2009 Michal Hlavinka <mhlavink@redhat.com> - 1.4.8-5.6
- fix broken patch for CVE-2009-1579

* Thu May 14 2009 Michal Hlavinka <mhlavink@redhat.com> - 1.4.8-5.5
- don't ship patch backup files

* Thu May 14 2009 Michal Hlavinka <mhlavink@redhat.com> - 1.4.8-5.4
- fix: CVE-2009-1581 : CSS positioning vulnerability
- fix: CVE-2009-1579 : Server-side code injection in map_yp_alias username map
- fix: CVE-2009-1578 : Multiple cross site scripting issues

* Sat Jan 17 2009 Tomas Hoger <thoger@redhat.com> - 1.4.8-5.3
- Update patch for CVE-2008-3663 to fix a session handling regression (#480224)

* Mon Dec 1 2008 Michal Hlavinka <mhlavink@redhat.com> - 1.4.8-5.2
- Resolves: CVE-2008-2379
- fix XSS issue caused by an insufficient html mail sanitation

* Fri Nov 28 2008 Michal Hlavinka <mhlavink@redhat.com> - 1.4.8-5.1
- don't transmit cookies under non-SSL connections if the session
  is started under an SSL (https) connection
- Resolves: CVE-2008-3663, #468398
- fix release number with respect to Z-stream nvr policy

* Thu May 10 2007 Martin Bacovsky <mbacovsk@redhat.com> - 1.4.8-4.0.1
- resolves: #239648: CVE-2007-1262 squirrelmail cross-site scripting flaw

* Mon Jan 22 2007 Warren Togami <wtogami@redhat.com> 1.4.8-4
- Clean up .orig files (#223648)

* Mon Jan 15 2007 Warren Togami <wtogami@redhat.com> 1.4.8-3
- CVE-2006-6142

* Tue Aug 15 2006 Warren Togami <wtogami@redhat.com> 1.4.8-2
- more Japanese filename fixes (#195639)

* Fri Aug 11 2006 Warren Togami <wtogami@redhat.com> 1.4.8-1
- 1.4.8 release with CVE-2006-4019 and upstream bug fixes

* Tue Jul 18 2006 Warren Togami <wtogami@redhat.com> 1.4.7-5
- More JP translation updates (#194598)

* Mon Jul 10 2006 Warren Togami <wtogami@redhat.com> 1.4.7-4
- Fix fatal typo in config_local.php (#198306)

* Sun Jul 09 2006 Warren Togami <wtogami@redhat.com> 1.4.7-2
- Move sqspell_config.php to /etc and mark it %%config(noreplace) (#192236)

* Fri Jul 07 2006 Warren Togami <wtogami@redhat.com> 1.4.7-1
- 1.4.7 with CVE-2006-3174
- Reduce patch for body text (#194457)
- Better JP translation for "Check mail" (#196117)

* Fri Jun 23 2006 Warren Togami <wtogami@redhat.com> 1.4.6-8
- Japanese zenkaku subject conversion      (#196017)
- Japanese MSIE garbled download ugly hack (#195639)
- Japanese multibyte attachment view text  (#195452)
- Japanese multibyte attachment body text  (#194457)
- Do not convert Japanese Help to UTF-8    (#194599)

* Wed Jun 07 2006 Warren Togami <wtogami@redhat.com> 1.4.6-7
- CVE-2006-2842 File Inclusion Vulnerability

* Mon Jun 05 2006 Warren Togami <wtogami@redhat.com> 1.4.6-6
- buildreq gettext (194169)

* Tue Apr 04 2006 Warren Togami <wtogami@redhat.com> 1.4.6-5
- Fix Chinese and Korean too

* Fri Mar 24 2006 Warren Togami <wtogami@redhat.com> 1.4.6-4
- Fix outgoing Japanese mail to iso-2022-jp for now (#185767)

* Fri Mar 3 2006 Warren Togami <wtogami@redhat.com> 1.4.6-3
- Fix regex in doc mangling (#183943 Michal Jaegermann)

* Fri Mar 3 2006 David Woodhouse <dwmw2@redhat.com> 1.4.6-2
- Add a %%build section, move the file mangling to it.
  (#162852 Nicolas Mailhot)

* Wed Mar 1 2006 David Woodhouse <dwmw2@redhat.com> 1.4.6-1
- Upgrade to 1.4.6 proper for CVE-2006-0377 CVE-2006-0195 CVE-2006-0188
- Script the charset changes instead of using a patch
- Convert the ko_KR files to UTF-8, dropping invalid characters from
  what's theoretically supposed to be EUC-KR in the original.

* Tue Jan 17 2006 Warren Togami <wtogami@redhat.com> 1.4.6-0.cvs20050812.3
- do not remove mo files
- require php-mbstring

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Sep 12 2005 David Woodhouse <dwmw2@redhat.com> 1.4.6-0.cvs20050812.2
- Convert all locales to UTF-8 instead of legacy character sets to
  work around bug #162852. Except for ko_KR, because iconv doesn't
  believe its help files are actually in EUC-KR as claimed.

* Sun Aug 14 2005 Warren Togami <wtogami@redhat.com> 1.4.6-0.cvs20050812.1
- snapshot of 1.4.6 because 1.4.5 upstream was a bad release
  this hopefully will also work on PHP5 too...

* Mon Jun 20 2005 Warren Togami <wtogami@redhat.com> 1.4.5-0.rc1
- 1.4.5-0.rc1

* Thu Jan 27 2005 Warren Togami <wtogami@redhat.com> 1.4.4-2
- 1.4.4
- re-include translations and Provide squirrelmail-i18n
  better compatible with upstream, but we cannot split sub-package
  due to support of existing distributions
- remove unnecessary .po files

* Fri Nov 19 2004 Warren Togami <wtogami@redhat.com> 1.4.3a-7
- CAN-2004-1036 Cross Site Scripting in encoded text
- #112769 updated splash screens

* Thu Oct 14 2004 Warren Togami <wtogami@redhat.com> 1.4.3a-5
- default_folder_prefix dovecot compatible by default
  /etc/squirrelmail/config_local.php if you must change it

* Wed Oct 13 2004 Warren Togami <wtogami@redhat.com> 1.4.3a-4
- HIGASHIYAMA Masato's patch to improve Japanese support
  (coordinated by Scott A. Hughes).
- real 1.4.3a tarball

* Tue Sep 21 2004 Gary Benson <gbenson@redhat.com> 1.4.3-3
- rebuilt.

* Tue Aug 31 2004 Warren Togami <wtogami@redhat.com> 1.4.3-2
- #125638 config_local.php and default_pref in /etc/squirrelmail/
  to match upstream RPM.  This should allow smoother drop-in
  replacements and upgrades.
- other spec cleanup.

* Mon Jun  7 2004 Gary Benson <gbenson@redhat.com> 1.4.3-1
- upgrade to 1.4.3a.
- retain stuff after version when adding release to it.

* Wed Jun  2 2004 Gary Benson <gbenson@redhat.com>
- upgrade to 1.4.3.

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt.

* Wed Jan 21 2004 Gary Benson <gbenson@redhat.com> 1.4.2-2
- fix calendar plugin breakage (#113902).

* Thu Jan  8 2004 Gary Benson <gbenson@redhat.com> 1.4.2-1
- upgrade to 1.4.2.
- tighten up permissions on /etc/squirrelmail/config.php (#112774).

* Mon May 12 2003 Gary Benson <gbenson@redhat.com> 1.4.0-1
- upgrade to 1.4.0.
- fix links in /usr/share/doc/squirrelmail-X.Y.Z/index.html (#90269).

* Mon Mar 24 2003 Gary Benson <gbenson@redhat.com> 1.2.11-1
- upgrade to 1.2.11 to fix CAN-2003-0160.

* Mon Feb 10 2003 Gary Benson <gbenson@redhat.com> 1.2.10-4
- fix syntax error in download.php (#82600).
- resized splash screen to be the same size as the one it replaces
  (#82790)
- remove piece of squirrelmail-1.2.10-xss.patch that changed the
  version from '1.2.10' to '1.2.11 [cvs]'

* Wed Jan 22 2003 Tim Powers <timp@redhat.com> 1.2.10-3
- rebuilt

* Wed Jan 15 2003 Tim Powers <timp@redhat.com> 1.2.10-2
- bump and rebuild

* Mon Dec  9 2002 Gary Benson <gbenson@redhat.com> 1.2.10-1
- patch to fix CAN-2002-1341 (#78982) and CAN-2002-1276 (#79147).

* Tue Dec 03 2002 Elliot Lee <sopwith@redhat.com> 1.2.8-2
- fix prep macro in changelog

* Fri Sep 20 2002 Gary Benson <gbenson@redhat.com> 1.2.8-1
- upgrade to 1.2.8 to fix CAN-2002-1131 and CAN-2002-1132 (#74313)

* Tue Aug  6 2002 Preston Brown <pbrown@redhat.com> 1.2.7-4
- replacement splash screen.

* Mon Jul 22 2002 Gary Benson <gbenson@redhat.com> 1.2.7-3
- get rid of long lines in the specfile.
- remove symlink in docroot and use an alias in conf.d instead.
- work with register_globals off (#68669)

* Tue Jul 09 2002 Gary Benson <gbenson@redhat.com> 1.2.7-2
- hardwire the hostname (well, localhost) into the config file (#67635)

* Mon Jun 24 2002 Gary Benson <gbenson@redhat.com> 1.2.7-1
- hardwire the locations into the config file and cron file.
- install squirrelmail-cleanup.cron as squirrelmail.cron.
- make symlinks relative.
- upgrade to 1.2.7.
- more dependency fixes.

* Fri Jun 21 2002 Gary Benson <gbenson@redhat.com>
- summarize the summary, fix deps, and remove some redundant stuff.
- tidy up the prep section.
- replace directory definitions with standard RHL ones.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 1.2.6-3
- automated rebuild

* Wed Jun 19 2002 Preston Brown <pbrown@redhat.com> 1.2.6-2
- adopted Konstantin Riabitsev <icon@duke.edu>'s package for Red Hat
  Linux.  Nice job Konstantin!
