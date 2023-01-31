import requests,json
from requests.auth import HTTPBasicAuth
import rest_utils



controller_ip    = "192.168.1.183"
controller_port  = "8181"
controller_user  = "admin"
controller_pass  = "admin"
config_uri       = "/restconf/config/ietf-access-control-list:access-lists/"
config_data      = {
    "access-lists": "delete"
}


rest_utils.delete(controller_ip, controller_port, controller_user, controller_pass, config_uri, config_data)

