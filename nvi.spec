Summary: New Berkeley Vi Editor (Experimental)
Name: nvi
Version: 1.79
Release: 2
Group: Textprocessing/Editor

Copyright: BSD
Packager: rwp@lst.de (Roger Pook)
Icon: nvi.xpm
URL: http://www.bostic.com/vi

Source0: http://mongoose.bostic.com/vi/packages/nvi-1.79.tar.gz
Patch0: nvi-1.79-make.patch
Patch1: nvi-1.79-tk.patch

# Provides: - optional -
# Requires: - optional -
# Conflicts: - optional -

BuildRoot: /tmp/nvi-1.79


%Description
New Berkeley Vi Editor (Experimental)
Nex/nvi are intended as bug-for-bug compatible replacements for 
the original Fourth Berkeley Software Distribution (4BSD) ex and 
vi programs.  For the rest of this manual page, nex/nvi is used
only when it's necessary to distinguish it from the historic 
implementations of ex/vi.  


%Prep
%setup
%patch0 -p1
%patch1 -p1

%Build
cd build

PATH=/usr/bin:/bin OPTFLAG="$RPM_OPT_FLAGS" CC=gcc \
  ./configure \
  --prefix=/usr \
  --program-prefix=n 
#  --enable-perlinterp \
#  --enable-tclinterp \
#  --enable-tknvi 

make


%Install
DESTDIR=$RPM_BUILD_ROOT; export DESTDIR
[ -n "`echo $DESTDIR | sed -n 's:^/tmp/[^.].*$:OK:p'`" ] && rm -rf $DESTDIR ||
(echo "Invalid BuildRoot: '$DESTDIR'! Check this .spec ..."; exit 1) || exit 1

install -d $DESTDIR/usr
cd build
make prefix=$DESTDIR/usr install
#install -s -o root -g root tknvi $DESTDIR/usr/bin
cd ..
#install tk/init.tcl -o root -g root $DESTDIR/usr/share/vi/tcl 

# gzip the Postscript documentation
gzip -v9 docs/USD.doc/vi.man/vi.0.ps
gzip -v9 docs/USD.doc/vi.ref/vi.ref.ps
gzip -v9 docs/USD.doc/edit/edittut.ps
gzip -v9 docs/USD.doc/exref/exref.ps
gzip -v9 docs/USD.doc/exref/summary.ps

# gzip man pages and fix sym-links
MANPATHS=`find $DESTDIR -type d -name "man[1-9n]" -print`
if [ -n "$MANPATHS" ]; then
  chown -Rvc root.root $MANPATHS
  find $MANPATHS -type l -print |
    perl -lne '($f=readlink($_))&&unlink($_)&&symlink("$f.gz","$_.gz")||die;'
  find $MANPATHS -type f -print |
    xargs -r gzip -v9nf
fi

%Post

%PostUn

%Clean
DESTDIR=$RPM_BUILD_ROOT; export DESTDIR
[ -n "`echo $DESTDIR | sed -n 's:^/tmp/[^.].*$:OK:p'`" ] && rm -rf $DESTDIR ||
(echo "Invalid BuildRoot: '$DESTDIR'! Check this .spec ..."; exit 1) || exit 1


%Files
%doc README LICENSE FAQ 
%doc docs/USD.doc/vi.man/vi.0.ps.gz
%doc docs/USD.doc/vi.ref/vi.ref.ps.gz
%doc docs/USD.doc/vi.ref/vi.ref.txt
%doc docs/USD.doc/edit/edittut.ps.gz
%doc docs/USD.doc/exref/exref.ps.gz
%doc docs/USD.doc/exref/summary.ps.gz
%doc docs/interp/interp
%doc docs/internals
/usr/bin/nvi
/usr/bin/nex
/usr/bin/nview
#/usr/bin/tknvi
/usr/man/man1/nvi.1.gz
/usr/man/man1/nex.1.gz
/usr/man/man1/nview.1.gz
%dir /usr/share/vi
/usr/share/vi/*



%ChangeLog
* Mon Jan 01 1997 ...
$Id: nvi.spec,v 1.1 1999-04-07 16:32:41 kloczek Exp $
