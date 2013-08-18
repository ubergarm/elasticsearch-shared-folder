#!/usr/bin/python

import os
from os import listdir
from os.path import isfile, join
import sys

os.environ['CLASSPATH'] = '/home/vagrant/tika-app-1.4.jar'
from jnius import autoclass

def main():
    if len(sys.argv) < 2:
        print "Usage: %s <directory to index into elasticsearch at localhost:9200>" % sys.argv[0]
        sys.exit(0)
    dname = sys.argv[1]
    files = [join(dname, f) for f in listdir(dname) if isfile(join(dname, f))]
    # files = [f for f in files if '.rtf' in f]

    ## Import the Java classes we are going to need
    Tika = autoclass('org.apache.tika.Tika')
    Metadata = autoclass('org.apache.tika.metadata.Metadata')
    FileInputStream = autoclass('java.io.FileInputStream')

    tika = Tika()
    meta = Metadata()

    ## use tika to extract text and metadata from all files in specified dir
    for filename in files:
        text = tika.parseToString(FileInputStream(filename), meta)
        print text
        for name in meta.names():
            print '{{ {0}: {1} }}'.format(name, meta.get(name))

if __name__ == '__main__':
    main()
