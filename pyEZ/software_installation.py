#!/usr/bin/python

from jnpr.junos import Device
from jnpr.junos.utils.sw import SW
PACKAGE = "some/package.tgz"

def progress_callback(dev, report):
    print(report)

if __name__ == '__main__':
    # Hardcoded credentials just for lab ease
    with Device(host='66.129.235.12', port=45002, user='jcluser', passwd='Juniper!1') as dev:

        sw = SW(dev)
        ok = sw.install(package=PACKAGE, no_copy=True, validate=False, progress=progress_callback)

        

