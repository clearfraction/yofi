Name:           yofi
Version:        %(unset https_proxy && curl -s https://api.github.com/repos/l4l/yofi/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")')
Release:        1
URL:            https://github.com/l4l/yofi
Source0:        https://github.com/l4l/yofi/archive/refs/tags/%{version}.tar.gz
Summary:        Minimalistic menu for Wayland-based compositors.
License:        GPLv3
BuildRequires:  rustc
BuildRequires:  wlroots-dev
BuildRequires:  lz4-dev

 
%description
minimalistic menu for Wayland-based compositors.

%prep
%setup -q -n yofi-%{version}
cargo fetch --locked


%build
export RUSTFLAGS="$RUSTFLAGS -C target-cpu=westmere -C target-feature=+avx -C opt-level=3 -C codegen-units=1 -C panic=abort -Clink-arg=-Wl,-z,now,-z,relro,-z,max-page-size=0x4000,-z,separate-code "
cargo build --release --locked --offline


%install
install -D -m755 target/release/yofi %{buildroot}/usr/bin/swww
strip --strip-debug %{buildroot}/usr/bin/yofi

%files
%defattr(-,root,root,-)
/usr/bin/yofi
