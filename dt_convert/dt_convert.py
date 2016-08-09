#coding:utf-8
import os 
import sys
import struct
from os.path import join, getsize

####################################################################
#需要修改的尾部字段个数;
DT_NEED_ALTER_CNT = 2
DT_NEED_ALTER_DATA = 46
####################################################################

####################################################################
#输入目录和输出目录;
DTScriptName = sys.argv[0]
DTInputDir = sys.argv[1]
DTOutputDir = sys.argv[2]
print DTScriptName
print DTInputDir
print DTOutputDir
####################################################################

####################################################################
#函数: 将指定文件中最后一个字节替换成指定的字符;
"""
inputFileName: 输入的文件名(全路径)
outputFileName:输出的文件名(全路径)
lastByteData:  最后一个字节字符;
"""
def dtConvertLastByte(inputFileName, outputFileName, lastByteData):
	#打印传入的字符串到标准显示设备上
	print inputFileName
	print outputFileName
	print lastByteData
	#转换文件;
	lastByteDataBinary = struct.pack("B",lastByteData)
	fileSize = getsize(inputFileName)
	fileData = open(inputFileName,'rb')
	WriteFileData = open(outputFileName,'wb')
	WriteFileData.write(fileData.read(fileSize-1))
	WriteFileData.write(lastByteDataBinary)
	WriteFileData.close()
	#打印文件大小;
	print getsize(inputFileName)
	print getsize(outputFileName)
	return
####################################################################
   
####################################################################
#遍历输入目录的所有文件;
for parent,dirnames,filenames in os.walk(DTInputDir):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
	#for dirname in  dirnames:                       #输出文件夹信息
		#print "parent is:" + parent
		#print  "dirname is" + dirname
	for filename in filenames:                        #输出文件信息
		#print "parent is:"+ parent
		#print "filename is:" + filename
		print "--- input:" + os.path.join(parent,filename) #输出文件路径信息
		print "--- output:" + os.path.join(DTOutputDir,filename) #输出文件路径信息
		dtConvertLastByte(os.path.join(parent,filename), os.path.join(DTOutputDir,filename), DT_NEED_ALTER_DATA)
####################################################################

### 2016.08.09 yanping;
####################################################################