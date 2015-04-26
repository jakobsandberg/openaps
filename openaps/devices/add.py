
"""
add    - add a new device configuration
"""
from openaps import vendors
from openaps.devices.device import Device
import sys

def configure_app (app, parser):
  parser._actions[-1].choices = None
  commands = vendors.get_configurable_devices(app)
  app.vendors = commands
  commands.configure_commands(parser)

def configure_parser (parser):
  pass

def main (args, app):
  # print "adding", app.selected.vendors.selected(args).method
  # device = app.selected.vendors.selected(args)(args, app)
  vendor = vendors.lookup(args.vendor)
  print "MY vendor", vendor
  print args
  device = Device(args.name, vendor)
  device.read(args=args)
  app.config.add_device(device)
  print device, device.items( )
  app.config.write(sys.stdout)
  app.config.save( )
