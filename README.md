# PyGTK3 Wireless Connection

Just a simple tool to connect to Wi-Fi networks.
I've made this application to act like a plank docklet, so the app closes when you iconify it.
Maybe someday I'll rewrite it in Vala to make that an actual plank docklet.

### Prerequisites

What things you need to install:

```
network-manager
libgtk-3-dev
python3.6 (or later)
gobject-introspection
```

### Installing

Get yourself this app by running in your terminal:

```
git clone https://github.com/Senyaaa/PyGTK3WirelessConnection.git && cd PyGTK3WirelessConnection
```

And open by:

```
python3 main.py
```

Then you will see something like this:

![](https://github.com/Senyaaa/PyGTK3WirelessConnection/blob/master/misc/screen.png?raw=true "PyGTK3 Wireless Connection")

### Settings

If you want to change start window position or size ‒ just open file main.py with any text editor you want, and make some manipulation with these variables:

```
APPLICATION_START_X_COORDINATE
APPLICATION_START_Y_COORDINATE
APPLICATION_X_SIZE
APPLICATION_Y_SIZE
```

## License

This project is licensed under the GNU General Public License v3.0 ‒ see the [LICENSE](https://github.com/Senyaaa/PyGTK3WirelessConnection/blob/master/LICENSE) file for details.