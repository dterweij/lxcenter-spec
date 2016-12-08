#
#    LxCenter RPM packages
#
#    Copyright (C) 2000-2009    LxLabs
#    Copyright (C) 2009-2013    LxCenter
#    Copyright (C) 2013-2016    dterweij
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

%define productname hypervm
%define destination /usr/local/lxlabs/%{productname}

Name: %{productname}
Summary: HyperVM - Virtualisation manager for OpenVZ/Xen
Version: 2.1.999
Release: 1%{?dist}
License: AGPLV3
URL: http://www.lxcenter.org/
Group: Applications/Internet

Source0: %{name}-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

# Stop installing if those are found
Conflicts: kloxo
# Not wanted packages
Obsoletes: lxlighttpd

# Defaults
Requires: mysql, mysql-server
Requires: openssl
Requires: wget, yum, zip, unzip, tar, which, yum-protectbase
Requires: rrdtool

# LxCenter Repository
Requires: lxcenter-release
# Core
Requires: hypervm-core-lighttpd
Requires: hypervm-core-php

Provides: %{name}

%description
Virtualization Manager for OpenVZ and Xen.

%pre
echo "Info: Starting LxCenter checks..."
    if [ -f /script/version ]; then
        echo "Info: Script dir found."
        if [ -d /usr/local/%{brand}/hypervm ]; then
                echo "Info: HyperVM found, checking for the version."
                versioncheck=`/script/version`
                echo "Info: Found HyperVM version: $versioncheck"
                        if [ $versioncheck == "2.0.7993" ]; then
                                echo "Error: This package only works with HyperVM 2.1.0+"
                                exit 1
                        fi
        fi
    else
        echo "Error: You have to install HyperVM first with the installer."
        exit 1
    fi

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
* Thu Dec 08 2016 Danny Terweij <danny@terweij.nl> - 2.1.999-1
- Initial start of this SPEC
