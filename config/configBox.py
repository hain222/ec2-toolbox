# File: configBox.py
# Author: Harrison Inocencio
# Date: 06-27-18
# Purpose: Defines the configBox class. Serves as a container for storing
#		   aws parameters, and reading/writing the .ini file that stores 
#		   them

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
import gconsts
import configparser
import config.args as args

# configBox class
class configBox():

	image_id = None
	inst_type = None
	key_name = None
	sg_id = None

	# __init__ func
	# By default, will automatically try to load ini file
	def __init__(self):
		try:
			self.ini_read()
		except FileNotFoundError:
			pass	
			
	# __parse_ini func
	# Parses init configuration file and sets attributes
	def __parse_ini(self):
		config = configparser.ConfigParser()
		config.read(gconsts.config_path)
		self.image_id = config[args.section_name][args.image_id_key]
		self.inst_type = config[args.section_name][args.inst_type_key]
		self.key_name = config[args.section_name][args.key_name_key]
		self.sg_id = config[args.section_name][args.sg_id_key]

	# __check_path func
	# Attempts to locate config file path
	# If not found, raises a FileNotFound exception
	def check_path(self):
		if not os.path.isfile(gconsts.config_path):
			raise(FileNotFoundError)

	# ini_read func
	# Attempts to update its attributes from the ini file
	# Will riase a FileNotFoundError if the file could not be located
	# Will raise a KeyError if a the file experiences a key formatting 
	# issue
	def ini_read(self):
		self.check_path()
		try:
			self.__parse_ini()
		except KeyError:
			raise(RuntimeError(args.key_error))

	# config_write func
	# The object will write out its current attributes into the config file
	# Will overwrite current config file
	def config_write(self):
		config = configparser.ConfigParser()
		config[args.section_name] = {}
		config[args.section_name][args.image_id_key] = self.image_id
		config[args.section_name][args.inst_type_key] = self.inst_type
		config[args.section_name][args.key_name_key] = self.key_name
		config[args.section_name][args.sg_id_key] = self.sg_id

		with open(gconsts.config_path, 'w') as fh:
			fh.write(args.config_header+'\n')
			config.write(fh)
	
	# tprint func
	# Print out all attributes (for testing)
	def tprint(self):
		print(self.image_id)
		print(self.inst_type)
		print(self.key_name)
		print(self.sg_id)
