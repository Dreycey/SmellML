#! usr/bin/python3
import sys
from smellml_modules.abstract_sniffer import Abstract_Sniffer
from smellml_modules.flake8_sniffer import Flake8_Sniffer
from smellml_modules.pylint_sniffer import Pylint_Sniffer
from smellml_modules.bandit_sniffer import Bandit_Sniffer
from smellml_modules.radon_sniffer import Radon_Sniffer

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
        self.tool_list = [flake8_sniff, bandit_sniff, pylint_sniff, radon_sniff]

    def download_codebase(self, githubURL):
        """ given a URL, this downloads the directory """
        raise notImplimentedError

    def run_pipeline_simple(self, inputfile, outsuffix):
        """ simply runs each tool on an input file """
        for tool in self.tool_list:
            tool.run_command(inputfile, outsuffix)

#####
# SmellML control
#####
HELP = """

SmellML - A tool for evaluating machine learning code bases written in python.

Usage:
python <path to ML codebase>

Example:
python3 SmellML.py faceswap/
"""
# MAIN METHOD
def main():
    """ this controls the script for the SmellML pipeline. """

    # if args aren't supplied print help
    if (len(sys.argv) < 2):
        print(HELP)
        exit(1)


    # instantiate the pipeline.
    pipeline = Pipeline_Manager()
    pipeline.run_pipeline_simple("pysmell", "pysmell")


if __name__ == "__main__":
    main()
