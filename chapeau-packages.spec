%define _use_internal_dependency_generator 0

Summary:	Chapeau
Name:		chapeau-packages
Version:	1
Release:	0
License:	distributable
Group:		Chapeau
URL:		http://chapeaulinux.org
BuildArch:	noarch

Requires:	plymouth-theme-chapeau
Requires:	chapeau-logos
Requires:	chapeau-release
#Requires:	chapeau-gnome-backgrounds
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
* Mon Jan 13 2014 Vince Pooley <vince@chapeaulinux.org>
- initial release

