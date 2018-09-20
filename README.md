# Project Title

DES toy, first coding assignment for CSCI 4230 Cryptography course at RPI.

## Overview

I implemented this in Python 2.7. This is a toy DES file transfer network. There are two clients (one sender and one receiver) and one server. First of all, the sender opens the file in the form of 64-bit "one-or-zero" binary string, such as "101010". Then he breaks the binary string into blocks, and each block contains a 64-bit-long string. Then each block is encrypted by DES, which was implemented in "des_supplementary.py". Then, for each block, DES generates another 64-bit encrypted string. The sender client sends all the encrypted blocks to the server. Next, server sends all the encrypted blocks to receiver client. Once upon receiving the encrypted blocks, receiver uses again DES algorithm in a reverse order to decrypt all the blocks. After that, receiver can concatenate those decrypted blocks into a whole string, which is the binary file string. Then receiver can use this string to restore the file.

## DES algorithm (des_supplementary.py)
I include all the details the algorithm needs in this file. 

### First: sub-keys
I create 16 sub-keys. Using the give 64-bit key, K, I used PC1 permutation to get the 56-bit string. Then I split this string into two halves, where each has 28 bits. For each half, do 16 iterations of left shifts. In each iteration, I use PC2 permutation to get one sub-key.


### Second: Encryption
Given message block M to be encrypted, first apply initial permutation(IP) on M. Then divide the initially permuted block into two halves, L0 and R0. Next, I use a round algorithm: 
	Ln = Rn-1
	Rn = Ln-1 XOR F(Rn-1, Kn), where Kn is the n-th sub-key.
Again, after 16 iterations we can get a result.

F(Rn-1, Kn) is a function described as follows:
	1) expand Rn-1, which is 32-bit, to a 48-bit block (implemented in expand(r))
	2) Then compute Kn XOR expand(Rn-1)
	3) Break it into 8 groups, each of size 6-bit
	4) For each group, there is a specific permutation methods (S-boxes)
	5) Concatenate the results of all the 8 group permutations
	6) Use P permutation to permutate the result
	7) return the new permutation P

After the 16 iterations, we can get R16 and L16. Concatenate R16 and L16 and apply final permutation FP to R16L16.

At last, the result of the final permutation is the cipher block. Both the cipher block and the text block are 64-bit long.

### Decryption
Decryption has almost the same procedures as encryption, except that the sub-keys in decryption should be used in reverse order

We just need to add this line of code if we want to decrypt a cipher block:
	subKeys = subKeys[::-1]



## Server (server.py)

This file starts a server to make the file transfer from one host(sender client) to another(receiver client). It uses the TCP protocol.

## Sender client (sender_client.py)

This file starts a sender client. After this client connects to the server, it will ask user to input the path of the file which he or she wants to encrypt and then send. 

"You are a sender. Please input your file directory to be encrypted and then sent to receiver:"

After knowing the file path, sender server will open the file and convert it into binary string form.

Then, the binary string will be encrypted with DES algorithm. After that, it will be sent to the server. 

## Receiver client (receiver_client.py)

This file starts a receiver client. It receives the cipher blocks from server. Then it decrypts all the cipher blocks. Then concatenate all the text ciphers into one binary string. Then, convert this binary string to the original file to restore the file in the receiver's host. What's more the encrypted cipher text(in hexadecimal) is also stored in a txt file in the current directory.



## How to test the network

First, start by running "server.py". 

Then open a new terminal tab, run "sender_client.py". After it requires you to enter the file path, you can just enter the test file in the repository, "smile.jpg".

Next, open another new terminal tab, run "receiver_client.py". You can just enter the new file name, such as "sm.jpg". Then the encrypted smile.jpg will be decrypted into sm.jpg and restored in the folder. Whats

