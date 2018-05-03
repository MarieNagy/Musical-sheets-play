
import cv2
import numpy as np
import imutils
import math
from scipy import ndimage


############# reads ##########


path = "C:\\Users\\Megzz\\Desktop\\twinkle.jpg"
img = cv2.imread(path,0)

keyUp = cv2.imread('k-.png',0)
dotted = cv2.imread('dot-.jpg',0)
keyDo = cv2.imread('k-1.jpg',0)
keyEm = cv2.imread('ek-1.jpg',0)
keyfk = cv2.imread('fk.jpg',0)
bar = cv2.imread('bar.jpg',0)
barEnd = cv2.imread('barEnd.jpg',0)
sol = cv2.imread('sol.jpg',0)



#####################  houghLines #######################
try: imgW, imgH = img.shape[::-1]
except: print("No Image Dude!!") 
     
HoughLinesConst = int(imgW*.5)
                      
gray = cv2.Canny(img, 50, 200)
lines = cv2.HoughLines(gray,1,np.pi/180,HoughLinesConst)

thetta = lines[0][1][1]
thetta = int(round(thetta *180/np.pi)) - 90


img = ndimage.rotate(img, thetta)

################## Resize #########################

resTmp = 0
solW, solH = sol.shape[::-1]

threshold = 0.6

resWidth = solW
for width in range(10,100,1):
    resized = imutils.resize(sol,width=width)
    w, h = resized.shape[::-1]

    if w >= imgW or h >= imgH:
        break
    resizeRes = cv2.matchTemplate(img,resized,cv2.TM_CCOEFF_NORMED)

    resizeLoc = np.where( resizeRes >= threshold)
    detectedPoints= zip(*resizeLoc[::-1])

   
    if len(detectedPoints)>0:
       
        if resTmp >= len(detectedPoints):
            resWidth = width - 1  
            break
            
        resTmp = len(detectedPoints)


scale= resWidth/float(solW)

wkeyUp, hkeyUp      = keyUp.shape[::-1]
wdotted, hdotted    = dotted.shape[::-1]
wkeyDo, hkeyDo      = keyDo.shape[::-1]
wkeyEm, hkeyEm      = keyEm.shape[::-1]
wkeyfk, hkeyfk      = keyfk.shape[::-1]
wbar, hbar          = bar.shape[::-1]
wbarEnd, hbarEnd    = barEnd.shape[::-1]

keyUp     = imutils.resize(keyUp,  width=int(scale*wkeyUp))
dotted    = imutils.resize(dotted, width=int(scale*wdotted))
keyDo     = imutils.resize(keyDo,  width=int(scale*wkeyDo))
keyEm     = imutils.resize(keyEm,  width=int(scale*wkeyEm))
keyfk     = imutils.resize(keyfk,  width=int(scale*wkeyfk))
bar       = imutils.resize(bar,    width=int(scale*wbar))
barEnd    = imutils.resize(barEnd, width=int(scale*wbarEnd))
sol       = imutils.resize(sol,    width=int(scale*solW))

solW, solH = sol.shape[::-1]                  

########### lines & rows #########
l=[]
tmp = []


for rho,theta in lines[0]:
    tmp.append(rho + float(np.sin(thetta*np.pi/180))* imgW )
    
tmp.sort()

a = tmp[0]
l = []
for i in range(1,len(tmp)):
    b = tmp[i] - tmp[i -1]
    if b > solW or i == len(tmp) - 1:
        spc = abs( tmp[i -1] - a)/4
        for n in range(0,5):
            l.append(a + spc*n)
        a = tmp[i]
    


   
######## matching #######.
    
w, h = keyUp.shape[::-1]

res = []
loc = []
loz = []
lo  = []
for i in range(0,8):
     temporary= []
     res.append(temporary)
     loc.append(temporary)
     loz.append(temporary)
     lo.append(temporary)


res[0] = cv2.matchTemplate(img,keyUp,cv2.TM_CCOEFF_NORMED)
res[1] = cv2.matchTemplate(img,dotted,cv2.TM_CCOEFF_NORMED)
res[2] = cv2.matchTemplate(img,keyDo,cv2.TM_CCOEFF_NORMED)
res[3] = cv2.matchTemplate(img,keyEm,cv2.TM_CCOEFF_NORMED)
res[4] = cv2.matchTemplate(img,keyfk,cv2.TM_CCOEFF_NORMED)
res[5] = cv2.matchTemplate(img,bar,cv2.TM_CCOEFF_NORMED)
res[6] = cv2.matchTemplate(img,barEnd,cv2.TM_CCOEFF_NORMED)
res[7] = cv2.matchTemplate(img,sol,cv2.TM_CCOEFF_NORMED)

threshold = float(0.8 - (1 - scale)/3.775)

loc[0] = np.where( res[0] >= threshold       )
loc[1] = np.where( res[1] >= threshold       )
loc[2] = np.where( res[2] >= threshold       )
loc[3] = np.where( res[3] >= threshold - 0.2 )
loc[4] = np.where( res[4] >= threshold       )
loc[5] = np.where( res[5] >= threshold + 0.05)
loc[6] = np.where( res[6] >= threshold + 0.1 )
loc[7] = np.where( res[7] >= threshold       )


###### cleaning #####
for i in range(0,8):
     loz[i] = zip(*loc[i][::-1])

