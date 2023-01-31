import requests,json
from requests.auth import HTTPBasicAuth
import rest_utils



controller_ip    = "192.168.1.183"
controller_port  = "8181"
controller_user  = "admin"
controller_pass  = "admin"
config_uri       = "/restconf/config/service-function-forwarder:service-function-forwarders"
config_data      = {
    "service-function-forwarders": {
        "service-function-forwarder": [
            {
                "sff-data-plane-locator": [
                    {
                        "service-function-forwarder-ovs:ovs-options": {
                            "nshc3": "flow", 
                            "remote-ip": "flow", 
                            "exts": "gpe", 
                            "key": "flow", 
                            "dst-port": "6633", 
                            "nsp": "flow", 
                            "nshc2": "flow", 
                            "nshc1": "flow", 
                            "nsi": "flow", 
                            "nshc4": "flow"
                        }, 
                        "name": "Client-SFF-1-dpl", 
                        "data-plane-locator": {
                            "ip": "192.168.1.150", 
                            "port": 6633, 
                            "transport": "service-locator:vxlan-gpe"
                        }
                    }
                ], 
                "name": "Client-SFF", 
                "service-node": "Client", 
                "service-function-forwarder-ovs:ovs-bridge": {
                    "bridge-name": "br-sfc"
                }
            }, 
            {
                "sff-data-plane-locator": [
                    {
                        "service-function-forwarder-ovs:ovs-options": {
                            "nshc3": "flow", 
                            "remote-ip": "flow", 
                            "exts": "gpe", 
                            "key": "flow", 
                            "dst-port": "6633", 
                            "nsp": "flow", 
                            "nshc2": "flow", 
                            "nshc1": "flow", 
                            "nsi": "flow", 
                            "nshc4": "flow"
                        }, 
                        "name": "Server-SFF-1-dpl", 
                        "data-plane-locator": {
                            "ip": "192.168.1.110", 
                            "port": 6633, 
                            "transport": "service-locator:vxlan-gpe"
                        }
                    }
                ], 
                "name": "Server-SFF", 
                "service-node": "Server", 
                "service-function-forwarder-ovs:ovs-bridge": {
                    "bridge-name": "br-sfc"
                }
            }, 
            {
                "service-function-dictionary": [
                    {
                        "sff-sf-data-plane-locator": {
                            "sff-dpl-name": "SFF1-1-dpl", 
                            "sf-dpl-name": "SF1-dpl"
                        }, 
                        "name": "SF1"
                    }, 
                    {
                        "sff-sf-data-plane-locator": {
                            "sff-dpl-name": "SFF1-2-dpl", 
                            "sf-dpl-name": "SF2-dpl"
                        }, 
                        "name": "SF2"
                    }, 
                    {
                        "sff-sf-data-plane-locator": {
                            "sff-dpl-name": "SFF1-3-dpl", 
                            "sf-dpl-name": "SF3-dpl"
                        }, 
                        "name": "SF3"
                    }
                ], 
                "sff-data-plane-locator": [
                    {
                        "service-function-forwarder-ovs:ovs-options": {
                            "nshc3": "flow", 
                            "remote-ip": "flow", 
                            "exts": "gpe", 
                            "key": "flow", 
                            "dst-port": "6633", 
                            "nsp": "flow", 
                            "nshc2": "flow", 
                            "nshc1": "flow", 
                            "nsi": "flow", 
                            "nshc4": "flow"
                        }, 
                        "name": "SFF1-1-dpl", 
                        "data-plane-locator": {
                            "ip": "192.168.1.44", 
                            "port": 6633, 
                            "transport": "service-locator:vxlan-gpe"
                        }
                    }, 
                    {
                        "service-function-forwarder-ovs:ovs-options": {
                            "nshc3": "flow", 
                            "remote-ip": "flow", 
                            "exts": "gpe", 
                            "key": "flow", 
                            "dst-port": "6633", 
                            "nsp": "flow", 
                            "nshc2": "flow", 
                            "nshc1": "flow", 
                            "nsi": "flow", 
                            "nshc4": "flow"
                        }, 
                        "name": "SFF1-2-dpl", 
                        "data-plane-locator": {
                            "ip": "192.168.1.44", 
                            "port": 6633, 
                            "transport": "service-locator:vxlan-gpe"
                        }
                    }, 
                    {
                        "service-function-forwarder-ovs:ovs-options": {
                            "nshc3": "flow", 
                            "remote-ip": "flow", 
                            "exts": "gpe", 
                            "key": "flow", 
                            "dst-port": "6633", 
                            "nsp": "flow", 
                            "nshc2": "flow", 
                            "nshc1": "flow", 
                            "nsi": "flow", 
                            "nshc4": "flow"
                        }, 
                        "name": "SFF1-3-dpl", 
                        "data-plane-locator": {
                            "ip": "192.168.1.44", 
                            "port": 6633, 
                            "transport": "service-locator:vxlan-gpe"
                        }
                    }
                ], 
                "name": "SFF1", 
                "service-node": "SN-SFF", 
                "service-function-forwarder-ovs:ovs-bridge": {
                    "bridge-name": "br-sfc"
                }
            }
        ]
    }
}


rest_utils.put(controller_ip, controller_port, controller_user, controller_pass, config_uri, config_data)

