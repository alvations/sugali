# -*- coding: utf-8 -*-

import codecs

DATADIR = '../data'
DATASOURCE = ['wikpedia','omniglot','odin','udhr','crubadan']

# TODO: this returns the language code used for the individual data source.
def specific_code(datasource,iso):
  return iso # placeholder

def get_data(datasource=None, iso=None, datatype=None):
  languagecode = specific_code(datasource, iso)
  filename =  '/'.join([DATADIR,datasource,languagecode,"{}_{}.tar".format(languagecode,datatype)])
  print filename
  return codecs.open(filename,'r','utf8')

''' 
#Informal test
get_data(DATASOURCE[2],'deu','1gram')
'''