%global _enable_debug_package 0
%global debug_package %{nil}

%global forgeurl https://github.com/YuriSizuku/OnscripterYuri
Version:    0.7.5beta4
%forgemeta

Name:       onsyuri
Release:	%autorelease
Summary:    An enhancement ONScripter project porting to many platforms, especially web. 
License:    GPLv2
URL:        %{forgeurl}
Source0:    %{forgesource}
# Patch0:     ld-all-dynamic-and-lua54.patch

BuildRequires:  gcc, g++, make, cmake
BuildRequires:  SDL2-devel, SDL2_ttf-devel, SDL2_image-devel, SDL2_mixer-devel
BuildRequires:  bzip2-devel, libjpeg-turbo-devel, libpng-devel
BuildRequires:  lua-devel, mesa-libGL-devel

%description
☘️ An enhancement ONScripter project porting to many platforms, especially web ！
We also support for windows, linux, mac, android, retroarch and psv. This project is base on ONScripter-Jh(https://github.com/jh10001/ONScripter-Jh) by SDL2.

%prep
%autosetup -n OnscripterYuri-%{version}
# cd %{_builddir}
# mv ./OnscripterYuri-%{version} ./%{name}-%{version}
# cd ./%{name}-%{version}

%build
%cmake . -DCMAKE_BUILD_TYPE=MinSizeRel
%make_build -C redhat-linux-build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}/
cp -p ./redhat-linux-build/onsyuri %{buildroot}%{_bindir}/

%files
%{_bindir}/onsyuri
