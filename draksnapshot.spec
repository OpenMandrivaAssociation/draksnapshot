Summary: Snapshot utility
Name:    draksnapshot
Version: 0.20.4
Release: 4
Source0: %{name}-%{version}.tar.lzma
URL:	    http://www.mandrivalinux.com
License: GPL
Group:   Archiving/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:  rsnapshot
%if %mdkversion >=  200900
Requires:  drakxtools >= 10.59
%else
Requires:  drakxtools >= 10.29.11
%endif
BuildRequires: gettext, perl-MDK-Common-devel intltool
BuildArch: 	noarch


%description
This is a backup program that uses rsync to take backup snapshots of
filesystems.  It uses hard links to save space on disk.

%prep
%setup -q

%build
%make
perl -pi -e 's!my \$ver = 1;!my \$ver = '"'%version-%release'"';!' draksnapshot-applet

%install
rm -rf %{buildroot}
%makeinstall_std PREFIX=$RPM_BUILD_ROOT 

# so that we remove cron entry on removal:
mkdir %{buildroot}%_sysconfdir/cron.d
touch %{buildroot}%_sysconfdir/cron.d/rsnapshot

%{find_lang} %{name}

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%defattr(-,root,root)
%ghost %_sysconfdir/cron.d/rsnapshot
%_bindir/*
%_datadir/%{name}
%_sysconfdir/xdg/autostart/autostart-draksnapshot.desktop
%_iconsdir/*.png
%_liconsdir/*.png
%_miconsdir/*.png
%_sbindir/*
%perl_vendorlib/MDV




%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.20.4-2mdv2011.0
+ Revision: 663861
- mass rebuild

* Fri Feb 18 2011 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 0.20.4-1
+ Revision: 638540
- New version: 0.20.4

* Thu Jul 22 2010 Funda Wang <fwang@mandriva.org> 0.20.3-2mdv2011.0
+ Revision: 557000
- rebuild

* Wed May 26 2010 Christophe Fergeau <cfergeau@mandriva.com> 0.20.3-1mdv2010.1
+ Revision: 546250
- 0.20.3
- translation updates

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.20.2-2mdv2010.1
+ Revision: 522512
- rebuilt for 2010.1

* Mon Jul 27 2009 Thierry Vignaud <tv@mandriva.org> 0.20.2-1mdv2010.0
+ Revision: 400603
- configurator:
  o add a standard shell shebang to the generated cron files

* Wed Apr 15 2009 Thierry Vignaud <tv@mandriva.org> 0.20.1-1mdv2009.1
+ Revision: 367421
- translation updates

* Fri Apr 03 2009 Thierry Vignaud <tv@mandriva.org> 0.20-1mdv2009.1
+ Revision: 363798
- draksnapshot-restore
  o do not try to mount '/'
  o display a success message before quitting

* Mon Mar 30 2009 Thierry Vignaud <tv@mandriva.org> 0.19.2-1mdv2009.1
+ Revision: 362379
- fix build due to fi translations
- translation updates

* Wed Dec 10 2008 Thierry Vignaud <tv@mandriva.org> 0.19.1-1mdv2009.1
+ Revision: 312516
- applet:
  o fix crash when hal is confused (#44966)
- configurator:
  o set 'no_create_root' option so that we skip backuping when devices
    are not mounted

* Wed Oct 01 2008 Funda Wang <fwang@mandriva.org> 0.18.1-2mdv2009.0
+ Revision: 290489
- new translation snapshot

* Tue Sep 30 2008 Thierry Vignaud <tv@mandriva.org> 0.18.1-1mdv2009.0
+ Revision: 290187
- applet:
  o fix crash introduced in 0.18

* Tue Sep 30 2008 Thierry Vignaud <tv@mandriva.org> 0.18-1mdv2009.0
+ Revision: 290120
- applet:
  o fix crash if DBus is active but Hal isn't (#44434)
- configurator:
  o use regular Advanced button on 2008.1
- adjust requires for 2008.1

* Tue Sep 30 2008 Thierry Vignaud <tv@mandriva.org> 0.17-1mdv2009.0
+ Revision: 289969
- configurator:
  o generate cron entries that do not send mails by default

* Mon Sep 29 2008 Thierry Vignaud <tv@mandriva.org> 0.16-1mdv2009.0
+ Revision: 289739
- configurator:
  o use Gtk+2's FileChooserDialog (#40717)
- applet:
  o hide applet if all discs got umounted (#41176)
  o use HAL in order to detect discs avaible for backup,
    thus not detecting some internal SATA discs (#41107)
- configurator:
  o do not save config when clicking "Close" (#39790)
  o default to HAL mounted disc path (#39802)

* Fri Sep 26 2008 Thierry Vignaud <tv@mandriva.org> 0.14-1mdv2009.0
+ Revision: 288628
- applet:
  o delay first check by 30s so that notification goes at the right
    place
  o do not crash if DBus isn't reachable
  o report DBus errors
- configurator:
  o do not offer anymore to configure intervals
    (too advanced option)
  o enable to disable backups
  o generate anacron friendly cron files (#43297)
  o make advanced settings pop up like installer

* Mon Sep 22 2008 Thierry Vignaud <tv@mandriva.org> 0.13-1mdv2009.0
+ Revision: 287014
- new icons

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.12-1mdv2009.0
+ Revision: 266575
- applet:
  o prevent running twice the same applet

* Tue Jun 24 2008 Thierry Vignaud <tv@mandriva.org> 0.11-1mdv2009.0
+ Revision: 228602
- applet:
  o make notifications be more informative (#40360)
  o keep running if configured once
  o only popup if something is mounted
  o try harder to show the icon before the bubble so that the later is
    correctly placed (#40361)
- configurator:
  o fix backup not done due to bad permissions (#39811)

* Fri May 09 2008 Thierry Vignaud <tv@mandriva.org> 0.10-1mdv2009.0
+ Revision: 205067
- applet:
  o do not crash if notify deamon failed on ->show (#40031)
  o do not consider USB root disc
- configurator:
  o exclude snapshot point from being backuped (thus preventing to
    recursively backup the backup directory) (#39801)
  o default to /media instead of /home if not configured, where the
    discs will be mounted by HAL (#39802)

* Thu Apr 03 2008 Thierry Vignaud <tv@mandriva.org> 0.9-1mdv2008.1
+ Revision: 192171
- do not wake up on CD insertion (#39748)

* Thu Apr 03 2008 Thierry Vignaud <tv@mandriva.org> 0.8-1mdv2008.1
+ Revision: 192106
- translation updates

* Wed Apr 02 2008 Thierry Vignaud <tv@mandriva.org> 0.7-1mdv2008.1
+ Revision: 191665
- configurator:
  o add a tooltip in order to explain what are intervals (#39509)
  o disable advanced settings if "backup the whole system" is selected
  o hide list under an "Advanced" expander
  o set 755 perms on cron entry (#39699)
  o use ad hoc config if "backup the whole system" is selected
  o use spin buttons for intervals
- draksnapshot-restore wasn't installed
- remove cron entry on removal (#38651)

* Fri Mar 28 2008 Thierry Vignaud <tv@mandriva.org> 0.6-1mdv2008.1
+ Revision: 190909
- applet:
  o switch to HAL for detecting new plugged USB devices
    (no more polling and fix memory leak in libmodprobe (#38601))

* Tue Mar 25 2008 Thierry Vignaud <tv@mandriva.org> 0.5-2mdv2008.1
+ Revision: 190165
- require drakxtools (and a version new enough) (#39341)

* Tue Mar 11 2008 Thierry Vignaud <tv@mandriva.org> 0.5-1mdv2008.1
+ Revision: 186248
- configurator:
  o actually use translations

* Wed Mar 05 2008 Thierry Vignaud <tv@mandriva.org> 0.4-1mdv2008.1
+ Revision: 180076
- applet:
  o check only every 5s
  o ligther check
- applet:
  o do not notify again if already done
  o do not skip initial check
  o hide again if no more USB disk
  o only show up if detecting new discs
  o refresh cache of USB devices list
  o run check every 2s instead of every 5mns

* Mon Mar 03 2008 Thierry Vignaud <tv@mandriva.org> 0.2-1mdv2008.1
+ Revision: 178077
- actually add patch
- patch 0: fix build due to errors in et translation
- fix path in autostart files (#38418)
- fix warning in xinit file (#38418)

* Wed Feb 27 2008 Thierry Vignaud <tv@mandriva.org> 0.1-1mdv2008.1
+ Revision: 175862
- buildrequires intltool
- import draksnapshot


* Wed Feb 27 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.1-1mdv2008.1
- initial release
