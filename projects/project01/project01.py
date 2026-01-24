#!/usr/bin/env python
"""

- scans VCF to find rare variants (AF_EXAC < 0.0001)
- extracts associated CLNDN disease names, excluding placeholders
- prints how many times each disease appears among rare variants

"""

from pprint import pprint

#VCF_FILE = "clinvar_20190923_short.vcf"

# parse_line reads a line and extract list of diseases if AF_EXAC is rare
def parse_line(line: str) -> list[str]:

    # ignore blank lines, metadata, header row
    if not line or line.startswith("#"):
        return []

    # remove trailing whitespace and split fields
    fields = line.rstrip("\n").split("\t")

    # only need INFO
    info_str = fields[7]  # INFO column has fixed position in VCF format (8th column)

    # INFO field extracted to dict
    info_dict = {}

    for item in info_str.split(";"):
        if not item:
            continue
        if "=" in item:
            k, v = item.split("=", 1)
            info_dict[k] = v
        else:
            info_dict[item] = None 
            # not in this VCF but if there's an item without = that isn't blank it will store it as [item]: None

    # if AF_EXAC is not present, skip the line
    if "AF_EXAC" not in info_dict or info_dict["AF_EXAC"] in (None, "", "."):
        return []
    
    # get AF_EXAC and make it a float
    af_exac = float(info_dict.get("AF_EXAC"))

    # if af_exac is not rare (>= 0.0001), return empty list
    if af_exac >= 0.0001:
        return []
    
    # get CLDN (string)
    clndn = info_dict.get("CLNDN").split("|")

    # make diseases list
    diseases = []

    for d in clndn:
        d = d.strip()

        if not d:
            continue
        if d.lower() in {"not_specified", "not_provided"}:
            continue

        diseases.append(d)

    return diseases

# read_file() reads a vcf file pass lines through parse_line()
def read_file(path: str) -> dict[str, int]:

    counts = {}

    with open(path, "r", encoding="utf-8") as f:

        for line in f:

            # parse_line returns a list of diseases (possibly empty)
            diseases = parse_line(line)

            # Update the running tally for each disease returned
            for disease in diseases:
                counts[disease] = counts.get(disease, 0) + 1

    return counts


if __name__ == "__main__":
    pprint(read_file("clinvar_20190923_short.vcf"))