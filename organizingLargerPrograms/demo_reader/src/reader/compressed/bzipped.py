import bz2
from ...reader.util import writer

opener = bz2.open

if __name__ == '__main__':
    writer.main(opener)
    # f = bz2.open(sys.argv[1], mode='wt')
    # f.write(' '.join(sys.argv[2:]))
    # f.close()
