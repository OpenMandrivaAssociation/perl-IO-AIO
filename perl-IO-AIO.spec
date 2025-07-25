%define	upstream_name	 IO-AIO
%define upstream_version 4.31

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary:	Asynchronous Input/Output 

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.gz
Requires:	perl(common::sense)
BuildRequires:	db5-devel
BuildRequires:	gdbm-devel
BuildRequires:	perl(common::sense)
BuildRequires:	perl-devel

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
%make CFLAGS="%{optflags}"

%check
%make test

%install
%makeinstall_std

%clean

%files
%{_mandir}/*/*
%{_bindir}/treescan
%{perl_vendorarch}/IO
%{perl_vendorarch}/auto/IO



