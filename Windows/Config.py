import wx
import Scan
import pandas as pd

tty = [
		"\\dev\\tty1" ,"\\dev\\tty2" ,"\\dev\\tty3" ,
		"\\dev\\tty4" ,"\\dev\\tty5" ,"\\dev\\tty6" ,
		"\\dev\\tty7" ,"\\dev\\tty8" ,"\\dev\\tty9" ,
		"\\dev\\tty10" ,"\\dev\\tty11" ,"\\dev\\tty12" ,
		"\\dev\\tty13" ,"\\dev\\tty14" ,"\\dev\\tty15" ,
		"\\dev\\tty16" ,"\\dev\\tty17" ,"\\dev\\tty18" ,
		"\\dev\\tty19" ,"\\dev\\tty20" ,"\\dev\\tty21" ,
		"\\dev\\tty22" ,"\\dev\\tty23" ,"\\dev\\tty24" ,
		"\\dev\\tty25" ,"\\dev\\tty26" ,"\\dev\\tty27" ,
		"\\dev\\tty28" ,"\\dev\\tty29" ,"\\dev\\tty30"]

COM = [
		"COM1" ,"COM2" ,"COM3" ,
		"COM4" ,"COM5" ,"COM6" ,
		"COM7" ,"COM8" ,"COM9" ,
		"COM10" ,"COM11" ,"COM12" ,
		"COM13" ,"COM14" ,"COM15" ,
		"COM16" ,"COM17" ,"COM18" ,
		"COM19" ,"COM20" ,"COM21" ,
		"COM22" ,"COM23" ,"COM24" ,
		"COM25" ,"COM26" ,"COM27" ,
		"COM28" ,"COM29" ,"COM30"]

class DataSMTConf:

	def __init__(self):
		self.Vel = 0
		self.IdVel = 0
		self.Serial1 = 0;
		self.Serial2 = 0;
		self.Serial3 = 0;
		self.Serial4 = 0;
		self.NumTanks = 0;
		self.SOid = 0;
		self.puerto = "";
	def __str__(self):
		return (str(self.IdVel)+","
		+str(self.Vel)+","
		+str(self.NumTanks)
		+","+str(self.Serial1)
		+","+str(self.Serial2)
		+","+str(self.Serial3)
		+","+str(self.Serial4)
		+","+str(self.SOid)
		+","+str(self.puerto)
		+",")
	

