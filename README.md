# vcd2tikztiming

converts ValueChangeDump-Files to tikz-timing-diagrams ( see https://sourceforge.net/projects/tikz-timing/ / https://ctan.org/pkg/tikz-timing for the latex-package)

needs:
 + python3
 + Verilog_VCD ( see https://pypi.org/project/Verilog_VCD/#files )
 + (optional) latexpand - if you want to use the tex-template (see later!)
 + a vcd-file (currently only digital signals will have a chance of working)
 + either a copy of vcd2tikztiming.py or a symlink named the same as your vcd-file in the same directory (extension .py)
 + (optional) a tex-template (again, same name, same directory, extension .tmp this time)
 + run the python file (for the example-directory: python siggen_tb.py)

creates:
 + a .dmp-file for every signal (basically a single line of tikz-timing-diagram data)
 + if a template was given the signals will be imported into the template (for me using input sadly did not work within tikztiming...) and the output will be saved as a .tex-file

parameters:
 + you can set starttime, stoptime and scale-factor from the symlink filename (see example directory)
   parameters will not be included in output-filename 
   you might want to use additional symlinks and directories in more compliacted cases

example:
![example time signal](https://github.com/ernstblecha/vcd2tikztiming/raw/master/example/siggen_tb.png)
