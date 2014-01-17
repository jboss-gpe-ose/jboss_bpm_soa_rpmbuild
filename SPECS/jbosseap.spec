Name:           jbosseap
Version:        6.1.1
Release:        1%{?dist}
Summary:        JBoss EAP 6.1.1 used specifically to support BPMS6 and FSW
Group:          Red Hat JBoss
License:        GPLv3+
URL:            http://www.redhat.com
Source0:        jboss-eap-6.1.1.zip 

%description
JBoss EAP 6.1.1 used specifically to support Red Hat JBoss BPMS6 and FSW


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt
unzip %{SOURCE0} -d $RPM_BUILD_ROOT/opt


%clean
rm -rf $RPM_BUILD_ROOT


%files
/opt/*
