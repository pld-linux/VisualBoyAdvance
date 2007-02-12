%define		_snap	050620
Summary:	One of the most powerful GameBoy Advance Emulators
Summary(pl.UTF-8):	Jeden z najlepszych emulatorów GameBoya Advance
Name:		VisualBoyAdvance
Version:	1.8.0
Release:	0.%{_snap}.1
License:	GPL v2
Group:		Applications/Emulators
Source0:	%{name}-%{version}-%{_snap}.tar.bz2
# Source0-md5:	caac298c7037603709feccd73285d582
URL:		http://vba.ngemu.com/
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpng-devel
BuildRequires:	nasm
BuildRequires:	pth-devel
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
One of the most powerful GameBoy Advance Emulators.

%description -l pl.UTF-8
Jeden z najlepszych emulatorów GameBoya Advance.

%prep
%setup -q -n %{name}-%{version}-%{_snap}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
%ifarch athlon
	--with-mmx
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS
%attr(755,root,root) %{_bindir}/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/VisualBoyAdvance.cfg
