import os

import eel

eel.init("www")

os.system('start msedge.exe --app="http://localhost:8000/index.html"')

eel.start('indext.html', mode=None, host='localhost', block=True)
