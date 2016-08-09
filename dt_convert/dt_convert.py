#coding:utf-8
import os 
import sys
import struct
from os.path import join, getsize

####################################################################
#��Ҫ�޸ĵ�β���ֶθ���;
DT_NEED_ALTER_CNT = 2
DT_NEED_ALTER_DATA = 46
####################################################################

####################################################################
#����Ŀ¼�����Ŀ¼;
DTScriptName = sys.argv[0]
DTInputDir = sys.argv[1]
DTOutputDir = sys.argv[2]
print DTScriptName
print DTInputDir
print DTOutputDir
####################################################################

####################################################################
#����: ��ָ���ļ������һ���ֽ��滻��ָ�����ַ�;
"""
inputFileName: ������ļ���(ȫ·��)
outputFileName:������ļ���(ȫ·��)
lastByteData:  ���һ���ֽ��ַ�;
"""
def dtConvertLastByte(inputFileName, outputFileName, lastByteData):
	#��ӡ������ַ�������׼��ʾ�豸��
	print inputFileName
	print outputFileName
	print lastByteData
	#ת���ļ�;
	lastByteDataBinary = struct.pack("B",lastByteData)
	fileSize = getsize(inputFileName)
	fileData = open(inputFileName,'rb')
	WriteFileData = open(outputFileName,'wb')
	WriteFileData.write(fileData.read(fileSize-1))
	WriteFileData.write(lastByteDataBinary)
	WriteFileData.close()
	#��ӡ�ļ���С;
	print getsize(inputFileName)
	print getsize(outputFileName)
	return
####################################################################
   
####################################################################
#��������Ŀ¼�������ļ�;
for parent,dirnames,filenames in os.walk(DTInputDir):    #�����������ֱ𷵻�1.��Ŀ¼ 2.�����ļ������֣�����·���� 3.�����ļ�����
	#for dirname in  dirnames:                       #����ļ�����Ϣ
		#print "parent is:" + parent
		#print  "dirname is" + dirname
	for filename in filenames:                        #����ļ���Ϣ
		#print "parent is:"+ parent
		#print "filename is:" + filename
		print "--- input:" + os.path.join(parent,filename) #����ļ�·����Ϣ
		print "--- output:" + os.path.join(DTOutputDir,filename) #����ļ�·����Ϣ
		dtConvertLastByte(os.path.join(parent,filename), os.path.join(DTOutputDir,filename), DT_NEED_ALTER_DATA)
####################################################################

### 2016.08.09 yanping;
####################################################################