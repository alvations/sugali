import os

def install_wpdownload(pwd):
    os.system("echo ", pwd, "sudo pip install progressbar wp-download")
    os.syste("wget -O wpdl.cfg http://pastebin.com/raw.php?i=UbAyiGR9")
    return

def download_wiki(wiki_dir):
    os.system("wp-download -c wpdl.cfg "+wiki_dir)


def main(pwd, indir):
    install_wpdownload(pwd)
    download_wiki(indir)
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: python %s sudo_password wiki_directory \n' % sys.argv[0])
        sys.exit(1)
    if os.path.exists(sys.argv[2]):
        main(sys.argv[1], sys.argv[2])