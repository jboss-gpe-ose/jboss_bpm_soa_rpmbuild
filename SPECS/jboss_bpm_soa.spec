Name:           jboss_bpm_soa
Version:        6.1.1
Release:        1%{?dist}
Summary:        JBoss EAP 6.1.1 used specifically to support BPMS6 and FSW for Openshift Enterprise
Group:          Red Hat JBoss
License:        GPLv3+
URL:            http://www.redhat.com
Source0:        jboss-eap-6.1.1.zip 

%description
# JBoss EAP 6.1.1 used specifically to support Red Hat JBoss BPMS6 and FSW.
# The jbappplatform channel of RHN contains JBoss EAP RPMs.
# The RPMs in the jbappplatform channel continously evolve and sys admins are free to upgrade thier environments as these upgrades to JBoss are released.
# Red Hat / JBoss BPMS and FSW have a hard-dependency on JBoss EAP 6.1.1, specifically.
# The purpose of this RPM is to package this specific version of JBoss EAP to support BPMS and FSW.

# When installed, this RPM will place JBoss EAP in:  /opt/jboss-eap-6.1 .
# No other files are installed via this RPM anywhere else on the operating system
# This JBoss EAP will not deconflict with the JBoss EAP from the jbappplatform in any way, either at installation nor at runtime.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/jboss_bpm_soa
unzip %{SOURCE0} -d $RPM_BUILD_ROOT/opt/jboss_bpm_soa

%clean
rm -rf $RPM_BUILD_ROOT

%files
/opt/jboss_bpm_soa/*
