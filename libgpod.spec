# TODO
# check: http://fred.uwcs.co.uk/diff (from http://www.fredemmott.co.uk/blog_121)
Summary:	Shared library to access the contents of an iPod
Summary(pl.UTF-8):	Biblioteka współdzielona do dostępu do zawartości iPodów
Name:		libgpod
Version:	0.7.0
Release:	2
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/gtkpod/%{name}-%{version}.tar.gz
# Source0-md5:	34eba68a6037e6b2feda20f46d1dbfb8
Patch0:		%{name}-gcc43.patch
URL:		http://www.gtkpod.org/libgpod.html
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.30
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	hal-devel < 0.6
BuildRequires:	hal-devel >= 0.5.7.1
BuildRequires:	intltool >= 0.35
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2.1.1
BuildRequires:	python-eyeD3 >= 0.6.6
BuildRequires:	python-mutagen >= 1.8
BuildRequires:	rpm-pythonprov
BuildRequires:	sg3_utils-devel >= 1.26
BuildRequires:	swig-python >= 1.3.24
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
Requires:	dbus-glib-devel >= 0.30
Requires:	gtk+2-devel >= 2.0
Requires:	hal-devel >= 0.5.7.1

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
Summary:	Libraries for libgpod access from Python
Summary(pl.UTF-8):	Biblioteki Pythona umożliwiające korzystanie z libgpod
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-eyeD3 >= 0.6.6
%pyrequires_eq	python-libs

%description -n python-gpod
This is the libgpod Python support package.

%description -n python-gpod -l pl.UTF-8
Biblioteki umożliwiające korzystanie z libgpod z poziomu Pythona.

%prep
%setup -q
%patch0 -p1

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
	--with-html-dir=%{_gtkdocdir} \
	--with-python=yes
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitedir}/gpod/*.{la,a}

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

%files -n hal-libgpod
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/hal/libgpod-callout
%{_datadir}/hal/fdi/policy/20thirdparty/20-libgpod-sysinfo-extended.fdi

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgpod.so
%{_libdir}/libgpod.la
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
