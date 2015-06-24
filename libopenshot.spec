%global optflags %(echo %{optflags} -Wl,--as-needed )

Name:           libopenshot
Version:        0.0.4
Release:        2%{?dist}
Summary:        Library for creating and editing videos

License:        LGPLv3+
URL:            http://www.openshot.org/
Source0:        https://launchpad.net/%{name}/0.0/%{version}/+download/%{name}-%{version}.tar.gz
Patch0:         libopenshot-0.0.4-swig.patch

BuildRequires:  cmake swig
BuildRequires:  python3-devel
BuildRequires:  ImageMagick-c++-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  libopenshot-audio-devel >= %{version}
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  unittest-cpp-devel


%description
OpenShot Library (libopenshot) is an open-source project
dedicated to delivering high quality video editing, animation,
and playback solutions to the world. For more information
visit <http://www.openshot.org/>.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package -n     python-%{name}
Summary:        Python bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Group:          Development/Libraries

%description    -n python-%{name}
The python-%{name} package contains python bindings for 
applications that use %{name}.


%prep
%setup -q
%patch0 -p1


%build
%cmake .
make %{?_smp_mflags}


%install
%make_install


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc AUTHORS COPYING README
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/*.so

%files -n python-libopenshot
%{python3_sitearch}/*


%changelog
* Wed Jun 24 2015 Sérgio Basto <sergio@serjux.com> - 0.0.4-2
- Fixed unused-direct-shlib-dependency in cmake with global optflags,
  instead use "export CXXFLAGS" that was override all flags .

* Mon May 18 2015 Hans de Goede <j.w.r.degoede@gmail.com> - 0.0.4-1
- New upstream release 0.0.4
- Fix FTBFS (rf#3624)

* Mon Oct 20 2014 Sérgio Basto <sergio@serjux.com> - 0.0.3-4
- Rebuilt for FFmpeg 2.4.3

* Fri Sep 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.0.3-3
- Rebuilt for FFmpeg 2.4.x

* Fri Sep 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.0.3-2
- Rebuilt for FFmpeg 2.4.x

* Tue Jul 15 2014 Richard Shaw <hobbes1069@gmail.com> - 0.0.3-1
- Initial packaging.
