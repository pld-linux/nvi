Summary:	Clone of the POSIX conform editor 'vi'
Summary(de):	Klon des POSIX konformen Editors 'vi'
Summary(pl):	Klon edytora POSIX-owego 'vi' i 'ex'
Name:		nvi
Version:	1.79
Release:	6
License:	BSD
Group:		Applications/System
Source0:	ftp://www.sleepycat.com/pub/%{name}-%{version}.tar.gz
# Source0-md5:	765e2153f5fc4f21793f2edc2647305a
Patch0:		%{name}.patch.gz
URL:		http://www.bostic.com/vi/
BuildRequires:	ncurses-devel >= 5.0
Provides:	vi
Obsoletes:	vim-static
Obsoletes:	elvis-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A freely redistributable replacement for the Berkeley ex and vi text
editors.

%description -l de
Frei verbreitabrer Ersatz für die Brekeley Text-Editoren vi und ex.

%description -l pl
Programy zastepcze dla Berkeley-owskich edytorów tekstów ex i vi.

%prep
%setup -q
%patch0 -p1

%build
cd build
CFLAGS="%{rpmcflags} -I/usr/include/db1 -I/usr/include/ncurses"
LDFLAGS="-lncurses -ldb1 %{rpmldflags}"
%configure2_13 \
	--disable-curses \
	--disable-db \
	--disable-perl
%{__make}

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc FAQ LICENSE LAYOUT README
%attr(755,root,root) /bin/*
%attr(755,root,root) /sbin/recover
%{_mandir}/man1/*
