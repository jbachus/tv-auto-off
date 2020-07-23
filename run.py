import broadlink
import socket, time, os, sys
from datetime import datetime

# Ensure required configuration variables
required_vars = ('ROKU_IP','BROADLINK_IP','POWER_IR_SIGNAL')
if not all(key in os.environ for key in required_vars):
    print("ROKU_IP BROADLINK_IP and POWER_IR_SIGNAL are required.  ROKU_PORT and MAX_MINUTES are optional")
    sys.exit(os.EX_CONFIG)

ROKU_CONNECTION = (os.environ.get('ROKU_IP'),int(os.environ.get('ROKU_PORT',8060)))
BROADLINK_IP = os.environ.get('BROADLINK_IP')
POWER_IR_SIGNAL = os.environ.get('POWER_IR_SIGNAL')
MAX_MINUTES = int(os.environ.get('MAX_MINUTES',60))

def is_on():
    s = socket.socket()
    s.settimeout(5)
    result = s.connect_ex(ROKU_CONNECTION)
    s.shutdown(socket.SHUT_RDWR)
    s.close()
    return result == 0

def send_power_command():
    devices = broadlink.discover(timeout=5,discover_ip_address=BROADLINK_IP)
    devices[0].auth()
    devices[0].send_data(bytes.fromhex(POWER_IR_SIGNAL))

while True:
    if is_on():
        print("[{}] TV is ON, waiting {} minutes to ensure it's off".format(datetime.now(),MAX_MINUTES))
        time.sleep(60*MAX_MINUTES)
        if is_on():
            print("[{}] TV is still ON after {} minutes, turning it off".format(datetime.now(),MAX_MINUTES))
            send_power_command()
            # Wait 10 seconds for it to power off
            time.sleep(10)
    else:
        # Sleep 1 minute
        time.sleep(60)
