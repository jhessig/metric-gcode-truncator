metric-gcode-truncator

This program modifies metric MakerCam generated GCode so as to be usable with grbl CNC firmware. When MakerCam generates GCode in metric mode, the coordinates it outputs are unusable in grbl due to too many decimal places. This program reduces the coordinates to four decimal places, making it usable with grbl.

To use, from the command line, go to the program directory and enter:

python truncate.py ~/filepath/filename.nc

The new file will appear in the file directory as filename-truncated.nc

License
---------------

    metric-gcode-truncator - Modify metric MakerCam Gcode for use with grbl CNC
    Copyright (C) 2013  Jeremy Hessig

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.


