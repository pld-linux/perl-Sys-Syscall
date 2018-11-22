#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Sys
%define	pnam	Syscall
Summary:	Sys::Syscall - access system calls that Perl doesn't normally provide access to
Summary(pl.UTF-8):	Sys::Syscall - dostęp do wywołań systemowych, do których sam Perl nie daje dostępu
Name:		perl-Sys-Syscall
Version:	0.25
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Sys/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	720a9ec5f67f867814a9011b2a725763
URL:		http://search.cpan.org/dist/Sys-Syscall/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Use epoll, sendfile, from Perl. Mostly Linux-only support now, but
more syscalls/OSes planned for future.

%description -l pl.UTF-8
Ten moduł pozwala używać wywołania takie jak epoll czy sendfile z
poziomu Perla. Jak na razie obsługiwane są w większości wywołania
tylko linuksowe, ale w przyszłości planowana jest obsługa większej
liczby wywołań i systemów operacyjnych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES
%{perl_vendorlib}/Sys/*.pm
%{_mandir}/man3/*
