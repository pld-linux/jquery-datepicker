%define		plugin	datepicker
Summary:	A flexible unobtrusive calendar component for jQuery
Name:		jquery-%{plugin}
Version:	2.1.2
Release:	0.2
License:	MIT
Group:		Applications/WWW
# svn export http://jquery-datepicker.googlecode.com/svn/tags/2.1.2 jquery-datepicker-2.1.2
# tar cjf jquery-datepicker-2.1.2.tar.bz2 jquery-datepicker-2.1.2
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	df393f932ff6d5a37d4a0856c1cbb216
URL:		http://www.kelvinluck.com/assets/jquery/datePicker/v2/demo/
BuildRequires:	js
BuildRequires:	rpmbuild(macros) >= 1.565
BuildRequires:	yuicompressor
Requires:	jquery >= 1.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
jQuery datepicker is a jQuery plugin which allows you to easily add
"date picker" calendars to you HTML forms. These calendars make it
much quicker, easier and less error prone for people to input certain
types of dates.

%package demo
Summary:	Demo for jQuery.datePicker
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu jQuery.datePicker
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description demo
Demonstrations and samples for jQuery.datePicker.

%prep
%setup -q

%build
install -d build

# pack .css
css=demo/styles/datePicker.css
out=build/datePicker.css
%if 0%{!?debug:1}
yuicompressor --charset UTF-8 $css -o $out
%else
cp -p $css $out
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_examplesdir}/%{name}-%{version}}
cp -p dist/jquery.datePicker.min-%{version}.js $RPM_BUILD_ROOT%{_appdir}/jquery.datePicker.js
cp -p build/datePicker.css $RPM_BUILD_ROOT%{_appdir}

cp -a demo/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
