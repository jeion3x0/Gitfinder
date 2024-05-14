#!/usr/bin/env python3

'''
 Developed by @jeion3x0

 Only for educational purposes!
'''

import argparse
import concurrent.futures
import urllib.request
import urllib.error
import sys
import ssl
import encodings.idna
from urllib.parse import urlparse

def findgitrepo(output_file, domain):
    domain = domain.strip()
    if not domain.startswith("http://") and not domain.startswith("https://"):
        domain = "http://" + domain
    paths_to_check = ['.git/HEAD', '.git/config', '.git/index']

    try:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_to_path = {executor.submit(check_url, domain, path): path for path in paths_to_check}
            for future in concurrent.futures.as_completed(future_to_path):
                path = future_to_path[future]
                try:
                    result = future.result()
                except Exception as exc:
                    result = False
                if result:
                    with open(output_file, 'a') as file_handle:
                        file_handle.write(f"{domain}\n")
                    print(f"[*] Found: {domain}")
                    break
    except (KeyboardInterrupt, SystemExit):
        raise

def check_url(domain, path):
    url = f"{domain}/{path}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ssl._create_unverified_context(), timeout=10) as response:
            if response.status == 200:
                # Ensure the final URL does not redirect
                final_url = response.geturl()
                parsed_final_url = urlparse(final_url)
                if parsed_final_url.path.rstrip('/') == f'/{path}':
                    return True
    except urllib.error.HTTPError:
        pass
    except urllib.error.URLError:
        pass
    except ConnectionResetError:
        pass
    except ValueError:
        pass
    return False

def read_file(filename):
    with open(filename) as file:
        return file.readlines()

def main():
    print("""
##################################
# Developed by @jeion3x0         #
#                                #
# Only for educational purposes! #
##################################
""")

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inputfile', default='input.txt', help='input file')
    parser.add_argument('-o', '--outputfile', default='output.txt', help='output file')
    args = parser.parse_args()

    domain_file = args.inputfile
    output_file = args.outputfile

    try:
        domains = read_file(domain_file)
    except FileNotFoundError as err:
        sys.exit(err)

    print("Scanning...")

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(lambda domain: findgitrepo(output_file, domain), domains)

    print("Finished")

if __name__ == '__main__':
    main()
