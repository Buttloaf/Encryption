import os
import sys
import rnw
import cryption as ep
import check as ch

#Variables
###########################################


duplicates = ['a', 'e', 'i', 'o', 'u']

denic = sys.argv[1]


#algorythm
#############################################

if denic == "--decryption" or denic == "-d" or denic == "-D":
    
    inp = sys.argv[2]
    key = sys.argv[3]
    lfp = sys.argv[4]
    lfd = rnw.readfile(lfp)
    enc_dt = rnw.readfile(inp)
    decrypted = ep.decrypt(enc_dt, lfd, key)
    print(decrypted)

elif denic == "--encryption" or denic == "-e" or denic == "-E":

    output = sys.argv[2]
    lfp = sys.argv[3]
    lfd = rnw.readfile(lfp)
    des = sys.argv[4]

    inp = sys.argv[5]
    os.system("touch " + output)

    if des == "-t" or des == "-T" or des == "--text":
        
        numi = ep.TextToNum(inp, lfd, duplicates)

    elif des == "-f" or des == "-F" or des == "--file":

        numi = ep.FileToNum(rnw.readfile(inp), lfd, duplicates)
        
    key, encry = ep.Encrypt(numi)

    rnw.WriteFile(output, encry)

    print("your encryption key: ", key)