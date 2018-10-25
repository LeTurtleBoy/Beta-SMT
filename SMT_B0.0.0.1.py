# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 15:51:50 2018

@author: chris
"""

import os
import signal
import sys
import wx
import wx.gizmos as gizmos
import time

sys.path.insert(0, 'Windows\\')
import Config
import Pest
import Pest1
#import Serial

        


class SMT_Beta(wx.Frame):

	#Inicio de la aplicación
	def __init__(self, *args, **kwargs):
		super(SMT_Beta, self).__init__(*args, **kwargs)
		self.Maximize(True) #Iniciar Maximizado
		self.InitUI()

	#Metodo de inicio
	def InitUI(self):
		#Inicio grafico y de estilo
		self.SetSize((800, 600)) #Tamaño
		self.SetTitle('SMT_Beta 0.0.0.2') #Titulo
		self.SetMaxSize((800,600))
		self.SetMinSize((800,600))
		self.SetIcon(wx.Icon(self.scale_bitmap(wx.Bitmap('Iconos\\png\\pie-chart-1.png'),30,30)))
		self.SetBackgroundColour((10,10,10,100))
		#Eventos Principales
		
		self.EventoSalida()
	
		#Inicio de propiedades
		self.Pestanhas()
		self.Menus() #Creo los menus con Iconos

	#Herramientas y Eventos

	#----------------------------------------------#
	#				Evento Salida SMT
	#----------------------------------------------#
	def EventoSalida(self):
		self.Bind(wx.EVT_CLOSE, self.OnClose)
		exitId = wx.NewId()
		self.Bind(wx.EVT_MENU, self.OnClose, id=exitId )
		accel_tbl = wx.AcceleratorTable([(wx.ACCEL_CTRL,  ord('Q'), exitId )])
		self.SetAcceleratorTable(accel_tbl)

	def OnClose(self, e):
		if wx.MessageBox("¿Desea Cerrar El Programa?",
						 "Salir SMT - Sistema de Medición de Tanques",
						 wx.ICON_QUESTION | wx.YES_NO) != wx.YES:
			return
		
		self.Destroy()
		print("Saliendo")
		os.kill(os.getpid(),signal.SIGTERM) #Salgo porque salgo
		

	#----------------------------------------------#
	#				Resize Imagenes
	#----------------------------------------------#
	def scale_bitmap(self,bitmap, width, height):
		image = bitmap.ConvertToImage()
		image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
		result = wx.Bitmap(image)
		return result

	#----------------------------------------------#
	#				MENU
	#----------------------------------------------#

	def Menus(self):
		self.count = 1			#Ventana inicial		
		self.maxcount =  10  	#Numero de ventanas
		self.toolbar = self.CreateToolBar(wx.CENTER)
		wx.SystemOptions.SetOption("msw.remap", 2)
		self.toolbar.SetBackgroundColour((230,230,230))
		self.toolbar.SetToolBitmapSize((30,30))
		self.toolbar.SetMargins(100,100)
		# set frame size to fit panel
		self.Fit()

	

		#Establecer imagenes
		Arrow1 = self.scale_bitmap(wx.Bitmap('Iconos\\png\\left-arrow.png'),40,40)
		Arrow2 = self.scale_bitmap(wx.Bitmap('Iconos\\png\\right-arrow2.png'), 40,40)
		Arrow3 = self.scale_bitmap(wx.Bitmap('Iconos2\\png\\settings-2.png'), 30,30)
		

		texit = self.toolbar.AddTool(wx.ID_NEW, '', Arrow3)
		for x in range(10):
			self.toolbar.AddSeparator()
		tundo = self.toolbar.AddTool(wx.ID_UNDO, 'Tango', Arrow1)
		for x in range(10):
			self.toolbar.AddSeparator()
		tredo = self.toolbar.AddTool(wx.ID_REDO, 'label', Arrow2)

		self.toolbar.Realize()

		self.Bind(wx.EVT_TOOL, self.Config, texit)
		self.Bind(wx.EVT_TOOL, self.Izquierda, tundo)
		self.Bind(wx.EVT_TOOL, self.Derecha, tredo)

		print("Menu Done")

	def Pestanhas(self):
		self.p = wx.Panel(self)
		self.nb = wx.Notebook(self.p)
		self.p.SetBackgroundColour((10,10,10))
		# Create the tab windows
		tab1 = Pest1.TabOne(self.nb)
		tab2 = Pest.TabTwo(self.nb)
		tab3 = Pest.TabThree(self.nb)
		tab4 = Pest.TabFour(self.nb)
		
		self.nb.SetBackgroundColour((255,255,255))

		font = wx.Font(12, wx.FONTFAMILY_MODERN, wx.NORMAL, wx.NORMAL)
		self.nb.SetFont(font)
		
		self.nb.AddPage(page = tab1, text = "Ventana1", select=True)
		self.nb.AddPage(page = tab2, text = "Ventana2", select=False)
		self.nb.AddPage(page = tab3, text = "Ventana3", select=False)
		self.nb.AddPage(page = tab4, text = "Ventana4", select=False)

		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(self.nb, 1, wx.ALL|wx.EXPAND, 5)
		self.p.SetSizer(sizer)

		print("Pestañas Done")

	def Izquierda(self, e):
		if self.count > 1 and self.count <= self.maxcount: #Si aprieto voy al menu
			self.count = self.count - 1
		if self.count == 1: #Si estoy en la 
			self.toolbar.EnableTool(wx.ID_UNDO, False)
		if self.count == self.maxcount-1:
			self.toolbar.EnableTool(wx.ID_REDO, True)
		#self.Ventana()
		self.setPagenb()

	def Derecha(self, e):
		if self.count < self.maxcount and self.count >= 1:
			self.count = self.count + 1
		if self.count == self.maxcount:
			self.toolbar.EnableTool(wx.ID_REDO, False)
		if self.count == 2:
			self.toolbar.EnableTool(wx.ID_UNDO, True)
		#self.Ventana()
		self.setPagenb()

	def Ventana(self):
		#Llamar la ventana que sea necesaria
		self.second_window = wx.Frame(None)
		self.second_window.Show()
		print(self.count)

	def setPagenb(self):
		try:
			self.nb.SetSelection(self.count-1)
		except Exception:
			print("Pagina no Existe")
			self.count -= 1

	def Config(self, event):
		self.second_window =Config.ConfigMenu()
		self.second_window.Show()

	def onbtn(self, event):
		print ("First radioBtn = ", self.radio.GetValue())
		print ("Second radioBtn = ", self.radio2.GetValue())


def main():
	app = wx.App()
	default = wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN | wx.FRAME_NO_TASKBAR | wx.STAY_ON_TOP
	ex = SMT_Beta(wx.Frame(None),style=default)
	ex.Show()
	app.MainLoop()
	print("State")
	return()


if __name__ == '__main__':
	main()
