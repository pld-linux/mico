Summary(pl):	Implementacja standardu CORBA 2.2
Name:		mico
Version:	2.2.7
Release:	1
Copyright:	LGPL
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Source:		ftp://diamant.vsb.cs.uni-frankfurt.de/pub/projects/mico/%{name}-%{version}.tar.gz
Patch:		mico-DESTDIR.patch
URL:		http://www.mico.org/
Buildroot:	/tmp/%{name}-%{version}-root

%define _prefix /usr/X11R6
%define	_mandir	%{_prefix}/man

%description
The acronym MICO expands to MICO Is CORBA. This library provide a freely
available and fully compilant implementation of the CORBA 2.2 standard.

You need this package if you want use KDE 2.0 or KOffice

%description -l pl
Akronim MICO oznacza "MICO jest CORBA" (ang. MICO Is CORBA). Biblioteka
ta dostarcza w pe³ni sprawnej i przenoszolnej na inne platformy
implementacji standardu CORBA 2.2

Pakiet ten jest niezbêdny, je¿eli chcesz u¿ywaæ KDE 2.0 lub KOffice

%package devel
Summary:	Include files and documentation
Summary(pl):	Pliki nag³owkowe oraz dokumentacja do biblioteki
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires: 	%{name} = %{version}

%description devel
Contains the files nessesary to develop applications using MICO: header
files, man pages and ps documentation.

%description -l pl devel
Zawiera niezbêdne pliki do tworzenia i kompilacji aplikacji korzystaj±cych
z MICO jak pliki nag³ówkowe oraz dokumentacjê.

%prep
%setup -q -n %{name}
%patch -p1

%build
CXXFLAGS="$RPM_OPT_FLAGS"; export CXXFLAGS
LDFLAGS="-s"; export LDFLAGS
%configure \
	--disable-mini-stl \
	--disable-debug
make

%install
rm -fr $RPM_BUILD_ROOT

make install INSTDIR=$RPM_BUILD_ROOT%{_prefix} \
	SHARED_INSTDIR=$RPM_BUILD_ROOT%{_prefix}

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/*.so

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man?/* \
	CHANGES CONVERT FAQ LICENSE* TODO doc/*.ps

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -fr $RPM_BUILD_ROOT

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

%attr(755,root,root) %{_libdir}/*

%files devel
%defattr(644,root,root,755)
%doc doc/*.ps.gz
%attr(755,root,root) %{_bindir}/mico-c++
%attr(755,root,root) %{_bindir}/mico-ld
%attr(755,root,root) %{_bindir}/mico-shc++
%attr(755,root,root) %{_bindir}/mico-shld
%{_mandir}/man[158]/*.gz
%{_includedir}/*
