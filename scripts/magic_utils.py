import sys

def info(msg):
    print "[INFO] " + msg

def warn(msg):
    print "[WARN] " + msg

def abort(msg):
    print '[ERROR] ' + msg
    sys.exit(1)

def parse_linesep_file(fname):
    f = open(fname, 'r')
    res = []
    for x in f.readlines():
        x = x.strip()
        if x and not x.startswith('#'):
            res.append(x)
    f.close()
    return res
