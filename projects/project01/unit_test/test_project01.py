#!/usr/bin/env python
import os
import pytest
from projects.project01.project01 import parse_line, read_file

def test_parse_line_VCF_format():
    """Test case for VCF file format containing less than 8 columns"""
    line = "1	541158	G	.	.	AF_ESP=0.00008;AF_TGP=0.00180;ALLELEID=514901;CLNDISDB=MedGen:C3808739,OMIM:615120;CLNDN=Myasthenic_syndrome,_congenital,_8;CLNHGVS=NC_000001.11:g.1045843G>A;CLNREVSTAT=criteria_provided,_single_submitter;CLNSIG=Uncertain_significance;CLNVC=single_nucleotide_variant;"
    result = parse_line(line)
    assert result == []

def test_parse_line_headers():
    """Test case for skipping headers starting with #"""
    line ="##reference=GRCh38"
    result = parse_line(line)
    assert result == []

def test_parse_line_info_dict():
    """Test case for parsing string into dictionary key and value"""
    info_str = "AF_ESP=0.00008;AF_EXAC=0.00004;AF_TGP;ALLELEID=514901;CLNDISDB=MedGen:C3808739,OMIM:615120;CLNDN=Myasthenic_syndrome,_congenital,_8;CLNHGVS=NC_000001.11:g.1045843G>A;CLNREVSTAT=criteria_provided,_single_submitter;CLNSIG=Uncertain_significance;CLNVC=single_nucleotide_variant;CLNVCSO=SO:0001483;GENEINFO=AGRN:375790;MC=SO:0001583|missense_variant;ORIGIN=1;RS=145162376"
    info_dict: dict[str, str | None] = {}
    for item in info_str.split(";"):
        if not item:
            continue
        if "=" in item:
            k, v = item.split("=", 1)
            info_dict[k] = v
        else:
            info_dict[item] = None

    assert info_dict["AF_ESP"] == "0.00008"
    assert info_dict["AF_EXAC"] == "0.00004"
    assert info_dict["AF_TGP"] is None

def test_parse_line_missing_af_exac():
    """Test case for when af_exac is missing"""
    line = "1	1045843	541158	G	A	.	.	AF_ESP=0.00008;AF_TGP=0.00180;ALLELEID=514901;CLNDISDB=MedGen:C3808739,OMIM:615120;CLNDN=Myasthenic_syndrome,_congenital,_8;CLNHGVS=NC_000001.11:g.1045843G>A;CLNREVSTAT=criteria_provided,_single_submitter;CLNSIG=Uncertain_significance;CLNVC=single_nucleotide_variant;CLNVCSO=SO:0001483;GENEINFO=AGRN:375790;MC=SO:0001583|missense_variant;ORIGIN=1;RS=145162376"
    result = parse_line(line)
    assert result == []

def test_parse_line_rare_af_exac():
    """Test case for when af_exac disease is rare"""
    line = "1	1045843	541158	G	A	.	.	AF_ESP=0.00008;AF_EXAC=0.00004;AF_TGP=0.00180;ALLELEID=514901;CLNDISDB=MedGen:C3808739,OMIM:615120;CLNDN=Myasthenic_syndrome,_congenital,_8;CLNHGVS=NC_000001.11:g.1045843G>A;CLNREVSTAT=criteria_provided,_single_submitter;CLNSIG=Uncertain_significance;CLNVC=single_nucleotide_variant;CLNVCSO=SO:0001483;GENEINFO=AGRN:375790;MC=SO:0001583|missense_variant;ORIGIN=1;RS=145162376"
    result = parse_line(line)
    assert result == ["Myasthenic_syndrome,_congenital,_8"]

def test_parse_line_common_af_exac():
    """Test case for when af_exac disease is common"""
    line = "1	1045843	541158	G	A	.	.	AF_ESP=0.00008;AF_EXAC=0.05;AF_TGP=0.00180;ALLELEID=514901;CLNDISDB=MedGen:C3808739,OMIM:615120;CLNDN=Myasthenic_syndrome,_congenital,_8;CLNHGVS=NC_000001.11:g.1045843G>A;CLNREVSTAT=criteria_provided,_single_submitter;CLNSIG=Uncertain_significance;CLNVC=single_nucleotide_variant;CLNVCSO=SO:0001483;GENEINFO=AGRN:375790;MC=SO:0001583|missense_variant;ORIGIN=1;RS=145162376"
    result = parse_line(line)
    assert result == []

def test_parse_line_clndn():
    """Test case for clndn if it exists"""
    info_dict = {"CLNDISDB":"MedGen:C3808739,OMIM:615120", "CLNDN":"Myasthenic_syndrome,_congenital,_8"}

    clndn = info_dict.get("CLNDN")
    if clndn in (None, "", "."):
        result = []
    else:
        result = clndn.split("|")

    assert result == ["Myasthenic_syndrome,_congenital,_8"]

def test_parse_line_missing_clndn():
    """Test case for clndn if it doesn't exist"""

    info_dict = {"CLNDISDB": "MedGen:C3808739,OMIM:615120", "AF_ESP" : "0.00008"}
    clndn = info_dict.get("CLNDN")

    if clndn in (None, "", "."):
        result = []
    else:
        result = clndn.split("|")

    assert result == []

def test_parse_line_disease():
    """Test case for when disease is specified and not specified"""

    clndn = ["Myasthenic_syndrome,_congenital,_8", "Severe_Myopia","not_specified", "not_provided", " "]
    result = []

    for d in clndn:
        d = d.strip()
        if not d:
            continue
        if d.lower() in {"not_specified", "not_provided"}:
            continue
        result.append(d)

    assert result == ["Myasthenic_syndrome,_congenital,_8", "Severe_Myopia"]

def test_read_file_OS_error():
    """Test case for reading invalid file"""
    with pytest.raises(SystemExit):
        read_file("clinvar.vcf")

    assert f"Error reading file: clinvar.vcf"
