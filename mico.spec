Summary:	An implementation of the CORBA 2.3 standard Object Request Broker
Summary(pl):	Implementacja standardu CORBA 2.3
Name:		mico
Version:	2.3.11
Release:	4
License:	GPL/LGPL
Group:		Libraries
Source0:	http://www.mico.org/%{name}-%{version}.tar.gz
# Source0-md5:	669d98ec5da2f6c50937a2a25e797eec
Patch0:		%{name}-libdir.patch
URL:		http://www.mico.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gtk+-devel
BuildRequires:	libstdc++-devel
BuildRequires:	readline-devel >= 4.2
BuildRequires:	tcl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MICO (MICO Is CORBA) is a freely available and fully compliant
implementation of the CORBA 2.3 standard Object Request Broker. The
mico package contains the shared libraries and demons needed to run
MICO applications.

%description -l pl
Akronim MICO oznacza "MICO jest CORBA" (ang. MICO Is CORBA).
Biblioteka ta dostarcza w pe³ni sprawnej i przenoszolnej na inne
platformy implementacji standardu CORBA 2.3.

%package devel
Summary:	Include files and documentation
Summary(pl):	Pliki nag³owkowe oraz dokumentacja do biblioteki
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Contains the files nessesary to develop applications using MICO:
header files, man pages and ps documentation.

%description devel -l pl
Zawiera niezbêdne pliki do tworzenia i kompilacji aplikacji
korzystaj±cych z MICO jak pliki nag³ówkowe oraz dokumentacjê.

%package static
Summary:	Static libraries for writing MICO applications
Summary(pl):	Biblioteki statyczne MICO
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libraries for writing MICO applications.

%description static -l pl
Biblioteki statyczne MICO.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__autoconf}
cp -f %{_datadir}/automake/install-sh admin
cp -f %{_datadir}/automake/config.sub admin
CXXFLAGS="%{rpmcflags} `gtk-config --cflags`"
%configure \
	--enable-namespace \
	--enable-shared \
	--enable-static \
	--enable-dynamic \
	--enable-final \
	--enable-ccm \
	--enable-coss \
	--with-gtk=/usr/X11R6 \
	--disable-debug \
	--with-tcl \
	--with-x \
	--with-ssl

# with those options mico doesn't compile for me :/
#	--enable-speed-tune \
#	--disable-externalize \
#	--disable-debug \
#	--disable-except \
#	--disable-mini-stl \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTDIR=$RPM_BUILD_ROOT%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT \
	SHARED_INSTDIR=$RPM_BUILD_ROOT%{_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES CONVERT FAQ LICENSE TODO
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
%doc doc/*.ps
%attr(755,root,root) %{_bindir}/mico-c++
%attr(755,root,root) %{_bindir}/mico-ld
%attr(755,root,root) %{_bindir}/mico-shc++
%attr(755,root,root) %{_bindir}/mico-shld
%attr(755,root,root) %{_libdir}/mico-setup.*
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
