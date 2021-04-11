#! usr/bin/python3
if (__name__ == "__main__"):
    from abstract_sniffer import Abstract_Sniffer
    import abc
    import os
else:
    from smellml_modules.abstract_sniffer import Abstract_Sniffer
    import abc
    import os

class Flake8_Sniffer(Abstract_Sniffer):

    CMD = str(f"flake8 INFILE --ignore=E501")
    sniffer_name = "flake8"

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

           # count issues
           issue_counter = {}
           for line in file:
               issue = line.strip("\n").split(" ")[1:]
               issue = " ".join(issue)
               if issue in issue_counter:
                   issue_counter[issue] += 1
               else:
                   issue_counter[issue] = 1
           f.close()
           sorted_top_issues = [k for k, v in sorted(issue_counter.items(),
                                                 key=lambda item: item[1],
                                                 reverse=True)]
           if (len(sorted_top_issues) > 2):
               out_dictionary["flake8_issue_one"] = sorted_top_issues[0]
               out_dictionary["flake8_issue_two"] = sorted_top_issues[1]
               out_dictionary["flake8_issue_three"] = sorted_top_issues[2]
           elif (len(sorted_top_issues) > 1):
               out_dictionary["flake8_issue_one"] = sorted_top_issues[0]
               out_dictionary["flake8_issue_two"] = sorted_top_issues[1]
           elif (len(sorted_top_issues) > 0):
               out_dictionary["flake8_issue_one"] = sorted_top_issues[0]


        return out_dictionary

if (__name__ == "__main__"):
    flake8_sniff = Flake8_Sniffer()
    print(flake8_sniff.getCMD())
    outfile = flake8_sniff.run_command("pysmell/", "flake8_out")
    outdirectory = os.path.dirname(outfile)
    flake8_sniff.parse_output(outfile, outdirectory)
