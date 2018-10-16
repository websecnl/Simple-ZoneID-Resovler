#!/usr/bin/env python
import os
banner = ("#############################\n"
          "## Simple ZoneID Resolver  ##\n"
          "##   By: Joel Aviad Ossi   ##\n"
          "#############################")
print(banner)
print('')
file = raw_input("PATH TO FILE: ")
print os.system('more < ' + str(file) + ':Zone.Identifier')
print('')
raw_input('PRESS ANY KEY TO CONTINIUE')
