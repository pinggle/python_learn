#coding:utf-8
import zipfile
import os
import sys
import hashlib
import win32clipboard as wincb
import win32con

reload(sys)  
sys.setdefaultencoding('utf8')  

#�ó�����Ҫ�����������Ƿ���Ч,���¼�����ʵ�ѹ��������,����ѹ����������д�����а�;
#build: python pyinstaller.py -onefile dt_check_res.py

var = 1

MAGIC_WOOD_NAME = 'pack_id'
TAIL_WOOD_NAME = '.zip'
DT_FILE_SEPARATOR = '\\'

# Command
cmd_exit_1 = 'exit'
cmd_exit_2 = 'q'

#��ȡ�������������
#DTScriptName = sys.argv[0]
#DTInputZip = sys.argv[1]
#DTOutputDir = sys.argv[2]
#print DTScriptName
#print DTInputZip
#print DTOutputDir

#input_A = raw_input("Input: ")
#print input_A

###�������д���ַ���
import os
def addToClipBoard(text):
	wincb.OpenClipboard()
	wincb.EmptyClipboard()
	wincb.SetClipboardData(win32con.CF_TEXT, text.encode('GB2312'))  #�����ı����ݵ������壬ϵͳ��̨�᷵���ڴ��ַ
	#print wincb.GetClipboardData(win32con.CF_TEXT)  #'Hello World!'
	wincb.CloseClipboard()
	#command = 'echo ' + text.decode('GB2312').strip() + '| clip'
	#os.system(command)
	
def CalcMD5(filepath):
	with open(filepath,'rb') as f:
		md5obj = hashlib.md5()
		md5obj.update(f.read())
		hash = md5obj.hexdigest()
#print(hash)
		return hash

# ���ݸ������ַ�������ļ�����;
def GetWoodNameWithLine(linedata):
	endIndex = linedata.rfind('"')
	endString = linedata[0:endIndex]
	startIndex = endString.rfind('"') + 1
	#print(startIndex)
	#print(endIndex)
	return(linedata[startIndex:endIndex])
	
# �������Ƿ���Ч;
def CheckWoodValid(filepath):
	woodValid = 0
	REAL_WOOD_NAME = '55AABB'
	if os.path.exists(filepath):
		zipFile = zipfile.ZipFile(os.path.join(os.getcwd(), filepath))
		try:    
			zipInfoEx = zipFile.getinfo('resources.json')
		except KeyError:
			woodValid=1
		if 1==woodValid:
		 	print("�ò���Ϊ��Ч����!")
		else:
			print("�ò���Ϊ��Ч����!")
			data = zipFile.read('resources.json')
			data1,data2,data3,data4 = data.split('\r\n', 3);
			if(data1.find(MAGIC_WOOD_NAME) != -1):
				REAL_WOOD_NAME=GetWoodNameWithLine(data1.decode('utf-8'))
			elif(data2.find(MAGIC_WOOD_NAME) != -1):
				REAL_WOOD_NAME=GetWoodNameWithLine(data2.decode('utf-8'))
			elif(data3.find(MAGIC_WOOD_NAME) != -1):
				REAL_WOOD_NAME=GetWoodNameWithLine(data3.decode('utf-8'))
			elif(data4.find(MAGIC_WOOD_NAME) != -1):
				REAL_WOOD_NAME=GetWoodNameWithLine(data4.decode('utf-8'))
			else:
				REAL_WOOD_NAME='55AABB'
			print(REAL_WOOD_NAME)
		zipFile.close()
	else:
	  	woodValid=1
	  	print("�ò����ļ�������!")
	return REAL_WOOD_NAME

#�������ļ�;
def DTRenameFile(filepath,newName):
	try:
		startIndex = 0
		endIndex = filepath.rfind(DT_FILE_SEPARATOR)
		newpath = filepath[startIndex:endIndex]+DT_FILE_SEPARATOR+newName+TAIL_WOOD_NAME
		#��ʼ�������ļ�;
		if True==os.path.exists(newpath):
			print('Ŀ���ļ��Ѿ�����,������������,�ļ����Ѹ��Ƶ����а�')
			addToClipBoard(str(newName))	# ���Ŀ���ļ��������а�;
		else:
			print(filepath)
			print(newpath)
			os.rename(filepath, newpath)
			print('Ŀ���ļ��������ɹ�!')
	except UnicodeDecodeError:
		print('Ŀ���ļ�������ʧ��,������������,�ļ����Ѹ��Ƶ����а�')
		addToClipBoard(str(newName))	# ���Ŀ���ļ��������а�;
			
#�����ļ���:
def CalculateWoodName(filepath):
	filemd5 = CalcMD5(filepath)
	#print filemd5
	filemd5hash = hash(filemd5)
	filemd5hash = filemd5hash & 0xFFFFffff
	print("���޸�ѹ��������Ϊ:"+str(filemd5hash))
	#print filemd5hashd
	addToClipBoard(str(filemd5hash))
	return filemd5hash

if __name__ == "__main__":
	if len(sys.argv)==1 :
		while var == 1:
			input_A = raw_input("���������·��: ")
			print input_A
			if cmd_exit_1==input_A:
				break;
			elif cmd_exit_2==input_A:
				break;
			else:
				#if ''==input_A:
				#	input_A='Y:\\dt\\tmp\\minecraftpe\\texture\\134335.zip';
				woodName=CheckWoodValid(input_A)
				print(woodName)
				if '55AABB'!=woodName:
					DTRenameFile(input_A,woodName)
					print(woodName)
					print('\n')
				continue;
	else:
		print("����֧���κβ���!")

