import ctypes,time

#Sets cursor position, remember: 0,0 is the very top left!
SetCursorPos = ctypes.windll.user32.SetCursorPos

#this is the mouse event for left click
mouse_event = ctypes.windll.user32.mouse_event

def click(x, y, numclicks=1):
  SetCursorPos(x, y)
  for i in xrange(numclicks):
      
#this means left mouse click down, but without releasing
   mouse_event(2, 0, 0, 0, 0)
   
#this means releasing of the mouse, or mouse left up
   mouse_event(4, 0, 0, 0, 0)

#You can while  loop to do this on a pixel as many times as you like:
# a = 1
# while a < <1000:    #we'll click 1000 times
#       click(100,100)   #click on this pixel of the screen
#       #time.sleep(1)   #optional time in between clicks (one second)
#       a = a+1
