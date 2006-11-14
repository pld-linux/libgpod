Summary:	Shared library to access the contents of an iPod
Summary(pl):	Biblioteka wspó³dzielona do dostêpu do zawarto¶ci iPodów
Name:		libgpod
Version:	0.4.0
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/gtkpod/%{name}-%{version}.tar.gz
# Source0-md5:	e427e0409b0cb2d7e76b17915b1396fa
URL:		http://www.gtkpod.org/libgpod.html
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.71
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.10.1
BuildRequires:	gtk-doc
BuildRequires:	hal-devel < 0.6
BuildRequires:	hal-devel >= 0.5.7.1
BuildRequires:	intltool >= 0.35
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-eyeD3 >= 0.6.6
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

%package -n python-gpod
Summary:	Libraries for libgpod access from Python
Summary(pl):	Biblioteki Pythona dla biblioteki libgpod
Group:		Development/Languages/Python
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	python-eyeD3 >= 0.6.6
%pyrequires_eq	python-libs

%description -n python-gpod
This is the libgpod Python support package.

%description -n python-gpod -l pl
Biblioteki umo¿liwiaj±ce korzystanie z libgpod z poziomu
Pythona.

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
	--with-unmount-command="/bin/umount" \
	--with-python=yes
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

%files -n python-gpod
%defattr(644,root,root,755)
%{py_sitescriptdir}/*
