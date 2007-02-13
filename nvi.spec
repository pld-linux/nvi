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
Version:	1.79
Release:	8
License:	BSD
Group:		Applications/System
Source0:	ftp://www.sleepycat.com/pub/%{name}-%{version}.tar.gz
# Source0-md5:	765e2153f5fc4f21793f2edc2647305a
Patch0:		%{name}.patch
Patch10:	%{name}-gtags.patch
URL:		http://www.bostic.com/vi/
BuildRequires:	automake
BuildRequires:	ncurses-devel >= 5.0
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
%patch0 -p1
%patch10 -p1

# these were deleted by previous version of patch
rm -f docs/USD.doc/{edit/edittut.ps,exref/exref.ps,exref/summary.ps} \
	docs/USD.doc/vi.man/{vi.0,vi.0.ps} \
	docs/USD.doc/vi.ref/{index.so,vi.ref.ps,vi.ref.txt} \
	docs/USD.doc/vitut/{summary.ps,viapwh.ps,vitut.ps}

%build
cd build
cp -f /usr/share/automake/config.* .
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
LDFLAGS="-lncurses %{rpmldflags}"
%configure2_13 \
	--disable-curses \
	--disable-perl
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_docdir}/%{name}-%{version},%{_bindir},%{_sbindir}}

install docs/USD.doc/vi.man/vi.1 $RPM_BUILD_ROOT%{_mandir}/man1/vi.1
install build/nvi $RPM_BUILD_ROOT%{_bindir}/vi

ln -sf vi $RPM_BUILD_ROOT%{_bindir}/ex
ln -sf vi $RPM_BUILD_ROOT%{_bindir}/view

echo ".so vi.1" > $RPM_BUILD_ROOT%{_mandir}/man1/ex.1
echo ".so vi.1" > $RPM_BUILD_ROOT%{_mandir}/man1/view.1

install build/recover $RPM_BUILD_ROOT%{_sbindir}/recover

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc FAQ LICENSE LAYOUT README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/recover
%{_mandir}/man1/*
