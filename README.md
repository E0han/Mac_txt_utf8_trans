# Mac_txt_utf8_trans

**This python script is used to trans GB2312 into UTF-8 characters, especially for Chinese users who is using mac os, when they need to download some Chinese novels from the internet, and find it was all error codes, just put this script under the same path as the file (or files) and run the script, it will trans the txt to normal utf-8.**

此脚本专门为mac os用户设计，尤其是中国用户，在下载了很多中文小说后发现文件内全是乱码，这是由于中文编码的问题所导致的。此脚本使用mac系统自带的iconv命令，批量转换编码，从GB2312转至UTF-8

###使用方法：

- 本项目包含两个文件，trans27.py和trans35.py 27是python2.7版本，给非专业人员直接使用，35是给python3.x用户使用
- 将一个或多个文件放入脚本的同目录下，直接双击运行脚本，或在终端进入目录(cd命令)，输入`python trans27.py`或`python3 trans35.py`，如果您改变过python的环境变量，按照您的实际改变为准
- 目录下所有txt乱码文件将会被转换为正常中文模式，并重命名(前面加个'new_')

作者: 0han

邮箱: 0han@protonmail.com

知乎: @0han

欢迎讨论
