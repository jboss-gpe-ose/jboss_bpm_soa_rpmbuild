procedure
  - clone this project from github
  - cd /path/to/this/rpmbuild
  - download jboss-eap-6.1.1.zip from the Red Hat Customer Support Portal
  - cp /path/to/jboss-eap-6.1.1.zip SOURCES
  - rpmbuild -ba SPECS/jbosseap.spec
  - rpm -qlp RPMS/x86_64/jbosseap-6.1.1-1.el6.x86_64.rpm
  - sudo rpm -ivh RPMS/x86_64/jbosseap-6.1.1-1.el6.x86_64.rpm
  - sudo rpm -e jbosseap

 TO-DO
 1)  change name to something more specific
 2)  add pre & post installs
 3)  add documentation to /usr/share/doc 
