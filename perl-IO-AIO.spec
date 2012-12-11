%define	upstream_name	 IO-AIO
%define upstream_version 4.0

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	2

Summary:	Asynchronous Input/Output 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.gz
Requires:	perl(common::sense)
BuildRequires:	db5-devel
BuildRequires:	gdbm-devel
BuildRequires:	perl(common::sense)
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module implements asynchronous I/O using whatever means your operating
system supports.

Currently, a number of threads are started that execute your read/writes and
signal their completion. You don't need thread support in your libc or perl,
and the threads created by this module will not be visible to the pthreads
library. In the future, this module might make use of the native aio functions
available on many operating systems. However, they are often not well-supported
(Linux doesn't allow them on normal files currently, for example), and they
would only support aio_read and aio_write, so the remaining functionality would
have to be implemented using threads anyway.

Although the module will work with in the presence of other threads, it is
currently not reentrant, so use appropriate locking yourself, always call
poll_cb from within the same thread, or never call poll_cb (or other aio_
functions) recursively.

After creating a new Gtk2::Ex::Simple::List object with the desired columns you
may set the list data with a simple Perl array assignment. Rows may be added or
deleted with all of the normal array operations. You can treat the data member
of the Simple::List object as an array reference, and manipulate the list data
with perl's normal array operators.

A mechanism has also been put into place allowing columns to be Perl scalars.
The scalar is converted to text through Perl's normal mechanisms and then
displayed in the list. This same mechanism can be expanded by defining
arbitrary new column types before calling the new function.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="$RPM_OPT_FLAGS"

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_mandir}/*/*
%{_bindir}/treescan
%{perl_vendorarch}/IO
%{perl_vendorarch}/auto/IO


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 4.0.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Mon Jul 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 4.0.0-1
+ Revision: 690268
- update to new version 4.0

* Tue Jul 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 3.930.0-1
+ Revision: 688748
- update to new version 3.93

* Fri Jun 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 3.900.0-1
+ Revision: 685816
- new version
- switch to db5

* Wed Mar 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 3.800.0-1
+ Revision: 649139
- update to new version 3.8

* Fri Dec 31 2010 Guillaume Rousse <guillomovitch@mandriva.org> 3.710.0-1mdv2011.0
+ Revision: 626832
- update to new version 3.71
- update to new version 3.7

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 3.650.0-2mdv2011.0
+ Revision: 555962
- rebuild for perl 5.12

* Wed Mar 31 2010 Jérôme Quelin <jquelin@mandriva.org> 3.650.0-1mdv2010.1
+ Revision: 530262
- update to 3.65

* Wed Feb 10 2010 Jérôme Quelin <jquelin@mandriva.org> 3.600.0-2mdv2010.1
+ Revision: 503944
- adding missing requires:

* Mon Jan 11 2010 Jérôme Quelin <jquelin@mandriva.org> 3.600.0-1mdv2010.1
+ Revision: 489515
- update to 3.6

* Fri Jan 08 2010 Jérôme Quelin <jquelin@mandriva.org> 3.500.0-1mdv2010.1
+ Revision: 487474
- update to 3.5

* Sun Jan 03 2010 Jérôme Quelin <jquelin@mandriva.org> 3.400.0-1mdv2010.1
+ Revision: 485851
- update to 3.4

* Thu Nov 12 2009 Jérôme Quelin <jquelin@mandriva.org> 3.310.0-1mdv2010.1
+ Revision: 465167
- update to 3.31

* Tue Aug 11 2009 Jérôme Quelin <jquelin@mandriva.org> 3.300.0-1mdv2010.0
+ Revision: 415038
- adding missing buildrequires:
- update to 3.3

* Fri Jul 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.261-1mdv2010.0
+ Revision: 391950
- update to new version 3.261

* Wed Jul 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.26-1mdv2010.0
+ Revision: 391184
- update to new version 3.26

* Sun Jun 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.25-1mdv2010.0
+ Revision: 390341
- update to new version 3.25

* Sun Jun 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.23-1mdv2010.0
+ Revision: 387779
- new version

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.19-1mdv2010.0
+ Revision: 370132
- update to new version 3.19

* Sat Nov 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.17-1mdv2009.1
+ Revision: 305728
- update to new version 3.17

* Thu Oct 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.16-1mdv2009.1
+ Revision: 296793
- update to new version 3.16

* Fri Oct 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.15-1mdv2009.1
+ Revision: 294655
- update to new version 3.15

* Sun Aug 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.07-1mdv2009.0
+ Revision: 270387
- update to new version 3.07

* Wed Jul 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.06-1mdv2009.0
+ Revision: 236266
- update to new version 3.06

* Mon Jun 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.05-1mdv2009.0
+ Revision: 227972
- update to new version 3.05

* Thu Jun 19 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.04-1mdv2009.0
+ Revision: 226193
- update to new version 3.04

* Fri May 30 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.03-1mdv2009.0
+ Revision: 213357
- update to new version 3.03

* Tue May 20 2008 Oden Eriksson <oeriksson@mandriva.com> 3.02-2mdv2009.0
+ Revision: 209548
- get rid of the db1-devel and db2-devel build deps, db4-devel is enough

* Tue May 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.02-1mdv2009.0
+ Revision: 209316
- fix build dependencies
- update to new version 3.02

* Tue May 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.62-1mdv2009.0
+ Revision: 201970
- update to new version 2.62

* Thu Apr 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.61-1mdv2009.0
+ Revision: 195434
- update to new version 2.61

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 2.51-2mdv2008.1
+ Revision: 151422
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Oct 13 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.51-1mdv2008.1
+ Revision: 98033
- update to new version 2.51
- update to new version 2.51


* Tue Mar 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.33-1mdv2007.0
+ Revision: 133706
- new version

* Thu Nov 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.2-1mdv2007.1
+ Revision: 84622
- new version
- Import perl-IO-AIO

* Fri Sep 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.73-2mdv2007.0
- Rebuild

* Thu Mar 02 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.73-1mdk
- New release 1.73

* Thu Feb 09 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.72-1mdk
- New release 1.72

* Thu Dec 29 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.71-1mdk
- New release 1.71
- use correct compilation flags

* Tue Dec 20 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.61-1mdk
- first mdk release

