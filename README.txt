Purpose
  - JBoss EAP 6 used specifically to support Red Hat JBoss BPMS, BRMS and FSW.
  - This RPM targets BPMS, BRMS and FSW in both OSE and traditional non-cloud, RHEL environments

Problem
  - The jbappplatform channel of RHN contains JBoss EAP RPMs.
  - The RPMs in the jbappplatform channel continously evolve and sys admins are free to upgrade thier environments as these upgrades to JBoss are released.
  - Red Hat / JBoss BPMS and FSW have a hard-dependency on JBoss EAP 6.1.1, specifically.

Alternatives
  1)  Use RPMs via jbappplatform channel
    - Its technically feasible that a system administrator could elect to install the version of JBoss EAP required to support BPMS and FSW
    - Once installed, the system administrator could elect never to upgrade as new versions of EAP are made available in RHN
    - This approach becomes problematic attempting to support  different JBoss EAP derived products (ie:  bpms, brms, fsw)  on the same OS (ie:  OSE) 

  2)  Don't use RPMs
    - Sys admins can also install FSW, BPMS and BRMS using the conventional zip downloads available from the Customer Support Portal
    - Even for OSE, it's technically feasible that RPMs to support BPMS, BRMS and FSW.
        - In particular, all functionality could be packaged as a 'downloadable' cartridge
        - ie, a BPMS6 downloadable cartridge would bundle:
            1)  JBoss EAP 6
            2)  BPMS6 modules
            3)  BPMS6 runtime web artifacts
        - The problem with this approach is :
            1)  size of download makes for a long, network intensive experience to provision an OSE application
            2)  once downloaded, the size of the contents included in this cartridge count against cgroups disk quota allocated by OSE



Solution
  - The purpose of this RPM is to package the specific version of JBoss EAP to support BPMS, BRMS and FSW.
  - When installed, this RPM will place JBoss EAP in:  /opt/jboss-bpm-soa/jboss-eap-6.1 .
  - No other files are installed via this RPM anywhere else on the operating system
  - This JBoss EAP will not conflict with the JBoss EAP from the jbappplatform in any way, either at installation nor at runtime.



Proposed Architecture
  - SOURCES/jboss_bpm_soa_package_mgmt.png provides an illustration of where this RPM fits into a software configuration architecture to support BPMS, BRMS and FSW.
  - it's proposed that the RPM from this project, jboss_bpm_soa, be included in the existing jbappplatform channel from RHN
  - the contents of this jboss_bpm_soa rpm install in:  /opt/jboss_bpm_soa
  - it's also proposed that the following channels be created and maintained in RHN:
    1)  jboss_brms
        - if a customer has purchased a subscription to BRMS, then that customer receives entitlements to this channel
        - this channel will include RPMs that layer BRMS modules into /opt/jboss_bpm_soa/jboss-eap-6.1
    2)  jboss_bpms
        - if a customer has purchased a subscription to BPMS, then that customer receives entitlements to this channel
        - this channel will include RPMs that layer BPMS modules into /opt/jboss_bpm_soa/jboss-eap-6.1
        - RPMs are also included that contain exploded business-central and dashbuilder web archives
    3)  jboss_fsw
        - if a customer has purchased a subscription to FSW, then that customer receives entitlements to this channel
        - this channel will include RPMs that layer FSW modules into /opt/jboss_bpm_soa/jboss-eap-6.1
        - RPMs are also included that contain exploded overlord and bpel web archives


Build Procedure
  - clone this project from github
  - download jboss-eap-6.1.1.zip from the Red Hat Customer Support Portal
  - cd /path/to/this/jboss_bpm_soa_rpmbuild
  - cp /path/to/jboss-eap-6.1.1.zip SOURCES
  - rpmbuild --define "_sourcedir `pwd`/SOURCES" -ba SPECS/jboss_bpm_soa.spec
  - rpm -qlp ~/rpmbuild/RPMS/x86_64/jbosseap-6.1.1-1.el6.x86_64.rpm
  - sudo rpm -ivh ~/rpmbuild/RPMS/x86_64/jbosseap-6.1.1-1.el6.x86_64.rpm
  - sudo rpm -e jbosseap

 TO-DO
 1)  change name to something more specific
 2)  add pre & post installs
 3)  add documentation to /usr/share/doc 
