# File: create.py
# Author: Harrison Inocencio
# Date: 06-25-18
# Purpose: Creates set number of workshop instances. Can create a single
#		   instance with specified vm name and user or can be given a list
#		   of vm and user names using the -f option

# Usage: Should be executed using the 'create' executable in 'bin'

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

from config.configBox import configBox
from instFactory import instFactory
import create.args as args

# main func
# Parses args, executes boto3 commands
def main():

	arg_dict = args.parse()
	nametag = arg_dict.nametag
	user = arg_dict.username

	cbox = configBox()
	try:
		cbox.check_path()
	except FileNotFoundError:
		print(args.path_error)
		exit(1)

	factory = instFactory()
	
	try:
		inst = factory.create_instance(nametag, cbox)
		print("%s Spun @ %s" % (inst.inst_id, insts.pub_ip))
		#inst.ws_user_setup(user)
	except:
		print(args.create_error)
		exit(1)


main()
