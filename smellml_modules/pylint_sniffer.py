#! usr/bin/python3
if (__name__ == "__main__"):
    from abstract_sniffer import Abstract_Sniffer
    import abc
    import os
else:
    from smellml_modules.abstract_sniffer import Abstract_Sniffer
    import abc
    import os

class Pylint_Sniffer(Abstract_Sniffer):
    CMD = str(f"pylint INFILE")
    sniffer_name = "pylint"
    def __init__(self):
        """ Pylint constructor """
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
           try:
               rating = float(file[-2].split(" ")[6].split("/")[0])
               out_dictionary["pylint_rating"] = rating
               f.close()
           except:
               print("something went wrong when parsing pylint")

        return out_dictionary

if (__name__ == "__main__"):
    pylint_sniff = Pylint_Sniffer()
    outfile = pylint_sniff.run_command("faceswap/tools/", "pylint_out2")
    outdirectory = os.path.dirname(outfile)
    pylint_sniff.parse_output(outfile, outdirectory)
