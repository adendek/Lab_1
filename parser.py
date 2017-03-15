#!/usr/bin/pyhon2.7.9

class LogParser:
	def parse_log (self, input_file, string_to_be_found):
		with open(input_file) as pl:
			for line in pl.readlines():
				if (string_to_be_found in line):
					print(line)

print("Log parser")
string = "PrChecker.Downs"
parser = LogParser()
print("baseline_BdJPsiKs_MagD")
parser.parse_log("baseline_BdJPsiKs_MagD.log", string)
print("DR_BdJPsiKs_MagD_1k")
parser.parse_log("DR_BdJPsiKs_MagD_1k.log", string)
print("DR_NE_BdJPsiKs_MagD")
parser.parse_log("DR_NE_BdJPsiKs_MagD.log", string)
print("DR_NE_BdJPsiKs_MagD_1k")
parser.parse_log("DR_NE_BdJPsiKs_MagD_1k.log", string)
