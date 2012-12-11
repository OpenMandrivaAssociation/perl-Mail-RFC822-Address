%define	real_name Mail-RFC822-Address
%define	name	perl-%{real_name}
%define	version	0.3
%define	release %mkrel 7

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



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.3-7mdv2010.0
+ Revision: 430486
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.3-6mdv2009.0
+ Revision: 257708
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.3-5mdv2009.0
+ Revision: 245780
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.3-3mdv2008.1
+ Revision: 140691
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.3-3mdv2008.0
+ Revision: 86529
- rebuild


* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.3-2mdk
- Fix According to perl Policy
	- Source URL
- use mkrel

* Wed Jul 20 2005 Andreas Hasenack <andreas@mandriva.com> 0.3-1mdk
- packaged for Mandriva

