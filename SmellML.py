#! usr/bin/python3
import sys
import os
import csv
import shutil
import git
from smellml_modules.flake8_sniffer import Flake8_Sniffer
from smellml_modules.pylint_sniffer import Pylint_Sniffer
from smellml_modules.bandit_sniffer import Bandit_Sniffer
from smellml_modules.radon_sniffer import Radon_Sniffer
from smellml_modules.smellml_sniffer import Smellml_Sniffer
from tqdm import tqdm
import time

"""
This master script controls the flow for the SmellML pipeline.
Here the script uses some of the underlying classes for each of
the underlying tools and uses these to perform a code base
smell.

Usage:
python <path to ML codebase>

Example:
python3 SmellML.py faceswap/
"""

class Pipeline_Manager:

    def __init__(self):
        self.threads = 0
        flake8_sniff = Flake8_Sniffer()
        bandit_sniff = Bandit_Sniffer()
        pylint_sniff = Pylint_Sniffer()
        radon_sniff = Radon_Sniffer()
        smellml_sniff = Smellml_Sniffer()
        self.tool_list = [flake8_sniff, bandit_sniff, pylint_sniff, radon_sniff, smellml_sniff]
        self.headernames = ["tool name",
                            "flake8_issue_one",
                            "flake8_issue_two",
                            "flake8_issue_three",
                            "bandit_issue_one",
                            "bandit_issue_two",
                            "bandit_issue_three",
                            "bandit_sev_undefined",
                            "bandit_sev_low",
                            "bandit_sev_med",
                            "bandit_sev_high",
                            "bandit_conf_undefined",
                            "bandit_conf_low",
                            "bandit_conf_med",
                            "bandit_conf_high",
                            "radon_complexity",
                            "pylint_rating",
                            "bandit_lines",
                            "bandit_issue_list",
                            "flake8_issue_list",
                            "smellml_LinesNotInClasses",
                            "smellml_LinesInClasses",
                            "smellml_LinesInMethods",
                            "smellml_NumMethods",
                            "smellml_NumClasses",
                            "smellml_NumCommentLines",
                            "smellml_LinesPerMethod",
                            "smellml_LinesPerClass",
                            "smellml_AvgNumParams",
                            "smellml_NumNestedLoops",
                            "smellml_MutableParamsCount",
                            "smellml_NumEnumerateIssues",
                            "time_for_pipeline"]

    def download_codebase(self, githubURL):
        """ given a URL, this downloads the directory """
        raise notImplimentedError

    def run_pipeline_simple(self, inputfile, outprefix):
        """ simply runs each tool on an input file """
        # run each tool in the pipeline
        print(f'working on: {str(inputfile.strip("/"))}')
        tool_dict = {}
        start_time = time.perf_counter()

        for tool in self.tool_list:
            # use the tool
            outfile = tool.run_command(inputfile, outprefix)
            # parse the output, add to total csv.
            outdirectory = os.path.dirname(outfile)
            subdict = tool.parse_output(outfile, outdirectory)
            tool_dict.update(subdict)
            tool_dict.update({"tool name" : str(inputfile.strip("/"))})

        end_time = time.perf_counter()
        time_difference = abs(end_time - start_time)
        tool_dict.update({"time_for_pipeline" : time_difference})
        print(f'DONE! time used: {time_difference} seconds')

        return tool_dict

    def addDictionaryToCSV(self, outfilename, out_dict, tool_name):
        """ adds the output dictionary to a csv """

        # write to a CSV
        with open(outfilename, 'a', newline='') as csvfile:
            fieldnames = self.headernames
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not (os.path.getsize(outfilename) > 0):
                writer.writeheader()
            {"tool name" : tool_name}
            writer.writerow(out_dict)

    def parse_each_output(self, tool_obj, outcsv):
        """
        parses the output from each tool.
        """
        return 0


def runPipeline(pipeline_obj, input_directory, output_path):
    """ This method runs the pipeline """
    #print(f"The out path is: {output_path}")
    # create out dir
    outdirectory = os.path.dirname(output_path)
    if not os.path.exists(outdirectory):
        os.makedirs(outdirectory)
    # run pipelin
    pipe_out = pipeline_obj.run_pipeline_simple(input_directory, output_path)
    if (sys.argv[2] != "--runcsv"):
        #print("\n collating information into a csv \n")
        pipeline_obj.addDictionaryToCSV(output_path+"_total_out.csv",
                                    pipe_out,
                                    str(input_directory))
    else:
        pipeline_obj.addDictionaryToCSV("total_out.csv",
                                    pipe_out,
                                    str(input_directory))


def downloadrepo(name, giturl):
    """ downloads a github repository """
    os.system(f"git clone {giturl} {name} > /dev/null 2>&1")

def deleterepo(reponame):
    """ deletes a github repository """
    shutil.rmtree(reponame)

#####
# SmellML control
#####
HELP = """

SmellML - A tool for evaluating machine learning code bases written in python.

Usage:
python SmellML.py <path to ML codebase> <path to output prefix>

Example:
python3 SmellML.py faceswap/ outdir/outprefix

OR

Usage:
python SmellML.py <path git csv> --runcsv

Example:
python3 SmellML.py  my-software2.0-dataset-20210331.csv  --runcsv
"""
# MAIN METHOD
def main():
    """ this controls the script for the SmellML pipeline. """

    # if args aren't supplied print help
    if (len(sys.argv) < 3) or (len(sys.argv) > 3):
        print(HELP)
        exit(1)

    input_directory = sys.argv[1]
    output_path = sys.argv[2]
    # instantiate the pipeline.
    pipeline = Pipeline_Manager()
    if (len(sys.argv) == 3):
        if (output_path == "--runcsv"):
            with open(input_directory, newline='') as csvfile:
                total_lines = len(csvfile.readlines())-1
            with open(input_directory, newline='') as csvfile:
                 spamreader = csv.reader(csvfile, delimiter=",", quotechar='|')
                 rowcounter = 0
                 for row in tqdm(spamreader, total=total_lines):
                     if (rowcounter > 0):
                         giturl = row[1]
                         name = giturl.split("/")[-1].strip('"').replace('.git',"")
                         downloadrepo(name, giturl)
                         runPipeline(pipeline, name, f"smellML_{name}/{name}")
                         deleterepo(name)
                     rowcounter += 1
        else:
            runPipeline(pipeline, input_directory, output_path)
    else:
        print(HELP)
        exit(1)

if __name__ == "__main__":
    main()
