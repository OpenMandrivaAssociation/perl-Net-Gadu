Summary:	Net::Gadu module to support Gadu-Gadu protocol
Name:		perl-Net-Gadu
Version:	1.8
Release:	%mkrel 1
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/~krzak/Net-Gadu/Gadu.pm
Source0:	http://www.cpan.org/modules/by-module/Net/Net-Gadu-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	libgadu-devel	>= 1.7
BuildRequires:  chrpath
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Net::Gadu module is intended to make it easy to add Gadu-Gadu
communication support to your scripts. It uses libgadu library.

%prep
%setup -qn Net-Gadu-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
install ex/ex1 example.pl

%makeinstall_std
rm -rf %{buildroot}/usr/lib/perl5/5.8.8/

%ifarch x86_64
mkdir -p %{buildroot}%{perl_vendorlib}/i386-linux
mv -f %{buildroot}%{perl_vendorlib}/x86_64-linux/Net %{buildroot}%{perl_vendorlib}/i386-linux/Net
mv -f %{buildroot}%{perl_vendorlib}/x86_64-linux/auto %{buildroot}%{perl_vendorlib}/i386-linux/auto
rm -rf %{buildroot}/usr/lib/perl5/5.8.8/x86_64-linux/
rm -rf %{buildroot}%{perl_vendorlib}/x86_64-linux/
chrpath -d %{buildroot}%{perl_vendorlib}/i386-linux/auto/Net/Gadu/Gadu.so
%endif    

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
    
%files
%defattr(644,root,root,755)
%doc Changes README example.pl contrib
%dir %{perl_vendorlib}/i386-linux/auto/Net/Gadu
%{perl_vendorlib}/i386-linux/Net/Gadu.pm
%attr(755,root,root) %{perl_vendorlib}/i386-linux/auto/Net/Gadu/Gadu.so
%{perl_vendorlib}/i386-linux/auto/Net/Gadu/autosplit.ix
%{_mandir}/man3/Net::Gadu.3pm*
