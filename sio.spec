#
%bcond_without  static_libs # don't build static libraries
%bcond_without	tests	# don't perform "make check"
#
Summary:	OSSP sio - Stream I/O
Summary(pl):	OSSP sio - biblioteka strumieni I/O
Name:		sio
Version:	0.9.3
Release:	0.1
Epoch:		0
License:	distributable (see README)
Group:		Libraries
Source0:	ftp://ftp.ossp.org/pkg/lib/sio/%{name}-%{version}.tar.gz
# Source0-md5:	8dcd991b8d9220810451138cf9dfa0ea
Patch0:		%{name}-libs.patch
URL:		http://www.ossp.org/pkg/lib/sio/
BuildRequires:	al-devel
BuildRequires:	ex-devel
BuildRequires:	sa-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OSSP sio is an I/O abstraction library for layered stream
communication. It was built to deal efficiently with complex I/O
protocols and includes capabilities to filter and multiplex data
streams. Its modular structure is fully supported by the underlying
OSSP al data buffer library.

%description -l pl
OSSP sio to biblioteka abstrakcji wej¶cia/wyj¶cia do warstwowej
komunikacji strumieniowej. Zosta³a stworzona, aby wydajnie obs³ugiwaæ
z³o¿one protoko³y wej¶cia/wyj¶cia i zawiera mo¿liwo¶ci filtrowania
oraz multipleksowania strumieni danych. Jej modularna struktra jest w
pe³ni obs³ugiwana przez le¿±c± poni¿ej bibliotekê buforowania danych
OSSP al.

%package devel
Summary:	OSSP sio - Stream I/O - header files and development libraries
Summary(pl):	OSSP sio - biblioteka strumieni I/O - pliki nag³ówkowe i biblioteki dla deweloperów
Group:		Development/Libraries
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description devel
OSSP sio - Stream I/O - header files and development libraries.

%description devel -l pl
OSSP sio - biblioteka strumieni I/O - pliki nag³ówkowe i biblioteki
dla deweloperów.

%package static
Summary:	OSSP sio - Stream I/O - static libraries
Summary(pl):	OSSP sio - biblioteka strumieni I/O - biblioteki statyczne
Group:		Development/Libraries
Requires:       %{name}-devel = %{epoch}:%{version}-%{release}

%description static
OSSP sio - Stream I/O - static libraries.

%description static -l pl
OSSP sio - biblioteka strumieni I/O - biblioteki statyczne.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--with-al \
	--with-sa \
	--with-ex \
	--enable-static=%{?with_static_libs:yes}%{!?with_static_libs:no}	
%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_mandir}/man3/*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.a
%endif
