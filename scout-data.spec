#
# spec file for package scout
#

# norootforbuild

Name:           scout-data
Version:        0
Release:        1
Url:            http://repo.or.cz/w/scout.git
License:        GPL v2 or later
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python lzma sqlite
Requires:       scout
Group:          System/Packages
Summary:        Index Data for Package Scout
BuildArch:      noarch

Source:         scout-gen.tar.bz2

Source10:       autoconf-sle10.txt.lzma
Source11:       autoconf-suse101.txt.lzma
Source12:       autoconf-suse102.txt.lzma
Source13:       autoconf-suse103.txt.lzma
Source14:       autoconf-suse110.txt.lzma

Source20:       bin-sle10.txt.lzma
Source21:       bin-suse101.txt.lzma
Source22:       bin-suse102.txt.lzma
Source23:       bin-suse103.txt.lzma
Source24:       bin-suse110.txt.lzma

Source30:       java-jpackage17.txt.lzma
Source31:       java-sle10.txt.lzma
Source32:       java-suse101.txt.lzma
Source33:       java-suse102.txt.lzma
Source34:       java-suse103.txt.lzma
Source35:       java-suse110.txt.lzma

%description
Index Data for Package Scout

%package -n scout-autoconf-sle10
Group:          System/Packages
Summary:        Index Data for Package Scout
Version:        2008.06.17
Requires:       scout

%description -n scout-autoconf-sle10
Package Scout Index Data - Autoconf macros from SUSE Linux Enterprise 10

%package -n scout-autoconf-suse101
Group:          System/Packages
Summary:        Index Data for Package Scout
Version:        2008.06.16
Requires:       scout

%description -n scout-autoconf-suse101
Package Scout Index Data - Autoconf macros from SUSE Linux 10.1

%package -n scout-autoconf-suse102
Group:          System/Packages
Summary:        Index Data for Package Scout
Version:        2008.06.16
Requires:       scout

%description -n scout-autoconf-suse102
Package Scout Index Data - Autoconf macros from openSUSE 10.2

%package -n scout-autoconf-suse103
Group:          System/Packages
Summary:        Index Data for Package Scout
Version:        2008.06.16
Requires:       scout

%description -n scout-autoconf-suse103
Package Scout Index Data - Autoconf macros from openSUSE 10.3

%package -n scout-autoconf-suse110
Group:          System/Packages
Summary:        Index Data for Package Scout
Version:        2008.06.16
Requires:       scout

%description -n scout-autoconf-suse110
Package Scout Index Data - Autoconf macros from openSUSE 11.0

%package -n scout-bin-sle10
Group:          System/Packages
Summary:        Index Data for Package Scout
Version:        2008.06.17
Requires:       scout

%description -n scout-bin-suse101
Package Scout Index Data - Binaries from SUSE Linux Enterprise 10

%package -n scout-bin-suse101
Group:          System/Packages
Summary:        Index Data for Package Scout
Version:        2008.06.14
Requires:       scout

%description -n scout-bin-suse101
Package Scout Index Data - Binaries from SUSE Linux 10.1

%package -n scout-bin-suse102
Group:          System/Packages
Summary:        Index Data for Package Scout
Version:        2008.06.14
Requires:       scout

%description -n scout-bin-suse102
Package Scout Index Data - Binaries from openSUSE 10.2

%package -n scout-bin-suse103
Group:          System/Packages
Summary:        Index Data for Package Scout
Version:        2008.06.14
Requires:       scout

%description -n scout-bin-suse103
Package Scout Index Data - Binaries from openSUSE 10.3

%package -n scout-bin-suse110
Group:          System/Packages
Summary:        Index Data for Package Scout
Version:        2008.06.14
Requires:       scout

%description -n scout-bin-suse110
Package Scout Index Data - Binaries from openSUSE 11.0

