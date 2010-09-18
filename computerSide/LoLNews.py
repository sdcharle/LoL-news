"""
This is for the fun LED Scrolling msg on the Lol shield
9/5/2010 SDC
"""
import serial
import time
import times_news

ARDY_SERIAL = "/dev/tty.usbserial-A7006QeX"
if __name__ == '__main__':
    ser = serial.Serial(ARDY_SERIAL, 9600)
    time.sleep(5)
    while 1:    
        data = times_news.grab_news()
        for res in data['results']:
            try:
                print "%s\n" % res['title']
                ser.write(res['title'])
                time.sleep(30)
            except Exception:
                print "%s oops, something in the string was un-ASCIIfied\n" % Exception