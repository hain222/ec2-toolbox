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
# 1. Consider creating a create object that will contain all elements
#	 needed for instance creation
# 2. Consider creating a parser object that contains all parsed elements
# 3. Consider adding comment/newline support for user/name files
# 4. Consider combining the two files into one (csv, tab, format)
# 5. Add a force option, to create a VM despite matching names

# -------------------------------------------------------------------

import os
from datetime import datetime
from create.argBox import argBox
from instFactory import instFactory
import create.args as args

# init_output func
# Writes output file headers etc...
def init_output(abox):
	o_path = "%s/%s" % (abox.cwd, abox.output)	
	with open(o_path, 'w') as o_file:
		o_file.write(args.output_header+'\n')

# gen_lists func
# Generates the user/nametag lists needed for the instance creation loop
# If not run with -f, will return lists consisting of one element each.
# If no name/name file provided, user will be used as the nametag for each
# machine
def gen_lists(asfile, abox):
	# Read params as files
	if asfile:
		user_path = "%s/%s" % (abox.cwd, abox.user)
		name_path = "%s/%s" % (abox.cwd, abox.name)

		with open(user_path, 'r') as user_file:
			user_list = user_file.readlines()

		# If name file provided, read into name_list
		# Otherwise, name_list is user_list
		if abox.name != None:
			with open(name_path, 'r') as name_file:
				name_list = name_file.readlines()
		else:
			name_list = user_list

		# Remove extra newlines
		name_list = [item.strip() for item in name_list]
		user_list = [item.strip() for item in user_list]

	# Read params literally
	else:
		user_list = [abox.user]
		if abox.name != None:
			name_list = [abox.name]
		else:
			name_list = user_list

	return user_list, name_list	

# fail_write func
# Writes out a failed instance line
def fail_write(name, user, abox):
	o_path = "%s/%s" % (abox.cwd, abox.output)
	with open(o_path, 'a') as o_file:
		o_file.write('<FAIL> %s:-:-:%s:-\n' % (name, user))

# std_write func
# Writes out a spun instance line
def std_write(sh_ret, inst, cur_time, abox):
	o_path = "%s/%s" % (abox.cwd, abox.output)
	with open(o_path, 'a') as o_file:
		o_file.write('<%s> %s:%s:%s:%s:%s\n' % (cur_time, inst.inst_name, inst.inst_id, inst.pub_ip, sh_ret[0], sh_ret[2]))

# main func
# Parses args, executes class functions
def main():
	# Parse Args
	arg_dict = args.parse()
	abox = argBox(arg_dict)
	
	# Initialize factory and output
	init_output(abox)
	factory = instFactory()

	# Print Header messages
	if arg_dict.asfile:
		print(args.multi_spin_head)
	else:
		print(args.sing_spin_head)
	print()

	# Construct lists for iteration
	user_list, name_list = gen_lists(arg_dict.asfile, abox)
	
	# Check list lengths
	if len(user_list) != len(name_list):
		print(args.length_error)
		exit(1)

	try:
		for idx in range(len(user_list)):
			# Skip Names that are already in existance
			if factory.check_exists(name_list[idx]):
				print('WARNING: [%s] already exists, instance not spun...' % name_list[idx])
				fail_write(name_list[idx], user_list[idx], abox)
			else:
				inst = factory.create_instance(name_list[idx], abox.cbox)
				cur_time = datetime.now().strftime(args.time_fmt)
				print("SPUN: <%s> Spun @ <%s> under <%s>" % (inst.inst_id, inst.pub_ip, inst.inst_name), end=" ")
				ret = inst.ws_user_setup(user_list[idx])
				print(' --- Setup Initiated @', inst.pub_ip)
				std_write(ret, inst, cur_time, abox)

	except Exception as err:
		print("%s: [%s]" % (args.create_error, err))
		exit(1)
main()
