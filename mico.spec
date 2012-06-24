Summary:	An implementation of the CORBA 2.3 standard Object Request Broker
Summary(pl):	Implementacja standardu CORBA 2.3
Name:		mico
Version:	2.3.0
Release:	5
License:	GPL/LGPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	ftp://diamant.vsb.cs.uni-frankfurt.de/pub/projects/mico/%{name}-%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-gcc295.patch
Patch2:		%{name}-gtk+.m4.patch
URL:		http://www.mico.org/
BuildRequires:	libstdc++-devel
BuildRequires:	readline-devel >= 4.2
BuildRequires:	tcl-devel
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MICO (MICO Is CORBA) is a freely available and fully compliant
implementation of the CORBA 2.3 standard Object Request Broker. The
mico package contains the shared libraries and demons needed to run
MICO applications.

%description -l pl
Akronim MICO oznacza "MICO jest CORBA" (ang. MICO Is CORBA).
Biblioteka ta dostarcza w pe�ni sprawnej i przenoszolnej na inne
platformy implementacji standardu CORBA 2.3.

%package devel
Summary:	Include files and documentation
Summary(pl):	Pliki nag�owkowe oraz dokumentacja do biblioteki
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Contains the files nessesary to develop applications using MICO:
header files, man pages and ps documentation.

%description -l pl devel
Zawiera niezb�dne pliki do tworzenia i kompilacji aplikacji
korzystaj�cych z MICO jak pliki nag��wkowe oraz dokumentacj�.

%package static
Summary:	Static libraries for writing MICO applications
Summary(pl):	Biblioteki statyczne MICO
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libraries for writing MICO applications.

%description -l pl static
Biblioteki statyczne MICO.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
autoconf
CXXFLAGS="%{rpmcflags} %{!?debug:-fno-exceptions} `glib-config --cflags`"
%configure \
	--enable-final \
	--enable-namespace \
	--enable-shared \
	--with-gtk=%{_prefix}/X11R6 \
	--with-tcl \
	--with-x \
	--enable-speed-tune \
	--disable-mini-stl \
	--disable-debug

%{__make} EHFLAGS="%{!?debug:-fno-exceptions} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf CHANGES CONVERT FAQ LICENSE* TODO doc/*.ps

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE*.gz FAQ.gz TODO.gz CONVERT.gz CHANGES.gz
%attr(755,root,root) %{_bindir}/eventd
%attr(755,root,root) %{_bindir}/idl
%attr(755,root,root) %{_bindir}/imr
%attr(755,root,root) %{_bindir}/iordump
%attr(755,root,root) %{_bindir}/ird
%attr(755,root,root) %{_bindir}/mico-ar
%attr(755,root,root) %{_bindir}/mico-cpp
%attr(755,root,root) %{_bindir}/micod
%attr(755,root,root) %{_bindir}/nsadmin
%attr(755,root,root) %{_bindir}/nsd
%attr(755,root,root) %{_bindir}/propertyd
%attr(755,root,root) %{_bindir}/traderd

%attr(755,root,root) %{_libdir}/lib*.so
%{_mandir}/man[158]/*

%files devel
%defattr(644,root,root,755)
%doc doc/*.ps.gz
%attr(755,root,root) %{_bindir}/mico-c++
%attr(755,root,root) %{_bindir}/mico-ld
%attr(755,root,root) %{_bindir}/mico-shc++
%attr(755,root,root) %{_bindir}/mico-shld
%attr(755,root,root) %{_libdir}/mico-setup.*
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
