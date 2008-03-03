Summary: Snapshot utility
Name:    draksnapshot
Version: 0.2
Release: %mkrel 1
Source0: %{name}-%{version}.tar.lzma
Patch0:  draksnapshot-build-fix.patch
URL:	    http://www.mandrivalinux.com
License: GPL
Group:   Archiving/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:  rsnapshot
BuildRequires: gettext, perl-MDK-Common-devel intltool
BuildArch: 	noarch


%description
This is a backup program that uses rsync to take backup snapshots of
filesystems.  It uses hard links to save space on disk.

%prep
%setup -q
%patch0 -p0

%build
%make
perl -pi -e 's!my \$ver = 1;!my \$ver = '"'%version-%release'"';!' draksnapshot-applet

%install
rm -rf %{buildroot}
%makeinstall_std PREFIX=$RPM_BUILD_ROOT 

%{find_lang} %{name}

%post
%{update_desktop_database}
%{update_mime_database}

%postun
%{clean_desktop_database}
%{clean_mime_database}

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%defattr(-,root,root)
%_bindir/*
%_datadir/%{name}
%_datadir/autostart/autostart-draksnapshot.desktop
%_datadir/gnome/autostart/gnome-autostart-draksnapshot.desktop
%_iconsdir/*.png
%_liconsdir/*.png
%_miconsdir/*.png
%_sbindir/*
%_sysconfdir/X11/xinit.d/draksnapshot-applet.xinit
%perl_vendorlib/MDV

