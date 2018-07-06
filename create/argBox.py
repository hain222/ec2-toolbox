# File: argBox.py
# Author: Harrison Inocencio
# Date: 7-3-2018
# Purpose: contains the argBox class, which is a container for 'creates'
#		   various parameters. Also contains helper processes/functions
#		   that format/update parameters

# Notes:
# 1.
# 2.
# 3.
# 4.
# 5.

# TODO:
# 1. 
# 2.
# 3.
# 4.
# 5.

# -------------------------------------------------------------------

import os
import create.args as args
from datetime import datetime
from config.configBox import configBox

# argBox class
class argBox:
	
	cwd = os.environ[args.cwd_env]
	cbox = configBox()

	# init func
	# Set all available attributes
	def __init__(self, arg_dict):
		self.name = arg_dict.name
		self.user = arg_dict.user
		self.output = arg_dict.output

		# Initial checks
		self.__set_defaults()
		self.__check_config()

	# __set_defaults func
	# Sets variable defaults if necessary
	def __set_defaults(self):
		if self.output == None:
			cur_time = datetime.now().strftime(args.time_fmt)
			self.output = "%s_%s%s" % (args.def_out_prefix, cur_time, args.def_out_suffix)


	# __check_config func
	# Validates the initialized cbox
	def __check_config(self):
		try:
			self.cbox.check_path()
		except FileNotFoundError:
			print(args.path_error)
			exit(1)
