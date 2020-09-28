#!/usr/bin/python

from jnpr.junos import Device
from jnpr.junos.utils.config import Config


if __name__ == '__main__':
    # Hardcoded credentials just for lab ease
    data = 'set system services netconf traceoptions file test.log'
    with Device(host='66.129.235.12', port=45002, user='jcluser', passwd='Juniper!1') as dev:
        with Config(dev, mode="exclusive") as conf: #Omits lock() and unlock()
            conf.load(data, format='set')
            diff = conf.diff()

            if not diff:
                print("Configuration is up to date")
            else:
                print(diff)
                conf.commit()
            

