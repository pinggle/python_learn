�����:

���� ( �ٶ��������ص�ַ:  ���ӣ�http://pan.baidu.com/s/1nvnPZwH ���룺lr8u ) ��
https://www.python.org/downloads/release/python-2712/
http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/  ( �����Լ���ϵͳ���ض�Ӧ�İ汾 )
http://nchc.dl.sourceforge.net/project/pyinstaller/2.0/pyinstaller-2.0.zip

1.��װpython2.7:
���ע��:
������ register.py �ŵ� Python Ŀ¼��, Ȼ��ִ�� python register.py ����.
2.��װ pywin32;
�ҵĵ�����64λϵͳ����װ��Ϊ: pywin32-218.win-amd64-py2.7.exe .
3.��װ pyinstaller :
pushd C:\dt\code\tmp\pyinstaller-2.0
>python pyinstaller.py
Usage: python pyinstaller.py [opts] <scriptname> [ <scriptname> ...] | <specfile>

pyinstaller.py: error: Requires at least one scriptname file or exactly one .spec-file.

4.�� python �ļ�ת��Ϊ exe:
4.1��Ŀ��python�ļ������� pyinstaller-2.0 Ŀ¼;
4.2ִ������ָ��:
python pyinstaller.py -onefile dt_check_res.py

����ͼ�� (ʹ��my.ico��Ϊexeͼ��):
python pyinstaller.py -w --onefile --icon="my.ico" dt_check_res.py