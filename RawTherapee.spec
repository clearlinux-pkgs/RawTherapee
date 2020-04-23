#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : RawTherapee
Version  : 5.8
Release  : 3
URL      : https://github.com/Beep6581/RawTherapee/archive/5.8/RawTherapee-5.8.tar.gz
Source0  : https://github.com/Beep6581/RawTherapee/archive/5.8/RawTherapee-5.8.tar.gz
Summary  : A powerful cross-platform raw photo processing program
Group    : Development/Tools
License  : GPL-3.0 Intel
Requires: RawTherapee-bin = %{version}-%{release}
Requires: RawTherapee-data = %{version}-%{release}
Requires: RawTherapee-license = %{version}-%{release}
Requires: RawTherapee-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : cmake
BuildRequires : libjpeg-turbo-dev
BuildRequires : libpng-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(cairomm-1.0)
BuildRequires : pkgconfig(expat)
BuildRequires : pkgconfig(fftw3f)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(giomm-2.4)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(glibmm-2.4)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(gtkmm-3.0)
BuildRequires : pkgconfig(lcms2)
BuildRequires : pkgconfig(lensfun)
BuildRequires : pkgconfig(libcanberra-gtk3)
BuildRequires : pkgconfig(libiptcdata)
BuildRequires : pkgconfig(librsvg-2.0)
BuildRequires : pkgconfig(libtiff-4)
BuildRequires : pkgconfig(sigc++-2.0)
BuildRequires : zlib-dev

%description
The Independent JPEG Group's JPEG software
==========================================

%package bin
Summary: bin components for the RawTherapee package.
Group: Binaries
Requires: RawTherapee-data = %{version}-%{release}
Requires: RawTherapee-license = %{version}-%{release}

%description bin
bin components for the RawTherapee package.


%package data
Summary: data components for the RawTherapee package.
Group: Data

%description data
data components for the RawTherapee package.


%package doc
Summary: doc components for the RawTherapee package.
Group: Documentation
Requires: RawTherapee-man = %{version}-%{release}

%description doc
doc components for the RawTherapee package.


%package license
Summary: license components for the RawTherapee package.
Group: Default

%description license
license components for the RawTherapee package.


%package man
Summary: man components for the RawTherapee package.
Group: Default

%description man
man components for the RawTherapee package.


%prep
%setup -q -n RawTherapee-5.8
cd %{_builddir}/RawTherapee-5.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1587641493
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake .. -DCMAKE_INSTALL_PREFIX=/usr \
-DLIBDIR=/usr/lib64
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1587641493
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/RawTherapee
cp %{_builddir}/RawTherapee-5.8/licenses/osx_libiomp5_LICENSE.txt %{buildroot}/usr/share/package-licenses/RawTherapee/7199ab66e2eba41e76504929b9d8d52e7a44413f
cp %{_builddir}/RawTherapee-5.8/rtdata/languages/LICENSE %{buildroot}/usr/share/package-licenses/RawTherapee/d6c3778e0861da294b04b13d20a00ae17abb6b56
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/rawtherapee
/usr/bin/rawtherapee-cli