for i in range(0, len(loz)):
            for pt in loz[i]:
                 
               flag = False
               for po in lo[i]:
                    x = abs(pt[0] - po[0])
                    y = abs(pt[1] - po[1])

                    if x < w and y < w :
                        flag = True
                        
               if flag == False :
                    lo[i].append(pt)

locations = []
for i in range(0, len(lo)):
     temporary = []
     locations.append(temporary)

     
for i in range(0, len(lo)):
     for pt in lo[i]:
         flag = False
         flag0 = False
         
         if   i == 0 :
             locations[i].append(pt)
             continue
            
         for n in range(0, len(lo)):
                 
                if  i == n:
                    continue
                
                for po in locations[n]:
                              
                     x = abs(pt[0] - po[0])
                     y = abs(pt[1] - po[1])

                     if x < w/2 and y < w/2 :
                          flag = True
         
         if flag == False :
            locations[i].append(pt)


######## On img detect ######
"""
img = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)

for pt in locations[0]:
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)

for pt in locations[1]:
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,255,0), 1)

for pt in locations[2]:
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,255,255), 1)
    
for pt in locations[3]:
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + w), (255,0,0), 1)
    
for pt in locations[4]:
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (255,255,0), 1)
    
for pt in locations[5]:
    cv2.rectangle(img, pt, (int(pt[0] + w*2), int(pt[1] + h*5)), (255,0,255), 1)
    
for pt in locations[6]:
    cv2.rectangle(img, pt, (int(pt[0] + w*2), int(pt[1] + h*5)), (0,100,100), 1)

for pt in locations[7]:
    cv2.rectangle(img, pt, (int(pt[0] + solW), int(pt[1] + solH)), (100,0,100), 1)


img = ndimage.rotate(img, -thetta)

cv2.imshow('Detected',img)
cv2.imwrite('Detected.jpg',img)


cv2.waitKey(0)
cv2.destroyAllWindows()

"""
##################### Sorting ###########
fullNote = []
rows = []
try: rowSpace = l[4] - l[0]
except: print("No lines were detected!! image might be too small '(")

for i in range(0,len(l)/5) :
     rows.append([])
     for n in range(0, len(locations) - 1):
          for pt in locations[n]:
               try:
                   if abs(pt[1] - l[i*5]) > rowSpace*1.5 or pt[0] < abs(locations[7][i][0] + solW*1.5 ):
                    continue
               except: continue
               rows[i].append(pt)
     rows[i].sort()
         
          
spc = abs(l[0]- l[1])

################# pinpointing ###############

for i in range(0,len(rows)):

   #  pos.append('$')
    # note.append('$')
     
     for pt in rows[i]:

          if pt in locations[0] :
               note = 'q'
               n = 'onLine'
          elif pt in locations[1] :
               note = 'h'
               n = 'onLine'
          elif pt in locations[2] :
               note = 'q'
               n = 'betLine'
          elif pt in locations[3] :
               note = 'h'
               n = 'onLine'
          elif pt in locations[4] :
               note = 'f'
               n = 'onLine'
               full = True
          elif pt in locations[5] or pt in locations[6]:
              #note.append('|')
               n = 'bar'
               
          temp = abs(pt[1] - l[0])
          for i in range(0,len(l)/5):
               y = abs(pt[1] - l[i*5])
               if y <= temp :
                    idx = i*5
                    temp = y
               else: break

               
          if n == 'onLine' or n == 'betLine' :

               
               t = pt[1] + h*0.5 

               if   t > l[idx + 2] - spc/4 and t < l[idx + 2] + spc/4 :
                    pos = 'B1'
               elif t > l[idx + 1] + spc/4 and t < l[idx + 2] - spc/4 :
                    pos = 'C1'
               elif t > l[idx + 1] - spc/4 and t < l[idx + 1] + spc/4 :
                    pos = 'D1'
               elif t > l[idx] + spc/4 and t < l[idx + 1] - spc/4:
                    pos = 'E1'
               elif t > l[idx] - spc/4 and t < l[idx] + spc/4 : 
                    pos = 'F1'
                    
               elif t > l[idx + 2] + spc/4 and t < l[idx + 3] - spc/4 :
                    pos = 'A0'
               elif t > l[idx + 3] - spc/4 and t < l[idx + 3] + spc/4 :
                    pos = 'G0'
               elif t > l[idx + 3] + spc/4 and t < l[idx + 4] - spc/4 :
                    pos = 'F0'
               elif t > l[idx + 4] - spc/4 and t < l[idx + 4] + spc/4:
                    pos = 'E0'
               elif t > l[idx + 4] + spc/4 and t < l[idx + 4] + spc*0.75:
                    pos = 'D0'
               elif t > l[idx + 4] + spc*1.25 and t < l[idx + 4] + spc*1.75:
                    pos = 'C0'
               elif t > l[idx + 4] + spc*2.25 and t < l[idx + 4] + spc*2.75 :
                    pos = 'B0'
               
               elif t > l[idx ] + spc/4 and t < l[idx] + spc*.75 :
                    pos = 'G1' 
               elif t > l[idx] + spc*1.25 and t < l[idx] + spc*1.75:
                    pos = 'A1'
               elif t > l[idx] + spc*2.25 and t < l[idx] + spc*2.75 : 
                    pos = 'B1'

               else: pos.append('B1')

                    
          
          fn = note + pos
          fullNote.append(fn)
                            


#print   (thetta, threshold, scale, HoughLinesConst, len(l))


####################

