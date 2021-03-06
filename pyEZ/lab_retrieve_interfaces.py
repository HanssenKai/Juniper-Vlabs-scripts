#!/usr/bin/python

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from pprint import pprint
from lxml import etree
from time import sleep

def print_interface_config(device):
    config_json = device.rpc.get_config(
        filter_xml="interfaces", options={"format": "json"})

    print("Interface configuration;")
    for interface in config_json["configuration"]["interfaces"]["interface"]:
        print(interface["name"])
        print(interface["unit"])

def print_interface_op_statuses(device):
    print("\nInterface operational status;")
    rpc_result = device.rpc.get_interface_information()
    # etree.dump(rpc_result)

    interfaces = rpc_result.xpath("physical-interface")
    for interface in interfaces:
        print("Interface: {}, status: {}".format(
            interface.findtext("name").strip(),
            interface.findtext("oper-status").strip()
        ))

def configure_device(device):
    with Config(device, mode=("exclusive")) as conf:
        print ("Disabling the interface...") 
        conf.load("set interfaces ge-0/0/0 disable", format="set")
        conf.pdiff() #print difference
        conf.commit()
        print("Commit complete, waiting...")
        sleep(5)
        print("Enabling interface...")
        conf.load("delete interfaces ge-0/0/0 disable", format="set")
        conf.pdiff()
        conf.commit()
        print("Finished")

def main():
    # Hardcoded credentials just for lab ease
    with Device(host='66.129.235.12', port=45002, user='jcluser', passwd='Juniper!1') as dev:
        # print_interface_config(dev)
        # print_interface_op_statuses(dev)
        configure_device(dev)

        



        #Changing configuration 
                


if __name__ == '__main__':
    main()
