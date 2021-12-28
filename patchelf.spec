#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : patchelf
Version  : 0.14.3
Release  : 7
URL      : https://github.com/NixOS/patchelf/archive/0.14.3/patchelf-0.14.3.tar.gz
Source0  : https://github.com/NixOS/patchelf/archive/0.14.3/patchelf-0.14.3.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: patchelf-bin = %{version}-%{release}
Requires: patchelf-license = %{version}-%{release}
Requires: patchelf-man = %{version}-%{release}

%description
PatchELF is a simple utility for modifying existing ELF executables and
libraries.  In particular, it can do the following:

%package bin
Summary: bin components for the patchelf package.
Group: Binaries
Requires: patchelf-license = %{version}-%{release}

%description bin
bin components for the patchelf package.


%package doc
Summary: doc components for the patchelf package.
Group: Documentation
Requires: patchelf-man = %{version}-%{release}

%description doc
doc components for the patchelf package.


%package license
Summary: license components for the patchelf package.
Group: Default

%description license
license components for the patchelf package.


%package man
Summary: man components for the patchelf package.
Group: Default

%description man
man components for the patchelf package.


%prep
%setup -q -n patchelf-0.14.3
cd %{_builddir}/patchelf-0.14.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640733705
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1640733705
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/patchelf
cp %{_builddir}/patchelf-0.14.3/COPYING %{buildroot}/usr/share/package-licenses/patchelf/8624bcdae55baeef00cd11d5dfcfa60f68710a02
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/patchelf

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/patchelf/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/patchelf/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/patchelf.1
