#! usr/bin/python3
if (__name__ == "__main__"):
    from abstract_sniffer import Abstract_Sniffer
    import abc
    import os
else:
    from smellml_modules.abstract_sniffer import Abstract_Sniffer
    import abc
    import os

class Bandit_Sniffer(Abstract_Sniffer):
    CMD = str(f"bandit -r INFILE")
    sniffer_name = "bandit"
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
        output_info = {}
        out_dictionary = {}
        if os.path.exists(outputfile) and \
              os.path.getsize(outputfile) > 600: # make sure exists and not empty.
           f = open(outputfile)
           file = f.readlines()
           line_counter = 0
           issue_counter = 0
           for line in file:
               if ">> Issue:" in line:
                   issue = file[line_counter].split(" ")[2]
                   severity = file[line_counter+1].strip().split(" ")[1]
                   confidence = file[line_counter+1].strip().split(" ")[5].strip("\n")
                   # add to "output_info" dictionary
                   output_info[issue_counter] = {}
                   output_info[issue_counter]["issue"] = issue
                   output_info[issue_counter]["severity"] = severity
                   output_info[issue_counter]["confidence"] = confidence

                   issue_counter += 1
               elif "Run metrics:" in line:
                   out_dictionary["bandit_sev_undefined"] = file[line_counter+2].split(" ")[1].strip("\n")
                   out_dictionary["bandit_sev_low"] = file[line_counter+3].split(" ")[1].strip("\n")
                   out_dictionary["bandit_sev_med"] = file[line_counter+4].split(" ")[1].strip("\n")
                   out_dictionary["bandit_sev_high"] = file[line_counter+5].split(" ")[1].strip("\n")
                   out_dictionary["bandit_conf_undefined"] = file[line_counter+7].split(" ")[1].strip("\n")
                   out_dictionary["bandit_conf_low"] = file[line_counter+8].split(" ")[1].strip("\n")
                   out_dictionary["bandit_conf_med"] = file[line_counter+9].split(" ")[1].strip("\n")
                   out_dictionary["bandit_conf_high"] = file[line_counter+10].split(" ")[1].strip("\n")

               line_counter += 1
           f.close()

           # parse output_info dictionary (make own method)
           issue_counter = {}
           for issue in output_info.keys():
               issue_topic = output_info[issue]["issue"]
               if issue_topic in issue_counter:
                   issue_counter[issue_topic] += 1
               else:
                   issue_counter[issue_topic] = 1

           sorted_top_issues = [k for k, v in sorted(issue_counter.items(),
                                                     key=lambda item: item[1],
                                                     reverse=True)]
           if (len(sorted_top_issues) > 2):
              out_dictionary["bandit_issue_one"] = sorted_top_issues[0]
              out_dictionary["bandit_issue_two"] = sorted_top_issues[1]
              out_dictionary["bandit_issue_three"] = sorted_top_issues[2]
           elif (len(sorted_top_issues) > 1):
              out_dictionary["bandit_issue_one"] = sorted_top_issues[0]
              out_dictionary["bandit_issue_two"] = sorted_top_issues[1]
           elif (len(sorted_top_issues) > 0):
              out_dictionary["bandit_issue_one"] = sorted_top_issues[0]

        else: #
            None

        return out_dictionary # empty if failed

if (__name__ == "__main__"):
    bandit_sniff = Bandit_Sniffer()
    outfile = bandit_sniff.run_command("pysmell/", "bandit_out_bandit.txt")
    outdirectory = os.path.dirname(outfile)
    bandit_sniff.parse_output(outfile, outdirectory)
