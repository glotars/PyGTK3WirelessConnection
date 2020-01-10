import subprocess
import shlex
import re

RADIO = "nmcli radio wifi"
DEVICE = "nmcli device"
DEVICE_WIFI = f"{DEVICE} wifi"

class Pynmcli:

    def __init__(self, APP_NAME):
        self.APP_NAME = APP_NAME

    def run_cmd(self, command):
        command =  shlex.split(command)
        result = subprocess.Popen(command, stdout = subprocess.PIPE)
        result.wait()
        return result.returncode, result.communicate()[0].decode("UTF-8")

    def _split_and_format_row(self, row):
        row = re.split(r'\s{2,}', row)
        return (row[1], row[5] + "%", row[7].strip().replace(" ", "\\"))

    def wifi_available_networks_list(self):
        wifi_list = self.run_cmd(DEVICE_WIFI)[1].split("\n")
        return [self._split_and_format_row(w) for w in wifi_list[1:-1]]

    def wifi_update_current_connection_status(self):
        result = self.run_cmd(DEVICE)[1]
        result = re.split(r'\s{2,}', result.split("\n")[1])
        result = result[-2]
        if result != "--":
            return result
        else:
            return None

    def wifi_module_status(self):
        if self.run_cmd(RADIO)[1] == "enabled\n":
            return True
        else:
            return False

    def wifi_module_enable(self):
        return self.run_cmd(f"{RADIO} on")

    def wifi_module_disable(self):
        return self.run_cmd(f"{RADIO} off")

    def wifi_current_connection_down(self):
        currently_connected_to = self.wifi_update_current_connection_status()
        if currently_connected_to is not None:
            return self.run_cmd(f"nmcli con down {currently_connected_to}")

    def wifi_establish_new_connection(self, SSID, password):
        COMMAND = f"{DEVICE_WIFI} connect {SSID} password {password}"
        result = self.run_cmd(COMMAND)
        if result[0] == 0:
            return self.notify_send(f"Successfully connected to {SSID}")
        else:
            return self.notify_send(f"Can\'t establish connection to {SSID}")

    def notify_send(self, text, urgency_level = 'normal'):
        notification_cmd = f'notify-send "{self.APP_NAME}" "{text}" -u {urgency_level} -a "{self.APP_NAME}"'
        return self.run_cmd(notification_cmd)