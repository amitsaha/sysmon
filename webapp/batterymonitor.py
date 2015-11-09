"""
Module which queries udev and uses the command line utility
acpi (via subprocess) to retrieve the current battery information

"""

import pyudev
import subprocess

# global context object
context = pyudev.Context()

def retrieve_battery_details():

    battery_details={}
    for powerdev in context.list_devices(subsystem='power_supply'):

        if powerdev.attributes['type'] == 'Battery':
            dev_attributes = {}
            for attrib in powerdev.attributes:
                try:
                    dev_attributes[attrib] = powerdev.attributes[attrib]
                except KeyError:
                    dev_attributes[attrib] = ''
            battery_details[powerdev] = dev_attributes

    return battery_details

def get_charge_stats():

    battery_details = retrieve_battery_details()
    battery = []
    for i,b in enumerate(battery_details):
        charge_now = float(battery_details[b]['charge_now'])
        charge_full = float(battery_details[b]['charge_full'])

        battery.append((charge_now/charge_full)*100)

    battery_stats={}
    #TODO: implement acpi command's logic in Python..
    for i, details in enumerate(subprocess.check_output(['acpi','-b']).splitlines()):
        battery_stats[i+1] = {'details':details,
                              'charge_percent':battery[i]
                              }
    return battery_stats

if __name__=='__main__':
    print get_charge_stats()
