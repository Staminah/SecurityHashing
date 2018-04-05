#!/usr/bin/env python

import sys, os
import BitVector

def hashing_function(pathfile):

    # Init hash value
    hash_val = BitVector(intVal = 0, size = 32)

    #print('hash value at start : ', hash_val)

    # Loop byte by byte
    with open(pathfile, 'r') as f:
        while 1:
            # Read next byte
            byte_read = f.read(1)
            print('byte read in ASCII :                               ', byte_read)

            # Stop if there's no byte left
            if not byte_read:
                break

            # BitVector from byte read
            byte_read = BitVector(textstring = byte_read)

            print('hash before shift : ', hash_val)
            # Circular shif left by 4 bits
            hash_val = hash_val << 4
            print('hash after shift :  ', hash_val)

            # XOR last byte of hash and byte read
            temp = hash_val[24:32] ^ byte_read
            print('byte in binary :                            ', byte_read)
            print('xor res :                                   ', temp)
            hash_val[24:32] = temp
            print('hash after xor :    ', hash_val)
            print('')

    return hash_val


def main(pathfolder):

    # File to save generated hashes
    hash_file = open('hashes.txt','w')

    # For each file inside the folder
    for filename in os.listdir(pathfolder):

        # Path to file
        path = os.path.join(pathfolder, filename)
        print(path)

        # If the file is a txt or python file
        if filename.endswith('.txt') or filename.endswith('.py'):
            # Run hashing function
            hash = hashing_function(path)
            print(hash)
            # Write hash to file
            hash_file.write(str(hash) + '\n')

    hash_file.close()


if __name__ == "__main__":

    # Check BitVector Version
    if BitVector.__version__ < '3.2':
        sys.exit("You need BitVector module of version 3.2 or higher" )
    from BitVector import *

    # Check arguments
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: %s  <the name of the folder>\n" % sys.argv[0])
        sys.exit(1)

    # Start main program
    main(sys.argv[1])
