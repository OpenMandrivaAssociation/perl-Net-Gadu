%define upstream_name Net-Gadu
%define upstream_version 1.9

Summary:	Perl module to support Gadu-Gadu protocol
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 2
License:	LGPLv2+
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	libgadu-devel	>= 1.7.1
BuildRequires:  chrpath
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Net-Gadu is a perl module. It is intended to make it easy to add Gadu-Gadu
communication support to your scripts. It uses libgadu library.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

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
