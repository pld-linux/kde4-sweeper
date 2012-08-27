#
# Conditional build:
#
%define         orgname     sweeper
%define         _state      stable
%define         qtver       4.8.0
#
Summary:	System cleaner
Summary(pl.UTF-8):	sweeper
Name:		kde4-sweeper
Version:	4.9.0
Release:	1
License:	LGPL v2
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	46976161a1e39212fdf6d4b8f7ee7be5
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
%attr(755,root,root) %{_bindir}/calgebra
%attr(755,root,root) %ghost %{_libdir}/libsweeper.so.?
%attr(755,root,root) %{_libdir}/libsweeper.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsweepergui.so.?
%attr(755,root,root) %{_libdir}/libsweepergui.so.*.*.*
