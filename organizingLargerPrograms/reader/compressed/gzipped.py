import gzip
import sys

opener = gzip.open()
"""gzip behaves like a normal open, but gzip.open() decompresses the contents 
    of the file during reading while open() does not"""

if __name__ == '__main__':
    f = gzip.open(sys.argv[1], mode='wt', encoding='utf-8')
    f.write(' '.join(sys.argv[2:]))
    f.close()
