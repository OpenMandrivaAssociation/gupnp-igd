%define api 1.0
%define major 4
%define libname %mklibname %name %api %major
%define develname %mklibname -d %name
Name:           gupnp-igd
Version:        0.2.1
Release:        1
Summary:        Handle Internet Gateway Device port mappings
Group:          System/Libraries
License:        LGPLv2+
URL:            http://www.gupnp.org/
Source0:	http://gupnp.org/sites/all/files/sources/%{name}-%{version}.tar.gz
BuildRequires: gtk-doc
BuildRequires: gupnp-devel >= 0.18
BuildRequires: python-devel
BuildRequires: python-gobject-devel
BuildRequires: gobject-introspection-devel
Patch0:	       disable_static.patch
Patch1:	       gmodule_linker_fix.patch

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
%py_requires

%description -n python-%{name}
Python bindings for %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure2_5x --disable-static
make

%install
%makeinstall_std

%files -n %libname
%doc AUTHORS COPYING README
%{_libdir}/libgupnp-igd-%api.so.%{major}*
%_libdir/girepository-1.0/GUPnPIgd-1.0.typelib

%files -n %develname
%{_datadir}/gtk-doc/html/gupnp-igd/
%{_includedir}/gupnp-igd-%api
%{_libdir}/pkgconfig/gupnp-igd-%api.pc
%{_libdir}/libgupnp-igd-%api.so
%_datadir/gir-1.0/GUPnPIgd-1.0.gir

%files -n python-%{name}
%{python_sitearch}/gupnp
