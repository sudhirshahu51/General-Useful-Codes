def copytree(src, dst,list_hard,not_these,  symlinks=False, ignore=None):
    for item in os.listdir(src):
        if item not in list_hard:
            if item not in not_these:
                try:
                    s = os.path.join(src, item)
                    d = os.path.join(dst, item)
                    if os.path.isdir(s):
                        shutil.copytree(s, d, symlinks, ignore)
                    else:
                        shutil.copy2(s, d)
                    print("file copied")
                except BaseException as e:
                    print("Folder cannot be created")
                    print(e)

import os
import shutil
dst = r'D:'
src = r'E:'
list_hard = os.listdir("D:\E Drive")
not_these = ['Sherlock.Season.4.S04.1080p.10bit.BluRay.5.1.x265.HEVC-MZABI', 'The Butterfly Effect 2 [2006]', 'The Butterfly Effect [2004]', 'The Curious Case Of Benjamin Button (2008)', 'Torrent', 'TV series', 'ubantu', 'Ubantu_computer', 'virtualization storage']
copytree(src, dst,list_hard,not_these,  symlinks=False, ignore=None)
