from operator import mul
from operator import xor
from functools import reduce
from struct import unpack
from itertools import permutations
import os

PATH = 'big_wordlist.txt'
HASH = '3093'
def main():
    try :
        with open(create_path_in_script_directory(PATH)) as f:
            words = [y.replace('\n','') for y in f.readlines()]
        t_perms = len(words)*(len(words)-1)*(len(words)-2)
        #print hash('password')
        for x in permutations(words,3) :
            if hash_simplified(''.join(x)) == HASH :
                print ''.join(x)
    except Exception as e :
        print e
        input()


def hash_simplified(word):
    coeff   = (2**20)
    lng     = len(word)
    ct_1    = (2**(4*1<<2)-1)
    ct_2    = 3405691582L
    res     = 3735928559L
    counter = 0
    while counter < lng * 2 :
        exp_1   = (ct_1*(counter%2>0))
        exp_2   = (bytearray(word)[counter/2]*ct_2)
        exp_3   = (0xface*(counter/2))
        res=(res ^( exp_1 &( exp_2 ^ exp_3 ))) & ct_1
        counter += 1

    return format(res, 'x')

def hash(d):
	j=unpack
	y=bytes
	e=mul
	w=bytearray
	n=xor
	i=reduce
	f=map
	l=b'\x3e\x68\x68\x69'
	q=w(b'\x0a'*4)
	r=len
	d=w(d)
	h=b'\x00\x0b\x01\x01\x00\x14\x2a\x2d'
	h=i(e,j(l,h))
	l=b'\x3e\x49'
	k=w(b'\xc0\xf4\xb0\xb4')
	c=h^(h&0x0)
	q=i(e,j(l,y(w(f(n,k,q)))))
	k=r(d)
	y,j=h^c,h
	while (y>>(c^3735928571))<k:
		j=(j^(((2**(4*1<<2)-1)*(y%(c^3736977135)>0))&((d[y>>(c^3735928571)]*q)^(0xface*(y>>(c^3735928571))))))&(2**(4*1<<2)-1)
		y+=(h^(h-0xf+0x2*7))
	return format(j, 'x')

def create_path_in_script_directory(file_name):
    #Get the script file path
    script_file_path=os.path.realpath(__file__)

    #Get the directory path
    script_directory=os.path.dirname(script_file_path)

    #Make sure directory exists if nested
    directory =os.path.join(script_directory,os.path.dirname(file_name))
    if not os.path.exists(directory):
        os.makedirs(directory)

    #Build the file path using the file name and the directory path
    file_path=os.path.join(script_directory,file_name)

    #return
    return file_path


if __name__ == '__main__':
    main()
