#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Math
%define		pnam	FixedPrecision
Summary:	Math::FixedPrecision - decimal math without floating point errors
Summary(pl.UTF-8):	Math::FixedPrecision - obliczenia dziesiętne bez błędów zmiennoprzecinkowych
Name:		perl-Math-FixedPrecision
Version:	0.21
Release:	1
License:	GPL v1+ or Artistic except commercial distribution on CD-ROM etc.
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3999a0e6ca3b6ad73f25466af6025c7f
Patch0:		%{name}-perl_paths.patch
URL:		http://search.cpan.org/dist/Math-FixedPrecision/
BuildRequires:	perl-Math-BigInt
BuildRequires:	perl(Math::BigFloat) >= 1.27
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl(Math::BigFloat) >= 1.27
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

%description -l pl.UTF-8
Jest wiele sytuacji, gdzie obliczenia zmiennoprzecinkowe nie są
odpowiednie, chociaż dane nie składają się z samych liczb całkowitych.
Ten moduł dodaje nowe możliwości do modułu Math::BigFloat, aby ten
automatycznie obliczał dokładność w czasie obliczeń. Jest to wygodny
moduł, ponieważ wszystkie operacje są wykonywane wewnętrznie przez
Math::BigFloat. Można robić wszystko z tym modułem ustawiając atrybuty
w Math::BigFloat. Ten moduł upraszcza zadanie przyjmując, że jeśli
liczba znaczących cyfr dziesiętnych została podana w wywołaniu new(),
to taka dokładność powinna być potem wszędzie używana w odniesieniu do
tego obiektu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -P0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

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
%{_mandir}/man3/Math::FixedPrecision.3pm*
