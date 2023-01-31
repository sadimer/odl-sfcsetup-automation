import requests,json
from requests.auth import HTTPBasicAuth
import rest_utils



controller_ip    = "192.168.1.183"
controller_port  = "8181"
controller_user  = "admin"
controller_pass  = "admin"
config_uri       = "/restconf/config/service-function-path-metadata:service-function-metadata/"
config_data      = {
    "service-function-metadata": {
        "context-metadata": [
            {
                "context-header4": "4", 
                "context-header3": "3", 
                "name": "NSH1", 
                "context-header2": "2", 
                "context-header1": "1"
            }
        ]
    }
}


rest_utils.put(controller_ip, controller_port, controller_user, controller_pass, config_uri, config_data)

