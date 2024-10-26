import socket
from desAlgo import DES

algo = DES()
key = "AMANAJAA"
print(f"Key: {key}")
key_bin = algo.ascii_to_bin(key)
rkb, rk = algo.generate_keys(key_bin)
rkb_rev = rkb[::-1]
rk_rev = rk[::-1]

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 1234))

while True:
    msg = input("B :")
    msg_bin = algo.ascii_to_bin(msg)
    encrypted_msg = algo.encrypt(msg_bin, rkb, rk)
    # client.send(algo.bin2hex(encrypted_msg).encode("utf-8"))
    client.send(encrypted_msg.encode("utf-8"))

    encrypted_res = client.recv(1024).decode("utf-8")
    if encrypted_res.lower() == 'quit':
        break
    else :
        decrypted_res = algo.bin_to_ascii(algo.decrypt(encrypted_res, rkb_rev, rk_rev))
        print("A :", decrypted_res)

client.close()
