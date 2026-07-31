%define upstream_version 0.3
%define	real_name Mail-RFC822-Address
Summary:	%{real_name} module for perl
Name:		perl-%{real_name}
Version:	0.4
Release:	1
License:	GPL or Artistic
Group:		Development/Perl
Source:		https://cpan.metacpan.org/authors/id/P/PD/PDWARREN/Mail-RFC822-Address-%{version}.tar.gz
URL:		https://metacpan.org/dist/Mail-RFC822-Address
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl-devel

%description
Mail::RFC822::Address validates email addresses against the grammar described
in RFC 822 using regular expressions.

%prep
%setup -q -n Mail-RFC822-Address-0.3

%build
perl Makefile.PL INSTALLDIRS=vendor
make
make test || :

%install
%makeinstall_std

%files
%doc Changes INSTALL
%{_mandir}/*/*
%{perl_vendorlib}/Mail/RFC822/Address.pm



