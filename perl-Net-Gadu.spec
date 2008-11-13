%define module Net-Gadu

Summary:	Perl module to support Gadu-Gadu protocol
Name:		perl-Net-Gadu
Version:	1.9
Release:	%mkrel 1
License:	LGPLv2+
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/Net/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	libgadu-devel	>= 1.7.1
BuildRequires:  chrpath
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Net-Gadu is a perl module. It is intended to make it easy to add Gadu-Gadu
communication support to your scripts. It uses libgadu library.

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot}%{perl_vendorarch} -type f | xargs chmod u+w
install ex/ex1 example.pl
chrpath -d %{buildroot}%{perl_vendorarch}/auto/Net/Gadu/Gadu.so

%clean
rm -rf %{buildroot}
    
%files
%defattr(-,root,root)
%doc Changes README example.pl contrib
%{perl_vendorarch}/auto/Net
%{perl_vendorarch}/Net
%{_mandir}/man3/Net::Gadu.3pm*
