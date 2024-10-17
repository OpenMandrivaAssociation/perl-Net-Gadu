%define upstream_name Net-Gadu
%define upstream_version 1.9

Summary:	Perl module to support Gadu-Gadu protocol
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5
License:	LGPLv2+
Group:		Development/Perl
URL:		https://search.cpan.org/dist/%{upstream_name}
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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.900.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.900.0-2mdv2011.0
+ Revision: 556025
- rebuild for perl 5.12

* Sun Sep 20 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.900.0-1mdv2010.0
+ Revision: 445107
- fix spec file

* Thu Nov 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.9-1mdv2009.1
+ Revision: 302853
- new version
  spec cleanup
  rename spec file

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.8-9mdv2009.0
+ Revision: 258012
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.8-8mdv2009.0
+ Revision: 246116
- rebuild

* Sat Mar 01 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.8-6mdv2008.1
+ Revision: 176993
- rebuild for new libgadu
- new license policy

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.8-5mdv2008.1
+ Revision: 171027
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- fix no-buildroot-tag

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.8-4mdv2008.1
+ Revision: 152218
- rebuild
- kill re-definition of %%buildroot on Pixel's request

* Wed Jul 18 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.8-3mdv2008.0
+ Revision: 53341
- rebuild
- some minor cleans

* Wed Jun 13 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.8-2mdv2008.0
+ Revision: 38585
- use correct perl macros
- provide Net::Gadu
- add %%check
- compile with optflags
- fix file list

* Mon Apr 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.8-1mdv2008.0
+ Revision: 17303
- new version
- bzip sources


* Sun Jan 21 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7-2mdv2007.0
+ Revision: 111487
- spec file clean
- bump release tag

* Wed Jan 17 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7-1mdv2007.1
+ Revision: 109715
- drop noarch
- fix build on x86_64
- Import perl-Net-Gadu

