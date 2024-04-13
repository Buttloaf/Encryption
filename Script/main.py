import os
import sys
sys.path.insert(3, "modules/")
import rnw
import cryption as ep
import argparse

parser = argparse.ArgumentParser()

#Functions to catch errors
############################################

def filerrcatch(f):
    if os.path.exists(f) is False:
        parser.error("Your given file " + f + " does not exists. CHECK THE MANUAL(-h)!!")


def reqrrcatch(arg):
    if arg['mode'] in ('d', 'D'):
        reqs = ['key']
    else:
        if arg['file'] is None and arg['text'] is None:
            parser.error("Both text(-t) and file(-f) commands weren\'t used, CHECK THE MANUAL(-h)!!")
        elif arg['file'] is None:
            reqs = ['text']
        elif arg['text'] is None:
            reqs = arg['file']

    for r in reqs:
        if arg[r] is None:
            parser.error("Missing required arguement " + r)

#Parsing arguments
###########################################
parser = argparse.ArgumentParser()

parser.add_argument(
    '-m',
    '--mode',
    type=str,
    required=True,
    choices=['e', 'E', 'd', 'D'],
    help="To set the software to ENCRYPTION(e) or DECRYPTION(d) mode"
)

parser.add_argument(
    '-l',
    '--list',
    type=str,
    default='list.txt',
    help='To give your own or the default list to use for encryption, defaultly uses list.txt.'
)

parser.add_argument(
    '-t',
    '--text',
    action='store',
    type=str,
    help="To use text mode if not using file mode"
)

parser.add_argument(
    '-f',
    '--file',
    type=str,
    help="To use a file for encryption, can\'t be used at the same with text mode"
)

parser.add_argument(
    '-o',
    '--output',
    type=str,
    default='output',
    help='Name of the file that your encrypted data that will be saved in, defaults to name output'
)

parser.add_argument(
    '-i',
    '--input',
    type=str,
    default='output',
    help='To give the encrypted file as input for decryption, defaults to file output'
)

parser.add_argument(
    '-k',
    '--key',
    type=str,
    help='Your encryption key to decrypt your data'
)

#Variables
###########################################

args = parser.parse_args().__dict__

duplicates = ['a', 'e', 'i', 'o', 'u']
mode = args['mode']
lfp = args['list']
key = args['key']
crypted = args['input']
output = args['output']
gvn_text = args['text']
gvn_file = args['file']


#Checking for requirements & list file
#############################################

reqrrcatch(args)
filerrcatch(lfp)

#processing
#############################################

if mode in ('d', 'D'):
    lfd = rnw.readfile(lfp)
    filerrcatch(crypted)
    enc_dt = rnw.readfile(crypted)
    decrypted = ep.decrypt(enc_dt, lfd, key)
    print(decrypted)

else:
    lfd = rnw.readfile(lfp)

    os.system("touch " + output)

    if gvn_text is not None:

        numi = ep.TextToNum(gvn_text, lfd, duplicates)

    elif gvn_file is not None:

        numi = ep.FileToNum(rnw.readfile(gvn_text), lfd, duplicates)
        
    key, encry = ep.Encrypt(numi)

    rnw.WriteFile(output, encry)

    print("your encryption key: ", key)