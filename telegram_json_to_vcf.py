import json
import os
import re


# vCard template
def vcf(fname, lname, cell):
    cell = cell.replace(" ", "")

    vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{fname} {lname}
N:{lname};{fname};;;
TEL;TYPE=CELL:{cell}
END:VCARD
"""

    return vcard


# Ask if the user wants to add the contact to vcf file.
# If add_all is True, then it does not ask the user.
def ask(vcard, add_all=False):
    if add_all:
        return True

    while True:
        is_okay = input(f"\n\nIs it okay?:\n\n{vcard}\n\n[Y, n]>>> ")
        if is_okay.lower() in ["", "y", "yes"]:
            return True
        elif is_okay.lower() in ["n", "no"]:
            return False
        else:
            continue


json_file = input("JSON path>>> ")
vcf_file = input("VCF path>>> ")
add_all = input("""Do you want to add all of the contacts to vcf file?
"Yes" to add all, "No" to add one by one>>> """)

if not vcf_file:
    working_dir = os.getcwd()
    vcf_file = working_dir + "Contacts.vcf"


# Check if the entered vcf_file is a directory or a file.
if os.path.isdir(vcf_file):
    print(f"\n{vcf_file} is a directory! 'Contacts.vcf' is created in it.")
    if os.name == "posix" and (not vcf_file.endswith("/")):
        vcf_file += "/"
    if os.name == "nt" and (not vcf_file.endswith("\\")):
        vcf_file += "\\"
    vcf_file += "Contacts.vcf"


# Check if the entered vcf_file exists.
# If the file already exists, then the file is renamed.
if os.path.isfile(vcf_file):
    pattern = re.compile(
        r"(?P<path>^([A-Z]:\\)?(\.*[\\/])*(.+[\\/])*)(?P<name>.+\.?.+)"
        )
    match = pattern.search(vcf_file)
    vcf_fname = match.group("name")
    vcf_fpath = match.group("path")

    # Trying to extract file name and its extension.
    try:
        file_name, extension = vcf_fname.rsplit(".")
    # If the file does not have an extension the it is set to "".
    except ValueError:
        file_name = vcf_fname
        extension = ""
    finally:
        new_file_name = file_name + "_new"

    print(f"\n{vcf_fname} already exists. Renaming it to {new_file_name}")
    vcf_file = vcf_fpath + new_file_name + extension


try:
    cts = json.load(open(json_file))
    cts = cts["contacts"]["list"]
except Exception as err:
    raise RuntimeError("An unexpected error happend!") from err


with open(vcf_file, "w") as f:
    for ct in cts:
        fname = ct["first_name"]
        lname = ct["last_name"]
        cell = ct["phone_number"]
        vcard = vcf(fname, lname, cell)

        is_okay = ask(vcard, add_all)
        if is_okay:
            f.write(vcard)
        else:
            continue
