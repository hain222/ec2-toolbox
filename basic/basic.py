# File: basic.py
# Author: Harrison Inocencio
# Date: 06-20-18
# Purpose: Will preform some operation based off given parameters,
#		   <start, stop, terminate, reboot>

# Usage:

# Notes:
# 1.
# 2.
# 3.
# 4.
# 5.

# TODO:
# 1. Have it print help menu when no arguments given
# 2. Add an error message for an instance operation that is trying to be 
#	 performed on an instance in an invalid state
# 3.
# 4.
# 5.

# -------------------------------------------------------------------

import basic.args as args
from instFactory import instFactory

# main func
# Parse args, calls terminate function
def main():
	# Parse args
	arg_dict = args.parse()
	op = arg_dict.operation
	target_insts = arg_dict.instance
	
	# Init factory
	factory = instFactory()
	if len(target_insts) == 0:
		print('No target instances given...')
		exit(0)

	# Treat as id
	if arg_dict.id:
		inst_list = factory.get_by_id(target_insts)
	# Treat as name
	else:
		inst_list = factory.get_by_nametag(target_insts)

	# No matching instances
	if len(inst_list) == 0:
		print('No matching instances found...')
		exit(1)

	# Determine operation type
	if op == 'start':
		for inst in inst_list:
			if inst.state in args.valid_start_states:
				print('Start: id =', inst.inst_id)
				inst.start()
	elif op == 'stop':
		for inst in inst_list:
			if inst.state in args.valid_stop_states:
				print('Stop: id =', inst.inst_id)
				inst.stop()
	elif op == 'terminate':
		for inst in inst_list:
			if inst.state in args.valid_terminate_states:
				print('Terminate: id =', inst.inst_id)
				inst.terminate()
	elif op == 'reboot':
		for inst in inst_list:
			if inst.state in args.valid_reboot_states:
				print('Reboot: id =', inst.inst_id)
				inst.reboot()

main()
