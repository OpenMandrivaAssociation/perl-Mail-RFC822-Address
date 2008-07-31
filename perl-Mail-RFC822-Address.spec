%define	real_name Mail-RFC822-Address
%define	name	perl-%{real_name}
%define	version	0.3
%define	release %mkrel 6

Summary:	%{real_name} module for perl
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Mail/%{real_name}-%{version}.tar.gz
URL:		http://search.cpan.org/dist/%{real_name}
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Mail::RFC822::Address validates email addresses against the grammar described
in RFC 822 using regular expressions.

%prep
%setup -q -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes INSTALL
%{_mandir}/*/*
%{perl_vendorlib}/Mail/RFC822/Address.pm

