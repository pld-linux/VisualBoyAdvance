Summary:	One of the most powerful GameBoy Advance Emulators
Summary(pl):	Jeden z najlepszych emulatorów GameBoya Advance
Name:		VisualBoyAdvance
Version:	1.6
Release:	1
License:	GPL v2
Group:		Applications/Emulators
Source0:	http://www.kernel.pl/~djurban/%{name}-%{version}-src.tar.bz2
# Source0-md5:	f02ea099d3c0f3038ba0b113a22856c6
URL:		http://vboy.emuhq.com/
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpng-devel
BuildRequires:	nasm
BuildRequires:  pth-devel
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
One of the most powerful GameBoy Advance Emulators.

%description -l pl
Jeden z najlepszych emulatorów GameBoya Advance.

%prep
%setup -q

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
