import wx
import random
import Pest
import wx.gizmos as gizmos
import time
from wx.lib.pubsub import pub
class TabOne(Pest.BasicTab):
    def __init__(self, parent):
        

        Pest.BasicTab.__init__(self,parent)
        self.parent = parent
        self.count = 0
        style = gizmos.LED_ALIGN_CENTER
        self.led = gizmos.LEDNumberCtrl(self, -1, (0, 0), (150,35), style)
        self.OnTimer(None)
        self.timer = wx.Timer(self, -1)
        self.timer.Start(1000)
        self.Bind(wx.EVT_TIMER, self.OnTimer)
        '''
        #Evento para pintar cada 100 ms
        self.Timer = wx.Timer(self)
        self.Timer.Start(100)
        self.Bind(wx.EVT_TIMER, self.OnPaint)
        '''
    def OnTimer(self, event):
        self.count += 1
        current = time.localtime(time.time())
        ts = time.strftime("%H %M %S", current)
        self.led.SetValue(ts)

'''
        pub.subscribe(self.myListener, "Pest1")

    def myListener(self, message, arg2=None):
        print("Pestana 2: " + message, arg2)
'''