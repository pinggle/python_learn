'下载python2.7文件
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

'创建桌面快捷方式
Set S = WScript.CreateObject("WScript.Shell")
Desktop = S.SpecialFolders("Desktop")
set lnk = S.CreateShortcut(Desktop & "\DT文件转换工具.lnk")
lnk.TargetPath = "C:\dt_convert\dt_convert.bat"
lnk.IconLocation = "write.exe, 0"
lnk.Description = "二进制文件修改工具" 
lnk.WorkingDirectory = Desktop
lnk.Save

'启动安装python2.7程序
Set objShell = CreateObject("Wscript.Shell") 
strCommandLine = "C:\dt_convert\python_2.7.12rc1_x64.msi"        '启动安装程序
objShell.Run(strCommandLine)