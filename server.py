import socket
from desAlgo import DES

algo = DES()
key = "AMANAJAA"
print(f"Key: {key}")
key_bin = algo.ascii_to_bin(key)
rkb, rk = algo.generate_keys(key_bin)
rkb_rev = rkb[::-1]
rk_rev = rk[::-1]

# --- BUAT SETUP KONEKSI
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 1234))
server.listen(5)
print("server started")
client, addr = server.accept()
print(f"connect to {addr}")

while True:
    msg = client.recv(1024).decode("utf-8")
    if msg.lower() == 'quit':
        break
    else :
        # msg_bin = algo.ascii_to_bin(msg)
        decrypted_msg = algo.bin_to_ascii(algo.decrypt(msg, rkb_rev, rk_rev))
        print("B :", decrypted_msg)
    
    res = input("A :")
    res_bin = algo.ascii_to_bin(res)
    encrypted_res = algo.encrypt(res_bin, rkb, rk)
    client.send(encrypted_res.encode("utf-8"))

client.close()
server.close()