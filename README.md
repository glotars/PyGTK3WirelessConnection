# PyGTK3 Wireless Connection

Just a simple tool to connect to Wi-Fi networks.
I've made this application to act like a plank docklet, so the app closes when you iconify it.
Maybe someday I'll rewrite it in Vala to make that an actual plank docklet.

### Prerequisites

What things you need to install:

```
network-manager
libgtk-3-dev
python3-pip (python 3.6 or later)
gobject-introspection
```

### Installing

Get yourself this app by running in your terminal:

```
git clone https://github.com/Senyaaa/PyGTK3WirelessConnection.git && cd PyGTK3WirelessConnection
```

### Settings

Check the parameters:

```
python3 pygtk3-wireless-connection.py --help
```

You will see this:

```
usage: pygtk3-wireless-connection [-h] Height Width X Y

A simple tool that acts like a some sort of widget and helps you to connect to
Wi-Fi!

positional arguments:
  Height      Application main window height
  Width       Application main window width
  X           Application main window left margin
  Y           Application main window padding on top

optional arguments:
  -h, --help  show this help message and exit
```

You can't open the app without those parameters. So if you try something like:

```
python3 pygtk3-wireless-connection.py 220 300 20 600
```


The application will be opened:

![](misc/screenshot.png?raw=true "PyGTK3 Wireless Connection")


## License

This project is licensed under the GNU General Public License v3.0 ‒ see the [LICENSE](LICENSE) file for details.
