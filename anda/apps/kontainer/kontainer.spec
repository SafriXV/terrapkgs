Name:           kontainer
Version:        1.4.1
Release:        1%?dist
Summary:        A Kirigami Distrobox GUI
URL:            https://github.com/DenysMb/Kontainer
Source0:        %url/archive/refs/tags/%{version}.tar.gz
# You should change the above link to the source tarball you got from the preparation section
License:        GPL-3.0-or-later
BuildRequires:  CMake >= 3.20
BuildRequires:  Qt6
BuildRequires:  KDE Frameworks 6
BuildRequires:  C++17 compatible compiler
BuildRequires:  git
Requires:       runtime deps here
# We require you to add yourself as the packager here (if this is an issue for you, let us know):
Packager:       Your Name <meowy@example.com>
