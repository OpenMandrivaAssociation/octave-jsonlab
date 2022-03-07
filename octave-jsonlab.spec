%global octpkg jsonlab

Summary:	A compact, portable, robust JSON/binary-JSON encoder/decoder for GNU Octave 
Name:		octave-%{octpkg}
Version:	2.0
Release:	1
Source0:	https://github.com/fangq/%{octpkg}/archive/v%{version}/%{octpkg}-%{version}.tar.gz
License:	GPLv3+ and BSD
Group:		Sciences/Mathematics
Url:		https://github.com/fangq/%{octpkg}/
BuildArch:	noarch

BuildRequires:	octave-devel >= 4.0.0
#BuildRequires:	octave-jsonlab
#BuildRequires:	octave-zmat

Requires:	octave(api) = %{octave_api}
#Requires:	octave-jsonlab
#Requires:	octave-zmat

Requires(post): octave
Requires(postun): octave

%description
An open-source JSON encoder and decoder for GNU Octave.

%files
%license COPYING
#doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
#find . -name \*~ -delete

# fix path
mkdir inst
mkdir src
rm -rf Contents.m
mv *.m inst
mv ChangeLog.txt NEWS
mv LICENSE_GPLv3.txt COPYING

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

