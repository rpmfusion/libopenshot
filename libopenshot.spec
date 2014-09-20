Name:           libopenshot
Version:        0.0.3
Release:        1%{?dist}
Summary:        Library for creating and editing videos

License:        LGPLv3+
URL:            http://www.openshot.org/
Source0:        https://launchpad.net/%{name}/0.0/%{version}/+download/%{name}-%{version}.tar.gz

BuildRequires:  cmake swig
BuildRequires:  python3-devel
BuildRequires:  ImageMagick-c++-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  libopenshot-audio-devel
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


%build
export CXXFLAGS="-Wl,--as-needed"
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
* Tue Jul 15 2014 Richard Shaw <hobbes1069@gmail.com> - 0.0.3-1
- Initial packaging.
