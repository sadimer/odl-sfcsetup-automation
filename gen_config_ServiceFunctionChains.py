import requests,json
from requests.auth import HTTPBasicAuth
import rest_utils



controller_ip    = "192.168.1.183"
controller_port  = "8181"
controller_user  = "admin"
controller_pass  = "admin"
config_uri       = "/restconf/config/service-function-chain:service-function-chains/"
config_data      = {
    "service-function-chains": {
        "service-function-chain": [
            {
                "symmetric": "true", 
                "name": "SFC1", 
                "sfc-service-function": [
                    {
                        "type": "dpi", 
                        "name": "SF1"
                    }, 
                    {
                        "type": "firewall", 
                        "name": "SF2"
                    }
                ]
            }, 
            {
                "symmetric": "true", 
                "name": "SFC2", 
                "sfc-service-function": [
                    {
                        "type": "dpi", 
                        "name": "SF1"
                    }, 
                    {
                        "type": "dpi", 
                        "name": "SF3"
                    }
                ]
            }
        ]
    }
}


rest_utils.put(controller_ip, controller_port, controller_user, controller_pass, config_uri, config_data)

