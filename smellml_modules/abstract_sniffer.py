#! usr/bin/python3
import abc
from abc import ABC, abstractmethod, abstractproperty
import subprocess
import os

class Abstract_Sniffer(ABC):

    def __init__(self):
        self.outdir = str()

    @property
    @abstractmethod
    def CMD(self):
        pass

    @property
    @abstractmethod
    def sniffer_name(self):
        pass

    def set_outdir(self, new_outdir):
        """ set a new out directory """
        self.outdir = new_outdir

    def get_outdir(self):
        """ returns string of outdir """
        return self.outdir

    def getCMD(self):
        """ returns the CMD """
        return self.CMD

    def run_command(self, infilepath, outdir):
        """ runs the command for the program """
        full_cmd = self.CMD.split("INFILE")[0] + infilepath + self.CMD.split("INFILE")[1]
        FNULL = open(os.devnull, 'w')
        subprocess.call(f"{full_cmd} > {outdir}_{self.sniffer_name}.txt",shell=True,stdout=FNULL,stderr=subprocess.STDOUT)
        return f"{outdir}_{self.sniffer_name}.txt"

    @abstractmethod
    def parse_output(self, outputfile, directory):
        pass
