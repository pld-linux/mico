Summary(pl):	Implementacja standardu CORBA 2.2
Name:		mico
Version:	2.2.7
Release:	1
Copyright:	LGPL
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Source:		ftp://diamant.vsb.cs.uni-frankfurt.de/pub/projects/mico/%{name}-%{version}.tar.gz
URL:		http://www.mico.org/
Buildroot:	/tmp/%{name}-%{version}-root

%define _prefix /usr/X11R6

%description
The acronym MICO expands to MICO Is CORBA. This library provide a freely
available and fully compilant implementation of the CORBA 2.2 standard.

You need this package if you want use KDE 2.0 or KOffice

%description -l pl
Akronim MICO oznacza ''MICO jest CORBA,, (ang. MICO Is CORBA). Biblioteka
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

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure --disable-mini-stl --prefix=$RPM_BUILD_ROOT%{_prefix}

make

%install
rm -fr $RPM_BUILD_ROOT

make install

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/*.so

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[158]/* CHANGES CONVERT FAQ LICENSE* \
	TODO doc/*.ps
	
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE*.gz FAQ.gz TODO.gz CONVERT.gz CHANGES.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*

%files devel
%defattr(644,root,root,755)
%doc doc/*.ps.gz
%{_mandir}/man[158]/*.gz
%{_includedir}/*

%changelog
* Mon 5 Jul 1999 Micha³ Zawalich <michalz@box43.gnet.pl>
  [2.2.7-1]
- initial version.
