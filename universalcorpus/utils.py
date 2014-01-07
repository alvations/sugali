# -*- coding: utf-8 -*-

def make_tarfile(output_filename, source_dir):
  """ Compress all files into a single tarfile. """
  import os, tarfile
  with tarfile.open(output_filename, "w") as tar:
    tar.add(source_dir, arcname=os.path.basename(source_dir))
    
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