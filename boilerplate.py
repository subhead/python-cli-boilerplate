#!/usr/bin/env python3

import os
import argparse
logger = __import__("logger")

def parse_args():
	parser = argparse.ArgumentParser(
		formatter_class=argparse.ArgumentDefaultsHelpFormatter
	)
	parser.add_argument("-v", "--verbosity",
                        help="logging verbosity",
                        default=logger.logging.WARN)


def main():
	args = parse_args()
	log_level = logger.logging.DEBUG if os.environ.get('LOGLEVEL', False) else logger.logging.WARN
	mainLogger = logger.init_logger('MAIN', log_level)
	mainLogger.info('Hello world')
	print(log_level)


if __name__ == '__main__':
	main()