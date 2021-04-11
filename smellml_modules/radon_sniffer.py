#! usr/bin/python3
if (__name__ == "__main__"):
    from abstract_sniffer import Abstract_Sniffer
    import abc
    import os
else:
    from smellml_modules.abstract_sniffer import Abstract_Sniffer
    import abc
    import os

class Radon_Sniffer(Abstract_Sniffer):
    CMD = str(f"radon cc INFILE -a -nc")
    sniffer_name = "radon"
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
              os.path.getsize(outputfile) > 600: # make sure exists and not empty.
           f = open(outputfile)
           file = f.readlines()
           complexity = file[-1].strip().split(" ")[-1].strip("(").strip(")")
           out_dictionary["radon_complexity"] = complexity
           f.close()

        return out_dictionary

if (__name__ == "__main__"):
    radon_sniff = Radon_Sniffer()
    radon_sniff.run_command("pysmell/", "radon_out")
    outfile = radon_sniff.run_command("pysmell/", "radon_out")
    outdirectory = os.path.dirname(outfile)
    radon_sniff.parse_output(outfile, outdirectory)
