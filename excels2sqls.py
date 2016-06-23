__author__='axe.xu xwx213960'
__date__ ='$2015-5-22 0:47:51$'
#THIS PROGRAM IS USED TO ANALYZE EXECELS AND WRITE THE RESULT TO DATABASE.
#PATTERNS AND RULES ARE PRESENTED IN THE EXECEL TEMPLATE

import xlrd,sqlite3,os
from wx import *
app = wx.App()
cvwin = wx.Frame(
    None,
    title = 'ChargeVerifyAide',
    size = (550,250))
cvwin.Center()
cvpanel = wx.Panel(cvwin)

#FUNCTIONS
def cvrule(a):
 
    return a
   
def handleinput(cvinputpathvalue):
    cvinputdata = xlrd.open_workbook(cvinputpathvalue)
    table1 = cvinputdata.sheets()[0]
    table2 = cvinputdata.sheets()[1]
    table3 = cvinputdata.sheets()[2]
    table4 = cvinputdata.sheets()[3]
    gaugecount = 0
    f = open('D:\cvsql.sql','w+')
#HANDLE TABLE2-4
    for i in range(table2.nrows):
        a = table2.row_values(i)
        sql2 = 'insert into S_PHONE values(%s,%s,%s);\n' % (a[0],a[1],str(a[2]).rstrip('.0'))
        f.write(sql2)
    cvgauge.SetValue(1)
 
    for j in range(table3.nrows):
        b = table3.row_values(j)
        sql3 = 'insert into S_PHONE values(%s,%s,%s);\n' % (a[0],a[1],str(a[2]).rstrip('.0'))
    cvgauge.SetValue(2)
 
    for k in range(table4.nrows):
        c = table4.row_values(k)
        sql4 = 'insert into S_PHONE values(%s,%s,%s);\n' % (a[0],a[1],str(a[2]).rstrip('.0'))
    cvgauge.SetValue(3)
#HANDLE TABLE1  
    for l in range(table1.nrows):
   #     a = table1.row_values(i)
   #     f.write(cvrule(a))
   #     gaugecount = gaugecount + 1
   #    
    f.close()
    return True

def handleoutput(cvoutputpathvalue):
#    cx = sqlite3.connect(cvoutputpathvalue)
#    cu = cx.cursor()
#    f = open('D:\cvsql.sql','r+')
#    gaugecount = 0
#    for line in f.readlines():
#	   line=line.strip('\n')
#	cu.execute(line)
#        gaugecount = gaugecount + 1
#        cvgauge.SetValue(gaugecount/len(f.readlines())*25)
#    f.close()
#	cu.close()
#    cx.close()
    return True

#WIN FUNCTIONS
#DIR OF EXECEL
def cvInput(evt):
    cvinputdialog = wx.FileDialog(
        cvwin,
        "OpenFrom",
        "",
        "",
        "*.*",
        wx.FD_FILE_MUST_EXIST)
    global cvinputpathvalue
    if cvinputdialog.ShowModal() == wx.ID_OK:
        cvinputpathvalue = cvinputdialog.GetPath()
    else:
        return
    cvinputpath.SetValue(cvinputpathvalue)

#DIR OF DB
def cvOutput(evt):
    cvoutputdialog = wx.FileDialog(
        cvwin,
        "SaveTo",
        "",
        "",
        "*.*",
        wx.FD_FILE_MUST_EXIST)
    global cvoutputpathvalue
    if cvoutputdialog.ShowModal() == wx.ID_OK:
        cvoutputpathvalue = cvoutputdialog.GetPath()
    else:
        return
    cvoutputpath.SetValue(cvoutputpathvalue)

#EXECUTE
def cvExecute(evt):
        handleinput(cvinputpathvalue)
        handleoutput(cvoutputpathvalue)
        wx.MessageBox('Success!','Info',wx.OK|wx.ICON_INFORMATION)
        #os.remove('D:\cvsql.sql')
        return True
   
#GUI
#BUTTON
cvInputButton = wx.Button(cvpanel, label ='InputPath')
cvInputButton.Bind(wx.EVT_BUTTON, cvInput)

cvOutputButton = wx.Button(cvpanel, label='OutputPath')
cvOutputButton.Bind(wx.EVT_BUTTON, cvOutput)

cvExecuteButton = wx.Button(cvpanel,label='Execute')
cvExecuteButton.Bind(wx.EVT_BUTTON,cvExecute)

#TextCtrl
cvinputpath = wx.TextCtrl(cvpanel, style=wx.TE_READONLY)
cvoutputpath = wx.TextCtrl(cvpanel, style=wx.TE_READONLY)

#Gauge
cvgauge = wx.Gauge(cvpanel, id=-1, range=5)

#BoxSizer|VERTICAL
cvbox = wx.BoxSizer(wx.VERTICAL)
cvbox.Add(cvInputButton,proportion=0, flag=wx.EXPAND | wx.ALL)
cvbox.Add(cvinputpath,proportion=0,flag=wx.EXPAND | wx.ALL)
cvbox.Add(cvOutputButton,proportion=0,flag=wx.EXPAND | wx.ALL)
cvbox.Add(cvoutputpath,proportion=0,flag=wx.EXPAND | wx.ALL)
cvbox.Add(cvExecuteButton,proportion=1,flag=wx.EXPAND | wx.ALL)
cvbox.Add(cvgauge,proportion=0,flag=wx.EXPAND | wx.ALL)

cvpanel.SetSizer(cvbox)
cvwin.Show()
app.MainLoop()


