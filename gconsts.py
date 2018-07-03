# File: gconsts.py
# Author: Harrison Inocencio
# Date: 06-20-18
# Purpose: Contains global constants needed by all scripts to function

# Notes:
# 1.
# 2.
# 3.
# 4.
# 5.

# TODO:
# 1. Eventually remove pem path variable. Put in create args or config
# 2.
# 3.
# 4.
# 5.

# -------------------------------------------------------------------

# Config file path
config_path = 'config/config.ini'

# Pem path
pem_path = 'ngs_master_kp.pem'

# Setup path
setup_path = 'setup/setup.sh'

# Tags
name_key = 'Name'

# Boto3 consts
state_choices = ['pending', 'running', 'shutting-down', 'terminated', 'stopping', 'stopped'] # All valid states
general_states = ['pending', 'running', 'shutting-down', 'stopping', 'stopped'] # All states minus terminated.
rsc_type = 'instance'

# Error messages
subprocess_error = 'ERROR: Non-zero subprocess returncode'
