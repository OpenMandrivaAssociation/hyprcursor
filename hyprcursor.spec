Name:           hyprcursor
Version:        0.1.4
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

%prep
%autosetup -p1
 
%build
%cmake -DCMAKE_BUILD_TYPE:STRING=Release
%make_build
 
%install
%make_install -C build

%files
