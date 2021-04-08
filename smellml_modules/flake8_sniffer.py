#! usr/bin/python3
if (__name__ == "__main__"):
    from abstract_sniffer import Abstract_Sniffer
    import abc
else:
    from smellml_modules.abstract_sniffer import Abstract_Sniffer
    import abc

class Flake8_Sniffer(Abstract_Sniffer):

    CMD = str(f"flake8 INFILE --ignore=E501")
    sniffer_name = "flake8"

    def __init__(self):
        """ Class Constructor """

        return None

    def get_sniffer_name(self):
        """ returns the name of the sniffer """
        return self.sniffer_name


if (__name__ == "__main__"):
    flake8_sniff = Flake8_Sniffer()
    flake8_sniff.parse_doc()
    print(flake8_sniff.getCMD())
    flake8_sniff.run_command("pysmell/", "flake8_out")
