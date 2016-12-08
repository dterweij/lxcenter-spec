# $Id: lxcenter-release.spec 1 2010-06-18 19:00:32Z lxcenter $
# Authority: lxcenter
# Upstream: lxcenter <system@lxcenter.org>

%define distribution        %(/usr/lib/rpm/redhat/dist.sh --distnum)

Summary: LxCenter release file and package configuration
Name: lxcenter-release
Version: 0.0.2
Release: 1
License: AGPLV3
Group: System Environment/Base
URL: http://lxcenter.org/

Source0: mirrors-lxcenter.tar.gz
BuildArch: noarch
Packager: lxcenter <system@lxcenter.org>
Vendor: LxCenter Repository, http://download.lxcenter.org/
BuildRequires: redhat-rpm-config


BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# Default when no match
SOURCE1: lxcenter.C6.yum

%if %{distribution} == 5
SOURCE1: lxcenter.C5.yum
%endif

%if %{distribution} == 6
SOURCE1: lxcenter.C6.yum
%endif

%description
LxCenter release file. This package contains yum configuration for the 
LxCenter RPM Repository.

%prep
%setup -c

MIRRORFILE="mirrors-lxcenter"

for mirror in $(%{__cat} $MIRRORFILE); do
	echo "$mirror/download/update/centos-%{distribution}/\$ARCH/"
done >mirrors-lxcenter.yum

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/yum.repos.d/lxcenter.repo
%{__install} -Dp -m0644 mirrors-lxcenter.yum %{buildroot}%{_sysconfdir}/yum.repos.d/mirrors-lxcenter

%clean
%{__rm} -rf %{buildroot}

%post

%files
%defattr(-, root, root, 0755)
%dir %{_sysconfdir}/yum.repos.d/
%config %{_sysconfdir}/yum.repos.d/lxcenter.repo
%config %{_sysconfdir}/yum.repos.d/mirrors-lxcenter

%changelog
* Mon Oct 06 2013 LxCenter <system@lxcenter.org> - 0.0.2-1
- Updated mirror file
- Detect centos version

* Fri May 06 2011 LxCenter <system@lxcenter.org> - 0.0.1-7
- Updated mirror file (repacked with proper mirror file)

* Tue May 03 2011 LxCenter <system@lxcenter.org> - 0.0.1-6
- Updated mirror file
- Added SRPMS repo
- Fixed typo lxcenter-test section

* Fri Jun 18 2010 LxCenter <system@lxcenter.org> - 0.0.1-1
- Initial package CentOS 5.
