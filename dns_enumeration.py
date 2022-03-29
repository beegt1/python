## To run, python3 ./dns_enumeration.py example.com 
## To run and export to a .txt file, python3 ./dns_enumeration.py example.com > example.txt
## if running the export way, be mindful it will not display results on the terminal - but in the file at the end.

import dns.resolver 
import sys


domain = sys.argv[1]
record_types = ['A', 'AAAA', 'NS', 'CNAME', 'MX', 'PTR', 'SOA', 'TXT']
for records in record_types:
    try:
        answers = dns.resolver.resolve(domain, records)
        print(f'\n{records} Records')
        print('-'*30)

        for server in answers:

            print(server.to_text())
    except dns.resolver.NoAnswer:
        pass
    except KeyboardInterrupt:
        quit()
        
