# python
just uploading scripts I make along the way

> DNS enumeration script
Listing every record of a Domain you enter :)
The array of record types include:
'A', 'AAAA', 'NS', 'CNAME', 'MX', 'PTR', 'SOA', 'TXT'

This script will require you to enter a domain name after the executable file.
    For example: python3 ./dns_enumeration.py example.com 

A way I like to export it only to a .txt file is like;
    python3 ./dns_enumeration.py example.com > example.txt
