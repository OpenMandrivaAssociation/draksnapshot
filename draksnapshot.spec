Summary:	Snapshot utility
Name:		draksnapshot
Version:	0.20.5
Release:	5
License:	GPLv2+
Group:		Archiving/Other
Url:		https://abf.rosalinux.ru/moondrake/draksnapshot
Source0:	%{name}-%{version}.tar.xz
BuildArch:		noarch

BuildRequires:	gettext perl-MDK-Common-devel
BuildRequires:	intltool
Requires:	rsnapshot
Requires:	drakxtools


%description
This is a backup program that uses rsync to take backup snapshots of
filesystems.  It uses hard links to save space on disk.

%prep
%setup -q

%build
%make
sed -i -e 's!my \$ver = 1;!my \$ver = '"'%{version}-%{release}'"';!' draksnapshot-applet

%install
%makeinstall_std

# so that we remove cron entry on removal:
mkdir %{buildroot}%{_sysconfdir}/cron.d
touch %{buildroot}%{_sysconfdir}/cron.d/rsnapshot

%find_lang %{name}

%files -f %{name}.lang
%ghost %{_sysconfdir}/cron.d/rsnapshot
%{_bindir}/draksnapshot-applet
%{_datadir}/%{name}
%{_sysconfdir}/xdg/autostart/autostart-draksnapshot.desktop
%{_iconsdir}/draksnapshot.png
%{_liconsdir}/draksnapshot.png
%{_miconsdir}/draksnapshot.png
%{_sbindir}/draksnapshot-config
%{_sbindir}/draksnapshot-restore
%{perl_vendorlib}/MDV
