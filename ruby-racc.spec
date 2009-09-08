%define rname racc
%define name ruby-%{rname}
%define version 1.4.5
%define release %mkrel 5

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

