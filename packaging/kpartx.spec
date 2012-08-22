Summary: Tools to manage multipath devices using device-mapper
Name: kpartx
Version: 0.4.9
Release: 7
License: GPL+
Group: System/Base
URL: http://christophe.varoqui.free.fr/
Source0: http://christophe.varoqui.free.fr/multipath-tools/multipath-tools-%{version}.tar.bz2
Patch0: udev.patch
Requires: device-mapper >= 1.02.02-2
BuildRequires: device-mapper-devel
BuildRequires: readline-devel, ncurses-devel
BuildRequires: readline-devel
BuildRequires: ncurses-devel
Obsoletes: device-mapper-multipath

%description
%{name} provides tools to manage multipath devices by
instructing the device-mapper multipath kernel module what to do. 
The tools are :
* multipath :   Scan the system for multipath devices and assemble them.
* multipathd :  Detects when paths fail and execs multipath to update things.

%prep
%setup -q -c -n multipath-tools-%{version}
%patch0 -p1

%build
cd kpartx
make %{?_smp_mflags} 

%install
rm -rf $RPM_BUILD_ROOT
cd kpartx
make install DESTDIR=$RPM_BUILD_ROOT bindir=/sbin

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root,-)
/sbin/kpartx
%{_libdir}/udev/rules.d/kpartx.rules
/%{_lib}/udev/kpartx_id
%{_mandir}/man8/kpartx.8.gz

