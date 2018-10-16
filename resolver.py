#!/usr/bin/env python
import os
banner = ("#############################\n"
          "## Simple ZoneID Resolver  ##\n"
          "##   By: Joel Aviad Ossi   ##\n"
          "#############################")
print(banner)
print('')
file = raw_input("PATH TO FILE: ")
print('\nRESOLVED: ')
string = os.system('more < ' + str(file) + ':Zone.Identifier')
raw_input('\nPRESS ANY KEY TO CONTINIUE')
