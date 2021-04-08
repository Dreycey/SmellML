#! usr/bin/python3
if (__name__ == "__main__"):
    from abstract_sniffer import Abstract_Sniffer
    import abc
else:
    from smellml_modules.abstract_sniffer import Abstract_Sniffer
    import abc

class Bandit_Sniffer(Abstract_Sniffer):
    CMD = str(f"bandit -r INFILE")
    sniffer_name = "bandit"
    def __init__(self):
        """ Class Constructor """
        return None

    def get_sniffer_name(self):
        """ returns the name of the sniffer """
        return self.sniffer_name


if (__name__ == "__main__"):
    bandit_sniff = Bandit_Sniffer()
    bandit_sniff.parse_doc()
    bandit_sniff.run_command("pysmell/", "bandit_out")
