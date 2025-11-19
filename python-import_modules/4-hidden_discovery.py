#!/usr/bin/python3
import dis
import marshal
import types

if __name__ == "__main__":
    # Open the .pyc file
    with open("/tmp/hidden_4.pyc", "rb") as f:
        f.read(16)  # skip header
        code_obj = marshal.load(f)

    names = set()

    def collect_names(co):
        for name in co.co_names:
            if not name.startswith("__"):
                names.add(name)
        for const in co.co_consts:
            if isinstance(const, types.CodeType):
                collect_names(const)

    collect_names(code_obj)

    for name in sorted(names):
        print(name)
