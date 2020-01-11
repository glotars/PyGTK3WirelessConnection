from nmcli_gui_application import MainWindow
import argparse


APP_NAME = "PyGTK3 Wireless Connection"


if __name__ == '__main__':
	
	main_argument_parser = argparse.ArgumentParser(
		prog = APP_NAME.replace(" ", "-").lower(),
		description = 'A simple tool that acts like a some sort of widget and helps you to connect to Wi-Fi!'
		)

	main_argument_parser.add_argument(
		'Height',
		type = int,
		help = 'Application main window height'
		)

	main_argument_parser.add_argument(
		'Width',
		type = int,
		help = 'Application main window width'
		)
	
	main_argument_parser.add_argument(
		'X',
		type = int,
		help = 'Application main window left margin'
		)

	main_argument_parser.add_argument(
		'Y',
		type = int,
		help = 'Application main window padding on top'
		)

	args = main_argument_parser.parse_args()

	MainWindow(
		APP_NAME,
		args.Height,
		args.Width,
		args.X,
		args.Y
		)