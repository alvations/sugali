# -*- coding: utf-8 -*-

DATADIR = '../data/'

DATASOURCE = ['wikpedia','omniglot','odin','udhr','crubadan']

# TODO: this returns the language code used for the individual data source.
def magic_iso_func(datasource,iso):
  pass

def get_data(datasource=None, iso=None, datatype=None):
  languagecode = magic_iso_func(datasource, iso)
  filename =  '/'.join([DATADIR,datasource,languagecode,datatype])
  return codecs.open(filename,'r','utf8')


get_data(DATASOURCE[2],'deu','1gram')