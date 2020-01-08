from pynmcli import Pynmcli
import threading
import time
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio, Gdk, GLib

APPLICATION_START_X_COORDINATE = 30
APPLICATION_START_Y_COORDINATE = 600

APPLICATION_X_SIZE = 220
APPLICATION_Y_SIZE = 300

def close_when_minimized(window, event):
    if event.new_window_state == Gdk.WindowState.ICONIFIED:
        Gtk.main_quit(window)


class EnterPasswordDialog(Gtk.Dialog):

    def __init__(self, parent, wifi_ssid, *args):
        Gtk.Dialog.__init__(self, "Password", parent, 0,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OK, Gtk.ResponseType.OK))

        HeaderBar = Gtk.HeaderBar()
        HeaderBar.set_show_close_button(False)
        HeaderBar.props.title = "Password"
        self.set_titlebar(HeaderBar)

        self.set_default_size(150, 100)
        self.wifi_ssid = wifi_ssid
        label = Gtk.Label(label = f"{self.wifi_ssid} password:")

        box = self.get_content_area()
        box.add(label)

        self.entry = Gtk.Entry()
        self.entry.set_visibility(False)
        box.add(self.entry)

        self.check_visible = Gtk.CheckButton(label = "Show password")
        self.check_visible.connect("toggled", self.show_password)
        self.check_visible.set_active(False)
        box.add(self.check_visible)

        self.show_all()

    def show_password(self, button):
        self.entry.set_visibility(button.get_active())

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(APPLICATION_X_SIZE, APPLICATION_Y_SIZE)
        self.set_resizable(False)
        self.move(APPLICATION_START_X_COORDINATE, APPLICATION_START_Y_COORDINATE)

        self.nm = Pynmcli()

        """
        Header Bar
        """

        HeaderBar = Gtk.HeaderBar()
        HeaderBar.set_show_close_button(False)
        HeaderBar.props.title = "Connect"
        self.set_titlebar(HeaderBar)

        self.update_wifi_spinner = Gtk.Spinner()
        HeaderBar.pack_end(self.update_wifi_spinner)

        self.switch = Gtk.Switch()
        self.switch.connect("notify::active", self.wifi_module_status)
        self.switch.set_active(self.nm.wifi_module_status())
        HeaderBar.pack_start(self.switch)

        """
        Wifi liststore
        """

        self.liststore_wifi = Gtk.ListStore(str, str, str)
        self.treeview = Gtk.TreeView(model = self.liststore_wifi)

        self.wifi_text = Gtk.CellRendererText()
        self.ssid_column = Gtk.TreeViewColumn("SSID", self.wifi_text, text=0)
        self.treeview.append_column(self.ssid_column)

        self.signal_column = Gtk.TreeViewColumn("Signal", self.wifi_text, text=1)
        self.treeview.append_column(self.signal_column)

        self.security_column = Gtk.TreeViewColumn("Security", self.wifi_text, text=2)
        self.treeview.append_column(self.security_column)

        self.treeview.connect("row-activated", self.wifi_connect)
        self.add(self.treeview)

        self.connect("window-state-event", close_when_minimized)
        self.show_all()

        """
        Updating wifi in another thread
        """

        updating_thread = threading.Thread(target = self.updating_network_list)
        updating_thread.daemon = True
        updating_thread.start()

    def updating_network_list(self):
        while True:
            GLib.timeout_add_seconds(1, self.getting_data_and_updating_liststore)
            time.sleep(30)

    def getting_data_and_updating_liststore(self):
        data = self.nm.wifi_available_networks_list()
        self.liststore_wifi.clear()
        
        if len(data) == 0:
            return False
        
        for network_index, d in enumerate(data):
            self.liststore_wifi.append(d)
        return False

    def wifi_connect(self, *args):
        dialog = EnterPasswordDialog(self, self.liststore_wifi[args[1][0]][0])
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            self.nm.wifi_current_connection_down()
            self.nm.wifi_establish_new_connection(dialog.wifi_ssid, dialog.entry.get_text())

        dialog.destroy()

    def wifi_module_status(self, *args):
        if self.switch.get_active() == True:
            self.nm.wifi_module_enable()
            self.update_wifi_spinner.start()

        else:
            self.nm.wifi_module_disable()
            self.update_wifi_spinner.stop()

def main():
    MainWindow()
    Gtk.main()

if __name__ == '__main__':
    main()