#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Ernst Blecha, https://github.com/ernstblecha/vcd2tikztiming"
__copyright__ = "Copyright 2018"
__credits__ = ["Sameer Gauria", "Florian Dietachmayr"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Ernst Blecha"
__email__ = "ernst.blecha@gmail.com"
__status__ = "Prototype"

import os
import sys
import pprint

from Verilog_VCD import parse_vcd,get_endtime,get_timescale,calc_mult
#Verilog_VCD.py version 1.11 taken from https://pypi.org/project/Verilog_VCD/#files

fn = os.path.basename(__file__)
fns = fn.split('.')

vcd = parse_vcd(fns[0]+'.vcd')

scale=1000
end = get_endtime()

data = {}
for d in vcd:
  u = vcd[d]['tv'][0]
  dv = []
  for v in vcd[d]['tv'][1:]:
    dv.append( ((v[0]-u[0])*1./scale, u[1]) )
    u = v
  dv.append( ((end-u[0])*1./scale, u[1]) )
  data = {**data, **dict([(vcd[d]['nets'][0]['name'],(vcd[d]['nets'][0]['size'],dv))])}

for d in data:
  s = d + " & ";
  for i in data[d][1]:
    if data[d][0] == "1":
      if i[0] == 0:
        s = s + "G"
      elif i[1] == "0":
        s = s + str(i[0]) + "L"
      elif i[1] == "1":
        s = s + str(i[0]) + "H"
      elif i[1] == "z" or i[1] == "Z":
        s = s + str(i[0]) + "Z"
      elif i[1] == "x" or i[1] == "X":
        s = s + str(i[0]) + "X"
      else:
        s = s + str(i[0]) + "U"
    else:
      s = s + str(i[0]) + "D{" + hex(int(i[1],2)) + "}"
  s = s + " \\\\"
  f = open(fns[0] + "_" + d + ".dmp", "w")
  f.write(s)
  f.close()

if os.path.isfile(fns[0] + ".tmp"):
  os.system("latexpand " + fns[0] + ".tmp > " + fns[0] + ".tex")
