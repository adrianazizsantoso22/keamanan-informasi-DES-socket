from desAlgo import DES

algo = DES()

pt="ADNAN ABDULLAH JUAN | 5025221155"
key="AMANAJAA"

pt_bin = algo.ascii_to_bin(pt)
# print(f"Plain Text: {pt_bin}")
key_bin = algo.ascii_to_bin(key)
rkb, rk = algo.generate_keys(key_bin)

print("Encryption")
cipher_text = algo.encrypt(pt_bin, rkb, rk)
print(f"Cipher Text: {algo.bin2hex(cipher_text)}")

print("Decryption")
rkb_rev = rkb[::-1]
rk_rev = rk[::-1]
decrypted_text = algo.decrypt(cipher_text, rkb_rev, rk_rev)
print(f"Decrypted Text: {algo.bin_to_ascii(decrypted_text)}")