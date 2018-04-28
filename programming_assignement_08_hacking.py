"""

### Hacking

Usage :

python programming_assignement_08_hacking.py [hash_of_original_msg] [hash_of_corrupted_msg]

**First arg :** Hash of the original message to create a collision with.
**Second arg :** Hash of the corrupted message you want to send.

The script generates a 58 bits string that is possible to add at the end of your corrupted message
(possible problem of encoding. Not every bytes of this string can be encoded in ASCII ...).
At this point, your new corrupted message has the same hash as the original message. We created a collision !

--------------------------------------------------------------------------------

Authors : Fleury Anthony, Schnaebele Marc
Date    : 28.04.2018

"""

#!/usr/bin/env python

import sys, os
import BitVector


def main(reference_hash, hash_after_alter):

    # The 56 bits string to add to the file to hack the hashing and create a collision
    final_result = BitVector(size = 56)

    # Hash we want to collision with
    reference_hash = [int(i) for i in reference_hash]
    # Hash obtained by hashing the file to which we want to add the generated string of bits to obtain the collision
    hash_after_alter = [int(i) for i in hash_after_alter]

    reference_hash = BitVector(bitlist = reference_hash)
    hash_after_alter = BitVector(bitlist = hash_after_alter)

    print('reference hash : ', reference_hash)
    print('after alt hash : ', hash_after_alter)

    # Loop 7 times to generates the 7 bytes to add at the end of the file to hack hashing
    for i in range(7):

        # HASHING STEP 1 : Circular left shift
        hash_after_alter = hash_after_alter << 4

        # The sixth first bytes are built by merge 4 bits of the reference hash and 4 zeros
        if i <= 5:
            # Build the byte to XOR with the hash by extracting the 4 leftest bits of the reference hash and concatening '0000'
            # We add '0000' because this part is lost at the next iterations, because the shit is only by 4 and not 8.
            reference_bits = reference_hash[i*4:(i+1)*4] + BitVector(intVal = 0, size=4)
            print(reference_bits)
        # The last byte takes directly the 8 last bits of the reference hash without adding '0000'
        else:
            # The last byte is created by extacting the last 8 bits in one time and there are no '0000' padded
            # We can do this in one step because this is the last iteration and the last 4 bits won't be overwritten
            reference_bits = reference_hash[i*4:(i+2)*4] # Take the last byte in one shot

        # XOR between the last 8 bits of the current hash and the 8 bits built previously =>  A xor B = C  <=> C xor B = A
        temp = hash_after_alter[24:32] ^ reference_bits
        # Append the output of the XOR to the final result (56 bits string)
        final_result[i*8:(i+1)*8] = temp

        print(temp)

        # HASHING STEP 2: Replace the 8 last bits of the current hash by the 8 ones built previoulsy
        hash_after_alter[24:32] = reference_bits

    # Display the final result in Binary
    print('final : ', final_result)
    # Display the final result in ASCII
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
