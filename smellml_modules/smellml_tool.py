#! usr/bin/python3
from directoryStats import directoryStats as dirstat
import sys
import csv
import os

def getOutput(dirstatobj):
    """ This takes the relevant output and creates a dictionary """
    output_dict = {}
    output_dict["LinesNotInClasses"] = dirstatobj.getLinesNotInClasses()
    output_dict["LinesInClasses"] = dirstatobj.getLinesInClasses()
    output_dict["LinesInMethods"] = dirstatobj.getLinesInMethods()
    output_dict["NumMethods"] = dirstatobj.getNumMethods()
    output_dict["NumClasses"] = dirstatobj.getNumClasses()
    output_dict["NumCommentLines"] = dirstatobj.getNumCommentLines()
    output_dict["LinesPerMethod"] = dirstatobj.getLinesPerMethod()
    output_dict["LinesPerClass"] = dirstatobj.getLinesPerClass()
    output_dict["AvgNumParams"] = dirstatobj.getAvgNumParams()
    output_dict["NumNestedLoops"] = dirstatobj.getNumNestedLoops()
    output_dict["MutableParamsCount"] = dirstatobj.getMutableParamsCount()
    output_dict["NumEnumerateIssues"] = dirstatobj.getNumEnumerateIssues()

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
    print(sys.argv)
    if (len(sys.argv) < 3):
        print(HELP)
        exit(1)

    ## arguments
    directory_path = str(sys.argv[1])
    outpath = str(sys.argv[2])

    ## Object instantiation
    dirstat_obj = dirstat(directory_path)
    outdict = getOutput(dirstat_obj)
    saveDictToFile(outdict, outpath)


if __name__ == "__main__":
    main()
