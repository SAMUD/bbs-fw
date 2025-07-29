# Responsible for writing the C header file.

class HeaderFile():
	def __init__(self, file_location):
		self.file = open(file_location, "w")
		self.write_line("#ifndef _FWCONFIG_H_")
		self.write_line("#define _FWCONFIG_H_", 1)
		self.write_line("")

	def write_line(self, line, indentation_level=0):
		self.file.write(f"{"  " * indentation_level}{line}\n")

	def write_define(self, key, value):
		self.write_line(f"#define {key} {value}", 1)

	def close_file(self):
		self.write_line("")
		self.write_line("#endif")
		self.file.close()
