#coding=utf-8
#this script is just for mac os
#python 2.7
#此脚本用于解决mac系统下 中文txt文档出现乱码的状况，在脚本的同目录下
#将乱码的文件都放进去，在终端执行此脚本
#这个脚本一个bug都没有 一遍过 哈哈哈哈哈
#author:0han, github:/e0han, email: 0han@protonmail.com
import os

def get_file():
    filename=[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.txt']
    return filename
def trans(filename):
    command='iconv -c -f GB2312 -t UTF-8 '+filename+' >> new_'+filename
    p=os.popen(command, 'r',1)
    p.close()
    os.remove(filename)
    print " [-]成功转换文件>"+filename

print "[+] 正在侦测操作系统类型..."
if os.name=='posix':
    file_list=get_file()
    for i in file_list:
        trans(i)
    print "[*] 已完全转换"
else:
    print '抱歉，本脚本暂不支持windows系统...'