# TODO
# check: http://fred.uwcs.co.uk/diff (from http://www.fredemmott.co.uk/blog_121)
# some warning at doc build:
#warning: failed to load external entity "../../docs/reference/xml/*.xml"
#unable to parse ../../docs/reference/xml/*.xml
#make[3]: [gpod_doc.i] Error 6 (ignored)
# - mountdir perms?: %dir %{_localstatedir}/run/%{name}
%include	/usr/lib/rpm/macros.mono
#
Summary:	Shared library to access the contents of an iPod
Summary(pl.UTF-8):	Biblioteka współdzielona do dostępu do zawartości iPodów
Name:		libgpod
Version:	0.8.0
Release:	4
License:	GPL v2
Group:		Libraries
Source0:	http://downloads.sourceforge.net/gtkpod/%{name}-%{version}.tar.gz
# Source0-md5:	6660f74cc53293dcc847407aa5f672ce
Patch0:		%{name}-gcc43.patch
Patch1:		%{name}-monodir.patch
URL:		http://www.gtkpod.org/libgpod/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.12.0
BuildRequires:	gdk-pixbuf2-devel >= 2.6.0
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	hal-devel < 0.6
BuildRequires:	hal-devel >= 0.5.7.1
BuildRequires:	intltool >= 0.35
BuildRequires:	libimobiledevice-devel >= 0.9.7
BuildRequires:	libplist-devel >= 1.0.0
BuildRequires:	libtool
BuildRequires:	libusb-devel
BuildRequires:	libxml2-devel
BuildRequires:	mono-devel >= 1.9.1
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2.1.1
BuildRequires:	python-eyeD3 >= 0.6.6
BuildRequires:	python-mutagen >= 1.8
BuildRequires:	python-pygobject-devel >= 2.8.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(monoautodeps)
BuildRequires:	sg3_utils-devel >= 1.26
BuildRequires:	sqlite3-devel
BuildRequires:	swig-python >= 1.3.24
BuildRequires:	zlib-devel
BuildRequires:	libsmbios-devel
# for noinst test only
#BuildRequires:	taglib-devel
Suggests:	hal-libgpod = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgpod is a library meant to abstract access to an iPod content. It
provides an easy to use API to retrieve the list of files and playlist
stored on an iPod, to modify them and to save them back to the iPod.

%description -l pl.UTF-8
libgpod to biblioteka mająca na celu wyabstrahowanie dostępu do
zawartości iPodów. Udostępnia łatwe w użyciu API do pobierania listy
plików i playlist zapisanych na iPodzie, modyfikowania ich i
zapisywania z powrotem na iPoda.

%package -n hal-libgpod
Summary:	HAL callout program for iPod devices
Summary(pl.UTF-8):	Program wywoływany przez HAL dla urządzeń iPod
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	hal >= 0.5

%description -n hal-libgpod
HAL callout program to initialize iPod devices for libgpod library.

%description -n hal-libgpod -l pl.UTF-8
Program wywoływany przez HAL do przygotowywania urządzeń iPod do
użytku z biblioteką libgpod.

%package devel
Summary:	Header files for libgpod library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libgpod
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gdk-pixbuf2-devel >= 2.6.0
Requires:	glib2-devel >= 1:2.16.0

%description devel
This is the package containing the header files for libgpod library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki libgpod.

%package static
Summary:	Static libgpod library
Summary(pl.UTF-8):	Statyczna biblioteka libgpod
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgpod library.

%description static -l pl.UTF-8
Statyczna biblioteka libgpod.

%package apidocs
Summary:	libgpod API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libgpod
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libgpod API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libgpod.

%package -n python-gpod
Summary:	Module for libgpod access from Python
Summary(pl.UTF-8):	Moduł Pythona umożliwiający korzystanie z biblioteki libgpod
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-eyeD3 >= 0.6.6
%pyrequires_eq	python-libs

%description -n python-gpod
This is the libgpod Python support package.

%description -n python-gpod -l pl.UTF-8
Moduł umożliwiający korzystanie z biblioteki libgpod z poziomu
Pythona.

%package -n dotnet-%{name}-sharp
Summary:	C#/.NET library to access iPod content
Summary(pl.UTF-8):	Biblioteka C#/.NET pozwalajaca na dostęp do iPoda
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description -n dotnet-%{name}-sharp
C#/.NET library to access iPod content. Provides bindings to the
libgpod library.

%description -n dotnet-%{name}-sharp -l pl.UTF-8
Biblioteka C#/.NET pozwalająca na dostęp do iPoda. Udostępnia wiązania
do biblioteki libgpod.

%package -n dotnet-%{name}-sharp-devel
Summary:	Development files for libgpod-sharp
Summary(pl.UTF-8):	Development files for libgpod-sharp
Group:		Development/Languages
Requires:	dotnet-%{name}-sharp = %{version}-%{release}
Requires:	pkgconfig

%description -n dotnet-%{name}-sharp-devel
C#/.NET library to access iPod content. Provides bindings to the
libgpod library.

This package contains the files required to develop programs that will
use dotnet-libgpod-sharp.

%description -n dotnet-%{name}-sharp-devel -l pl.UTF-8
Pliki programistyczne biblioteki C#/.NET libgpod-sharp.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
	--disable-silent-rules \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	--with-temp-mount-dir=%{_localstatedir}/run/%{name} \
	--with-python=yes
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/gpod/*.la \
        $RPM_BUILD_ROOT%{_libdir}/libgpod.la

%py_postclean

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/ipod-read-sysinfo-extended
%attr(755,root,root) %{_libdir}/libgpod.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgpod.so.4
%dir %{_localstatedir}/run/%{name}

%files -n hal-libgpod
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/hal/scripts/libgpod-callout
%attr(755,root,root) %{_libdir}/hal/scripts/iphone-callout
%{_datadir}/hal/fdi/policy/20thirdparty/20-libgpod-sysinfo-extended.fdi

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgpod.so
%{_pkgconfigdir}/libgpod-1.0.pc
%{_includedir}/gpod-1.0

%files static
%defattr(644,root,root,755)
%{_libdir}/libgpod.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libgpod

%files -n python-gpod
%defattr(644,root,root,755)
%dir %{py_sitedir}/gpod
%{py_sitedir}/gpod/*.py[co]
%attr(755,root,root) %{py_sitedir}/gpod/_gpod.so

%files -n dotnet-%{name}-sharp
%defattr(644,root,root,755)
%dir %{_prefix}/lib/libgpod
%{_prefix}/lib/libgpod/libgpod-sharp-test.exe
%{_prefix}/lib/libgpod/libgpod-sharp-test.exe.mdb
%{_prefix}/lib/libgpod/libgpod-sharp.dll
%{_prefix}/lib/libgpod/libgpod-sharp.dll.config
%{_prefix}/lib/libgpod/libgpod-sharp.dll.mdb

%files -n dotnet-%{name}-sharp-devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/libgpod-sharp.pc
