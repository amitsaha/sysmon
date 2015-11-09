About sysmon
============

sysmon is a Django powered web application which on deployed on a host
system makes battery information and the wireless access points
visible to the system. By making using of Web Workers, these data are
updated at regular intervals. Hence, via this web application a user
is provided with continuously updating system information such as
above.

Source structure
================

The application is contained within the webapp/ directory. At the
top-level, it has both Django specific modules: manage.py, views.py,
settings.py and urls.py and helper modules such as batterymonitor.py
and scanwifi.py.

The static/ directory consists of Javascript and CSS files in the js/
and css/ sub-directories respectively.

The templates/ directory contains the Django templates used to render
the web page.

Development environment
=======================

The project was developed using Django 1.3, Python 2.7 on Ubuntu
12.04. In addition, for it's functioning, the project needs the following two packages to
be installed: acpi and python-pyudev.

The BASH script, check_deps.sh can be used to check the dependencies
and install them if necessary.

Running the web application
===========================

To start the web application, run the BASH script, start_webapp.sh
and then visit the web page <your-ip>:8080

No testing has been done to make this applicaion run under a WSGI container.
