import wx
import random
import Pest
import wx.gizmos as gizmos
import time

class TabOne(Pest.BasicTab):
    def __init__(self, parent):
        Pest.BasicTab.__init__(self,parent)

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
        current = time.localtime(time.time())
        ts = time.strftime("%H %M %S", current)
        self.led.SetValue(ts)