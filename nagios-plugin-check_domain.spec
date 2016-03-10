%define		plugin	check_domain
Summary:	Nagios/Icinga plugin for checking a domain name expiration date
Name:		nagios-plugin-%{plugin}
Version:	1.4.6
Release:	1
License:	GPL
Group:		Networking
Source0:	https://github.com/glensc/monitoring-plugin-check_domain/archive/v%{version}/%{plugin}-%{version}.tar.gz
# Source0-md5:	1a27f053cbb2d7ea4b26a79ed5d9a0c6
URL:		https://github.com/glensc/monitoring-plugin-check_domain
Requires:	whois
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nagios/plugins
%define		plugindir	%{_prefix}/lib/nagios/plugins

%description
Nagios/Icinga plugin for checking a domain name expiration date.

%prep
%setup -q -n monitoring-plugin-%{plugin}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{plugindir}}
install -p %{plugin}.sh $RPM_BUILD_ROOT%{plugindir}/%{plugin}
sed -e 's,@plugindir@,%{plugindir},' %{plugin}.cfg > $RPM_BUILD_ROOT%{_sysconfdir}/%{plugin}.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{plugin}.cfg
%attr(755,root,root) %{plugindir}/%{plugin}
