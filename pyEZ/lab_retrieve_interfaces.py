#!/usr/bin/python

from jnpr.junos import Device
from pprint import pprint

def main():
    # Hardcoded credentials just for lab ease
    with Device(host='66.129.235.12', port=45002, user='jcluser', passwd='Juniper!1') as dev:
        config_json = dev.rpc.get_config(filter_xml="interfaces", options={"format": "json"})     
        
        print("Interface configuration;")
        for interface in config_json["configuration"]["interfaces"]["interface"]:
            print(interface["name"])
            print(interface["unit"])
        
        


if __name__ == '__main__':
    main()