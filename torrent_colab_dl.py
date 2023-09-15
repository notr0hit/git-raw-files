# @markdown **Torrent Downloader**</font>

import importlib, urllib.request, os
from IPython.display import clear_output
import time

if not os.path.exists("/root/.ipython/peeklab.py"):
    urllib.request.urlretrieve("https://raw.githubusercontent.com/ImPeekaboo/mytools/main/source/peeklab.py", "/root/.ipython/peeklab.py")

from peeklab import installLX

if importlib.util.find_spec("libtorrentx") is None:
    installLX()

magnet_link = input('paste your magnet link here:\n')
command = f"python -m libtorrentx -m \"{magnet_link}\""
clear_output()

!{command}

# take a break
time.sleep(5)

# copy most recent added file to drive
import glob
import os

if not os.path.exists("drive/MyDrive/"):
  print('Drive not mounted')
  exit()
  

list_of_files = glob.glob('/content/downloads/*') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)

!cp -a {latest_file}/. drive/MyDrive/