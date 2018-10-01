import serial

def scan():
    """scan for available ports. return a list of tuples (num, name)"""
    available = []
    for i in range(256):
        try:
            s = serial.Serial('COM'+str(i))
            available.append( (i, s.portstr))
            s.close() 
        except serial.SerialException:
            pass
    return available

if __name__=='__main__':
    print ("Found ports:")
    for n,s in scan():
        print ("Puerto: ", s)