%define		snap		20011119

Name:		cryptix-asn1
Version:	0.%{snap}
Release:	0.1
Summary:	Cryptix ASN1 implementation
License:	BSD style
Group:		Development/Languages/Java
URL:		http://cryptix-asn1.sf.net
# http://www.rtfm.com/cgi-bin/distrib.cgi?Cryptix-asn1-20011119.tar.gz
Source0:	Cryptix-asn1-%{snap}.tar.gz
# Source0-md5:	ac4080eee24b1cf0a476cee4fe501149
Source1:	%{name}.build.xml
Requires:	cryptix
BuildRequires:	jakarta-ant >= 1.5
BuildRequires:	cryptix
BuildRequires:	gnu.getopt
BuildRequires:	jakarta-log4j
BuildRequires:	jikes
BuildRequires:	junit
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description
Java crypto package and asn1 implementation.

%prep
%setup -q -n Cryptix-asn1-%{snap}
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
