#
%define		snap	20060715
#
Summary:	Shared library to access the contents of an iPod
Summary(pl):	Biblioteka wspó³dzielona do dostêpu do zawarto¶ci iPodów
Name:		libgpod
Version:	0.3.3
Release:	2.%{snap}.1
Epoch:		0
License:	GPL v2
Group:		Libraries
#Source0:	http://dl.sourceforge.net/gtkpod/%{name}-%{version}-%{snap}.tar.gz
Source0:	%{name}-%{version}-%{snap}.tar.bz2
# Source0-md5:	6d8684739f5229cfe1e97d3f3d086149
URL:		http://www.gtkpod.org/libgpod.html
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.71
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.10.1
BuildRequires:	hal-devel >= 0.5.7.1
BuildRequires:	hal-devel < 0.6
BuildRequires:	intltool >= 0.35
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgpod is a library meant to abstract access to an iPod content. It
provides an easy to use API to retrieve the list of files and playlist
stored on an iPod, to modify them and to save them back to the iPod.

%description -l pl
libgpod to biblioteka maj±ca na celu wyabstrahowanie dostêpu do
zawarto¶ci iPodów. Udostêpnia ³atwe w u¿yciu API do pobierania listy
plików i playlist zapisanych na iPodzie, modyfikowania ich i
zapisywania z powrotem na iPoda.

%package devel
Summary:	Header files for libgpod library
Summary(pl):	Pliki nag³ówkowe biblioteki libgpod
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-glib-devel >= 0.71
Requires:	gtk+2-devel >= 2:2.10.1
Requires:	hal-devel >= 0.5.7.1

%description devel
This is the package containing the header files for libgpod library.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe biblioteki libgpod.

%package static
Summary:	Static libgpod library
Summary(pl):	Statyczna biblioteka libgpod
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgpod library.

%description static -l pl
Statyczna biblioteka libgpod.

%prep
%setup -q

%build
%{__gtkdocize}
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-eject-command="/usr/bin/eject" \
	--with-unmount-command="/bin/umount"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libgpod.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libgpod.la
%attr(755,root,root) %{_libdir}/libgpod.so
%{_pkgconfigdir}/libgpod-1.0.pc
%{_includedir}/gpod-1.0

%files static
%defattr(644,root,root,755)
%{_libdir}/libgpod.a
