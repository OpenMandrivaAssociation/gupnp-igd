%define api 1.0
%define major 3
%define libname %mklibname %name %api %major
%define develname %mklibname -d %name
Name:           gupnp-igd
Version:        0.1.6
Release:        %mkrel 1
Summary:        Handle Internet Gateway Device port mappings
Group:          System/Libraries
License:        LGPLv2+
URL:            http://www.gupnp.org/
Source0:        http://www.gupnp.org/sources/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gtk-doc
BuildRequires: gupnp-devel
BuildRequires: python-devel
BuildRequires: python-gobject-devel

%description
GUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The GUPnP API is intended to be easy to use, efficient and flexible.

GUPnP-Igd is a library that handle Internet Gateway Device port mappings.

%package -n %libname
Summary: Handle Internet Gateway Device port mappings
Group: System/Libraries

%description -n %libname
GUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The GUPnP API is intended to be easy to use, efficient and flexible.

GUPnP-Igd is a library that handle Internet Gateway Device port mappings.


%package -n %develname
Summary: Development package for gupnp-igd
Group: Development/C
Requires: %libname = %{version}-%{release}
Provides: %name-devel = %version-%release
Provides: lib%name-devel = %version-%release

%description -n %develname
Files for development with gupnp-igd.

%package -n python-%{name}
Summary: Python bindings for %{name}
Group: Development/Python
Requires: %libname = %{version}-%{release}

%description -n python-%{name}
Python bindings for %{name}.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdvver < 200900
%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_libdir}/libgupnp-igd-%api.so.%{major}*

%files -n %develname
%defattr(-,root,root,-)
%{_datadir}/gtk-doc/html/gupnp-igd/
%{_includedir}/gupnp-igd-%api
%{_libdir}/pkgconfig/gupnp-igd-%api.pc
%{_libdir}/libgupnp-igd-%api.so
%{_libdir}/libgupnp-igd-%api.la

%files -n python-%{name}
%defattr(-,root,root,-)
%{python_sitearch}/gupnp
%{python_sitearch}/gupnp/igd.so
%{python_sitearch}/gupnp/igd.la

