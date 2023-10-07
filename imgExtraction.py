import sys
import time
import piexif
import base64
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def steg(inImg):
    t1=time.time()
    b64_rev={'000000': 'A', '000001': 'B', '000010': 'C', '000011': 'D', '000100': 'E', '000101': 'F', '000110': 'G', '000111': 'H', '001000': 'I', '001001': 'J', '001010': 'K', '001011': 'L', '001100': 'M', '001101': 'N', '001110': 'O', '001111': 'P', '010000': 'Q', '010001': 'R', '010010': 'S', '010011': 'T', '010100': 'U', '010101': 'V', '010110': 'W', '010111': 'X', '011000': 'Y', '011001': 'Z', '011010': 'a', '011011': 'b', '011100': 'c', '011101': 'd', '011110': 'e', '011111': 'f', '100000': 'g', '100001': 'h', '100010': 'i', '100011': 'j', '100100': 'k', '100101': 'l', '100110': 'm', '100111': 'n', '101000': 'o', '101001': 'p', '101010': 'q', '101011': 'r', '101100': 's', '101101': 't', '101110': 'u', '101111': 'v', '110000': 'w', '110001': 'x', '110010': 'y', '110011': 'z', '110100': '0', '110101': '1', '110110': '2', '110111': '3', '111000': '4', '111001': '5', '111010': '6', '111011': '7', '111100': '8', '111101': '9', '111110': '+', '111111': '/'}

    exif_dict = piexif.load(inImg)
    exif = exif_dict["Exif"].get(piexif.ExifIFD.UserComment)
    meta_stuff = eval(bytes(exif).decode("UTF-8"))
    meta_ar = list(meta_stuff)
    print(str(meta_ar))

    byteDepth=meta_ar[0]
    img = Image.open(inImg).convert('RGB')
    img_ar = np.array(img)
    select_px = img_ar[:int(meta_ar[1][0])+1, :int(meta_ar[1][1])+1]

    plt.imshow(select_px)
    plt.show()

    def bin_extract(x):
        bin_val = bin(int(x))[2:].zfill(8)
        bin_val = list(bin_val)
        bin_str = "".join(bin_val[-byteDepth:])
        return bin_str
    vfunc = np.vectorize(bin_extract)
    decoded_px = vfunc(select_px)

    print(decoded_px.flatten())
    decoded_bin=decoded_px.flatten().tolist()
    s="".join(decoded_bin)
    decoded_ar = np.array(list(s))
    decoded_ar = decoded_ar.reshape(int(len(decoded_ar)/6),6)
    print(decoded_ar)
    decoded_ar = np.array(list(map("".join, decoded_ar)))

    def bin_b64(x,d):
        return d[x]

    vfun = np.vectorize(bin_b64)
    encode_bin = vfun(decoded_ar, b64_rev)
    print(encode_bin)
    b64_str="".join(encode_bin).encode("ascii")

    print(len(b64_str))

    outFile = "outFile."+meta_ar[2].split(".")[-1]
    print(outFile)
    f = open(outFile, "wb")
    decoded_b64 = base64.b64decode(b64_str)
    f.write(decoded_b64)
    
    t2=time.time()
    print("\n\nExecTime",t2-t1)

steg(sys.argv[1])