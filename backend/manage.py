#!/usr/bin/env python
# manage.py - entry point for Django administrative commands.

import os  # provides functions to interact with the OS
import sys  # allows access to command line arguments

# When executed directly, configure Django and hand off control to it
if __name__ == '__main__':
    # Set default settings module so Django knows where configuration lives
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsfeed.newsfeed.settings')
    # Import the command line utility
    from django.core.management import execute_from_command_line
    # Execute commands passed via the command line
    execute_from_command_line(sys.argv)
