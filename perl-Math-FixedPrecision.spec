#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	FixedPrecision
Summary:	Math::FixedPrecision - decimal math without floating point errors
Summary(pl):	Math::FixedPrecision - obliczenia dziesiêtne bez b³êdów zmiennoprzecinkowych
Name:		perl-Math-FixedPrecision
Version:	0.21
Release:	1
License:	GPL v1+ or Artistic except commercial distribution on CD-ROM etc.
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3999a0e6ca3b6ad73f25466af6025c7f
BuildRequires:	perl-Math-BigInt
BuildRequires:	perl(Math::BigFloat) >= 1.27
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
There are numerous instances where floating point math is unsuitable,
yet the data does not consist solely of integers. This module employs
new features in Math::BigFloat to automatically maintain precision
during math operations. This is a convenience module, since all of the
operations are handled by Math::BigFloat internally. You could do
everything this module does by setting some attributes in
Math::BigFloat. This module simplifies that task by assuming that if
you specify a given number of decimal places in the call to new() then
that should be the precision for that object going forward.

%description -l pl
Jest wiele sytuacji, gdzie obliczenia zmiennoprzecinkowe nie s±
odpowiednie, chocia¿ dane nie sk³adaj± siê z samych liczb ca³kowitych.
Ten modu³ dodaje nowe mo¿liwo¶ci do modu³u Math::BigFloat, aby ten
automatycznie oblicza³ dok³adno¶æ w czasie obliczeñ. Jest to wygodny
modu³, poniewa¿ wszystkie operacje s± wykonywane wewnêtrznie przez
Math::BigFloat. Mo¿na robiæ wszystko z tym modu³em ustawiaj±c atrybuty
w Math::BigFloat. Ten modu³ upraszcza zadanie przyjmuj±c, ¿e je¶li
liczba znacz±cych cyfr dziesiêtnych zosta³a podana w wywo³aniu new(),
to taka dok³adno¶æ powinna byæ potem wszêdzie u¿ywana w odniesieniu do
tego obiektu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Math/FixedPrecision.pm
%{_mandir}/man3/*
