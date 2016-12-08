%define kloxo /usr/local/lxlabs/kloxo/
%define productname kloxo
%define packagename theme-feather
%define sourcename %{packagename}

Name: %{productname}-%{packagename}
Summary: Feather Kloxo Theme 
Version: 1.0
Release: 1%{?dist}
License: AGPLV3
URL: http://www.lxcenter.org/
Group: Kloxo

Source0: %{name}.zip

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

%description
The Feather Kloxo Theme

%prep
%setup -c -n %{name}

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir} -p -m0755 $RPM_BUILD_ROOT%{kloxo}
%{__cp} -rp * $RPM_BUILD_ROOT%{kloxo}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(644,lxlabs,lxlabs,755)
%{kloxo}

%changelog
* Wed Feb 12 2014 Danny Terweij <contact@lxcenter.org> - 1.0-1
- Initial start of this SPEC
