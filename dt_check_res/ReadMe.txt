环境搭建:

下载 ( 百度云盘下载地址:  链接：http://pan.baidu.com/s/1nvnPZwH 密码：lr8u ) ：
https://www.python.org/downloads/release/python-2712/
http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/  ( 根据自己的系统下载对应的版本 )
http://nchc.dl.sourceforge.net/project/pyinstaller/2.0/pyinstaller-2.0.zip

1.安装python2.7:
解决注册:
将附件 register.py 放到 Python 目录下, 然后执行 python register.py 即可.
2.安装 pywin32;
我的电脑是64位系统，安装包为: pywin32-218.win-amd64-py2.7.exe .
3.安装 pyinstaller :
pushd C:\dt\code\tmp\pyinstaller-2.0
>python pyinstaller.py
Usage: python pyinstaller.py [opts] <scriptname> [ <scriptname> ...] | <specfile>

pyinstaller.py: error: Requires at least one scriptname file or exactly one .spec-file.

4.将 python 文件转化为 exe:
4.1将目标python文件拷贝到 pyinstaller-2.0 目录;
4.2执行以下指令:
python pyinstaller.py -onefile dt_check_res.py

加上图标 (使用my.ico作为exe图标):
python pyinstaller.py -w --onefile --icon="my.ico" dt_check_res.py