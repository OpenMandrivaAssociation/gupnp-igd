%define api 1.0
%define major 4
%define libname %mklibname %{name} %{api} %{major}
%define develname %mklibname -d %{name}

Name:		gupnp-igd
Version:	0.2.1
Release:	1
Summary:	Handle Internet Gateway Device port mappings
Group:		System/Libraries
License:	LGPLv2+
URL:		http://www.gupnp.org/
Source0:	http://gupnp.org/sites/all/files/sources/%{name}-%{version}.tar.gz
Patch0:		disable_static.patch
Patch1:		gmodule_linker_fix.patch
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(gupnp-1.0) >= 0.18
BuildRequires:	python-devel
BuildRequires:	pkgconfig(pygobject-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)

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

%package -n %{develname}
Summary:	Development package for gupnp-igd
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %{develname}
Files for development with gupnp-igd.

%package -n python-%{name}
Summary:	Python bindings for %{name}
Group:		Development/Python
Requires:	%{libname} = %{version}-%{release}
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

%files -n %{libname}
%doc AUTHORS COPYING README
%{_libdir}/libgupnp-igd-%{api}.so.%{major}*
%{_libdir}/girepository-1.0/GUPnPIgd-1.0.typelib

%files -n %{develname}
%{_datadir}/gtk-doc/html/gupnp-igd/
%{_includedir}/gupnp-igd-%{api}
%{_libdir}/pkgconfig/gupnp-igd-%{api}.pc
%{_libdir}/libgupnp-igd-%{api}.so
%{_datadir}/gir-1.0/GUPnPIgd-1.0.gir

%files -n python-%{name}
%{python_sitearch}/gupnp

%changelog
* Tue Jan 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.2.1-1
+ Revision: 759357
- version update 0.2.1

* Mon Nov 07 2011 Götz Waschk <waschk@mandriva.org> 0.2.0-1
+ Revision: 728128
- new version
- bump gupnp dep
- new major

* Thu May 26 2011 Götz Waschk <waschk@mandriva.org> 0.1.11-1
+ Revision: 679165
- new version
- drop patch
- new source URL
- disable parallel make
- enable introspection

* Fri Apr 29 2011 Funda Wang <fwang@mandriva.org> 0.1.7-3
+ Revision: 660643
- rebuild

* Fri Nov 05 2010 Funda Wang <fwang@mandriva.org> 0.1.7-2mdv2011.0
+ Revision: 593644
- fix build

* Fri Jul 23 2010 Jani Välimaa <wally@mandriva.org> 0.1.7-1mdv2011.0
+ Revision: 557292
- new version 0.1.7

* Thu Jan 07 2010 Jani Välimaa <wally@mandriva.org> 0.1.6-1mdv2010.1
+ Revision: 487177
- new version 0.1.6
- create a subpackage for python bindings
- add BR

* Fri Jan 01 2010 Emmanuel Andry <eandry@mandriva.org> 0.1.5-1mdv2010.1
+ Revision: 484807
- New version 0.1.5
- new major 3

* Sun Sep 20 2009 Frederik Himpe <fhimpe@mandriva.org> 0.1.3-3mdv2010.0
+ Revision: 445874
- Rebuild for new gupnp

* Sun Sep 20 2009 Götz Waschk <waschk@mandriva.org> 0.1.3-2mdv2010.0
+ Revision: 445814
- rebuild for new gupnp

* Sun Jun 21 2009 Frederik Himpe <fhimpe@mandriva.org> 0.1.3-1mdv2010.0
+ Revision: 387833
- Update to new version 0.1.3 (new major)

* Thu Mar 05 2009 Emmanuel Andry <eandry@mandriva.org> 0.1.1-1mdv2009.1
+ Revision: 349317
- import gupnp-igd

