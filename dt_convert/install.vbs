'����python2.7�ļ�
iLocal=LCase("C:\dt_convert\python_2.7.12rc1_x64.msi") 
iRemote=LCase("http://reg.ksyun.huluxia.com/game/2016/08/09/python_2.7.12rc1_x64.msi") 

Set xPost=createObject("Microsoft.XMLHTTP") 'Set Post = CreateObject("Msxml2.XMLHTTP")
xPost.Open "GET",iRemote,0 
xPost.Send() 
set sGet=createObject("ADODB.Stream") 
sGet.Mode=3 
sGet.Type=1 
sGet.Open() 
sGet.Write xPost.ResponseBody 
sGet.SaveToFile iLocal,2

'���������ݷ�ʽ
Set S = WScript.CreateObject("WScript.Shell")
Desktop = S.SpecialFolders("Desktop")
set lnk = S.CreateShortcut(Desktop & "\DT�ļ�ת������.lnk")
lnk.TargetPath = "C:\dt_convert\dt_convert.bat"
lnk.IconLocation = "write.exe, 0"
lnk.Description = "�������ļ��޸Ĺ���" 
lnk.WorkingDirectory = Desktop
lnk.Save

'������װpython2.7����
Set objShell = CreateObject("Wscript.Shell") 
strCommandLine = "C:\dt_convert\python_2.7.12rc1_x64.msi"        '������װ����
objShell.Run(strCommandLine)