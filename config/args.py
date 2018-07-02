# File: args.py
# Author: Harrison Inocencio
# Date: 06-27-18
# Purpose: Contains the argument parsing and constants for config/

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

import argparse

# Config contents
config_header = '# This is an automatically generated configuration file\n'

# ini contents
section_name = 'AWS'
image_id_key = 'ImageId'
inst_type_key = 'InstanceType'
key_name_key = 'KeyPairName'
sg_id_key = 'SecurityGroupId'

# Calls used for prompts
image_id_call = 'Image Identifier'
inst_type_call = 'Instance Type'
key_name_call = 'Key/Pair Name'
sg_id_call = 'Security Group Identifier'

# Error messages
key_interrupt = "\nExiting: Config File Unchanged..."
key_error = 'ERROR: INI Key Error Encountered...'

# Messages
new_query_msg = '[NEW CONFIG]'
complete_msg = 'Success!'
