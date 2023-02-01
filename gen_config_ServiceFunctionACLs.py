import requests,json
from requests.auth import HTTPBasicAuth
import rest_utils



controller_ip    = "192.168.1.183"
controller_port  = "8181"
controller_user  = "admin"
controller_pass  = "admin"
config_uri       = "/restconf/config/ietf-access-control-list:access-lists/"
config_data      = {
    "access-lists": {
        "acl": [
            {
                "acl-name": "Endpoint-http-client", 
                "acl-type": "ietf-access-control-list:ipv4-acl", 
                "access-list-entries": {
                    "ace": [
                        {
                            "matches": {
                                "destination-ipv4-network": "10.100.156.0/22", 
                                "destination-port-range": {
                                    "lower-port": 80, 
                                    "upper-port": 80
                                }, 
                                "source-ipv4-network": "10.100.156.0/22", 
                                "protocol": 6, 
                                "source-port-range": {
                                    "lower-port": 0, 
                                    "upper-port": 0
                                }
                            }, 
                            "actions": {
                                "service-function-acl:rendered-service-path": "RSP-SFC1"
                            }, 
                            "rule-name": "webmail"
                        }
                    ]
                }
            }, 
            {
                "acl-name": "Endpoint-http-server", 
                "acl-type": "ietf-access-control-list:ipv4-acl", 
                "access-list-entries": {
                    "ace": [
                        {
                            "matches": {
                                "destination-ipv4-network": "10.100.156.0/22", 
                                "destination-port-range": {
                                    "lower-port": 0, 
                                    "upper-port": 0
                                }, 
                                "source-ipv4-network": "10.100.156.0/22", 
                                "protocol": 6, 
                                "source-port-range": {
                                    "lower-port": 80, 
                                    "upper-port": 80
                                }
                            }, 
                            "actions": {
                                "service-function-acl:rendered-service-path": "RSP-SFC1-Reverse"
                            }, 
                            "rule-name": "webmail"
                        }
                    ]
                }
            }, 
            {
                "acl-name": "Endpoint-ssh-client", 
                "acl-type": "ietf-access-control-list:ipv4-acl", 
                "access-list-entries": {
                    "ace": [
                        {
                            "matches": {
                                "destination-ipv4-network": "10.100.156.0/22", 
                                "destination-port-range": {
                                    "lower-port": 8080, 
                                    "upper-port": 8080
                                }, 
                                "source-ipv4-network": "10.100.156.0/22", 
                                "protocol": 6, 
                                "source-port-range": {
                                    "lower-port": 0, 
                                    "upper-port": 0
                                }
                            }, 
                            "actions": {
                                "service-function-acl:rendered-service-path": "RSP-SFC2"
                            }, 
                            "rule-name": "ssh"
                        }
                    ]
                }
            }, 
            {
                "acl-name": "Endpoint-ssh-server", 
                "acl-type": "ietf-access-control-list:ipv4-acl", 
                "access-list-entries": {
                    "ace": [
                        {
                            "matches": {
                                "destination-ipv4-network": "10.100.156.0/22", 
                                "destination-port-range": {
                                    "lower-port": 0, 
                                    "upper-port": 0
                                }, 
                                "source-ipv4-network": "10.100.156.0/22", 
                                "protocol": 6, 
                                "source-port-range": {
                                    "lower-port": 8080, 
                                    "upper-port": 8080
                                }
                            }, 
                            "actions": {
                                "service-function-acl:rendered-service-path": "RSP-SFC2-Reverse"
                            }, 
                            "rule-name": "ssh"
                        }
                    ]
                }
            }
        ]
    }
}


rest_utils.put(controller_ip, controller_port, controller_user, controller_pass, config_uri, config_data)

