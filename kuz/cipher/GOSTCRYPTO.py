import gostcrypto
import time
from PIL import Image
import binascii

#ey = os.urandom(32)
# MASTER_KEY = "8899aabbccddeeff0011223344556677fedcba98765432100123456789abcdef"
# key = binascii.unhexlify(MASTER_KEY)
# print(f"KEY IS {key}")


#ECB MODE
def ENC_ECB(img, key, cipher_path):
    start_time = time.time()
    key = binascii.unhexlify(key)
    cipher_obj = gostcrypto.gostcipher.new('kuznechik',
                                        key,
                                        gostcrypto.gostcipher.MODE_ECB,
                                        )

    img = Image.open(img).convert('RGB')
    byte_img = img.tobytes()
    cipher_byte = cipher_obj.encrypt(byte_img)
    cipher_byte = bytes(cipher_byte)
    en = Image.frombytes(img.mode, img.size, cipher_byte)
    en.save(cipher_path, format='PNG')
    print("--- %s seconds ---" % (time.time() - start_time))


def DEC_ECB(img, key, pathDec):
    start_time = time.time()
    key = binascii.unhexlify(key)
    cipher_obj = gostcrypto.gostcipher.new('kuznechik',
                                        key,
                                        gostcrypto.gostcipher.MODE_ECB,
                                        )

    img = Image.open(img).convert('RGB')
    byte_img = img.tobytes()
    cipher_byte = cipher_obj.decrypt(byte_img)
    cipher_byte += b'\x00\x00\x00'
    cipher_byte = bytes(cipher_byte)
    
    dec = Image.frombytes(img.mode, img.size, cipher_byte)
    #dec.save('DEC_ECB_MYRESULT.png', format='PNG')

    dec.save(pathDec, format='PNG')
    print("--- %s seconds ---" % (time.time() - start_time))

#CTR MODE
def ENC_CTR(img, key, cipher_path):
    start_time = time.time()
    key = binascii.unhexlify(key)
    init_vect = bytearray([
    0x12, 0x34, 0x56, 0x78, 0x90, 0xab, 0xce, 0xf0,
    ])

    cipher_obj = gostcrypto.gostcipher.new('kuznechik',
                                            key,
                                            gostcrypto.gostcipher.MODE_CTR,
                                            init_vect=init_vect)

    img = Image.open(img).convert('RGB')
    byte_img = img.tobytes()
    cipher_byte = cipher_obj.encrypt(byte_img)
    cipher_byte = bytes(cipher_byte)
    en = Image.frombytes(img.mode, img.size, cipher_byte)
    en.save(cipher_path, format='PNG')
    print("---CTR ENC IN %s seconds ---" % (time.time() - start_time))


def DEC_CTR(img, key,pathDec):
    start_time = time.time()
    key = binascii.unhexlify(key)
    init_vect = bytearray([
    0x12, 0x34, 0x56, 0x78, 0x90, 0xab, 0xce, 0xf0,
    ])

    cipher_obj = gostcrypto.gostcipher.new('kuznechik',
                                            key,
                                            gostcrypto.gostcipher.MODE_CTR,
                                            init_vect=init_vect)

    img = Image.open(img).convert('RGB')
    byte_img = img.tobytes()
    cipher_byte = cipher_obj.decrypt(byte_img)
    cipher_byte = bytes(cipher_byte)
    dec = Image.frombytes(img.mode, img.size, cipher_byte)
    dec.save(pathDec, format='PNG')
    print("---CTR DEC IN %s seconds ---" % (time.time() - start_time))