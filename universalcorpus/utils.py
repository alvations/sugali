# -*- coding: utf-8 -*-

def remove_tags(text):
  """ Removes <tags> in angled brackets from text. """
  import re
  tags = {i:" " for i in re.findall("(<[^>\n]*>)",text.strip())}
  no_tag_text = reduce(lambda x, kv:x.replace(*kv), tags.iteritems(), text)
  return " ".join(no_tag_text.split())

def remove_words_in_brackets(text):
  """ Remove words in parentheses, [in]:'foo (bar bar)' [out]:'foo'. """ 
  import re
  patterns = [r"\(.{1,}\)",r"[\(\)]"]
  for pat in patterns:
    text = re.sub(pat,'',text)
  return text

def make_tarfile(output_filename, source_dir):
  """ Compress all files into a single tarfile. """
  import os, tarfile
  with tarfile.open(output_filename, "w") as tar:
    tar.add(source_dir, arcname=os.path.basename(source_dir))

def read_tarfile(intarfile):
  """ Extracts a tarfile to a temp directory, then yield one file at a time. """
  import tempfile, tarfile, os
  TEMP_DIR = tempfile.mkdtemp()
  with tarfile.open(intarfile) as tf:
    for member in tf.getmembers():
      tf.extract(member, TEMP_DIR)
  
  for infile in os.listdir(TEMP_DIR):
    yield TEMP_DIR+'/'+infile