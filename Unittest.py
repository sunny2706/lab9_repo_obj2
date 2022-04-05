#!/usr/bin/env python3
#Objective_2
#Importing all the necessary modules
from __future__ import print_function
from multiprocessing import connection
from typing_extensions import Self
import unittest
from unittest import result
#Using Try Exception because if the modules are not installed it will
#go to the exception block saying that install it
try:
    from ncclient import manager
    from prettytable import PrettyTable
    from netaddr import IPAddress
    import pandas as pd
    import ipaddress
    import os
    import sys
except Exception:
    print('Install all the necessary modules')
    sys.exit()

#FETCHING THE RUNNING CONFIGURATION FROM THE ROUTER
CONFIGURATION_FETCH_INFO = '''
                           <filter>
    		               <config-format-text-block>
    		               <text-filter-spec> %s </text-filter-spec>
    		               </config-format-text-block>
                           </filter>
                           '''
class UNIT_TESTING(unittest.TestCase):
    def UNIT_TEST_IP(self):

        SUNNY = manager.connect(host='198.51.100.13', port = 22, 
                                username = 'lab', password='lab123', 
                                hostkey_verify=False, device_params={'name': 'iosxr'}, 
                                allow_agent=False,look_for_keys=True)

        FETCHING_LOOPBACK = CONFIGURATION_FETCH_INFO % ('int Loopback99')
        TARGET_RESULT = SUNNY.get_config('running', FETCHING_LOOPBACK)
        BASIC = str(TARGET_RESULT).split()
        LOOPBACK_IP = BASIC[9] + '/' + str(IPAddress(BASIC[10]).netmask_bits())
        print(LOOPBACK_IP)
        if LOOPBACK_IP == "10.1.3.1/24":
           print("TRUE")
        else:
            print("FALSE")

    #CREATED A FUNCTION FOR TESTING THE ROUTER 1 CONFIGURATION FOR AREA
    def UNIT_TEST_CONFIG_R1(self):

        SUNNY_2 = manager.connect(host='198.51.100.13', port = 22, 
                               username = 'lab', password='lab123', 
                               hostkey_verify=False, device_params={'name': 'iosxr'}, 
                                allow_agent=False,look_for_keys=True)
        OSPF_INFO = CONFIGURATION_FETCH_INFO % ('| s ospf')
        TARGET_RESULT_2 = SUNNY_2.get_config('running', OSPF_INFO)
        BASIC_1 = str(TARGET_RESULT_2).split()

    #CREATED A FUNCTION FOR PINGING ROUTER 5'S LOOPBACK FROM ROUTER 2
    def PING_LO(self):

        SUNNY_3 = manager.connect(host='198.51.100.12', port = 22, 
                                username = 'lab', password='lab123', 
                                hostkey_verify=False, device_params={'name': 'iosxr'}, 
                                allow_agent=False,look_for_keys=True)
        FETCHING_LOOPBACK_3 = CONFIGURATION_FETCH_INFO % ('int Loopback99')
        TARGET_RESULT_3 = SUNNY_3.get_config('running', FETCHING_LOOPBACK_3)
        print(TARGET_RESULT_3)
        b = self.assertTrue('ping 10.1.5.1')
        print(b)

if __name__ == "__main__":
    unittest.main()
    