%define major 0

%define libname %mklibname hyprcursor
%define devname %mklibname -d hyprcursor

Name:           hyprcursor
Version:        0.1.8
Release:        1
Summary:        The hyprland cursor format, library and utilities. 
License:        BSD-3-Clause license 
Group:          Hyprland
URL:            https://github.com/hyprwm/hyprcursor/
Source0:        https://github.com/hyprwm/hyprcursor/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  pkgconfig(hyprlang)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(tomlplusplus)

Requires:	%{libname} = %{EVRD}

%description
The hyprland cursor format, library and utilities.
Why?

XCursor sucks, and we still use it today.

    Scaling of XCursors is horrible
    XCursor does not support vector cursors
    XCursor is ridiculously space-inefficient

Hyprcursor fixes all three. It's an efficient cursor theme format that doesn't suck as much.
Notable advantages over XCursor

    Automatic scaling according to a configurable, per-cursor method.
    Support for SVG cursors
    Way more space-efficient. As an example, Bibata-XCursor is 44.1MB, while it's 6.6MB in hyprcursor.

%package -n %{libname}
Summary:        Shared library for %{name}
Requires:	%{name} = %{EVRD}

%description -n %{libname}
Shared library for Hyprcursor.

%package -n %{devname}
Summary:    Development files for %{name}
Requires:	%{libname} = %{EVRD}
Requires:	%{name} = %{EVRD}

%description -n %{devname}
This package contains development files for %{name}.

%prep
%autosetup -p1
 
%build
# Compilation with Clang 18 failed, problem reported to upstream: https://github.com/hyprwm/hyprcursor/issues/8
export CC=gcc
export CXX=g++
%cmake -DCMAKE_BUILD_TYPE:STRING=Release
%make_build
 
%install
%make_install -C build

%files
%{_bindir}/hyprcursor-util

%files -n %{libname}
%{_libdir}/libhyprcursor.so.%{major}
%{_libdir}/libhyprcursor.so.%{version}

%files -n %{devname}
%{_libdir}/libhyprcursor.so
%{_libdir}/pkgconfig/hyprcursor.pc
%{_includedir}/hyprcursor.hpp
%{_includedir}/hyprcursor/
