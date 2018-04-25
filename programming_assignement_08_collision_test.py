#!/usr/bin/env python

import sys, os

def main(filename):

    hash_list = []

    # Get hashes from file
    with open(filename) as f:
        hash_list = f.readlines()
    # Removes \n
    hash_list = [x.strip() for x in hash_list]

    seen = {} # Contains hashes met and number of time they are in the file
    dupes = [] # Contains hashes that are multiple times in the file

    # Iterates over hashes list and add first-time-seen hash in seen dictionary
    # add duplicated hashes in dupes list
    for hash in hash_list:
        if hash not in seen:
            seen[hash] = 1
        else:
            if seen[hash] == 1:
                dupes.append(hash)
            seen[hash] += 1

    # Display the results
    print('\nHashes entries : ', seen, '\n')
    print('Duplicated hashes : ', dupes)

if __name__ == "__main__":

    # Check arguments
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: %s  <the name of the file>\n" % sys.argv[0])
        sys.exit(1)

    # Start main program
    main(sys.argv[1])
