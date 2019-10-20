import urllib.request
import urllib3
import xmltodict
import warnings

from Bio import BiopythonWarning
from Bio.Seq import Seq, translate
from Bio.Alphabet import IUPAC

from .results import Results

warnings.simplefilter('ignore', BiopythonWarning)


def parse_uniprot(up_id):
    try:
        with urllib.request.urlopen("http://www.uniprot.org/uniprot/" + up_id + ".txt") as url:
            s = url.read()
        s = s.decode("utf-8")
        s = s.split("\n")
        sequence = ""
        description = ""

        description_found = False
        start = False
        for line in s:
            if line.startswith("//"):
                break
            elif not description_found:
                if line.startswith("DE") and "Full=" in line:
                    description_found = True
                    description = line[line.split("\n")[0].find("Full") + 5:]
            if start:
                sequence += line
            if line.startswith("SQ"):
                start = True
        sequence = sequence.replace(" ", "")
        if len(sequence) > 100:
            return Results(error=True, error_type="sequence is too long",
                           description=description, sequence=sequence)
        else:
            if len(sequence) >= 4:
                return Results(error=False, error_type="no error",
                               description=description, sequence=sequence)
            else:
                return Results(error=True, error_type="sequence is too short",
                               description=description, sequence=sequence)
    except:
        return Results(error=True, error_type="UniProtKB accession number not found", description="", sequence="")


def get_xml(id):
    url = "http://parts.igem.org/cgi/xml/part.cgi?part=" + id
    http = urllib3.PoolManager()

    response = http.request('GET', url)
    try:
        data = xmltodict.parse(response.data)
    except:
        print("Failed to parse xml from response (%s)" % traceback.format_exc())
    return data


def get_part_info(xml):
    part_list = xml["rsbpml"]["part_list"]
    if "ERROR" in part_list.keys():
        return Results(error=True, error_type="part not found", description=part_list["ERROR"], sequence="")
    elif "scar" in part_list.keys():
        return Results(error=True, error_type="part not found", description="", sequence="")
    else:
        if part_list["part"]["part_type"] == "Coding":
            nt_sequence = part_list["part"]["sequences"]["seq_data"].replace("\n", "")

            # remove start codon
            if nt_sequence.startswith("atg"):
                nt_sequence = Seq(nt_sequence[3:], IUPAC.unambiguous_dna)

            # translate to protein sequence
            prot_sequence = str(translate(nt_sequence))

            # remove characters after stop codon
            prot_sequence = prot_sequence.split("*")[0]

            # discard sequence that are too long for a CPP
            if len(prot_sequence) > 40:
                return Results(error=True, error_type="sequence is too long",
                               description=part_list["part"]["part_short_desc"], sequence=prot_sequence)
            else:  # all requirements for prediction passed
                if len(prot_sequence) >= 4:
                    return Results(error=False, error_type="none", description=part_list["part"]["part_short_desc"],
                                   sequence=prot_sequence)
                else:
                    return Results(error=True, error_type="sequence is too short",
                                   description=part_list["part"]["part_short_desc"], sequence=prot_sequence)
        else:
            return Results(error=True, error_type="non-coding sequence",
                           description=part_list["part"]["part_short_desc"], sequence="")


def get_registry_info(id):
    registry_entry = get_xml(id)
    return get_part_info(registry_entry)
