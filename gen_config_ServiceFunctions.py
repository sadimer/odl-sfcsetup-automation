import requests,json
from requests.auth import HTTPBasicAuth
import rest_utils



controller_ip    = "192.168.1.183"
controller_port  = "8181"
controller_user  = "admin"
controller_pass  = "admin"
config_uri       = "/restconf/config/service-function:service-functions"
config_data      = {
    "service-functions": {
        "service-function": [
            {
                "sf-data-plane-locator": {
                    "ip": "192.168.1.220", 
                    "service-function-forwarder": "SFF1", 
                    "name": "SF1-dpl", 
                    "transport": "service-locator:vxlan-gpe", 
                    "port": 6633
                }, 
                "rest-uri": "http://192.168.1.220:5000", 
                "name": "SF1", 
                "nsh-aware": "true", 
                "ip-mgmt-address": "192.168.1.220", 
                "type": "dpi"
            }, 
            {
                "sf-data-plane-locator": {
                    "ip": "192.168.1.166", 
                    "service-function-forwarder": "SFF1", 
                    "name": "SF2-dpl", 
                    "transport": "service-locator:vxlan-gpe", 
                    "port": 6633
                }, 
                "rest-uri": "http://192.168.1.166:5000", 
                "name": "SF2", 
                "nsh-aware": "true", 
                "ip-mgmt-address": "192.168.1.166", 
                "type": "firewall"
            }, 
            {
                "sf-data-plane-locator": {
                    "ip": "192.168.1.71", 
                    "service-function-forwarder": "SFF1", 
                    "name": "SF3-dpl", 
                    "transport": "service-locator:vxlan-gpe", 
                    "port": 6633
                }, 
                "rest-uri": "http://192.168.1.71:5000", 
                "name": "SF3", 
                "nsh-aware": "true", 
                "ip-mgmt-address": "192.168.1.71", 
                "type": "dpi"
            }
        ]
    }
}


rest_utils.put(controller_ip, controller_port, controller_user, controller_pass, config_uri, config_data)

