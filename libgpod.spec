Summary:	Shared library to access the contents of an iPod
Name:		libgpod
Version:	0.1.6
Release:	0.1
Epoch:		0
License:	GPL v2
Group:		Libraries
Source0:	http://dl.sourceforge.net/gtkpod/%{name}-%{version}.tar.gz
# Source0-md5:	5d74f888921330bae4f355924e4b4874
URL:		http://www.gtkpod.org/libgpod.html
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	intltool >= 0.21
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgpod is a library meant to abstract access to an iPod content. It
provides an easy to use API to retrieve the list of files and playlist
stored on an iPod, to modify them and to save them back to the iPod.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
