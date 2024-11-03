Name:           onagre
Version:        %(unset https_proxy && curl -s https://api.github.com/repos/onagre-launcher/onagre/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")')
Release:        1
URL:            https://github.com/l4l/yofi
Source0:        https://github.com/l4l/yofi/archive/refs/tags/%{version}.tar.gz
Summary:        General purpose application launcher for X and Wayland inspired by Rofi/Wofi and Alfred
License:        MIT
BuildRequires:  rustc
BuildRequires:  wlroots-dev
BuildRequires:  freetype-dev
BuildRequires:  fontconfig-dev
BuildRequires:  xkbcomp-dev

 
%description
General purpose application launcher for X and Wayland inspired by Rofi/Wofi and Alfred

%prep
%setup -q -n onagre-%{version}
cargo fetch --locked


%build
export RUSTFLAGS="$RUSTFLAGS -C target-cpu=westmere -C target-feature=+avx -C opt-level=3 -C codegen-units=1 -C panic=abort -Clink-arg=-Wl,-z,now,-z,relro,-z,max-page-size=0x4000,-z,separate-code "
cargo build --release --locked --offline


%install
install -D -m755 target/release/onagre %{buildroot}/usr/bin/onagre
strip --strip-debug %{buildroot}/usr/bin/onagre

%files
%defattr(-,root,root,-)
/usr/bin/onagre
