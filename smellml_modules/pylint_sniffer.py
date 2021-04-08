#! usr/bin/python3
if (__name__ == "__main__"):
    from abstract_sniffer import Abstract_Sniffer
    import abc
else:
    from smellml_modules.abstract_sniffer import Abstract_Sniffer
    import abc

class Pylint_Sniffer(Abstract_Sniffer):
    CMD = str(f"pylint INFILE")
    sniffer_name = "pylint"
    def __init__(self):
        """ Pylint constructor """
        return None

    def get_sniffer_name(self):
        """ returns the name of the sniffer """
        return self.sniffer_name


if (__name__ == "__main__"):
    pylint_sniff = Pylint_Sniffer()
    pylint_sniff.parse_doc()
    pylint_sniff.run_command("pysmell/", "pylint_out")
