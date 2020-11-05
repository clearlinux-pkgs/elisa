#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : elisa
Version  : 20.08.3
Release  : 2
URL      : https://download.kde.org/stable/release-service/20.08.3/src/elisa-20.08.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.08.3/src/elisa-20.08.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.08.3/src/elisa-20.08.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC-BY-SA-4.0 CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0
Requires: elisa-bin = %{version}-%{release}
Requires: elisa-data = %{version}-%{release}
Requires: elisa-lib = %{version}-%{release}
Requires: elisa-license = %{version}-%{release}
Requires: elisa-locales = %{version}-%{release}
BuildRequires : baloo-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kconfig-dev
BuildRequires : kconfigwidgets-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : kdeclarative-dev
BuildRequires : kdoctools-dev
BuildRequires : kfilemetadata-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : kirigami2-dev
BuildRequires : kpackage-dev
BuildRequires : kxmlgui-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libvlc)
BuildRequires : qtbase-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qtdeclarative-dev
BuildRequires : qtquickcontrols2-dev

%description
<!--
SPDX-License-Identifier: LGPL-3.0-or-later
-->
# Elisa
Elisa music player
## Introduction

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


%package doc
Summary: doc components for the elisa package.
Group: Documentation

%description doc
doc components for the elisa package.


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
%setup -q -n elisa-20.08.3
cd %{_builddir}/elisa-20.08.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604592551
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1604592551
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/elisa
cp %{_builddir}/elisa-20.08.3/COPYING %{buildroot}/usr/share/package-licenses/elisa/f45ee1c765646813b442ca58de72e20a64a7ddba
cp %{_builddir}/elisa-20.08.3/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/elisa/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
cp %{_builddir}/elisa-20.08.3/LICENSES/CC-BY-SA-4.0.txt %{buildroot}/usr/share/package-licenses/elisa/7b3e5f0e946c0b599b04a45deebb1aaed782070d
cp %{_builddir}/elisa-20.08.3/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/elisa/8287b608d3fa40ef401339fd907ca1260c964123
cp %{_builddir}/elisa-20.08.3/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/elisa/e712eadfab0d2357c0f50f599ef35ee0d87534cb
cp %{_builddir}/elisa-20.08.3/LICENSES/GPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/elisa/6091db0aead0d90182b93d3c0d09ba93d188f907
cp %{_builddir}/elisa-20.08.3/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/elisa/3c3d7573e137d48253731c975ecf90d74cfa9efe
cp %{_builddir}/elisa-20.08.3/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/elisa/757b86330df80f81143d5916b3e92b4bcb1b1890
cp %{_builddir}/elisa-20.08.3/LICENSES/LGPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/elisa/757b86330df80f81143d5916b3e92b4bcb1b1890
pushd clr-build
%make_install
popd
%find_lang elisa

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/elisa

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.elisa.desktop
/usr/share/icons/hicolor/128x128/apps/elisa.png
/usr/share/icons/hicolor/16x16/apps/elisa.png
/usr/share/icons/hicolor/22x22/apps/elisa.png
/usr/share/icons/hicolor/32x32/apps/elisa.png
/usr/share/icons/hicolor/48x48/apps/elisa.png
/usr/share/icons/hicolor/64x64/apps/elisa.png
/usr/share/icons/hicolor/scalable/apps/elisa.svg
/usr/share/metainfo/org.kde.elisa.appdata.xml
/usr/share/qlogging-categories5/elisa.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/en/elisa/Screenshot_20180912_232200.png
/usr/share/doc/HTML/en/elisa/index.cache.bz2
/usr/share/doc/HTML/en/elisa/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/elisa/libelisaLib.so.0
/usr/lib64/elisa/libelisaLib.so.0.1
/usr/lib64/qt5/qml/org/kde/elisa/libelisaqmlplugin.so
/usr/lib64/qt5/qml/org/kde/elisa/plugins.qmltypes
/usr/lib64/qt5/qml/org/kde/elisa/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/elisa/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/elisa/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/elisa/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/elisa/7b3e5f0e946c0b599b04a45deebb1aaed782070d
/usr/share/package-licenses/elisa/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/elisa/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/elisa/e712eadfab0d2357c0f50f599ef35ee0d87534cb
/usr/share/package-licenses/elisa/f45ee1c765646813b442ca58de72e20a64a7ddba

%files locales -f elisa.lang
%defattr(-,root,root,-)

