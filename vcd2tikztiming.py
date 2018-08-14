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
pp = pprint.PrettyPrinter(indent=4)

from Verilog_VCD import parse_vcd,get_endtime
#Verilog_VCD.py version 1.11 taken from https://pypi.org/project/Verilog_VCD/#files

fn = os.path.basename(__file__)
fns = fn.split('.')

vcd = parse_vcd(fns[0]+'.vcd')

scale = 1000
start = 0
end = get_endtime()

data = {}
for d in vcd:
  tv = [(t[0],t[1],i) for i,t in enumerate(vcd[d]['tv'])]

  results = [(t[0],t[1],t[2]) for t in tv if t[0] > start and t[0] < end]
  if results[0][0] > start and results[0][2] > 0:
    results.insert(0, (start, tv[results[0][2] - 1][1], tv[results[0][2] - 1][2]) )
  if results[-1][0] < end and results[-1][2] < tv[-1][2]:
    results.append( (end, tv[results[-1][2] + 1][1], tv[results[-1][2] + 1][2]) )

  u = results[0]
  dv = []
  for v in results[1:]:
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
  f = open(fns[0] + "_timecodes.tex", "w")
  f.write("\\providecommand\\timeStart{0}")
  f.write("\\renewcommand\\timeStart{" + str(start*1./scale) + "}");
  f.write("\\providecommand\\timeEnd{0}")
  f.write("\\renewcommand\\timeEnd{" + str(end*1./scale) + "}");
  f.close();
  os.system("latexpand " + fns[0] + ".tmp > " + fns[0] + ".tex")
