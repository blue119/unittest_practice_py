from glob import glob

def calc_factory(calc = "null"):
    """docstring for calc_factory"""

    if not glob("calc/%s.py" % calc):
        calc = "null"

    mod_path = "calc.%s" % calc
    mod = __import__(mod_path)
    return getattr(mod, calc)

