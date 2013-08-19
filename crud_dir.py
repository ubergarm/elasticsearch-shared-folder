#!/usr/bin/python

import os
from os import listdir
from os.path import isfile, join
import sys

from pyes import *

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

    ## connecto to local elasticsearch server with pyes
    conn = ES('127.0.0.1:9200')
    ## delete the old index
    try:
        conn.indices.delete_index('files-index')
    except:
        pass
    ## create a new index
    conn.indices.create_index('files-index')
    ## set up index mapping via dict
    mapping = {
            'filename': {
                'boost': 1.0,
                'index': 'not_analyzed',
                'store': 'yes',
                'type': 'string',
                },
            'parsedtext': {
                'boost': 1.0,
                'index': 'analyzed',
                'store': 'yes',
                'type': 'string',
                'term_vector' : 'with_positions_offsets'
                }
            }
    conn.indices.put_mapping('files-type', {'properties':mapping}, ['files-index'])

    ## use tika to extract text and metadata from all files in specified dir and index results in elasticsearch
    numFiles = len(files)
    curFile = 0
    for filename in files:
        curFile += 1
        print '------ PARSING {0} of {1}: {2} ------'.format(curFile, numFiles, filename)

        tika = Tika()
        meta = Metadata()

        try:
            text = tika.parseToString(FileInputStream(filename), meta)
        except Exception as E:
            # print E
            # print 'Error processing {0}'.format(filename)
            continue

        # for name in meta.names():
        #     print '{{ {0}: {1} }}'.format(name, meta.get(name))
        # print text
        # possible future fields to throw into elasticsearch:
        # title, Author, creator, date, plaintext, size

        print '------ INDEXING: {0} ------'.format(filename)
        print ''
        conn.index({'filename':'{0}'.format(filename), 'parsedtext':'{0}'.format(text)}, 'files-index', 'files-type', curFile)

        ## refresh index after each file is parsed so you don't have to wait
        conn.indices.refresh('files-index')

    ## DONE
    print 'ALL DONE!'
    print 'To see what you indexed, point your browser at:'
    print '\thttp://localhost:9200/files-index/_search?q=blah'
    print 'To use flask search bar, point your browser at:'
    print '\thttp://localhost:8080/search_text/blah'

if __name__ == '__main__':
    main()
