#!/usr/bin/env python
"""

- scans VCF to find rare variants (AF_EXAC < 0.0001)
- extracts associated CLNDN disease names, excluding placeholders
- prints how many times each disease appears among rare variants

"""

from pprint import pprint

# parse_line reads a line and extract list of diseases if AF_EXAC is rare
def parse_line(line: str) -> list[str]:

    # ignore blank lines, metadata, header row
    if not line or line.startswith("#"):
        return []

    # remove trailing whitespace and split fields
    fields = line.rstrip("\n").split("\t")

    # only need INFO
    if len(fields)<8: 
        return [] # in case of malformed lines
    info_str = fields[7]  # INFO column has fixed position in VCF format (8th column)

    # INFO field extracted to dict
    info_dict : dict[str,str|None] = {}
    for item in info_str.split(";"):
        if not item:
            continue
        if "=" in item:
            k, v = item.split("=", 1)
            info_dict[k] = v
        else:
            info_dict[item] = None 
            # flags if present will be stored as keys with no value

    # get AF_EXAC -> af_exac if it exists
    af_exac = info_dict.get("AF_EXAC")
    if af_exac in (None,"","."):
        return []

    # float af_exac if possible
    try:
        af_exac = float(af_exac)
    except (TypeError,ValueError):
        return []

    # if af_exac is not rare (>= 0.0001), return empty list
    if af_exac >= 0.0001:
        return []
    
    # get CLDN (string) if it exists
    clndn = info_dict.get("CLNDN")
    if clndn in (None, "", "."):
        return []
    clndn = clndn.split("|")

    # make diseases list
    diseases : list[str] = []
    for d in clndn:
        d = d.strip()

        if not d:
            continue
        if d.lower() in {"not_specified", "not_provided"}:
            continue

        diseases.append(d)

    return diseases

# read_file() reads a vcf file and passes lines through parse_line()
def read_file(path: str) -> dict[str, int]:

    counts: dict[str, int] = {}
    try:

        with open(path, "r", encoding="utf-8") as f:

            for line in f:
                # parse_line() returns a list of diseases (possibly empty)
                diseases = parse_line(line)

                # update tally
                for disease in diseases:
                    # if key doesn't exist yet, default value is 0
                    counts[disease] = counts.get(disease, 0) + 1
    except OSError as e:
        raise SystemExit(f"Error reading file: {e}")

    return counts


if __name__ == "__main__":
    pprint(read_file("clinvar_20190923_short.vcf"))