import wx
import random
from wx.lib.pubsub import pub

class BasicTab(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)
		#Meto todos los metodos comunes de las TAB



class TabTwo(BasicTab):
	def __init__(self, parent):
		BasicTab.__init__(self,parent)

 
class TabThree(BasicTab):
	def __init__(self, parent):
		BasicTab.__init__(self,parent)
 
class TabFour(BasicTab):
	def __init__(self, parent):
		BasicTab.__init__(self,parent)
 