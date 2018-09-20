from des_supplementary import *
import base64
import time

start = time.time()

file_in_binary = convertFileToBinary('abc.txt')

encrypted_blocks, num_zeroes = encrypt(file_in_binary)

print "************* !ENCRYPTION OVER! *************"
mid = time.time()
print (mid - start) / 60.





total_decrypted = decrypt(encrypted_blocks, num_zeroes)

convertBinaryToFile(total_decrypted, 'aaaqqq.txt')

print "************* !DECRYPTION OVER! *************"

done = time.time()

print (done - start) / 60.
print (done - mid) / 60.
