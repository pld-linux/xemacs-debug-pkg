Summary:	GUD, gdb, dbx debugging support macros
Summary(pl):	Makra do obs³ugi odpluskwiaczy GUD, gdb, dbx
Name:		xemacs-debug-pkg
%define 	srcname	debug
Version:	1.17
Release:	2
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	e45715132f64e4dbc7f14a22128b9279
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-base-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GUD, gdb, dbx debugging support.

%description -l pl
Makra do obs³ugi odpluskwiaczy GUD, gdb, dbx.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/debug/ChangeLog
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
