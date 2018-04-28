
# SecurityHashing
Homework problems in security hashing field to understand and demonstrate how hashing works.

## Requirements

    pip install -r requirements.txt

## Files

 - `sha1_from_command_line.py` : Base example of SHA-1
 - `sha256_file_based.py` : Base example of SHA-256 (arg = file)
 - `sha256_from_command_line.py` : Base example of SHA-256 (arg = string)
 - `sha512_from_command_line.py` : **Exercise 09 - SHA-512 (arg = string)**
 - `programming_assignement_08_hashing.py` : **Exercise 08 - Hashing Shifted XOR (arg = directory)**
 - `programming_assignement_08_hashing_enhanced.py` : **Exercise 08 - Hashing Shifted XOR Enhanced with permutation and message lenght padding (arg = directory)**
 - `programming_assignement_08_collision_test.py` : **Exercise 08 - Script to test the files hashes.txt and detect if there are any collision**
 - `programming_assignement_08_hacking.py` : **Exercise 08 - Hacking Script to get a string to add at the end of a message to create a hash collision**
 -  `proof_hacking.txt` : Proof step by step that our scripts work. It had to be prooved by text because of the encoding problems. Some bytes of the generated string cannot be convert to ASCII.
 
## Usage
### Hashing & Hashing Advanced

    python programming_assignement_08_hashing.py [path_to_the_directory]

Creates a file named `hashes.txt` containing the output.  

The advanced script uses the same pattern. It is the same as the first hashing script but this time a **padding with the lenght of the message** is used and also a **permutation** is done.

### Collision testing

    python programming_assignement_08_collision_test.py [path_to_file_containing_the_hashes]
Uses the output file of the hashing script as input of the collision test file. 
The output is console only and displays a dictionnary containing all the hashes and their number of occurrences. An other array lists all the hashes that are duplicated.

### Hacking

    python programming_assignement_08_hacking.py [hash_of_original_msg] [hash_of_corrupted_msg]
**First arg :** Hash of the original message to create a collision with.
**Second arg :** Hash of the corrupted message you want to send. 

The script generates a 58 bits string that is possible to add at the end of your corrupted message (possible problem of encoding. Not every bytes of this string can be encoded in ASCII ...). At this point, your new corrupted message has the same hash as the original message. We created a collision !
    

