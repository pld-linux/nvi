Summary:      	Clone of the POSIX conform editor 'vi'.
Summary(de):	Klon des POSIX konformen Editors 'vi'.
Summary(pl):	Klon edytora POSIX-owego 'vi' i 'ex'.
Name:		nvi
Version:	1.79
Release:      	2
Copyright:    	BSD
Group:        	Utilities/System
Group(pl):	Narzêdzia/System
Source: 	ftp://www.bostic.com/pub/%{name}-%{version}.tar.gz
Patch0: 	nvi.patch
Provides:     	vi
URL:		http://www.bostic.com/vi/
BuildPrereq:	ncurses-devel
Buildroot:	/tmp/%{name}-%{version}-root

%description
A freely redistributable replacement for the Berkeley ex and vi text
editors.

%description -l pl
Programy zastepcze dla Berkeley-owskich edytorów tekstów ex i vi.

%description -l de
Frei verbreitabrer Ersatz für die Brekeley Text-Editoren vi und ex.

%prep
%setup -q
%patch0 -p1

%build
cd build && \
CFLAGS="$RPM_OPT_FLAGS -I/usr/include/db1 -I/usr/include/ncurses" LDFLAGS="-lncurses -ldb1 -s" \
./configure %{_target} \
	--disable-curses \
	--disable-db \
	--disable-perl
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_defaultdocdir}/%{name}-%{version},/bin,/sbin}

install docs/USD.doc/vi.man/vi.1 $RPM_BUILD_ROOT%{_mandir}/man1/vi.1
install build/nvi $RPM_BUILD_ROOT/bin/vi

ln -sf vi $RPM_BUILD_ROOT/bin/ex
ln -sf vi $RPM_BUILD_ROOT/bin/view

echo ".so vi.1" > $RPM_BUILD_ROOT%{_mandir}/man1/ex.1
echo ".so vi.1" > $RPM_BUILD_ROOT%{_mandir}/man1/view.1

install build/recover $RPM_BUILD_ROOT/sbin/recover

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	FAQ LICENSE LAYOUT README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *gz
%attr(755,root,root) /bin/*
%attr(755,root,root) /sbin/recover
%{_mandir}/man1/*

%changelog
* Sun May 30 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.79-2]
- disable using curses headre files durin compilation,
- added URL,
- more rpm macros,
- added full Source: Url.

* Thu Apr 15 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.79-1]
- removed man group from man pages,
- link against libncurses instead libtermcap,
- added -s to LDFLAGS,
- ex(1) and view(1) man pages make as *roff include,
- added some %doc.

* Wed Apr  7 1999 Marcin Dalecki <dalecki@cs.net.pl>
- Initial release for PLD.
