#
# Note about gtags-patch !!
#
# Future releases of Nvi (1.81.5) will not need it anymore.
# Instead they will need --enable-perlinterp when configuring
# and Requires: gtags-perl-wrapper in this specfile
#

Summary:	Clone of the POSIX conform editor 'vi'
Summary(de.UTF-8):	Klon des POSIX konformen Editors 'vi'
Summary(pl.UTF-8):	Klon edytora POSIX-owego 'vi' i 'ex'
Name:		nvi
Version:	1.81.5
Release:	1
License:	BSD
Group:		Applications/System
Source0:	http://www.kotnet.org/~skimo/nvi/devel/%{name}-%{version}.tar.bz2
# Source0-md5:	82262d08803b364033dd7ab38190305a
Patch1:	%{name}-header.patch
Patch2:	%{name}-tcsetattr.patch
Patch3:	%{name}-gcc4.patch
Patch4:	%{name}-autoconf.patch
Patch5:	%{name}-db4.patch
URL:		http://www.bostic.com/vi/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	db-static >= 4.0
Provides:	vi
Obsoletes:	elvis-static
Obsoletes:	vim-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		/bin
%define		_sbindir	/sbin

%description
A freely redistributable replacement for the Berkeley ex and vi text
editors.

%description -l de.UTF-8
Frei verbreitabrer Ersatz für die Brekeley Text-Editoren vi und ex.

%description -l pl.UTF-8
Programy zastępcze dla Berkeley-owskich edytorów tekstów ex i vi.

%prep
%setup -q
%patch1 -p1
%patch2 -p0
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
cd dist
cp ../clib/*.c .
cp -f /usr/share/automake/config.* .
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-widechar
%{__make} \
	LDFLAGS=-all-static

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_docdir}/%{name}-%{version},%{_bindir},%{_sbindir}}

cd dist
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install recover $RPM_BUILD_ROOT%{_sbindir}
cd ..

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/recover
%{_mandir}/man1/*
