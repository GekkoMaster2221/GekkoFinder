#!/usr/bin/env python3
# Displays an ASCII "Searching" header and an animated radar in the terminal.
# Save as a .py file and run in a terminal.

import os
import sys
import time
import math
import subprocess
import builtins
# Big ASCII "GekkoFinder" header
GEKKO_HEADER = [
    "   ▗▄▄▖▗▄▄▄▖▗▖ ▗▖▗▖ ▗▖ ▗▄▖             ▗▄▄▄▖ ▗▄▄▖▗▖ ▗▖ ▗▄▖", 
   "▐▌   ▐▌   ▐▌▗▞▘▐▌▗▞▘▐▌ ▐▌            ▐▌   ▐▌   ▐▌ ▐▌▐▌ ▐▌",
   "▐▌▝▜▌▐▛▀▀▘▐▛▚▖ ▐▛▚▖ ▐▌ ▐▌            ▐▛▀▀▘▐▌   ▐▛▀▜▌▐▌ ▐▌",
   "▝▚▄▞▘▐▙▄▄▖▐▌ ▐▌▐▌ ▐▌▝▚▄▞▘            ▐▙▄▄▖▝▚▄▄▖▐▌ ▐▌▝▚▄▞▘"       



]

SMALL_RADAR = [
    "        ,-.                                   ",
    "       / \  `.  __..-,O                      ",
    "      :   \ --''_..-'.'                    ",
    "      |    . .-' `. '.                      ",
    "      :     .     .`.'                      ",
    "       \     `.  /  ..                      ",
    "        \      `.   ' .                     ",
    "         `,       `.   \                    ",
    "        ,|,`.        `-.",
    ".||||  ``-...__..-`  
   -----------------"