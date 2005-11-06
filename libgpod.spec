Summary:	Shared library to access the contents of an iPod
Name:		libgpod
Version:	0.1.8
%define	_snap	20051106
Release:	0.%{_snap}.2
Epoch:		0
License:	GPL v2
Group:		Libraries
#Source0:	http://dl.sourceforge.net/gtkpod/%{name}-%{version}.tar.gz
Source0:	%{name}-%{_snap}.tar.bz2
# Source0-md5:	7f8237149051cb3a6d0c9f21007b2691
URL:		http://www.gtkpod.org/libgpod.html
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	intltool >= 0.33
BuildRequires:	pkgconfig
%if 0%{?_snap:1}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libtool
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgpod is a library meant to abstract access to an iPod content. It
provides an easy to use API to retrieve the list of files and playlist
stored on an iPod, to modify them and to save them back to the iPod.

%package devel
Summary:	Development libraries and header files for libgpod library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the development libraries and header
files for libgpod

%package static
Summary:	Static libgpod library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libgpod library.

%prep
%setup -q %{?_snap:-n %{name}}

%build
%if 0%{?_snap:1}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%endif
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

# MKINSTALLDIRS is problem with combination of gettext-0.14.4 and automake-1.8
# See TROUBLESHOOTING for more details.
%{__make} install \
	MKINSTALLDIRS="install -d" \
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
