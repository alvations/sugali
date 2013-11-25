# -*- coding: utf-8 -*-

import omniglot, udhr

"""
This function will crawl and clean the multilingual phrases from Omniglot, 
and saves the resulting tarfile in '../data/omniglot/omniglot-phrases.tar'.

When parameter **testing=True**, a single page will be crawled and the tarfile
will be output to 'sugarlike/test/omniglot-phrases.tar'.

NOTE: the tarfile is already in the github, please avoid re-running
      this function. Because omniglot's firewall blocks excessive crawling.

P/S: REQUIRES INTERNET CONNECTION to crawl Omniglot!!!
"""
omniglot.get_phrases(testing=True)


"""
This function converts the UDHR files from various encodings into utf8,
and saves the resulting tarfile in '../data/udhr/udhr-utf8.tar'.

When parameter **testing=True**, the resulting tarfile will be output to 
'sugarlike/test/udhr-utf8.tar' instead of '../data/udhr/udhr-utf8.tar'.

NOTE: the tarfile is already in the github, please avoid re-running
      this function.

P/S: REQUIRES INTERNET CONNECTION to download the udhr.zip!!!
"""
udhr.convert_to_utf8(testing=True)

