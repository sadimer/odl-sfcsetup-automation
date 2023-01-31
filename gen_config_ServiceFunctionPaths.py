import requests,json
from requests.auth import HTTPBasicAuth
import rest_utils



controller_ip    = "192.168.1.183"
controller_port  = "8181"
controller_user  = "admin"
controller_pass  = "admin"
config_uri       = "/restconf/config/service-function-path:service-function-paths/"
config_data      = {
    "service-function-paths": {
        "service-function-path": [
            {
                "symmetric": "true", 
                "starting-index": 255, 
                "context-metadata": "NSH1", 
                "name": "SFC1-SFP", 
                "service-chain-name": "SFC1"
            }, 
            {
                "symmetric": "true", 
                "starting-index": 255, 
                "context-metadata": "NSH1", 
                "name": "SFC2-SFP", 
                "service-chain-name": "SFC2"
            }
        ]
    }
}


rest_utils.put(controller_ip, controller_port, controller_user, controller_pass, config_uri, config_data)

