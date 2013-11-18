# -*- coding: utf-8 -*-

import codecs, os, platform

def is_utf8(fname):
  """ 
  Check if a file is unicode readable 
  NOTE: This doesn't mean that the characters are in unicode !!!
  """
  try:
    codecs.open(fname,'r','utf8').read()
  except UnicodeDecodeError:
    return False
  return True

def what_the_encoding(fname):
  """
  Using libmagic to determine encoding of file.
  """
  try:
    import magic
  except:
    if platform.system() == "Linux":
      os.system('sudo apt-get install libmagic-dev')
      os.system('sudo pip install python-magic')
    else:
      err_message = "You must be using "+platform.system()+" OS\n" 
      err_message+= "No libmagic magicness for you "
      err_message+= "unless you install it manually =("
      raise OSError(err_message)
  return magic.Magic(mime_encoding=True).from_buffer(open(fname).read())