import requests,json
from requests.auth import HTTPBasicAuth
import rest_utils



controller_ip    = "192.168.1.183"
controller_port  = "8181"
controller_user  = "admin"
controller_pass  = "admin"
config_uri       = "/restconf/config/service-function-classifier:service-function-classifiers/"
config_data      = {
    "service-function-classifiers": {
        "service-function-classifier": [
            {
                "name": "scl1", 
                "scl-service-function-forwarder": [
                    {
                        "interface": "veth-br", 
                        "name": "Server-SFF"
                    }
                ], 
                "acl": {
                    "type": "ietf-access-control-list:ipv4-acl", 
                    "name": "Endpoint-http-server"
                }
            }, 
            {
                "name": "scl2", 
                "scl-service-function-forwarder": [
                    {
                        "interface": "veth-br", 
                        "name": "Server-SFF"
                    }
                ], 
                "acl": {
                    "type": "ietf-access-control-list:ipv4-acl", 
                    "name": "Endpoint-ssh-server"
                }
            }, 
            {
                "name": "scl3", 
                "scl-service-function-forwarder": [
                    {
                        "interface": "veth-br", 
                        "name": "Client-SFF"
                    }
                ], 
                "acl": {
                    "type": "ietf-access-control-list:ipv4-acl", 
                    "name": "Endpoint-http-client"
                }
            }, 
            {
                "name": "scl4", 
                "scl-service-function-forwarder": [
                    {
                        "interface": "veth-br", 
                        "name": "Client-SFF"
                    }
                ], 
                "acl": {
                    "type": "ietf-access-control-list:ipv4-acl", 
                    "name": "Endpoint-ssh-client"
                }
            }
        ]
    }
}


rest_utils.put(controller_ip, controller_port, controller_user, controller_pass, config_uri, config_data)

