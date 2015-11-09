from django.shortcuts import render
import os
import datetime
import batterymonitor
import scanwifi

def gettime(request):
    """ View providing the current time
    on the system"""

    return render(request, 'time.html',
                  {'time': datetime.datetime.now()}
                  )

def networks(request):
    """ View providing the Wireless networks currently
    visible"""

    return render(request,'wifinetworks.html',
                  {'networks':scanwifi.get_all_bssids()}
                  )

def battery(request):
    """ View providing the battery statistics
    """

    return render(request,'battery.html',
                  {'battery':batterymonitor.get_charge_stats()}
                  )

def sysmon(request):
    """ View providing some system information
    """

    return render(request, 'current_sysinfo.html',
                  {'osname':os.uname()
                   })
