import requests,json
from requests.auth import HTTPBasicAuth
import rest_utils



controller_ip    = "192.168.1.183"
controller_port  = "8181"
controller_user  = "admin"
controller_pass  = "admin"
config_uri       = "/restconf/operations/rendered-service-path:create-rendered-path/"


config_data1      = {
    "input": {
        "symmetric": "true", 
        "name": "RSP-SFC1", 
        "parent-service-function-path": "SFC1-SFP"
    }
}
rest_utils.post(controller_ip, controller_port, controller_user, controller_pass, config_uri, config_data1)

config_data2      = {
    "input": {
        "symmetric": "true", 
        "name": "RSP-SFC2", 
        "parent-service-function-path": "SFC2-SFP"
    }
}
rest_utils.post(controller_ip, controller_port, controller_user, controller_pass, config_uri, config_data2)

