
# Conditional build:
#
%define         orgname     sweeper
%define         _state      stable
%define         qtver       4.8.0
#
Summary:	System cleaner
Summary(pl.UTF-8):	sweeper
Name:		kde4-sweeper
Version:	4.9.1
Release:	1
License:	LGPL v2
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	07a3d38100127b4a8c414ab7d452122b
URL:		http://www.kde.org/
BuildRequires:	automoc4
BuildRequires:	cmake >= 2.6.3
BuildRequires:	kde4-kdelibs-devel >= %{_kdever}
BuildRequires:	qt4-build >= %{qt_ver}
BuildRequires:	qt4-qmake >= %{qt_ver}
BuildRequires:	readline-devel
BuildRequires:	rpmbuild(macros) >= 1.293
Obsoletes:	kde4-kdeutils-sweeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
System cleaner.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sweeper
%{_desktopdir}/kde4/sweeper.desktop
%dir %{_datadir}/apps/sweeper
%{_datadir}/apps/sweeper/sweeperui.rc
%{_datadir}/dbus-1/interfaces/org.kde.sweeper.xml
%{_docdir}/kde/HTML/en/sweeper
