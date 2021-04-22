#! usr/bin/python3
from directoryStats import directoryStats as dirstat
import sys
import csv
import os

def getOutput(dirstatobj):
    """ This takes the relevant output and creates a dictionary """
    output_dict = {}
    output_dict["smellml_LinesNotInClasses"] = dirstatobj.getLinesNotInClasses()
    output_dict["smellml_LinesInClasses"] = dirstatobj.getLinesInClasses()
    output_dict["smellml_LinesInMethods"] = dirstatobj.getLinesInMethods()
    output_dict["smellml_NumMethods"] = dirstatobj.getNumMethods()
    output_dict["smellml_NumClasses"] = dirstatobj.getNumClasses()
    output_dict["smellml_NumCommentLines"] = dirstatobj.getNumCommentLines()
    output_dict["smellml_LinesPerMethod"] = dirstatobj.getLinesPerMethod()
    output_dict["smellml_LinesPerClass"] = dirstatobj.getLinesPerClass()
    output_dict["smellml_AvgNumParams"] = dirstatobj.getAvgNumParams()
    output_dict["smellml_NumNestedLoops"] = dirstatobj.getNumNestedLoops()
    output_dict["smellml_MutableParamsCount"] = dirstatobj.getMutableParamsCount()
    output_dict["smellml_NumEnumerateIssues"] = dirstatobj.getNumEnumerateIssues()

    return output_dict

def saveDictToFile(out_dict, outfilename):
    """
    this method saves a CSV based on the output dictionary
    """
    # write to a CSV
    with open(outfilename, 'a', newline='') as csvfile:
        fieldnames = out_dict.keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not (os.path.getsize(outfilename) > 0):
            writer.writeheader()
        writer.writerow(out_dict)

def printResults(out_dict):
    """
    this method prints the resulting output dictionary
    """
    print(','.join([str(i) for i in out_dict.keys()]))
    print(','.join([str(i) for i in out_dict.values()]))

HELP = """

Usage:
python3 smellml_tool.py <directory path> <outfile path>

Example:
python3 smellml_tool.py toolin/ toolin.txt

OUTPUT:
LinesNotInClasses,LinesInClasses,LinesInMethods,NumMethods,NumClasses,NumCommentLines,LinesPerMethod,LinesPerClass,AvgNumParams,NumNestedLoops,MutableParamsCount,NumEnumerateIssues
3086,50,357,118,22,188,3.0254237288135593,2.272727272727273,0.8305084745762712,15,0,0
"""
def main():
    """ This runs the smell ML parser """
    ## argument checker
    if (len(sys.argv) < 2):
        print(HELP)
        exit(1)

    ## arguments
    directory_path = str(sys.argv[1])
    #outpath = str(sys.argv[2])
    ## Object instantiation
    dirstat_obj = dirstat(directory_path)
    outdict = getOutput(dirstat_obj)
    #saveDictToFile(outdict, outpath)
    printResults(outdict)

if __name__ == "__main__":
    main()
