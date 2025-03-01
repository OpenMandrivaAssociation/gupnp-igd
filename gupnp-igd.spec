%define url_ver %(echo %{version}|cut -d. -f1,2)

%define api	1.6
%define major	0
%define libname %mklibname %{name} %{api} %{major}
%define girname %mklibname %{name}-gir %{api}
%define devname %mklibname -d %{name}

Summary:	Handle Internet Gateway Device port mappings
Name:		gupnp-igd
Version:	1.6.0
Release:	1
Group:		System/Libraries
License:	LGPLv2+
Url:		https://www.gupnp.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gupnp-igd/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	meson
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gupnp-1.6) >= 0.18
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(pygobject-2.0)

%description
GUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The GUPnP API is intended to be easy to use, efficient and flexible.

GUPnP-Igd is a library that handle Internet Gateway Device port mappings.

%package -n %{libname}
Summary:	Handle Internet Gateway Device port mappings
Group:		System/Libraries

%description -n %{libname}
GUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The GUPnP API is intended to be easy to use, efficient and flexible.

GUPnP-Igd is a library that handle Internet Gateway Device port mappings.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Conflicts:	%{_lib}gupnp-igd1.0_4 < 0.2.2-1

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Summary:	Development package for gupnp-igd
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Files for development with gupnp-igd.

%package -n python-%{name}
Summary:	Python bindings for %{name}
Group:		Development/Python
Requires:	%{libname} = %{version}-%{release}
BuildRequires:	python-devel

%description -n python-%{name}
Python bindings for %{name}.

%prep
%autosetup -p1
%meson \
	-Dintrospection=true

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/libgupnp-igd-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GUPnPIgd-%{api}.typelib

%files -n %{devname}
%doc AUTHORS COPYING README
%{_includedir}/gupnp-igd-%{api}
%{_libdir}/pkgconfig/gupnp-igd-%{api}.pc
%{_libdir}/libgupnp-igd-%{api}.so
%{_datadir}/gir-1.0/GUPnPIgd-%{api}.gir