class ConfigMenu(wx.Frame):
	#----------------------------------------------------------------------
	def __init__(self):
		# Inicio del frame de configuración 
		wx.Frame.__init__(self, None, 
			title = "Configuración", 
			style = wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN | wx.FRAME_NO_TASKBAR | wx.STAY_ON_TOP)

		#Constantes y Variables
		self.lblList = ['2400','4800','9600','14400','19200','28800','38400','56000','57600','115200'] 
		self.dataSMT = DataSMTConf()
		#Eventos
		self.Bind(wx.EVT_CLOSE, self.OnClose)
		#Interfaz
		self.InitUI()
		self.Habilitar()
		
		
	def InitUI(self):
		#Panel de velocidades
		pnl = wx.Panel(self)
		#self.Text
		self.rbox = wx.RadioBox(pnl, label = 'Velocidad de comunicación serial', pos = (10,10), choices = self.lblList,majorDimension = 2, style = wx.RA_SPECIFY_ROWS) 
		self.rbox.Bind(wx.EVT_RADIOBOX,self.onRadioBox)

		wx.StaticLine    ( pnl, pos = (10 ,90 ),size  = (315,2))

		self.LabelS0 = wx.StaticText  ( pnl, pos = (10 ,100), label ="Tanques:")
		self.NumSerial = wx.SpinCtrl  ( pnl, pos = (80,100), min=1, max=4, initial=1, name="NumTanks", size = (50,20))
			
		self.Bind(wx.EVT_SPINCTRL, self.DesHabTanques, self.NumSerial)


		wx.StaticLine    ( pnl, pos = (10 ,125 ),size  = (315,2))

		self.LabelS1 = wx.StaticText  ( pnl, pos = (10 ,135), label = "Tanque 1:")
		self.Serial1 = wx.SpinCtrl    ( pnl, pos = (80 ,135), min   = 100000, max = 999999, initial = 100000, name = "Serial 1: ", size = (68,20))
		self.LabelS2 = wx.StaticText  ( pnl, pos = (170,135), label = "Tanque 2:")
		self.Serial2 = wx.SpinCtrl    ( pnl, pos = (240,135), min   = 100000, max = 999999, initial = 100000, name = "Serial 2: ", size = (68,20))
		
		self.LabelS3 = wx.StaticText  ( pnl, pos = (10 ,170), label = "Tanque 3:")
		self.Serial3 = wx.SpinCtrl    ( pnl, pos = (80 ,170), min   = 100000, max = 999999, initial = 100000, name = "Serial 3: ", size = (70,20))
		self.LabelS4 = wx.StaticText  ( pnl, pos = (170,170), label = "Tanque 4:")
		self.Serial4 = wx.SpinCtrl    ( pnl, pos = (240,170), min   = 100000, max = 999999, initial = 100000, name = "Serial 4: ", size = (70,20))
		
		wx.StaticLine    ( pnl, pos = (10 ,195), size  = (315,2))

		self.rbox2 = wx.RadioBox(pnl, label = 'Sistema Operativo', pos = (10,200), choices = ["Linux","Windows"],majorDimension = 2, style = wx.RA_SPECIFY_ROWS) 
		self.rbox2.Bind(wx.EVT_RADIOBOX,self.SistemaOperativo)
		self.Label5 = wx.StaticText  ( pnl, pos = (170,200), label = "Selección de puerto serial:")
		
		self.SerialL = wx.Choice      ( pnl, pos = (170,220), choices=tty, style=0 ,size = (100,20))
		self.SerialW = wx.Choice      ( pnl, pos = (170,250), choices=COM, style=0 ,size = (100,20))

		wx.StaticLine    ( pnl, pos = (10 ,280), size  = (315,2))
		self.SerialW.Bind(wx.EVT_CHOICE, self.Win)
		self.SerialL.Bind(wx.EVT_CHOICE, self.Lin)
		#Cargar Datos Actuales
		self.LoadInfo()
		self.SetSize((350,600))
		self.SetMaxSize((350,600))
		self.SetMinSize((350,600))

	def SistemaOperativo(self,event):
		self.dataSMT.SOid = self.rbox2.GetSelection()
		if (self.dataSMT.SOid == 0):
			self.SerialL.Enable()
			self.SerialW.Disable()
		else:
			self.SerialL.Disable()
			self.SerialW.Enable()

	def Win(self,event):
		self.dataSMT.puerto =  self.SerialW.GetCurrentSelection()+1
		print(self.dataSMT.puerto)

	def Lin(self,event):
		self.dataSMT.puerto = self.SerialL.GetCurrentSelection()+1
		print(self.dataSMT.puerto)

	def LoadInfo(self):
		try:
			#Obtengo la información
			Data = open("Data.smt", 'r').read()
			#La Parto
			self.dataSMT.IdVel    = int(Data.split(',')[0])
			self.dataSMT.Vel      = int(Data.split(',')[1])
			self.dataSMT.NumTanks = int(Data.split(',')[2])
			self.dataSMT.Serial1  = int(Data.split(',')[3])
			self.dataSMT.Serial2  = int(Data.split(',')[4])
			self.dataSMT.Serial3  = int(Data.split(',')[5])
			self.dataSMT.Serial4  = int(Data.split(',')[6])
			self.dataSMT.SOid 	  = int(Data.split(',')[7])
			self.dataSMT.puerto   = int(Data.split(',')[8])

			self.rbox.SetSelection  (self.dataSMT.IdVel   )
			self.NumSerial.SetValue (self.dataSMT.NumTanks)
			self.Serial1.SetValue   (self.dataSMT.Serial1 )
			self.Serial2.SetValue   (self.dataSMT.Serial2 )
			self.Serial3.SetValue   (self.dataSMT.Serial3 )
			self.Serial4.SetValue   (self.dataSMT.Serial4 )
			self.rbox2.SetSelection (self.dataSMT.SOid    )
			if(self.dataSMT.SOid == 1):
				self.SerialW.SetSelection(self.dataSMT.puerto - 1)
			else:
				self.SerialL.SetSelection(self.dataSMT.puerto - 1)

			self.Habilitar()
			if (self.dataSMT.SOid == 0):
				self.SerialL.Enable()
				self.SerialW.Disable()
			else:
				self.SerialL.Disable()
				self.SerialW.Enable()

		except:
			self.dataSMT.IdVel = 2
			self.dataSMT.Vel = 9600
			self.rbox.SetSelection(self.dataSMT.IdVel)
			self.dataSMT.NumTanks = 4
			self.NumSerial.SetValue(self.dataSMT.NumTanks)

	def onRadioBox(self,e):
		self.dataSMT.IdVel = self.rbox.GetSelection()
		self.dataSMT.Vel   = self.rbox.GetStringSelection()
		
	#----------------------------------------------------------------------

	def load(self,event):
		file = open(filename.GetValue())
		contents.SetValue(file.read())
		file.close()

	def save(self,event):
		file = open(filename.GetValue(), 'w')
		file.write(contents.GetValue())
		file.close()

	def Habilitar(self):
		Tanques = self.NumSerial.GetValue()
		if(Tanques == 1):
			self.Serial1.Enable()
			self.Serial2.Disable()
			self.Serial3.Disable()
			self.Serial4.Disable()
		if(Tanques == 2):
			self.Serial1.Enable()
			self.Serial2.Enable()
			self.Serial3.Disable()
			self.Serial4.Disable()
		if(Tanques == 3):
			self.Serial1.Enable()
			self.Serial2.Enable()
			self.Serial3.Enable()
			self.Serial4.Disable()
		if(Tanques == 4):
			self.Serial1.Enable()
			self.Serial2.Enable()
			self.Serial3.Enable()
			self.Serial4.Enable()

	def DesHabTanques(self, event):
		self.Habilitar()

	def OnClose(self):
		self.dataSMT.Serial1 = self.Serial1.GetValue()
		self.dataSMT.Serial2 = self.Serial2.GetValue()
		self.dataSMT.Serial3 = self.Serial3.GetValue()
		self.dataSMT.Serial4 = self.Serial4.GetValue()
		self.dataSMT.NumTanks = self.NumSerial.GetValue()
		file = open("Data.smt",'w')
		file.write(str(self.dataSMT))
		file.close()
		print("Muriendo")
		self.Destroy()
