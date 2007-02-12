%define		snap		20011119

Summary:	Cryptix ASN1 implementation
Summary(pl.UTF-8):	Implementacja Cryptix ASN1
Name:		cryptix-asn1
Version:	0.%{snap}
Release:	0.1
License:	BSD-like
Group:		Development/Languages/Java
# http://www.rtfm.com/cgi-bin/distrib.cgi?Cryptix-asn1-20011119.tar.gz
Source0:	Cryptix-asn1-%{snap}.tar.gz
# Source0-md5:	ac4080eee24b1cf0a476cee4fe501149
Source1:	%{name}.build.xml
URL:		http://cryptix-asn1.sourceforge.net/
Patch0:		%{name}-java-1.5.patch
BuildRequires:	ant >= 1.5
BuildRequires:	cryptix
BuildRequires:	gnu.getopt
BuildRequires:	jakarta-log4j
#BuildRequires:	jikes
BuildRequires:	junit
Requires:	cryptix
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description
Java crypto package containing ASN1 implementation.

%description -l pl.UTF-8
Pakiet kryptograficzny Javy zawierający implementację ASN1.

%prep
%setup -q -n Cryptix-asn1-%{snap}
%patch0 -p1
cp %{SOURCE1} build.xml
find . -name "*.jar" -exec rm -f {} \;

%build
ant clean jar javadoc

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javalibdir}
cp build/lib/*.jar $RPM_BUILD_ROOT%{_javalibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc build/api
%{_javalibdir}/*.jar
