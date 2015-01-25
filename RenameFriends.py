__author__ = 'navy'
import os
import re
import sys

def renamefile(dirname):
   '''把dirname目录下的文件改名.'''
   for filename in os.listdir(dirname):
      path = dirname + "/" + filename

      if os.path.isdir(path):
         renamefile(path)
      else:
         print("processing ", path)
         matchObj = re.match( r'.*全(.*)集.*?S(\d\d)(.*)', filename)
         if matchObj:
            # print(matchObj.group(1), "-", matchObj.group(2), "-", matchObj.group(3))
            os.rename(path, dirname + "/Friends.S" + matchObj.group(2) + "(" + matchObj.group(1) + ")" + matchObj.group(3))
         else:
            print("No match! filename is:", filename)

if len(sys.argv) < 2:
   print("请指定目录的路径")

renamefile(sys.argv[1])

