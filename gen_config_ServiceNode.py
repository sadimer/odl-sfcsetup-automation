import requests,json
from requests.auth import HTTPBasicAuth
import rest_utils



controller_ip    = "192.168.1.183"
controller_port  = "8181"
controller_user  = "admin"
controller_pass  = "admin"
config_uri       = "/restconf/config/service-node:service-nodes"
config_data      = {
    "service-nodes": {
        "service-node": [
            {
                "name": "Client", 
                "ip-mgmt-address": "192.168.1.150"
            }, 
            {
                "name": "Server", 
                "ip-mgmt-address": "192.168.1.110"
            }, 
            {
                "name": "SN-SFF", 
                "ip-mgmt-address": "192.168.1.44"
            }, 
            {
                "name": "SN-SF1", 
                "ip-mgmt-address": "192.168.1.220"
            }, 
            {
                "name": "SN-SF2", 
                "ip-mgmt-address": "192.168.1.166"
            }, 
            {
                "name": "SN-SF3", 
                "ip-mgmt-address": "192.168.1.71"
            }
        ]
    }
}


rest_utils.put(controller_ip, controller_port, controller_user, controller_pass, config_uri, config_data)

