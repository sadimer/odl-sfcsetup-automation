# odl-sfcsetup-automation
Python scripts to enable SFC provisioning for OpenDaylight Controller

# This is work in progress

1. Specifiy all the configuration for provisioning SFC in json format , please use
   example.json as reference.

2. sfc_config_util.py script can be used for generating config scripts that can be used for
   configuring OpenDaylight controller.

Usage: sfc_config_util.py {config json filename}


Requirements for hosts:
1. Ubuntu 14.04 x86_64 LTS - trusty
2. user used for configuration should be part of sudoer's list and should be set for nopassword
   TBD: script to be checkedin
3. git to be already installed