%files data
%defattr(-,root,root,-)
/usr/share/applications/rawtherapee.desktop
/usr/share/icons/hicolor/128x128/apps/rawtherapee.png
/usr/share/icons/hicolor/16x16/apps/rawtherapee.png
/usr/share/icons/hicolor/24x24/apps/rawtherapee.png
/usr/share/icons/hicolor/256x256/apps/rawtherapee.png
/usr/share/icons/hicolor/48x48/apps/rawtherapee.png
/usr/share/metainfo/com.rawtherapee.RawTherapee.appdata.xml
/usr/share/rawtherapee/camconst.json
"/usr/share/rawtherapee/dcpprofiles/Canon EOS 100D.dcp"
"/usr/share/rawtherapee/dcpprofiles/Canon EOS 1300D.dcp"
"/usr/share/rawtherapee/dcpprofiles/Canon EOS 20D.dcp"
"/usr/share/rawtherapee/dcpprofiles/Canon EOS 400D.dcp"
"/usr/share/rawtherapee/dcpprofiles/Canon EOS 40D.dcp"
"/usr/share/rawtherapee/dcpprofiles/Canon EOS 450D.dcp"
"/usr/share/rawtherapee/dcpprofiles/Canon EOS 50D.dcp"
"/usr/share/rawtherapee/dcpprofiles/Canon EOS 550D.dcp"
"/usr/share/rawtherapee/dcpprofiles/Canon EOS 5D Mark III.dcp"
"/usr/share/rawtherapee/dcpprofiles/Canon EOS 5D.dcp"
"/usr/share/rawtherapee/dcpprofiles/Canon EOS 600D.dcp"
"/usr/share/rawtherapee/dcpprofiles/Canon EOS 60D.dcp"
"/usr/share/rawtherapee/dcpprofiles/Canon EOS 650D.dcp"
"/usr/share/rawtherapee/dcpprofiles/Canon EOS 6D Mark II.dcp"
"/usr/share/rawtherapee/dcpprofiles/Canon EOS 6D.dcp"
"/usr/share/rawtherapee/dcpprofiles/Canon EOS 7D Mark II.dcp"
"/usr/share/rawtherapee/dcpprofiles/Canon EOS 7D.dcp"
"/usr/share/rawtherapee/dcpprofiles/Canon EOS D60.dcp"
"/usr/share/rawtherapee/dcpprofiles/Canon EOS RP.dcp"
"/usr/share/rawtherapee/dcpprofiles/Canon EOS-1D Mark III.dcp"
"/usr/share/rawtherapee/dcpprofiles/Canon PowerShot G10.dcp"
"/usr/share/rawtherapee/dcpprofiles/Canon PowerShot G12.dcp"
"/usr/share/rawtherapee/dcpprofiles/Canon PowerShot G7 X.dcp"
"/usr/share/rawtherapee/dcpprofiles/Canon PowerShot S110.dcp"
"/usr/share/rawtherapee/dcpprofiles/FUJIFILM FinePix F600EXR.dcp"
"/usr/share/rawtherapee/dcpprofiles/FUJIFILM GFX 50R.dcp"
"/usr/share/rawtherapee/dcpprofiles/FUJIFILM X-Pro2.dcp"
"/usr/share/rawtherapee/dcpprofiles/FUJIFILM X-S1.dcp"
"/usr/share/rawtherapee/dcpprofiles/FUJIFILM X-T1.dcp"
"/usr/share/rawtherapee/dcpprofiles/FUJIFILM X-T10.dcp"
"/usr/share/rawtherapee/dcpprofiles/FUJIFILM X-T2.dcp"
"/usr/share/rawtherapee/dcpprofiles/FUJIFILM X-T20.dcp"
"/usr/share/rawtherapee/dcpprofiles/FUJIFILM X-T30.dcp"
"/usr/share/rawtherapee/dcpprofiles/FUJIFILM X100S.dcp"
"/usr/share/rawtherapee/dcpprofiles/FUJIFILM X100T.dcp"
"/usr/share/rawtherapee/dcpprofiles/Fujifilm FinePix S9500.dcp"
"/usr/share/rawtherapee/dcpprofiles/Fujifilm X-E1.dcp"
"/usr/share/rawtherapee/dcpprofiles/Fujifilm X-E2.dcp"
"/usr/share/rawtherapee/dcpprofiles/LG Mobile LG-H815.dcp"
"/usr/share/rawtherapee/dcpprofiles/Leaf Aptus 75.dcp"
"/usr/share/rawtherapee/dcpprofiles/MINOLTA DYNAX 7D.dcp"
"/usr/share/rawtherapee/dcpprofiles/NIKON COOLPIX P7800.dcp"
"/usr/share/rawtherapee/dcpprofiles/NIKON D300.dcp"
"/usr/share/rawtherapee/dcpprofiles/NIKON D50.dcp"
"/usr/share/rawtherapee/dcpprofiles/NIKON D5000.dcp"
"/usr/share/rawtherapee/dcpprofiles/NIKON D5600.dcp"
"/usr/share/rawtherapee/dcpprofiles/NIKON D600.dcp"
"/usr/share/rawtherapee/dcpprofiles/NIKON D700.dcp"
"/usr/share/rawtherapee/dcpprofiles/NIKON D70s.dcp"
"/usr/share/rawtherapee/dcpprofiles/NIKON D7200.dcp"
"/usr/share/rawtherapee/dcpprofiles/NIKON D750.dcp"
"/usr/share/rawtherapee/dcpprofiles/NIKON D80.dcp"
"/usr/share/rawtherapee/dcpprofiles/NIKON D800E.dcp"
"/usr/share/rawtherapee/dcpprofiles/NIKON D810.dcp"
"/usr/share/rawtherapee/dcpprofiles/Nikon D200.dcp"
"/usr/share/rawtherapee/dcpprofiles/Nikon D3000.dcp"
"/usr/share/rawtherapee/dcpprofiles/Nikon D3100.dcp"
"/usr/share/rawtherapee/dcpprofiles/Nikon D3S.dcp"
"/usr/share/rawtherapee/dcpprofiles/Nikon D5100.dcp"
"/usr/share/rawtherapee/dcpprofiles/Nikon D7000.dcp"
"/usr/share/rawtherapee/dcpprofiles/OLYMPUS E-510.dcp"
"/usr/share/rawtherapee/dcpprofiles/OLYMPUS E-M10.dcp"
"/usr/share/rawtherapee/dcpprofiles/OLYMPUS E-M1MarkII.dcp"
"/usr/share/rawtherapee/dcpprofiles/Olympus E-1.dcp"
"/usr/share/rawtherapee/dcpprofiles/Olympus E-520.dcp"
"/usr/share/rawtherapee/dcpprofiles/Olympus E-M5.dcp"
"/usr/share/rawtherapee/dcpprofiles/Olympus E-P2.dcp"
"/usr/share/rawtherapee/dcpprofiles/Olympus XZ-1.dcp"
"/usr/share/rawtherapee/dcpprofiles/PENTAX K-5 II.dcp"
"/usr/share/rawtherapee/dcpprofiles/PENTAX K-5.dcp"
"/usr/share/rawtherapee/dcpprofiles/PENTAX K10D.dcp"
"/usr/share/rawtherapee/dcpprofiles/Panasonic DC-G9.dcp"
"/usr/share/rawtherapee/dcpprofiles/Panasonic DC-GX9.dcp"
"/usr/share/rawtherapee/dcpprofiles/Panasonic DC-S1.dcp"
"/usr/share/rawtherapee/dcpprofiles/Panasonic DC-TZ91.dcp"
"/usr/share/rawtherapee/dcpprofiles/Panasonic DMC-FZ1000.dcp"
"/usr/share/rawtherapee/dcpprofiles/Panasonic DMC-FZ150.dcp"
"/usr/share/rawtherapee/dcpprofiles/Panasonic DMC-FZ35.dcp"
"/usr/share/rawtherapee/dcpprofiles/Panasonic DMC-FZ38.dcp"
"/usr/share/rawtherapee/dcpprofiles/Panasonic DMC-G1.dcp"
"/usr/share/rawtherapee/dcpprofiles/Panasonic DMC-G3.dcp"
"/usr/share/rawtherapee/dcpprofiles/Panasonic DMC-G5.dcp"
"/usr/share/rawtherapee/dcpprofiles/Panasonic DMC-GH1.dcp"
"/usr/share/rawtherapee/dcpprofiles/Panasonic DMC-GH2.dcp"
"/usr/share/rawtherapee/dcpprofiles/Panasonic DMC-GX7.dcp"
"/usr/share/rawtherapee/dcpprofiles/Panasonic DMC-GX85.dcp"
"/usr/share/rawtherapee/dcpprofiles/Pentax K-r.dcp"
"/usr/share/rawtherapee/dcpprofiles/Pentax K200D.dcp"
"/usr/share/rawtherapee/dcpprofiles/RICOH GR III.dcp"
"/usr/share/rawtherapee/dcpprofiles/RICOH PENTAX K-1.dcp"
"/usr/share/rawtherapee/dcpprofiles/RICOH PENTAX K-3.dcp"
"/usr/share/rawtherapee/dcpprofiles/SONY DSLR-A580.dcp"
"/usr/share/rawtherapee/dcpprofiles/SONY ILCE-6000.dcp"
"/usr/share/rawtherapee/dcpprofiles/SONY ILCE-6300.dcp"
"/usr/share/rawtherapee/dcpprofiles/SONY ILCE-6500.dcp"
"/usr/share/rawtherapee/dcpprofiles/SONY ILCE-7M2.dcp"
"/usr/share/rawtherapee/dcpprofiles/SONY ILCE-7M3.dcp"
"/usr/share/rawtherapee/dcpprofiles/SONY ILCE-7RM3.dcp"
"/usr/share/rawtherapee/dcpprofiles/SONY SLT-A99V.dcp"
"/usr/share/rawtherapee/dcpprofiles/Sony DSLR-A700.dcp"
"/usr/share/rawtherapee/dcpprofiles/Sony DSLR-A900.dcp"
"/usr/share/rawtherapee/dcpprofiles/Sony NEX-5N.dcp"
"/usr/share/rawtherapee/dcpprofiles/Sony SLT-A55V.dcp"
"/usr/share/rawtherapee/dcpprofiles/YI TECHNOLOGY M1.dcp"
/usr/share/rawtherapee/dcpprofiles/camera_model_aliases.json
"/usr/share/rawtherapee/iccprofiles/input/Canon EOS 20D.icc"
"/usr/share/rawtherapee/iccprofiles/input/Canon EOS 40D.icc"
"/usr/share/rawtherapee/iccprofiles/input/Canon EOS 450D.icc"
"/usr/share/rawtherapee/iccprofiles/input/Canon EOS 550D.icc"
"/usr/share/rawtherapee/iccprofiles/input/Canon EOS 5D.icc"
"/usr/share/rawtherapee/iccprofiles/input/Canon EOS-1D Mark III.icc"
"/usr/share/rawtherapee/iccprofiles/input/Canon PowerShot G10.icc"
"/usr/share/rawtherapee/iccprofiles/input/Canon PowerShot G12.icc"
"/usr/share/rawtherapee/iccprofiles/input/Nikon D200.icc"
"/usr/share/rawtherapee/iccprofiles/input/Nikon D3000.icc"
"/usr/share/rawtherapee/iccprofiles/input/Nikon D3100.icc"
"/usr/share/rawtherapee/iccprofiles/input/Nikon D3S.icc"
"/usr/share/rawtherapee/iccprofiles/input/Nikon D700.icc"
"/usr/share/rawtherapee/iccprofiles/input/Nikon D7000.icc"
"/usr/share/rawtherapee/iccprofiles/input/Olympus E-P2.icc"
"/usr/share/rawtherapee/iccprofiles/input/Panasonic DMC-FZ150.icc"
"/usr/share/rawtherapee/iccprofiles/input/Panasonic DMC-FZ35.icc"
"/usr/share/rawtherapee/iccprofiles/input/Panasonic DMC-FZ38.icc"
"/usr/share/rawtherapee/iccprofiles/input/Panasonic DMC-G1.icc"
"/usr/share/rawtherapee/iccprofiles/input/Panasonic DMC-G3.icc"
"/usr/share/rawtherapee/iccprofiles/input/Panasonic DMC-GH1.icc"
"/usr/share/rawtherapee/iccprofiles/input/Panasonic DMC-GH2.icc"
"/usr/share/rawtherapee/iccprofiles/input/Pentax K200D.icc"
"/usr/share/rawtherapee/iccprofiles/input/Sony DSLR-A700.icc"
"/usr/share/rawtherapee/iccprofiles/input/Sony DSLR-A900.icc"
"/usr/share/rawtherapee/iccprofiles/input/Sony SLT-A55V.icc"
/usr/share/rawtherapee/iccprofiles/input/sd14-bl15-crop-matrix-gamma-wp10.icm
/usr/share/rawtherapee/iccprofiles/input/sd14-bl15-crop-matrix-gamma-wp11.icm
/usr/share/rawtherapee/iccprofiles/input/sd14-bl15-crop-matrix-gamma-wp12.icm
/usr/share/rawtherapee/iccprofiles/input/sd1_merrill_cloudy8140-CROP-WP10.icm
/usr/share/rawtherapee/iccprofiles/input/sd1_merrill_cloudy8140-CROP-WP11.icm
/usr/share/rawtherapee/iccprofiles/input/sd1_merrill_sunny8161-crop-wp10.icm
/usr/share/rawtherapee/iccprofiles/input/sd1_merrill_sunny8161-crop-wp11.icm
/usr/share/rawtherapee/iccprofiles/input/sd1_merrill_tungsten8130-CROP-WP10.icm
/usr/share/rawtherapee/iccprofiles/input/sd1_merrill_tungsten8130-CROP-WP11.icm
"/usr/share/rawtherapee/iccprofiles/output/DCI-P3 D65.icc"
"/usr/share/rawtherapee/iccprofiles/output/DCI-P3 Theater.icc"
/usr/share/rawtherapee/iccprofiles/output/RTv2_ACES-AP0.icc
/usr/share/rawtherapee/iccprofiles/output/RTv2_ACES-AP1.icc
/usr/share/rawtherapee/iccprofiles/output/RTv2_Best.icc
/usr/share/rawtherapee/iccprofiles/output/RTv2_Beta.icc
/usr/share/rawtherapee/iccprofiles/output/RTv2_Bruce.icc
/usr/share/rawtherapee/iccprofiles/output/RTv2_Large.icc
/usr/share/rawtherapee/iccprofiles/output/RTv2_Medium.icc
/usr/share/rawtherapee/iccprofiles/output/RTv2_Rec2020.icc
/usr/share/rawtherapee/iccprofiles/output/RTv2_Wide.icc
/usr/share/rawtherapee/iccprofiles/output/RTv2_sRGB.icc
/usr/share/rawtherapee/iccprofiles/output/RTv4_ACES-AP0.icc
/usr/share/rawtherapee/iccprofiles/output/RTv4_ACES-AP1.icc
/usr/share/rawtherapee/iccprofiles/output/RTv4_Best.icc
/usr/share/rawtherapee/iccprofiles/output/RTv4_Beta.icc
/usr/share/rawtherapee/iccprofiles/output/RTv4_Bruce.icc
/usr/share/rawtherapee/iccprofiles/output/RTv4_Large.icc
/usr/share/rawtherapee/iccprofiles/output/RTv4_Medium.icc
/usr/share/rawtherapee/iccprofiles/output/RTv4_Rec2020.icc
/usr/share/rawtherapee/iccprofiles/output/RTv4_Wide.icc
/usr/share/rawtherapee/iccprofiles/output/RTv4_sRGB.icc
/usr/share/rawtherapee/images/add-small.svg
/usr/share/rawtherapee/images/add.svg
/usr/share/rawtherapee/images/aperture.svg
/usr/share/rawtherapee/images/arrow-down-small.svg
/usr/share/rawtherapee/images/arrow-left-small.svg
/usr/share/rawtherapee/images/arrow-right-small.svg
/usr/share/rawtherapee/images/arrow-up-small.svg
/usr/share/rawtherapee/images/arrow-updown.svg
/usr/share/rawtherapee/images/arrow2-left.svg
/usr/share/rawtherapee/images/arrow2-right.svg
/usr/share/rawtherapee/images/atom.svg
/usr/share/rawtherapee/images/bayer.svg
/usr/share/rawtherapee/images/beforeafter.svg
/usr/share/rawtherapee/images/cancel-small.svg
/usr/share/rawtherapee/images/cancel.svg
/usr/share/rawtherapee/images/circle-black-small.svg
/usr/share/rawtherapee/images/circle-blue-green-small.svg
/usr/share/rawtherapee/images/circle-blue-red-small.svg
/usr/share/rawtherapee/images/circle-blue-small.svg
/usr/share/rawtherapee/images/circle-blue-yellow-small.svg
/usr/share/rawtherapee/images/circle-cyan-red-small.svg
/usr/share/rawtherapee/images/circle-cyan-small.svg
/usr/share/rawtherapee/images/circle-darkgray-small.svg
/usr/share/rawtherapee/images/circle-empty-blue-small.svg
/usr/share/rawtherapee/images/circle-empty-darkgray-small.svg
/usr/share/rawtherapee/images/circle-empty-gray-small.svg
/usr/share/rawtherapee/images/circle-empty-green-small.svg
/usr/share/rawtherapee/images/circle-empty-purple-small.svg
/usr/share/rawtherapee/images/circle-empty-red-small.svg
/usr/share/rawtherapee/images/circle-empty-yellow-small.svg
/usr/share/rawtherapee/images/circle-gray-blue-small.svg
/usr/share/rawtherapee/images/circle-gray-green-small.svg
/usr/share/rawtherapee/images/circle-gray-red-small.svg
/usr/share/rawtherapee/images/circle-gray-small.svg
/usr/share/rawtherapee/images/circle-green-blue-small.svg
/usr/share/rawtherapee/images/circle-green-red-small.svg
/usr/share/rawtherapee/images/circle-green-small.svg
/usr/share/rawtherapee/images/circle-magenta-small.svg
/usr/share/rawtherapee/images/circle-orange-small.svg
/usr/share/rawtherapee/images/circle-purple-small.svg
/usr/share/rawtherapee/images/circle-red-blue-small.svg
/usr/share/rawtherapee/images/circle-red-cyan-small.svg
/usr/share/rawtherapee/images/circle-red-green-small.svg
/usr/share/rawtherapee/images/circle-red-small.svg
/usr/share/rawtherapee/images/circle-white-small.svg
/usr/share/rawtherapee/images/circle-yellow-blue-small.svg
/usr/share/rawtherapee/images/circle-yellow-small.svg
/usr/share/rawtherapee/images/color-circles.svg
/usr/share/rawtherapee/images/color-picker-add-hicontrast.svg
/usr/share/rawtherapee/images/color-picker-add.svg
/usr/share/rawtherapee/images/color-picker-bars.svg
/usr/share/rawtherapee/images/color-picker-hicontrast.svg
/usr/share/rawtherapee/images/color-picker-hide.svg
/usr/share/rawtherapee/images/color-picker-small.svg
/usr/share/rawtherapee/images/color-picker.svg
/usr/share/rawtherapee/images/contrastmask-off.svg
/usr/share/rawtherapee/images/contrastmask-on.svg
/usr/share/rawtherapee/images/copy.svg
/usr/share/rawtherapee/images/crop-auto-small.svg
/usr/share/rawtherapee/images/crop-auto.svg
/usr/share/rawtherapee/images/crop-point-hicontrast.svg
/usr/share/rawtherapee/images/crop-small.svg
/usr/share/rawtherapee/images/crop.svg
/usr/share/rawtherapee/images/crossed-arrows-in.svg
/usr/share/rawtherapee/images/crossed-arrows-out.svg
/usr/share/rawtherapee/images/crosshair-adjust.svg
/usr/share/rawtherapee/images/crosshair-hicontrast.svg
/usr/share/rawtherapee/images/crosshair-node-curve.svg
/usr/share/rawtherapee/images/crosshair-small.svg
/usr/share/rawtherapee/images/curve-catmullrom-small.svg
/usr/share/rawtherapee/images/curve-catmullrom.svg
/usr/share/rawtherapee/images/curve-controlpoints-small.svg
/usr/share/rawtherapee/images/curve-controlpoints.svg
/usr/share/rawtherapee/images/curve-flat-small.svg
/usr/share/rawtherapee/images/curve-flat.svg
/usr/share/rawtherapee/images/curve-linear-small.svg
/usr/share/rawtherapee/images/curve-linear.svg
/usr/share/rawtherapee/images/curve-nurbs-small.svg
/usr/share/rawtherapee/images/curve-nurbs.svg
/usr/share/rawtherapee/images/curve-parametric-small.svg
/usr/share/rawtherapee/images/curve-parametric.svg
/usr/share/rawtherapee/images/curve-spline-small.svg
/usr/share/rawtherapee/images/curve-spline.svg
/usr/share/rawtherapee/images/detail.svg
/usr/share/rawtherapee/images/device-floppy.svg
/usr/share/rawtherapee/images/device-hdd.svg
/usr/share/rawtherapee/images/device-network.svg
/usr/share/rawtherapee/images/device-optical.svg
/usr/share/rawtherapee/images/device-usb.svg
/usr/share/rawtherapee/images/distortion-auto-small.svg
/usr/share/rawtherapee/images/distortion-auto.svg
/usr/share/rawtherapee/images/distortion-barrel-small.svg
/usr/share/rawtherapee/images/distortion-barrel.svg
/usr/share/rawtherapee/images/distortion-pincushion-small.svg
/usr/share/rawtherapee/images/distortion-pincushion.svg
/usr/share/rawtherapee/images/edit-point.svg
/usr/share/rawtherapee/images/empty.png
/usr/share/rawtherapee/images/equilizer-narrow.svg
/usr/share/rawtherapee/images/equilizer-wide.svg
/usr/share/rawtherapee/images/expander-closed-small.svg
/usr/share/rawtherapee/images/expander-open-small.svg
/usr/share/rawtherapee/images/exposure.svg
/usr/share/rawtherapee/images/filetype-hdr.svg
/usr/share/rawtherapee/images/filetype-ps.svg
/usr/share/rawtherapee/images/filter-clear.svg
/usr/share/rawtherapee/images/filter-original.svg
/usr/share/rawtherapee/images/filter-original2.svg
/usr/share/rawtherapee/images/filter.svg
/usr/share/rawtherapee/images/flip-horizontal.svg
/usr/share/rawtherapee/images/flip-vertical.svg
/usr/share/rawtherapee/images/focusscreen-off.svg
/usr/share/rawtherapee/images/focusscreen-on.svg
/usr/share/rawtherapee/images/folder-closed-home-small.svg
/usr/share/rawtherapee/images/folder-closed-home.svg
/usr/share/rawtherapee/images/folder-closed-recent-small.svg
/usr/share/rawtherapee/images/folder-closed-recent.svg
/usr/share/rawtherapee/images/folder-closed-small.svg
/usr/share/rawtherapee/images/folder-closed.svg
/usr/share/rawtherapee/images/folder-open-recent-small.svg
/usr/share/rawtherapee/images/folder-open-recent.svg
/usr/share/rawtherapee/images/folder-open-small.svg
/usr/share/rawtherapee/images/folder-open.svg
/usr/share/rawtherapee/images/fullscreen-enter.svg
/usr/share/rawtherapee/images/fullscreen-leave.svg
/usr/share/rawtherapee/images/gamut-hist.svg
/usr/share/rawtherapee/images/gamut-plus.svg
/usr/share/rawtherapee/images/gamut-softproof.svg
/usr/share/rawtherapee/images/gamut-warning.svg
/usr/share/rawtherapee/images/gamut_srgb_prophoto_xy.svg
/usr/share/rawtherapee/images/gears-pause.svg
/usr/share/rawtherapee/images/gears-play.svg
/usr/share/rawtherapee/images/gears-small.svg
/usr/share/rawtherapee/images/gears.svg
/usr/share/rawtherapee/images/goto-end-small.svg
/usr/share/rawtherapee/images/goto-start-small.svg
/usr/share/rawtherapee/images/hand-closed-hicontrast.svg
/usr/share/rawtherapee/images/hand-open-hicontrast.svg
/usr/share/rawtherapee/images/hand-open.svg
/usr/share/rawtherapee/images/histogram-bar-off-small.svg
/usr/share/rawtherapee/images/histogram-bar-on-small.svg
/usr/share/rawtherapee/images/histogram-bayer-off-small.svg
/usr/share/rawtherapee/images/histogram-bayer-on-small.svg
/usr/share/rawtherapee/images/histogram-blue-off-small.svg
/usr/share/rawtherapee/images/histogram-blue-on-small.svg
/usr/share/rawtherapee/images/histogram-gold-off-small.svg
/usr/share/rawtherapee/images/histogram-gold-on-small.svg
/usr/share/rawtherapee/images/histogram-green-off-small.svg
/usr/share/rawtherapee/images/histogram-green-on-small.svg
/usr/share/rawtherapee/images/histogram-mode-linear-small.svg
/usr/share/rawtherapee/images/histogram-mode-logx-small.svg
/usr/share/rawtherapee/images/histogram-mode-logxy-small.svg
/usr/share/rawtherapee/images/histogram-red-off-small.svg
/usr/share/rawtherapee/images/histogram-red-on-small.svg
/usr/share/rawtherapee/images/histogram-silver-off-small.svg
/usr/share/rawtherapee/images/histogram-silver-on-small.svg
/usr/share/rawtherapee/images/info.svg
/usr/share/rawtherapee/images/intent-absolute.svg
/usr/share/rawtherapee/images/intent-perceptual.svg
/usr/share/rawtherapee/images/intent-relative.svg
/usr/share/rawtherapee/images/intent-saturation.svg
/usr/share/rawtherapee/images/magnifier-1to1-small.svg
/usr/share/rawtherapee/images/magnifier-1to1.svg
/usr/share/rawtherapee/images/magnifier-crop.svg
/usr/share/rawtherapee/images/magnifier-fit.svg
/usr/share/rawtherapee/images/magnifier-minus-small.svg
/usr/share/rawtherapee/images/magnifier-minus.svg
/usr/share/rawtherapee/images/magnifier-plus-small.svg
/usr/share/rawtherapee/images/magnifier-plus.svg
/usr/share/rawtherapee/images/magnifier.svg
/usr/share/rawtherapee/images/metadata.svg
/usr/share/rawtherapee/images/node-move-nw-se-hicontrast.svg
/usr/share/rawtherapee/images/node-move-sw-ne-hicontrast.svg
/usr/share/rawtherapee/images/node-move-x-hicontrast.svg
/usr/share/rawtherapee/images/node-move-xy-hicontrast.svg
/usr/share/rawtherapee/images/node-move-y-hicontrast.svg
/usr/share/rawtherapee/images/one-to-one-small.svg
/usr/share/rawtherapee/images/ornament1.svg
/usr/share/rawtherapee/images/padlock-locked-small.svg
/usr/share/rawtherapee/images/padlock-unlocked-small.svg
/usr/share/rawtherapee/images/palette-brush.svg
/usr/share/rawtherapee/images/panel-to-bottom.svg
/usr/share/rawtherapee/images/panel-to-left.svg
/usr/share/rawtherapee/images/panel-to-right.svg
/usr/share/rawtherapee/images/panel-to-top.svg
/usr/share/rawtherapee/images/paste.svg
/usr/share/rawtherapee/images/perspective-horizontal-left-small.svg
/usr/share/rawtherapee/images/perspective-horizontal-left.svg
/usr/share/rawtherapee/images/perspective-horizontal-right-small.svg
/usr/share/rawtherapee/images/perspective-horizontal-right.svg
/usr/share/rawtherapee/images/perspective-vertical-bottom-small.svg
/usr/share/rawtherapee/images/perspective-vertical-bottom.svg
/usr/share/rawtherapee/images/perspective-vertical-top-small.svg
/usr/share/rawtherapee/images/perspective-vertical-top.svg
/usr/share/rawtherapee/images/power-inconsistent-small.svg
/usr/share/rawtherapee/images/power-off-small.svg
/usr/share/rawtherapee/images/power-on-small.svg
/usr/share/rawtherapee/images/preferences.svg
/usr/share/rawtherapee/images/profile-filled.svg
/usr/share/rawtherapee/images/profile-partial.svg
/usr/share/rawtherapee/images/questionmark.svg
/usr/share/rawtherapee/images/rawtherapee-logo-128.png
/usr/share/rawtherapee/images/rawtherapee-logo-16.png
/usr/share/rawtherapee/images/rawtherapee-logo-24.png
/usr/share/rawtherapee/images/rawtherapee-logo-256.png
/usr/share/rawtherapee/images/rawtherapee-logo-32.png
/usr/share/rawtherapee/images/rawtherapee-logo-48.png
/usr/share/rawtherapee/images/rawtherapee-logo-64.png
/usr/share/rawtherapee/images/rawtherapee.ico
/usr/share/rawtherapee/images/rawtherapee_ico.xcf
/usr/share/rawtherapee/images/redo-all.svg
/usr/share/rawtherapee/images/redo-small.svg
/usr/share/rawtherapee/images/redo.svg
/usr/share/rawtherapee/images/refresh-red-small.svg
/usr/share/rawtherapee/images/refresh-small.svg
/usr/share/rawtherapee/images/refresh.svg
/usr/share/rawtherapee/images/remove-small.svg
/usr/share/rawtherapee/images/remove.svg
/usr/share/rawtherapee/images/rotate-aroundnode-hicontrast.svg
/usr/share/rawtherapee/images/rotate-aroundnode.svg
/usr/share/rawtherapee/images/rotate-left-90.svg
/usr/share/rawtherapee/images/rotate-left-small.svg
/usr/share/rawtherapee/images/rotate-left.svg
/usr/share/rawtherapee/images/rotate-right-90.svg
/usr/share/rawtherapee/images/rotate-right-small.svg
/usr/share/rawtherapee/images/rotate-right.svg
/usr/share/rawtherapee/images/rotate-straighten-small.svg
/usr/share/rawtherapee/images/rotate-straighten.svg
/usr/share/rawtherapee/images/rt-logo.svg
/usr/share/rawtherapee/images/save-small.svg
/usr/share/rawtherapee/images/save.svg
/usr/share/rawtherapee/images/saved-no-small.svg
/usr/share/rawtherapee/images/saved-yes-small.svg
/usr/share/rawtherapee/images/splash.svg
/usr/share/rawtherapee/images/splash_template.svg
/usr/share/rawtherapee/images/square-toggle-black-off-narrow.svg
/usr/share/rawtherapee/images/square-toggle-black-on-narrow.svg
/usr/share/rawtherapee/images/square-toggle-blue-off-narrow.svg
/usr/share/rawtherapee/images/square-toggle-blue-on-narrow.svg
/usr/share/rawtherapee/images/square-toggle-gray-off-narrow.svg
/usr/share/rawtherapee/images/square-toggle-gray-on-narrow.svg
/usr/share/rawtherapee/images/square-toggle-green-off-narrow.svg
/usr/share/rawtherapee/images/square-toggle-green-on-narrow.svg
/usr/share/rawtherapee/images/square-toggle-luminosity-off-narrow.svg
/usr/share/rawtherapee/images/square-toggle-luminosity-on-narrow.svg
/usr/share/rawtherapee/images/square-toggle-red-off-narrow.svg
/usr/share/rawtherapee/images/square-toggle-red-on-narrow.svg
/usr/share/rawtherapee/images/square-toggle-theme-off-narrow.svg
/usr/share/rawtherapee/images/square-toggle-theme-on-narrow.svg
/usr/share/rawtherapee/images/square-toggle-white-off-narrow.svg
/usr/share/rawtherapee/images/square-toggle-white-on-narrow.svg
/usr/share/rawtherapee/images/star-gold-hollow-narrow.svg
/usr/share/rawtherapee/images/star-gold-hollow-small.svg
/usr/share/rawtherapee/images/star-gold-narrow.svg
/usr/share/rawtherapee/images/star-gold-small.svg
/usr/share/rawtherapee/images/star-hollow-narrow.svg
/usr/share/rawtherapee/images/star-hollow-small.svg
/usr/share/rawtherapee/images/star-narrow.svg
/usr/share/rawtherapee/images/star-small.svg
/usr/share/rawtherapee/images/star.svg
/usr/share/rawtherapee/images/template-16.svg
/usr/share/rawtherapee/images/template-24.svg
/usr/share/rawtherapee/images/template-narrow.svg
/usr/share/rawtherapee/images/tick-green-hollow-small.svg
/usr/share/rawtherapee/images/tick-green-hollow.svg
/usr/share/rawtherapee/images/tick-green-small.svg
/usr/share/rawtherapee/images/tick-green.svg
/usr/share/rawtherapee/images/tick-hollow-small.svg
/usr/share/rawtherapee/images/tick-small.svg
/usr/share/rawtherapee/images/tick.svg
/usr/share/rawtherapee/images/transform.svg
/usr/share/rawtherapee/images/trash-delete.svg
/usr/share/rawtherapee/images/trash-empty-show.svg
/usr/share/rawtherapee/images/trash-empty.svg
/usr/share/rawtherapee/images/trash-full-show.svg
/usr/share/rawtherapee/images/trash-full.svg
/usr/share/rawtherapee/images/trash-hide-deleted.svg
/usr/share/rawtherapee/images/trash-remove-small.svg
/usr/share/rawtherapee/images/trash-remove.svg
/usr/share/rawtherapee/images/trash-small.svg
/usr/share/rawtherapee/images/undo-all.svg
/usr/share/rawtherapee/images/undo-small.svg
/usr/share/rawtherapee/images/undo.svg
/usr/share/rawtherapee/images/warning-highlights.svg
/usr/share/rawtherapee/images/warning-shadows.svg
/usr/share/rawtherapee/images/warning.svg
/usr/share/rawtherapee/images/wavelets.svg
/usr/share/rawtherapee/images/wb-auto-small.svg
/usr/share/rawtherapee/images/wb-auto.svg
/usr/share/rawtherapee/images/wb-camera-small.svg
/usr/share/rawtherapee/images/wb-camera.svg
/usr/share/rawtherapee/images/wb-cloudy-small.svg
/usr/share/rawtherapee/images/wb-cloudy.svg
/usr/share/rawtherapee/images/wb-custom-small.svg
/usr/share/rawtherapee/images/wb-custom.svg
/usr/share/rawtherapee/images/wb-flash-small.svg
/usr/share/rawtherapee/images/wb-flash.svg
/usr/share/rawtherapee/images/wb-fluorescent-small.svg
/usr/share/rawtherapee/images/wb-fluorescent.svg
/usr/share/rawtherapee/images/wb-lamp-small.svg
/usr/share/rawtherapee/images/wb-lamp.svg
/usr/share/rawtherapee/images/wb-led-small.svg
/usr/share/rawtherapee/images/wb-led.svg
/usr/share/rawtherapee/images/wb-shade-small.svg
/usr/share/rawtherapee/images/wb-shade.svg
/usr/share/rawtherapee/images/wb-sun-small.svg
/usr/share/rawtherapee/images/wb-sun.svg
/usr/share/rawtherapee/images/wb-tungsten-small.svg
/usr/share/rawtherapee/images/wb-tungsten.svg
/usr/share/rawtherapee/images/wb-water-small.svg
/usr/share/rawtherapee/images/wb-water.svg
/usr/share/rawtherapee/images/window-add.svg
/usr/share/rawtherapee/languages/Catala
"/usr/share/rawtherapee/languages/Chinese (Simplified)"
/usr/share/rawtherapee/languages/Czech
/usr/share/rawtherapee/languages/Deutsch
"/usr/share/rawtherapee/languages/English (UK)"
"/usr/share/rawtherapee/languages/English (US)"
/usr/share/rawtherapee/languages/Espanol
/usr/share/rawtherapee/languages/Francais
/usr/share/rawtherapee/languages/Italiano
/usr/share/rawtherapee/languages/Japanese
/usr/share/rawtherapee/languages/LICENSE
/usr/share/rawtherapee/languages/Magyar
/usr/share/rawtherapee/languages/Nederlands
/usr/share/rawtherapee/languages/Polish
/usr/share/rawtherapee/languages/Portugues
"/usr/share/rawtherapee/languages/Portugues (Brasil)"
/usr/share/rawtherapee/languages/README
/usr/share/rawtherapee/languages/Russian
"/usr/share/rawtherapee/languages/Serbian (Cyrilic Characters)"
/usr/share/rawtherapee/languages/Slovenian
/usr/share/rawtherapee/languages/Swedish
/usr/share/rawtherapee/languages/default
/usr/share/rawtherapee/options
"/usr/share/rawtherapee/profiles/Auto-Matched Curve - ISO High.pp3"
"/usr/share/rawtherapee/profiles/Auto-Matched Curve - ISO Low.pp3"
"/usr/share/rawtherapee/profiles/Auto-Matched Curve - ISO Medium.pp3"
/usr/share/rawtherapee/profiles/Non-raw/Brighten.pp3
"/usr/share/rawtherapee/profiles/Pixel Shift/PS ISO High.pp3"
"/usr/share/rawtherapee/profiles/Pixel Shift/PS ISO Low.pp3"
"/usr/share/rawtherapee/profiles/Pixel Shift/PS ISO Medium.pp3"
"/usr/share/rawtherapee/profiles/Pixel Shift/PS No Motion.pp3"
"/usr/share/rawtherapee/profiles/Pop/Pop 1.pp3"
"/usr/share/rawtherapee/profiles/Pop/Pop 2 Lab.pp3"
"/usr/share/rawtherapee/profiles/Pop/Pop 3 Skin.pp3"
"/usr/share/rawtherapee/profiles/Pop/Pop 4 Black-and-White.pp3"
"/usr/share/rawtherapee/profiles/Standard Film Curve - ISO High.pp3"
"/usr/share/rawtherapee/profiles/Standard Film Curve - ISO Low.pp3"
"/usr/share/rawtherapee/profiles/Standard Film Curve - ISO Medium.pp3"
/usr/share/rawtherapee/profiles/Unclipped.pp3
/usr/share/rawtherapee/sounds/BatchComplete.wav
/usr/share/rawtherapee/sounds/Empty.wav
/usr/share/rawtherapee/sounds/ProcessComplete.wav
/usr/share/rawtherapee/themes/RawTherapee-GTK3-20_.css
/usr/share/rawtherapee/themes/RawTherapee-GTK3-_19.css
"/usr/share/rawtherapee/themes/TooWaBlue - Bright-GTK3-20_.css"
"/usr/share/rawtherapee/themes/TooWaBlue - Dark-GTK3-20_.css"
/usr/share/rawtherapee/themes/TooWaBlue-GTK3-20_.css
/usr/share/rawtherapee/themes/TooWaBlue-GTK3-_19.css
"/usr/share/rawtherapee/themes/TooWaGrey - Average Surround-GTK3-20_.css"
"/usr/share/rawtherapee/themes/TooWaGrey - Bright-GTK3-20_.css"
"/usr/share/rawtherapee/themes/TooWaGrey - Dark-GTK3-20_.css"
/usr/share/rawtherapee/themes/TooWaGrey-GTK3-20_.css
/usr/share/rawtherapee/themes/images/svg/twb/checkbox-checked-disabled.svg
/usr/share/rawtherapee/themes/images/svg/twb/checkbox-checked.svg
/usr/share/rawtherapee/themes/images/svg/twb/checkbox-inconsistent-disabled.svg
/usr/share/rawtherapee/themes/images/svg/twb/checkbox-inconsistent.svg
/usr/share/rawtherapee/themes/images/svg/twb/checkbox-unchecked-disabled.svg
/usr/share/rawtherapee/themes/images/svg/twb/checkbox-unchecked.svg
/usr/share/rawtherapee/themes/images/svg/twb/radio-checked-disabled.svg
/usr/share/rawtherapee/themes/images/svg/twb/radio-checked.svg
/usr/share/rawtherapee/themes/images/svg/twb/radio-inconsistent-disabled.svg
/usr/share/rawtherapee/themes/images/svg/twb/radio-inconsistent.svg
/usr/share/rawtherapee/themes/images/svg/twb/radio-unchecked-disabled.svg
/usr/share/rawtherapee/themes/images/svg/twb/radio-unchecked.svg
/usr/share/rawtherapee/themes/images/twb/checkbox-checked-disabled.png
/usr/share/rawtherapee/themes/images/twb/checkbox-checked.png
/usr/share/rawtherapee/themes/images/twb/checkbox-inconsistent-disabled.png
/usr/share/rawtherapee/themes/images/twb/checkbox-inconsistent.png
/usr/share/rawtherapee/themes/images/twb/checkbox-unchecked-disabled.png
/usr/share/rawtherapee/themes/images/twb/checkbox-unchecked.png
/usr/share/rawtherapee/themes/images/twb/radio-checked-disabled.png
/usr/share/rawtherapee/themes/images/twb/radio-checked.png
/usr/share/rawtherapee/themes/images/twb/radio-inconsistent-disabled.png
/usr/share/rawtherapee/themes/images/twb/radio-inconsistent.png
/usr/share/rawtherapee/themes/images/twb/radio-unchecked-disabled.png
/usr/share/rawtherapee/themes/images/twb/radio-unchecked.png
/usr/share/rawtherapee/themes/size.css
/usr/share/rawtherapee/themes/system.iconset

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/rawtherapee/AUTHORS.txt
/usr/share/doc/rawtherapee/AboutThisBuild.txt
/usr/share/doc/rawtherapee/LICENSE.txt
/usr/share/doc/rawtherapee/RELEASE_NOTES.txt

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/RawTherapee/7199ab66e2eba41e76504929b9d8d52e7a44413f
/usr/share/package-licenses/RawTherapee/d6c3778e0861da294b04b13d20a00ae17abb6b56

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/rawtherapee.1
