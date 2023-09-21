import sys
import time
import math
import base64
import numpy as np
from PIL import Image
from colorama import Fore,Style

def steg(byte_depth, InputImageFile, InputAudioFile, OutImage):
    t1=time.time()
    b64={'A': '000000', 'B': '000001', 'C': '000010', 'D': '000011', 'E': '000100', 'F': '000101', 'G': '000110', 'H': '000111', 'I': '001000', 'J': '001001', 'K': '001010', 'L': '001011', 'M': '001100', 'N': '001101', 'O': '001110', 'P': '001111', 'Q': '010000', 'R': '010001', 'S': '010010', 'T': '010011', 'U': '010100', 'V': '010101', 'W': '010110', 'X': '010111', 'Y': '011000', 'Z': '011001', 'a': '011010', 'b': '011011', 'c': '011100', 'd': '011101', 'e': '011110', 'f': '011111', 'g': '100000', 'h': '100001', 'i': '100010', 'j': '100011', 'k': '100100', 'l': '100101', 'm': '100110', 'n': '100111', 'o': '101000', 'p': '101001', 'q': '101010', 'r': '101011', 's': '101100', 't': '101101', 'u': '101110', 'v': '101111', 'w': '110000', 'x': '110001', 'y': '110010', 'z': '110011', '0': '110100', '1': '110101', '2': '110110', '3': '110111', '4': '111000', '5': '111001', '6': '111010', '7': '111011', '8': '111100', '9': '111101', '+': '111110', '/': '111111'}
    print(Fore.MAGENTA+Style.BRIGHT+"Byte_Depth: ", byte_depth, Fore.RESET)
    byte_depth = int(byte_depth)
    
    f = open(InputAudioFile, 'rb')
    b64_str = f.read()
    aud_data = base64.urlsafe_b64encode(b64_str)
    aud_b64 = aud_data.decode('ascii').replace("_","/").replace("-","+").replace('=','')
    encode_ar=np.array(list(aud_b64))
