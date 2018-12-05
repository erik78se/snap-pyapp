#!/usr/bin/env python3

import logging

logging.basicConfig(level=logging.DEBUG,
					format='%(asctime)s - %(levelname)s - %(message)s')




if __name__ == "__main__":
	# Logg picked up by filebeat
	logging.info('Something important happened.')
	print("I logged a message.")