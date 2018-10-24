import wx
import Scan
import pandas as pd

class DataSMTConf:

    def __init__(self):
        self.Vel = 0
        self.IdVel = 0
        self.Serial1 = 0;
        self.Serial2 = 0;
        self.Serial3 = 0;
        self.NumTanks = 0;
    def __str__(self):
        return str(self.IdVel)+","+str(self.Vel)+","+str(self.NumTanks)+","+str(self.Serial1)+","+str(self.Serial2)+","+str(self.Serial3)
    

class ConfigMenu(wx.Frame):

    #----------------------------------------------------------------------
    def __init__(self):
        # Inicio del frame de configuración 
        wx.Frame.__init__(self, None, 
            title = "Configuración", 
            style = wx.RESIZE_BORDER | wx.SYSTEM_MENU 
            | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN 
            | wx.FRAME_NO_TASKBAR | wx.STAY_ON_TOP)


        #Constantes y Variables
        self.lblList = ['2400','4800','9600','14400','19200','28800','38400','56000','57600','115200'] 
        self.dataSMT = DataSMTConf()
        #Eventos
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        #Interfaz
        self.InitUI()
        
        
    def InitUI(self):

        #Panel de velocidades
        pnl = wx.Panel(self)
        #self.Text
        self.rbox = wx.RadioBox(pnl, label = 'Velocidad de comunicación serial', pos = (10,10), choices = self.lblList,majorDimension = 2, style = wx.RA_SPECIFY_ROWS) 
        self.rbox.Bind(wx.EVT_RADIOBOX,self.onRadioBox)

        self.NumSerial = wx.SpinCtrl(pnl, pos = (100,130), min=1, max=4, initial=1, name="NumTanks")
        self.LabelS0 = wx.StaticText( pnl, pos=  (10,100), label ="Número de tanques:")


        self.Serial1 = wx.SpinCtrl(   pnl, pos = (100,130), min=0, max=100000, initial=30000, name="Serial 1: ")
        self.LabelS1 = wx.StaticText( pnl, pos=  (10,130), label ="Serial tanque 1:")

        self.Serial2 = wx.SpinCtrl(   pnl, pos = (100,160), min=0, max=100000, initial=30000, name="Serial 2: ")
        self.LabelS2 = wx.StaticText( pnl, pos = (10,160), label ="Serial tanque 2:")

        self.Serial3 = wx.SpinCtrl(   pnl, pos = (100,190), min=0, max=100000, initial=30000, name="Serial 3: ")
        self.LabelS3 = wx.StaticText( pnl, pos = (10,190), label ="Serial tanque 3:")


        #Cargar Datos Actuales
        self.LoadInfo()
        self.SetSize((350,600))
        
    def LoadInfo(self):
        try:
            #Obtengo la información
            Data = open("Data.smt", 'r').read()
            #La Parto
            print(Data.split(','))
            self.dataSMT.IdVel    = int(Data.split(',')[0])
            self.dataSMT.Vel      = int(Data.split(',')[1])
            self.dataSMT.NumTanks = int(Data.split(',')[2])
            self.dataSMT.Serial1  = int(Data.split(',')[3])
            self.dataSMT.Serial2  = int(Data.split(',')[4])
            self.dataSMT.Serial3  = int(Data.split(',')[5])


            print("Velocidad:",str(self.dataSMT.Vel), " Id: ",self.dataSMT.IdVel)
            print("Serial 1:",str(self.dataSMT.Serial1),"Serial 2:",str(self.dataSMT.Serial2),"Serial 3:",str(self.dataSMT.Serial3))

            self.NumSerial.SetValue(self.dataSMT.NumTanks)
            self.Serial1.SetValue(self.dataSMT.Serial1)
            self.Serial2.SetValue(self.dataSMT.Serial2)
            self.Serial3.SetValue(self.dataSMT.Serial3)
            self.rbox.SetSelection(self.dataSMT.IdVel)


        except:
            self.dataSMT.IdVel = 2
            self.dataSMT.Vel = 9800
            self.rbox.SetSelection(self.dataSMT.IdVel)

     
    def onRadioBox(self,e):
        self.dataSMT.IdVel = self.rbox.GetSelection()
        self.dataSMT.Vel   = self.rbox.GetStringSelection()
        print(self.rbox.GetStringSelection(),' is clicked from Radio Box')  
        
    #----------------------------------------------------------------------
    def onBtn(self, event):
        """"""
        print ("First radioBtn = ", self.radio.GetValue())
        print ("Second radioBtn = ", self.radio2.GetValue())

    def load(self,event):
        file = open(filename.GetValue())
        contents.SetValue(file.read())
        file.close()

    def save(self,event):
        file = open(filename.GetValue(), 'w')
        file.write(contents.GetValue())
        file.close()


    def OnClose(self, e):
        self.dataSMT.Serial1 = self.Serial1.GetValue()
        self.dataSMT.Serial2 = self.Serial2.GetValue()
        self.dataSMT.Serial3 = self.Serial3.GetValue()
        print(self.dataSMT.Serial1,self.dataSMT.Serial2,self.dataSMT.Serial3)
        file = open("Data.smt",'w')
        file.write(str(self.dataSMT))
        file.close()
        self.Destroy() 
