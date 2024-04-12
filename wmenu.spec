Name     : wmenu
Version  : 0.1.7
Release  : 1
URL      : https://sr.ht/~adnano/wmenu
Source0  : https://git.sr.ht/~adnano/wmenu/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary  : Header files for rofi plugins
Group    : Development/Tools
License  : MIT
BuildRequires : gcc
BuildRequires : buildreq-meson
BuildRequires : flex
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(cairo-xcb)
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(librsvg-2.0)
BuildRequires : pkgconfig(libstartup-notification-1.0)
BuildRequires : pkgconfig(pango)
BuildRequires : pkgconfig(pangocairo)
BuildRequires : pkgconfig(xcb-xrm)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : wayland-dev wayland-protocols-dev


%description
An efficient dynamic menu for Sway and wlroots based Wayland compositors.

%prep
%setup -q

%build
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605557300
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
meson \
    --libdir=lib64 --prefix=/usr \
    --buildtype=plain builddir -Dwerror=false
ninja -v -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install
rm -rf %{buildroot}/usr/share/man

%files
%defattr(-,root,root,-)
/usr/bin/wmenu