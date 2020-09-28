#!/usr/bin/python

from jnpr.junos import Device
from lxml import etree


if __name__ == '__main__':
    # Hardcoded credentials just for lab ease
    with Device(host='66.129.235.12', port=45002, user='jcluser', passwd='Juniper!1') as dev:
        #dev.open() ^with statements omits manual connection open and close for reliability. 

        # Launch rpc from pyEZ, using etree as parser
        cnf = dev.rpc.get_config(filter_xml=etree.XML('<configuration><interfaces/></configuration>'))        
        print (etree.tostring(cnf))


        #dev.close()
