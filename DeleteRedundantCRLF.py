__author__ = 'navy'


import os
import sys
import codecs
def delCrlf(dirname):
    '''txt 文件中不适当的换行多出来CRLF（一句话还没完就换行了）, 导致在手机上看格式很差，这个脚本就是去掉这些多余的CRLF'''
    for filename in os.listdir(dirname):
        path = dirname + "/" + filename

        if os.path.isdir(path):
            delCrlf(path)
        else:
            # if not filename.endswith(".ori"):
            #     continue

            print("processing ", path)
            if filename.endswith(".ori"):
                oriPath = path;
                path = oriPath[0 : len(oriPath)-4]
            else:
                oriPath = dirname + "/" + filename + ".ori"
                os.rename(path, oriPath)
            fsrc = codecs.open(oriPath, 'r', fileEncode)
            fdst = codecs.open(path, "w", fileEncode)
            slineNext = ""
            lineNum = 0
            while True:
                lineNum = lineNum+1;
                # if (lineNum >= 20):
                #     break

                if (slineNext == ""):
                    sline = fsrc.readline()
                else:
                    sline = slineNext;

                if (sline == ""):
                    break
                else:
                    slineNext = fsrc.readline()
                    if (slineNext == ""):
                        fdst.write(sline) # 写最后一行，然后结束
                        break;
                    if (slineNext.startswith(" ") or slineNext.startswith("　")  or wholeLineAre(slineNext, '-') or wholeLineAre(sline, '-')): # 后面是一个新的段落或空行
                        fdst.write(sline)
                        # print(sline)or slineNext == "\r\n"
                    else: # 后面是同一行, 去掉\r\n, 和下一行接起来
                        fdst.write(sline[0 : len(sline) - 2]) # \r\n
                        # print(sline[0 : len(sline) - 2])
            #navy
            print("lineNum="+str(lineNum))

            fsrc.close()
            fdst.close()

def wholeLineAre(linestr, ch):
    if (linestr == "\r\n"):
        return False
    for c in linestr[0:len(linestr)-2]:
        if (c != ch):
            return False

    return True

fileEncode = 'GB18030'
if len(sys.argv) < 2:
    print("请指定目录的路径")
else:
    delCrlf(sys.argv[1])