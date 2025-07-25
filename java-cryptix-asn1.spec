%bcond_without	javadoc		# build api docs

%define		snap		20011119
%define		srcname		cryptix-asn1
Summary:	Cryptix ASN1 implementation
Summary(pl.UTF-8):	Implementacja Cryptix ASN1
Name:		java-cryptix-asn1
Version:	0.%{snap}
Release:	3
License:	BSD-like
Group:		Libraries/Java
# http://www.rtfm.com/cgi-bin/distrib.cgi?Cryptix-asn1-20011119.tar.gz
Source0:	Cryptix-asn1-%{snap}.tar.gz
# Source0-md5:	ac4080eee24b1cf0a476cee4fe501149
Source1:	%{srcname}.build.xml
URL:		http://cryptix-asn1.sourceforge.net/
Patch0:		%{srcname}-java-1.5.patch
BuildRequires:	ant >= 1.5
BuildRequires:	java-cryptix
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	java-cryptix
Obsoletes:	cryptix-asn1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Java crypto package containing ASN1 implementation.

%description -l pl.UTF-8
Pakiet kryptograficzny Javy zawierający implementację ASN1.

%package javadoc
Summary:	Online manual for %{srcname}
Summary(pl.UTF-8):	Dokumentacja online do %{srcname}
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	cryptix-asn1-javadoc

%description javadoc
Documentation for %{srcname}.

%description javadoc -l pl.UTF-8
Dokumentacja do %{srcname}.

%description javadoc -l fr.UTF-8
Javadoc pour %{srcname}.

%prep
%setup -q -n Cryptix-asn1-%{snap}
%patch -P0 -p1
cp %{SOURCE1} build.xml
find -name '*.jar' | xargs rm -f

%build
CLASSPATH=$(build-classpath cryptix)
%ant clean jar %{?with_javadoc:javadoc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
cp build/lib/*.jar $RPM_BUILD_ROOT%{_javadir}

# javadoc
%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
cp -a build/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{srcname}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}
%endif
