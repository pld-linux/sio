#
# Conditional build:
%bcond_without	tests	# don't perform "make check"
#
Summary:	OSSP sio - Stream I/O
Summary(pl):	OSSP sio - biblioteka strumieni I/O
Name:		sio
Version:	0.9.2
Release:	0.2
Epoch:		0
License:	distributable (see README)
Group:		Libraries
Source0:	ftp://ftp.ossp.org/pkg/lib/sio/%{name}-%{version}.tar.gz
# Source0-md5:	fa39b36c13324ed5f3233698eda9de9f	
Patch0:		%{name}-libs.patch
URL:		http://www.ossp.org/pkg/lib/sio/
BuildRequires:	al-devel
#BuildRequires:	ex-devel
BuildRequires:	sa-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OSSP sio is an I/O abstraction library for layered stream
communication. It was built to deal efficiently with complex I/O
protocols and includes capabilities to filter and multiplex data
streams. Its modular structure is fully supported by the underlying
OSSP al data buffer library.

%description -l pl
OSSP sio to biblioteka abstrakcji wej�cia/wyj�cia do warstwowej
komunikacji strumieniowej. Zosta�a stworzona, aby wydajnie obs�ugiwa�
z�o�one protoko�y wej�cia/wyj�cia i zawiera mo�liwo�ci filtrowania
oraz multipleksowania strumieni danych. Jej modularna struktra jest w
pe�ni obs�ugiwana przez le��c� poni�ej bibliotek� buforowania danych
OSSP al.

%package devel
Summary:	OSSP sio - Stream I/O - header files and development libraries
Summary(pl):	OSSP sio - biblioteka strumieni I/O - pliki nag��wkowe i biblioteki dla deweloper�w
Group:		Development/Libraries
Requires:       %{name} = %{epoch}:%{version}-%{release}

%description devel
OSSP sio - Stream I/O - header files and development libraries.

%description devel -l pl
OSSP sio - biblioteka strumieni I/O - pliki nag��wkowe i biblioteki
dla deweloper�w.

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
	--with-sa
#	--with-ex \ # build fails; compiler bug?
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

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.a
