import gzip

# from reader.util import writer
from ...reader.util import writer

opener = gzip.open
"""gzip behaves like a normal open, but gzip.open() decompresses the contents 
    of the file during reading while open() does not"""

if __name__ == '__main__':
    writer.main(opener)
