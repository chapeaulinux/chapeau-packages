%define _use_internal_dependency_generator 0

Summary:	Chapeau
Name:		chapeau-packages
Version:	2
Release:	3%{?dist}
License:	distributable
Group:		Chapeau
URL:		http://chapeaulinux.org
BuildArch:	noarch

Requires:	plymouth-theme-chapeau
Requires:	chapeau-logos
Requires:	chapeau-repos
Requires:	chapeau-backgrounds
Requires:	chapeau-gnome-theme
#Requires:	b43-firmware
Requires:	yumex-dnf
Requires:	hht
Obsoletes:	yumex
#Requires:	chapeau-gnome-defaults
#Requires:	chapeau-firefox-defaults


%description
A meta package which requires the packages unique to the Chapeau Remix

%prep

%build

%clean 

%install

%post
# remove self after required packages are pulled.
#rpm -e %{name}

%files 


%changelog
* Thu Nov 05 2015 Vince Pooley <vince@chapeaulinux.org>
- Commented requirement for b43-firmware package for now

* Tue Nov 03 2015 Vince Pooley <vince@chapeaulinux.org>
- Added requirement for hht

* Fri Jun 12 2015 Vince Pooley <vince@chapeaulinux.org>
- Added requirement for yumex-dnf & Broadcom firmware package
- Obsoletes yumex package

* Fri Apr 03 2015 Vince Pooley <vince@chapeaulinux.org>
- Added requirement for chapeau-gnome-theme meta package

* Thu Jan 08 2015 Vince Pooley <vince@chapeaulinux.org>
- Added requirement for chapeau-backgrounds package

* Sat Jan 03 2015 Vince Pooley <vince@chapeaulinux.org>
- Added chapeau-repos package to prep for Chapeau 21 release

* Mon Jan 13 2014 Vince Pooley <vince@chapeaulinux.org>
- initial release

