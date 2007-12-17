%define module Net-Gadu

Summary:	Net-Gadu is a perl module to support Gadu-Gadu protocol
Name:		perl-Net-Gadu
Version:	1.8
Release:	%mkrel 3
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/~krzak/Net-Gadu/Gadu.pm
Source0:	http://www.cpan.org/modules/by-module/Net/Net-Gadu-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	libgadu-devel	>= 1.7.1
BuildRequires:  chrpath

%description
Net-Gadu is a perl module. It is intended to make it easy to add Gadu-Gadu
communication support to your scripts. It uses libgadu library.

%prep
%setup -qn %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor

%make OPTIMIZE="%{optflags}"

%check
make test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std
rm -rf %{buildroot}/usr/lib/perl5/5.8.8/

install ex/ex1 example.pl

chrpath -d %{buildroot}%{perl_vendorarch}/auto/Net/Gadu/Gadu.so

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
    
%files
%defattr(-,root,root)
%doc Changes README example.pl contrib
%dir %{perl_vendorarch}/auto/Net/Gadu
%{perl_vendorarch}/auto/Net/Gadu/autosplit.ix
%{perl_vendorarch}/auto/Net/Gadu/Gadu.so
%{perl_vendorarch}/Net/Gadu.pm
%{_mandir}/man3/Net::Gadu.3pm*
