#!/usr/bin/env python3
"""
The purpose of this module is to import and store all of the data from
the external data files in one organized place for all modules in the project.
"""

from collections import defaultdict

###############################################################################
#       Initialization                                                        #
###############################################################################

# names of data files
COLOR_DATA_FILE = 'colors.dat'
KEYBIND_DATA_FILE = 'keybinds.dat'
DELTAS_DATA_FILE = 'deltas.dat'

colors = {}
try:
    with open(COLOR_DATA_FILE) as f:
        for line in f:
            if line[0] not in '#\n':
                color_name, color_value = line.split('=')
                color_name = color_name.strip()
                color_value = int(color_value.strip(),16)
                colors[color_name] = color_value
except ValueError:
    print('')
    # this functionality doesn't work yet obviously lol


keybinds = [{} for _ in range(8)]
try:
    with open(KEYBIND_DATA_FILE) as f:
        for line in f:
            if line[0] not in '#\n':
                event_name = line.split('=')[0].strip()
                keybind_values = line.split('=')[1]
                for binding in keybind_values.split(','):
                    modifier = 0
                    prefix = binding[:3]
                    if '+' in prefix:
                        prefix = prefix.replace('+','')
                        modifier += 1
                    if '!' in prefix:
                        prefix = prefix.replace('!','')
                        modifier += 2
                    if '^' in prefix:
                        prefix = prefix.replace('^','')
                        modifier += 4
                    binding = prefix + binding[3:]
                    keybinds[modifier][binding.strip()] = event_name
except:
    print('Error reading in keybinds.')

deltas = defaultdict(dict)
