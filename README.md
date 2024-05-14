#Setup
pip3 install -r requirements.txt


#Git Finder

Git Finder is a Python script designed to identify exposed Git repositories on web servers. It scans a list of domain names and checks if they contain Git repositories by inspecting specific paths within the .git directory.
Features

    Parallel Execution: Utilizes multithreading for faster scanning of multiple domains simultaneously.
    HTTPS Support: Supports both HTTP and HTTPS URLs for scanning.
    Robust Error Handling: Handles various errors gracefully during the scanning process.
    Customizable Output: Allows specifying input and output files for flexibility.

#Usage

    Prepare Input File: Create a text file (input.txt by default) containing a list of domain names to scan. Each domain should be on a separate line.

    Run the Script: Open a terminal or command prompt, navigate to the directory containing the script, and execute the following command:

    css

> python3 git_finder.py -i input.txt -o output.txt

> python3 gitfinder.py -h
usage: gitfinder.py [-h] [-i INPUTFILE] [-o OUTPUTFILE] [-t THREADS]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUTFILE, --inputfile INPUTFILE
                        input file
  -o OUTPUTFILE, --outputfile OUTPUTFILE
                        output file
  -t THREADS, --threads THREADS
                        threads
