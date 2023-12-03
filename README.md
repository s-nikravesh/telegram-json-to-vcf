# Telegram Contacts JSON to VCF
You can export your Telegram contacts via Telegram desktop app 
(Settings -> Advanced -> Export Telegram data).\
To convert the exported contacts (JSON file) to a VCF file and import it by 
your phone, use this script.

#### Usage
`python3 telegram_json_to_vcf.py json_file vcf_file`\
Arguments:\
`json_file`: Path to JSON file\
`vcf_file`: Path to VCF file

Example:\
`python3 telegram_json_to_vcf.py ./contacts.json .`

#### Notes
1. JSON file must have UTF-8 encoding.
2. You can specify the VCF file name (see the examples).
3. In case another file exists with the same name, then the VCF file is renamed.
