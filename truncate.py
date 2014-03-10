import re
import sys
filename = sys.argv[-1]
gcode = open(filename)
data = gcode.read()

def replace(match):
	match = match.group(2)
	return "." + match[0:4]

pattern = re.compile(r"([.])([0-9]+)")
output = re.sub(pattern, replace, data)
new_filename = filename[:-3] + '-truncated.nc'
file = open(new_filename, "w")
file.write("(Modified by metric-gcode-truncator. Intended for use in absolute mode. Incremental mode may cause errors.)")
file.write(output)
file.close()
gcode.close()
