import wx
import Scan
import pandas as pd

º

class DataSMTConf:

    def __init__(self):
        self.Vel = 0
        self.IdVel = 0

    def __str__(self):
        return str(self.IdVel)+","+str(self.Vel)
    

class ConfigMenu(wx.Frame):

    #----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Configuración")
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
        self.rbox = wx.RadioBox(pnl, label = 'Velocidad de comunicación Serial', pos = (10,10), choices = self.lblList,majorDimension = 2, style = wx.RA_SPECIFY_ROWS) 
        self.rbox.Bind(wx.EVT_RADIOBOX,self.onRadioBox)
        #Cargar Datos Actuales
        self.LoadInfo()
        self.SetSize((350,600))
        
    def LoadInfo(self):
        try:
            #Obtengo la información
            Data = open("Data.smt", 'r').read()
            
            #La Parto
            print(Data.split(','))
            self.dataSMT.IdVel = int(Data.split(',')[0])
            self.dataSMT.Vel =   int(Data.split(',')[1])
            print("Velocidad:",str(self.dataSMT.Vel), " Id: ",self.dataSMT.IdVel)
            self.rbox.SetSelection(self.dataSMT.IdVel)
        except:
            self.dataSMT.IdVel = 0
            self.dataSMT.Vel = 2400
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
        file = open("Data.smt",'w')
        file.write(str(self.dataSMT))
        file.close()
        self.Destroy() 
