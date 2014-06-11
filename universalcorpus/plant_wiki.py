import os

def install_wpdownload():
    os.system("sudo pip install progressbar wp-download")
    os.system("wget -O wpdl.cfg http://pastebin.com/raw.php?i=UbAyiGR9")
    return

def download_wiki(wiki_dir):
    os.system("wp-download -c wpdl.cfg "+wiki_dir)


def main(indir):
    install_wpdownload()
    download_wiki(indir)
    ## install wiki extractor.
    ## run wiki extractor.
    ## run cleaner.
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: python %s wiki_directory \n' % sys.argv[0])
        sys.exit(1)
    if os.path.exists(sys.argv[1]):
        main(sys.argv[1])