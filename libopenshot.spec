Name:           libopenshot
Version:        0.2.0
Release:        1%{?dist}
Summary:        Library for creating and editing videos

License:        LGPLv3+
URL:            http://www.openshot.org/
Source0:        https://github.com/OpenShot/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         ffmpeg40_buildfix.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  swig
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ImageMagick-c++-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  libopenshot-audio-devel >= 0.1.6
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  unittest-cpp-devel
BuildRequires:  cppzmq-devel
BuildRequires:  zeromq-devel
BuildRequires:  ruby-devel


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


%package -n     python%{python3_pkgversion}-%{name}
Summary:        Python bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Group:          Development/Libraries
Obsoletes:      python-%{name} < 0.1.1-2
Provides:       python-%{name}

%description -n python%{python3_pkgversion}-%{name}
The python-%{name} package contains python bindings for 
applications that use %{name}.


%package -n     ruby-%{name}
Summary:        Ruby bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Group:          Development/Libraries

%description -n ruby-%{name}
The ruby-%{name} package contains ruby bindings for
applications that use %{name}.


%prep
%autosetup -p1


%build
export CXXFLAGS="%{optflags} -Wl,--as-needed -Wno-error"
%cmake .
%make_build


%install
%make_install


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc AUTHORS README
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/*.so

%files -n python%{python3_pkgversion}-libopenshot
%{python3_sitearch}/*

%files -n ruby-libopenshot
%{ruby_vendorarchdir}/*


%changelog
* Tue Jul 31 2018 FeRD (Frank Dana) <ferdnyc AT gmail com> - 0.2.0-1
- New upstream release

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.9-6
- Rebuilt for Python 3.7

* Thu Mar 08 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.1.9-5
- Rebuilt for new ffmpeg snapshot

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 17 2018 Sérgio Basto <sergio@serjux.com> - 0.1.9-3
- require libopenshot-audio 0.1.5

* Wed Jan 17 2018 Leigh Scott <leigh123linux@googlemail.com> - 0.1.9-2.1
- Rebuilt for ffmpeg-3.5 git

* Sat Jan 13 2018 Richard Shaw <hobbes1069@gmail.com> - 0.1.9-1.1
- Build against correct libopenshot-audio.

* Sat Jan 13 2018 Richard Shaw <hobbes1069@gmail.com> - 0.1.9-1
- Update to latest upstream release.

* Wed Nov 22 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.1.8-3
- Adjust python for el7

* Tue Oct 17 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.1.8-2
- Rebuild for ffmpeg update

* Thu Sep 07 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.1.8-1
- Update libopenshot to 0.1.8

* Sat Sep 02 2017 Sérgio Basto <sergio@serjux.com> - 0.1.7-1
- Update libopenshot to 0.1.7
- Fix compilation with GCC 7 by adding -Wno-error, reference
  https://github.com/monocasual/giada/issues/139

* Sun Aug 27 2017 Nicolas Chauvet <kwizart@gmail.com> - 0.1.6-2
- Rebuilt for ImageMagick

* Fri May 19 2017 Richard Shaw <hobbes1069@gmail.com> - 0.1.6-1
- Update to latest upstream release.

* Sat Apr 29 2017 Leigh Scott <leigh123linux@googlemail.com> - 0.1.4-2
- Rebuild for ffmpeg update

* Thu Apr 06 2017 Sérgio Basto <sergio@serjux.com> - 0.1.4-1
- Update to 0.1.4

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Mar 14 2017 Richard Shaw <hobbes1069@gmail.com> - 0.1.3-1
- Update to latest upstream release.

* Mon Oct 17 2016 Richard Shaw <hobbes1069@gmail.com> - 0.1.2-1
- Update to latest upstream release.

* Sat Jul 30 2016 Julian Sikorski <belegdol@fedoraproject.org> - 0.1.1-3
- Rebuilt for ffmpeg-3.1.1

* Mon Apr 18 2016 Richard Shaw <hobbes1069@gmail.com> - 0.1.1-2
- Rename python-libopenshot to python3-libopenshot.

* Fri Apr  8 2016 Richard Shaw <hobbes1069@gmail.com> - 0.1.1-1
- Update to latest upstream release.

* Tue Feb  9 2016 Richard Shaw <hobbes1069@gmail.com> - 0.1.0-1
- Update to latest upstream release.

* Mon Nov 16 2015 Richard Shaw <hobbes1069@gmail.com> - 0.0.6-1
- Update to latest upstream release.

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

>>>>>>> master
* Tue Jul 15 2014 Richard Shaw <hobbes1069@gmail.com> - 0.0.3-1
- Initial packaging.
