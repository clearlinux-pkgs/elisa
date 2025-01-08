#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: 5424026
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : elisa
Version  : 24.12.0
Release  : 56
URL      : https://download.kde.org/stable/release-service/24.12.0/src/elisa-24.12.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.12.0/src/elisa-24.12.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.12.0/src/elisa-24.12.0.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause CC0-1.0 GPL-3.0 LGPL-2.1 LGPL-3.0
Requires: elisa-bin = %{version}-%{release}
Requires: elisa-data = %{version}-%{release}
Requires: elisa-lib = %{version}-%{release}
Requires: elisa-license = %{version}-%{release}
Requires: elisa-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kfilemetadata-dev
BuildRequires : kirigami-dev
BuildRequires : kirigami2-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libvlc)
BuildRequires : qqc2-desktop-style-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<!--
SPDX-License-Identifier: LGPL-3.0-or-later
-->
# Elisa
<a href='https://flathub.org/apps/details/org.kde.elisa'><img width='190px' alt='Download on Flathub' src='https://flathub.org/assets/badges/flathub-badge-i-en.png'/></a>

%package bin
Summary: bin components for the elisa package.
Group: Binaries
Requires: elisa-data = %{version}-%{release}
Requires: elisa-license = %{version}-%{release}

%description bin
bin components for the elisa package.


%package data
Summary: data components for the elisa package.
Group: Data

%description data
data components for the elisa package.


%package lib
Summary: lib components for the elisa package.
Group: Libraries
Requires: elisa-data = %{version}-%{release}
Requires: elisa-license = %{version}-%{release}

%description lib
lib components for the elisa package.


%package license
Summary: license components for the elisa package.
Group: Default

%description license
license components for the elisa package.


%package locales
Summary: locales components for the elisa package.
Group: Default

%description locales
locales components for the elisa package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n elisa-24.12.0
cd %{_builddir}/elisa-24.12.0
pushd ..
cp -a elisa-24.12.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1735201749
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1735201749
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/elisa
cp %{_builddir}/elisa-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/elisa/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/elisa-%{version}/COPYING %{buildroot}/usr/share/package-licenses/elisa/f45ee1c765646813b442ca58de72e20a64a7ddba || :
cp %{_builddir}/elisa-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/elisa/ea97eb88ae53ec41e26f8542176ab986d7bc943a || :
cp %{_builddir}/elisa-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/elisa/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/elisa-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/elisa/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/elisa-%{version}/LICENSES/GPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/elisa/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/elisa-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/elisa/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/elisa-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/elisa/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/elisa-%{version}/LICENSES/LGPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/elisa/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/elisa-%{version}/autotests/data/music/cover.jpg.license %{buildroot}/usr/share/package-licenses/elisa/6abf17d8d0933bb54aadf315aafae46eba0d41dd || :
cp %{_builddir}/elisa-%{version}/autotests/data/music/test.m4a.license %{buildroot}/usr/share/package-licenses/elisa/6abf17d8d0933bb54aadf315aafae46eba0d41dd || :
cp %{_builddir}/elisa-%{version}/autotests/data/music/test.mp3.license %{buildroot}/usr/share/package-licenses/elisa/6abf17d8d0933bb54aadf315aafae46eba0d41dd || :
cp %{_builddir}/elisa-%{version}/autotests/data/music/test.ogg.license %{buildroot}/usr/share/package-licenses/elisa/6abf17d8d0933bb54aadf315aafae46eba0d41dd || :
cp %{_builddir}/elisa-%{version}/po/tr/docs/elisa/index.docbook.license %{buildroot}/usr/share/package-licenses/elisa/6abf17d8d0933bb54aadf315aafae46eba0d41dd || :
cp %{_builddir}/elisa-%{version}/src/elisa_core.kcfg.license %{buildroot}/usr/share/package-licenses/elisa/6abf17d8d0933bb54aadf315aafae46eba0d41dd || :
cp %{_builddir}/elisa-%{version}/src/elisa_settings.kcfgc.license %{buildroot}/usr/share/package-licenses/elisa/6abf17d8d0933bb54aadf315aafae46eba0d41dd || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang elisa
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/elisa
/usr/bin/elisa

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.elisa.desktop
/usr/share/dbus-1/services/org.kde.elisa.service
/usr/share/icons/hicolor/128x128/apps/elisa.png
/usr/share/icons/hicolor/16x16/apps/elisa.png
/usr/share/icons/hicolor/22x22/apps/elisa.png
/usr/share/icons/hicolor/32x32/apps/elisa.png
/usr/share/icons/hicolor/48x48/apps/elisa.png
/usr/share/icons/hicolor/64x64/apps/elisa.png
/usr/share/icons/hicolor/scalable/apps/elisa.svg
/usr/share/metainfo/org.kde.elisa.appdata.xml
/usr/share/qlogging-categories6/elisa.categories

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/elisa/libelisaLib.so.0.1
/usr/lib64/elisa/libelisaLib.so.0
/usr/lib64/elisa/libelisaLib.so.0.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/elisa/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/elisa/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/elisa/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/elisa/6abf17d8d0933bb54aadf315aafae46eba0d41dd
/usr/share/package-licenses/elisa/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/elisa/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/elisa/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/elisa/ea97eb88ae53ec41e26f8542176ab986d7bc943a
/usr/share/package-licenses/elisa/f45ee1c765646813b442ca58de72e20a64a7ddba

%files locales -f elisa.lang
%defattr(-,root,root,-)

