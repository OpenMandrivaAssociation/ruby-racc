%define rname racc
%define name ruby-%{rname}
%define version 1.4.5
%define release 6

Summary: LALR(1) Parser Generator
Name: %{name}
Version: %{version}
Release: %{release}
URL: http://i.loveruby.net/en/racc.html
Source0: %{rname}-%{version}-all.tar.bz2
License: LGPL
Group: Development/Ruby
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: ruby >= 1.8
BuildRequires: ruby-devel
BuildArch: noarch 

%description
Racc is Ruby yACC. It is written in Ruby and generates ruby code.
Now almost all functions of yacc are implemented.

%prep
%setup -q -n %{rname}-%{version}-all 

%build
ruby setup.rb config --bin-dir=%{_bindir} --rb-dir=%{ruby_sitelibdir} --with=racc
ruby setup.rb setup

%install
rm -rf %buildroot
ruby setup.rb install --prefix=%buildroot

%check
cd packages/racc/test
ruby test.rb

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{ruby_sitelibdir}/racc
%{_bindir}/*
%doc README.* packages/racc/NEWS.* packages/racc/doc.*



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.4.5-5mdv2010.0
+ Revision: 433545
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.4.5-4mdv2009.0
+ Revision: 269235
- rebuild early 2009.0 package (before pixel changes)

* Sat May 10 2008 Pascal Terjan <pterjan@mandriva.org> 1.4.5-3mdv2009.0
+ Revision: 205434
- Add check section and some missing doc

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.4.5-2mdv2008.1
+ Revision: 140755
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Apr 22 2007 Pascal Terjan <pterjan@mandriva.org> 1.4.5-2mdv2008.0
+ Revision: 16765
- Use Development/Ruby group
- Use std macros


* Mon Nov 21 2005 Pascal Terjan <pterjan@mandriva.org> 1.4.5-1mdk
- 1.4.5
- mkrel

* Sun Apr 17 2005 Pascal Terjan <pterjan@mandrake.org> 1.4.4-3mdk
- fix lib64

* Fri Oct 22 2004 Pascal Terjan <pterjan@mandrake.org> 1.4.4-2mdk
- rebuild

* Thu Dec 25 2003 Pascal Terjan <CMoi@tuxfamily.org> 1.4.4-1mdk 
- first mdk release

