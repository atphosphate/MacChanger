import subprocess
import optparse
import re

def get_info():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i","--interface", dest="interface", help="interface to change")
    parse_object.add_option("-m","--mac", dest="mac_adress", help="new mac adress")
    return parse_object.parse_args()

def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface]).decode("utf-8")
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig)

    if new_mac:
        return new_mac.group(0)
    else:
        return None

def change_mac(user_interface, user_mac_adress):
    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_adress])
    subprocess.call(["ifconfig", user_interface, "up"])

print("MacChanger has started")

(user_input, arguments) = get_info()
change_mac(user_input.interface, user_input.mac_adress)
finalized_mac = control_new_mac(user_input.interface)

if finalized_mac == user_input.mac_adress:
    print("Success!")
else:
    print("Error!")