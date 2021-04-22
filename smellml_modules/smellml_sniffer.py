#! usr/bin/python3
if (__name__ == "__main__"):
    from abstract_sniffer import Abstract_Sniffer
else:
    from smellml_modules.abstract_sniffer import Abstract_Sniffer
import abc
import os
import csv

class Smellml_Sniffer(Abstract_Sniffer):
    cwd = os.getcwd()
    CMD = str(f"python {cwd}/smellml_modules/smellml_tool.py INFILE")
    sniffer_name = "smellml"
    def __init__(self):
        """ Class Constructor """
        return None

    def get_sniffer_name(self):
        """ returns the name of the sniffer """
        return self.sniffer_name

    def parse_output(self, outputfile, directory):
        """
        parses the output file and adds to final.csv in directory.

        output:

            out_dictionary = {
                           "column x" : value (float or string)
                           "column y" : value (float or string)
                           ...
                           "column n" : value (float or string)
                          }
            OR

            out_dictionary = {} if no outfile or if empty
        """
        out_dictionary = {}
        if os.path.exists(outputfile) and \
              os.path.getsize(outputfile) > 0: # make sure exists and not empty.
           with open(outputfile, newline='') as csvfile:
               reader = csv.DictReader(csvfile)
               for row in reader:
                   out_dictionary = dict(row)
        return out_dictionary

if (__name__ == "__main__"):
    smellml_sniff = Smellml_Sniffer()
    outfile = smellml_sniff.run_command("GoogleScraper/", "smellml_out")
    outdirectory = os.path.dirname(outfile)
    smellml_sniff.parse_output(outfile, outdirectory)
