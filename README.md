# vcd2tikztiming

converts ValueChangeDump-Files to tikz-timing-diagrams

needs:
 + python
 + Verilog_VCD ( see https://pypi.org/project/Verilog_VCD/#files )
 + (optional) latexpand - if you want to use the tex-template (see later!)
 + a vcd-file (currently only digital signals will have a chance of working)
 + either a copy of vcd2tikztiming.py or a symlink named the same as your vcd-file in the same directory (extension .py)
 + (optional) a tex-template (again, same name, same directory, extension .tmp this time)
 + run the python file (for the example-directory: python siggen_tb.py)

creates:
 + a .dmp-file for every signal
 + if a template was given the signals will be imported into the template (for me using input sadly did not work within tikztiming...)
