

#import libraries
from glob import iglob
import shutil
import os
#create path variable
path = r'C:\Users\USUARIO\Desktop\BEING RELAXED\AUDIOS'


eits = r'C:\Users\USUARIO\Desktop\BEING RELAXED\AUDIOS\(3).mp3'
#create everything.mp3
destination = open(r'C:\Users\USUARIO\Desktop\BEING RELAXED\piqeuzin\fd.mp3', 'wb')
for filename in iglob(os.path.join(path, '*.mp3')):
   
   shutil.copyfileobj(open(filename, 'rb'), destination)
   shutil.copyfileobj(open(eits, 'rb'), destination)
#make them all together with for
destination.close()