%package -n scout-java-jpackage17
Group:          System/Packages
Summary:        Index Data for Package Scout
Version:        2008.06.14
Requires:       scout

%description -n scout-java-jpackage17
Package Scout Index Data - Java classes from Jpackage 1.7

%package -n scout-java-sle10
Group:          System/Packages
Summary:        Index Data for Package Scout
Version:        2008.06.14
Requires:       scout

%description -n scout-java-sle10
Package Scout Index Data - Java classes from SUSE Linux Enterprise 10

%package -n scout-java-suse101
Group:          System/Packages
Summary:        Index Data for Package Scout
Version:        2008.06.14
Requires:       scout

%description -n scout-java-suse101
Package Scout Index Data - Java classes from SUSE Linux 10.1

%package -n scout-java-suse102
Group:          System/Packages
Summary:        Index Data for Package Scout
Version:        2008.06.14
Requires:       scout

%description -n scout-java-suse102
Package Scout Index Data - Java classes from openSUSE 10.2

%package -n scout-java-suse103
Group:          System/Packages
Summary:        Index Data for Package Scout
Version:        2008.06.14
Requires:       scout

%description -n scout-java-suse103
Package Scout Index Data - Java classes from openSUSE 10.3

%package -n scout-java-suse110
Group:          System/Packages
Summary:        Index Data for Package Scout
Version:        2008.06.14
Requires:       scout

%description -n scout-java-suse110
Package Scout Index Data - Java classes from openSUSE 11.0

%prep
%setup -q -c -n data-gen
cp -a %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} %{SOURCE14} .
cp -a %{SOURCE20} %{SOURCE21} %{SOURCE22} %{SOURCE23} %{SOURCE14} .
cp -a %{SOURCE30} %{SOURCE31} %{SOURCE32} %{SOURCE33} %{SOURCE34} %{SOURCE35} .

%build
python gen-autoconf.py
python gen-bin.py
python gen-java.py
sh gen

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/scout
cp -a *.db $RPM_BUILD_ROOT%{_datadir}/scout

%clean
rm -rf $RPM_BUILD_ROOT

%files -n scout-autoconf-sle10
%defattr(-,root,root)
%{_datadir}/scout/autoconf-suse101*

%files -n scout-autoconf-suse101
%defattr(-,root,root)
%{_datadir}/scout/autoconf-suse101*

%files -n scout-autoconf-suse102
%defattr(-,root,root)
%{_datadir}/scout/autoconf-suse102*

%files -n scout-autoconf-suse103
%defattr(-,root,root)
%{_datadir}/scout/autoconf-suse103*

%files -n scout-autoconf-suse110
%defattr(-,root,root)
%{_datadir}/scout/autoconf-suse110*

%files -n scout-bin-sle10
%defattr(-,root,root)
%{_datadir}/scout/bin-suse101*

%files -n scout-bin-suse101
%defattr(-,root,root)
%{_datadir}/scout/bin-suse101*

%files -n scout-bin-suse102
%defattr(-,root,root)
%{_datadir}/scout/bin-suse102*

%files -n scout-bin-suse103
%defattr(-,root,root)
%{_datadir}/scout/bin-suse103*

%files -n scout-bin-suse110
%defattr(-,root,root)
%{_datadir}/scout/bin-suse110*

%files -n scout-java-jpackage17
%defattr(-,root,root)
%{_datadir}/scout/java-jpackage17*

%files -n scout-java-sle10
%defattr(-,root,root)
%{_datadir}/scout/java-sle10*

%files -n scout-java-suse101
%defattr(-,root,root)
%{_datadir}/scout/java-suse101*

%files -n scout-java-suse102
%defattr(-,root,root)
%{_datadir}/scout/java-suse102*

%files -n scout-java-suse103
%defattr(-,root,root)
%{_datadir}/scout/java-suse103*

%files -n scout-java-suse110
%defattr(-,root,root)
%{_datadir}/scout/java-suse110*

%changelog
