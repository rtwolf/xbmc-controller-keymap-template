#!/usr/bin/python
# Automatically generate a controller map to help with testing.
# RT Wolf. Dec 15, 2013
# https://github.com/rtwolf/xbmc-controller-keymap-template

import os

def main():
	try:
		template = open ("ps3_controller_keymap_template.xml", "r")
		text = template.read()
		template.close()

		text = text.replace("#joystick_name#", "Afterglow controller for PS3")
		text = text.replace("#square#", "1")
		text = text.replace("#X#", "2")
		text = text.replace("#circle#", "3")
		text = text.replace("#triangle#", "4")
		text = text.replace("#L1#", "5")
		text = text.replace("#R1#", "6")
		text = text.replace("#L2#", "7")
		text = text.replace("#R2#", "8")
		text = text.replace("#select#", "9")
		text = text.replace("#start#", "10")
		text = text.replace("#L3#", "11")
		text = text.replace("#R3#", "12")
		text = text.replace("#ps_button#", "13")

		text = text.replace("#d-pad_up#", "hat id=\"1\" position=\"up\"")
		text = text.replace("#d-pad_down#", "hat id=\"1\" position=\"down\"")
		text = text.replace("#d-pad_left#", "hat id=\"1\" position=\"left\"")
		text = text.replace("#d-pad_right#", "hat id=\"1\" position=\"right\"")
		text = text.replace("#d-pad_closing_tag#", "hat")
		
		generated = open ('afterglow_keymap.xml', "w") # w overwrites file if it exists
		generated.write(text)
		generated.close()

	except IOError:
		print "Uh-oh"

if __name__ == '__main__':
	main()