#!/usr/bin/env python

import sys, os
import BitVector


def main(reference_hash, hash_after_alter):

    final_result = BitVector(size = 56)

    reference_hash = [int(i) for i in reference_hash]
    hash_after_alter = [int(i) for i in hash_after_alter]

    # print('reference hash : ', reference_hash)
    # print('after alt hash : ', hash_after_alter)

    reference_hash = BitVector(bitlist = reference_hash)
    hash_after_alter = BitVector(bitlist = hash_after_alter)

    print('reference hash : ', reference_hash)
    print('after alt hash : ', hash_after_alter)

    print('reference hash : ', reference_hash)
    print('after alt hash : ', hash_after_alter)

    for i in range(7):
        print(i)

        hash_after_alter = hash_after_alter << 4

        if i <= 5:
            # 4 bits by 4 bits
            reference_bits = reference_hash[i*4:(i+1)*4] + BitVector(intVal = 0, size=4)
            print(reference_bits)

        else:
            reference_bits = reference_hash[i*4:(i+2)*4] # Take the last byte in one shot

        temp = hash_after_alter[24:32] ^ reference_bits
        final_result[i*8:(i+1)*8] = temp

        print(temp)

        hash_after_alter[24:32] = reference_bits

    print('final : ', final_result)
    print('final str :', final_result.get_bitvector_in_ascii())



if __name__ == "__main__":

    # Check BitVector Version
    if BitVector.__version__ < '3.2':
        sys.exit("You need BitVector module of version 3.2 or higher" )
    from BitVector import *

    # Check arguments
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: %s  <the name of the file>\n" % sys.argv[0])
        sys.exit(1)

    # Start main program
    main(sys.argv[1], sys.argv[2])
