#! usr/bin/python3
if (__name__ == "__main__"):
    from abstract_sniffer import Abstract_Sniffer
    import abc
else:
    from smellml_modules.abstract_sniffer import Abstract_Sniffer
    import abc

class Radon_Sniffer(Abstract_Sniffer):
    CMD = str(f"radon cc INFILE -a -nc")
    sniffer_name = "radon"
    def __init__(self):
        """ Class Constructor """
        return None

    def get_sniffer_name(self):
        """ returns the name of the sniffer """
        return self.sniffer_name


if (__name__ == "__main__"):
    radon_sniff = Radon_Sniffer()
    radon_sniff.parse_doc()
    radon_sniff.run_command("pysmell/", "radon_out")
