# File: configQuery.py
# Author: Harrison Inocencio
# Date: 06-27-18
# Purpose: Queries a user for aws parameters in order to create a new, or
#		   update an existing config.ini

# Usage: Should be used through 'bin/configure'

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

import config.args as args
from config.configBox import configBox

# update_query_helper func
# Produces a query formatted for update_query given a specific call and 
# attribute
def update_query_helper(call, attribute):
	response = input("%s [%s] : " % (call, attribute))
	if response == '':
		response = attribute
	
	return response

# update_query func
# Queries user for new config parameters
# Formats queries for when a config file is being 'updated'
def update_query(cbox):
	cbox.image_id = update_query_helper(args.image_id_call, cbox.image_id)
	cbox.inst_type = update_query_helper(args.inst_type_call, cbox.inst_type)
	cbox.key_name = update_query_helper(args.key_name_call, cbox.key_name)
	cbox.sg_id = update_query_helper(args.sg_id_call, cbox.sg_id)

# new_query_helper func
# Produces a query formatted for new_query given a specific call
def new_query_helper(call):
	response = input("%s : " % call)
	while response == '':
		print('[Field Required]')
		response = input("%s : " % call)

	return response

# new_query func
# Queries user for new config parameters
# Formats queries for when a new config file is needed
def new_query(cbox):
	cbox.image_id = new_query_helper(args.image_id_call)
	cbox.inst_type = new_query_helper(args.inst_type_call)
	cbox.key_name = new_query_helper(args.key_name_call)
	cbox.sg_id = new_query_helper(args.sg_id_call)

# main func
# Contains try loops.
def main():
	
	cbox = configBox()
	try:
		# Update Config
		try:
			cbox.ini_read()
			update_query(cbox)
		# New Config
		except FileNotFoundError:
			print(args.new_query_msg)
			new_query(cbox)
		cbox.config_write()
		#print(args.complete_msg)

	except KeyboardInterrupt:
		print(args.key_interrupt)
		exit(1)

main()
