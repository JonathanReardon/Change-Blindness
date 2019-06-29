#!/usr/bin/env python3

from psychopy import visual, core, gui, event, sound
from psychopy.data import getDateStr
import os
import glob
import csv

# Set window and mouse
win = visual.Window([800,600],color=(1,1,1), colorSpace='rgb', allowGUI=True, monitor='testMonitor', units='deg', fullscr=True)
myMouse = event.Mouse(visible=True,win=win)

# Practice Circles
circles_on = 0

prac_circle1 = visual.Circle(win, units='deg', radius=1, pos=(0.4,6.4),lineColor="red", opacity=circles_on)
prac_circle2 = visual.Circle(win, units='deg', radius=1, pos=(-7.6,-3.5),lineColor="yellow", opacity=circles_on)
prac_circle3 = visual.Circle(win, units='deg', radius=1, pos=(9.2, -6.1),lineColor="blue", opacity=circles_on)

# Image1 correct detection areas (to display ticks)
circle1 = visual.Circle(win, units='deg', radius=1, pos=(-7.6,-4.1))
circle2 = visual.Circle(win, units='deg', radius=1, pos=(6.2,-5.3), lineColor="yellow")
circle3 = visual.Circle(win, units='deg', radius=1, pos=(3.9,1), lineColor="green")
circle4 = visual.Circle(win, units='deg', radius=1, pos=(.9,-5.3), lineColor="blue")
circle5 = visual.Circle(win, units='deg', radius=1, pos=(-10,-7), lineColor="black")

# Image2 correct detection areas (to display ticks)
circle6 = visual.Circle(win, units='deg', radius=1, pos=(0.6,6.1), lineColor="red")
circle7 = visual.Circle(win, units='deg', radius=1, pos=(10.5,-7), lineColor="yellow")
circle8 = visual.Circle(win, units='deg', radius=1, pos=(11.2,7.6), lineColor="orange")
circle9 = visual.Circle(win, units='deg', radius=1, pos=(-10,3.3), lineColor="blue")
circle10 = visual.Circle(win, units='deg', radius=1, pos=(-10,-7), lineColor="black")

# Image3 correct detection areas (to display ticks)
circle11 = visual.Circle(win, units='deg', radius=1, pos=(.3,-4.4), lineColor="red")
circle12 = visual.Circle(win, units='deg', radius=1, pos=(-9.4,-3.1), lineColor="yellow")
circle13 = visual.Circle(win, units='deg', radius=1, pos=(-11,7), lineColor="orange")
circle14 = visual.Circle(win, units='deg', radius=1, pos=(0,6), lineColor="blue")
circle15 = visual.Circle(win, units='deg', radius=1, pos=(2,6), lineColor="black")

# Image4 correct detection areas (to display ticks)
circle16 = visual.Circle(win, units='deg', radius=1, pos=(9.5,-6.8), lineColor="red")
circle17 = visual.Circle(win, units='deg', radius=1, pos=(-8.1,-5.3), lineColor="yellow")
circle18 = visual.Circle(win, units='deg', radius=1, pos=(14,2), lineColor="orange")
circle19 = visual.Circle(win, units='deg', radius=1, pos=(-9.7,7.7), lineColor="blue")
circle20 = visual.Circle(win, units='deg', radius=1, pos=(9,6), lineColor="black")

# Set clock and other variables
clock = core.Clock()
rt_clock = core.Clock()
default_time=.5
blank_time=.5
shape_rad = 1
refresh_rate = 60.0

#learning_period = 3             # change to edit the learning time
#detection_time = 3

fix = 3
blank = 2
tick_size=1.5

#detection = detection_time * refresh_rate
#detection = int(detection)

fix_time = fix * refresh_rate
fix_time = int(fix_time)

#learning_time = learning_period * refresh_rate
#learning_time = int(learning_time)

blank_screen = blank * refresh_rate
blank_screen = int(blank_screen)

stim_size = (2560/2.7,1556/2.7)
prac_stim_size = (2560/100,1556/100)

rt = []
correct = 0

practice_gate1 = 0
practice_gate2 = 0
practice_gate3 = 0

gate1 = 0
gate2 = 0
gate3 = 0
gate4 = 0
gate5 = 0
gate6 = 0 
gate7 = 0 
gate8 = 0 
gate9 = 0 
gate10 = 0 
gate11 = 0 
gate12 = 0 
gate13 = 0 
gate14 = 0 
gate15 = 0 
gate16 = 0 
gate17 = 0 
gate18 = 0 
gate19 = 0 
gate20 = 0 

# -------------------------- Import stim directories ---------------------------- 

Practice_image_prior     = glob.glob(os.path.join('../practice','*.png')) 
Practice_image_after     = glob.glob(os.path.join('../practice','*.jpg'))

learning_images          = glob.glob(os.path.join('../learning','*.png')) 
change_detection         = glob.glob(os.path.join('../change','*.jpg')) 
tick_stim                = glob.glob(os.path.join('../tick','*.png'))

# ------------------------ Make image objects --------------------------------------

learning        = [visual.ImageStim(win, img, name='learning_image' + img, units='pix', size=(stim_size))  for img in learning_images[:]]
change          = [visual.ImageStim(win, img, name='detection_image' + img, units='pix', size=(stim_size)) for img in change_detection[:]]
tick            = [visual.ImageStim(win, img, name='tick_image' + img, units='deg', size=(tick_size))      for img in tick_stim[:]] 

practice_1      = [visual.ImageStim(win, img, name='prac_1' + img, units='deg', size=(prac_stim_size))     for img in Practice_image_prior[:]] 
practice_2      = [visual.ImageStim(win, img, name='prac_2' + img, units='deg', size=(prac_stim_size))     for img in Practice_image_after[:]] 

tick1      = tick[0]
prac_tick1 = tick[0]
prac_tick2 = tick[1]
prac_tick3 = tick[2]
prac1      = practice_1[0]
prac2      = practice_2[0]

tick1 = tick[3]
tick2 = tick[4]
tick3 = tick[5]
tick4 = tick[6]
tick5 = tick[7]
tick6 = tick[8]
tick7 = tick[9]
tick8 = tick[10]
tick9 = tick[11]
tick10 = tick[12]
tick11 = tick[13]
tick12 = tick[14]
tick13 = tick[15]
tick14 = tick[16]
tick15 = tick[17]
tick16 = tick[18]
tick17 = tick[19]
tick18 = tick[20]
tick19 = tick[21]
tick20 = tick[22]

# practice tick positions

prac_tick1.pos = (0.4,6.4)
prac_tick2.pos = (-7.6,-3.5)
prac_tick3.pos = (9.2, -6.1)

# image1 tick positions

tick1.pos = (-7.6,-4.1)
tick2.pos = (6.2,-5.3)
tick3.pos = (3.9,1)
tick4.pos = (.9,-5.3)
tick5.pos = (-10,-7)

# image2 tick positions

tick6.pos = (.6,6.1)
tick7.pos = (10.5,-7)
tick8.pos = (11.2,7.6)
tick9.pos = (-10,3.3)
tick10.pos = (-10,-7)

# image3 tick positions

tick11.pos = (.3,-4.4)
tick12.pos = (-9.4,-3.1)
tick13.pos = (-11,7)
tick14.pos = (0,6)
tick15.pos = (2,6)

# image4 tick positions

tick16.pos = (9.5,-6.8)
tick17.pos = (-8.1,-5.3)
tick18.pos = (14,2)
tick19.pos = (-9.7,7.7)
tick20.pos = (9,6)

# Set stim order (because they were not appearing in the order that they appear in the directory

jamie = learning[0]
diver = learning[3]
spy = learning[1]
blonde = learning[2]

learning_set = [jamie, diver, spy, blonde] # list of learning images

jamie_change = change[0]
diver_change = change[3]
spy_change = change[1]
blonde_change = change[2]

change_set = [jamie_change, diver_change, spy_change, blonde_change] # list of change-detection images

horiz_lineA = (-18,0)
horiz_lineB = (18,0)

vert_lineA = (0,-12)
vert_lineB = (0,12)

class Fixation(object): 
    def __init__(self): 
        """Create visual components of the fixation"""
        self.circle  = visual.Circle(win,radius=.5, edges=32, fillColor='white') 
        self.circle2 = visual.Circle(win,radius=.1, edges=32, fillColor='black') 
        self.linev   = visual.Line(win, start=(0,.8), end=(0,-.8), lineWidth=6, lineColor='black') 
        self.lineh   = visual.Line(win, start=(.8,0), end=(-.8,0), lineWidth=6, lineColor='black') 

        self.components = [self.circle,self.linev,self.lineh, self.circle2] 

    def draw(self): 
        """Draw all components of the fixation on the screen.""" 
        [component.draw() for component in self.components] 
        
fix_cross = Fixation()

class Line1(object):
    def __init__(self):
        """create visual components of triangle"""
        self.triangle = visual.ShapeStim(win, units = 'deg', vertices = ((horiz_lineA),(horiz_lineB)) , lineColor='blue')
   
        self.components = [self.triangle]
        
    def draw(self):
        [component.draw() for component in self.components]
        
class Line2(object):
    def __init__(self):
        """create visual components of triangle"""
        self.triangle = visual.ShapeStim(win, units = 'deg', vertices = ((vert_lineA),(vert_lineB)) , lineColor='blue')
   
        self.components = [self.triangle]
        
    def draw(self):
        [component.draw() for component in self.components]
        
#function, look in main exp at the beginning for this

instructions = visual.TextStim(win, text="The current experiment will look to assess your perceptive ability in different VOD environments. You will subsequently view 2 images of All4 and two images of YouTube which each have had 5 different changes made to them. Your task is to identify the 5 changes within each image as quickly as you can! Each trial will consist of a 15 second learning phase in which you must attempt to learn as much about the image as possible. After this, an altered version of the image will replace the one seen previously and you must spot the changes as quickly as you can. To identify a potential change, click on the area you believe to be manipulated and if correct, the choosen area will display a green tick. Once all of the changes are identified the trial will be over\n\n            PRESS SPACEBAR TO CONTINUE", color="black", units="deg", antialias=True,alignHoriz='center',alignVert='center',height = 0.6)
practice_instruction = visual.TextStim(win, text="Here's a trial run so you get a feel for the task ahead; there are only three changes in this practice. Remember, in the first 15 second presentation you need to try and remember as much about the image as you can. Then when the altered image is presented you must click on the areas you think have been changed. Once you've got all three changes, the practice will be over. It's against the clock, so be as quick as you can.\n\n            PRESS SPACEBAR TO CONTINUE", color="black", units="deg", antialias=True,alignHoriz='center',alignVert='center',height = 0.6)
ready = visual.TextStim(win, text="Ready to begin the learning phase? Remember to study the image carefully!\n\n                PRESS SPACEBAR TO BEGIN", color="black", units="deg", antialias=True,alignHoriz='center',alignVert='center',height = 0.6)

def intro_screen():
    instructions.draw()
    win.flip()
    event.waitKeys()
    
def phase_screen():
    ready.draw()
    win.flip()
    event.waitKeys()
    
def practice_screen():
    practice_instruction.draw()
    win.flip()
    event.waitKeys()
        
hoz_line = Line1()
vert_line = Line2()

user_circle = visual.Circle(win, units = 'deg', pos=(0,0), radius=shape_rad, lineColor="red")

rt_list = []

rt_list1 = []
rt_list2 = []
rt_list3 = []
rt_list4 = []

counter_practice = 0
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0

# -------------------- PRACTICE TRIAL --------------------

end_practice = 1
displaycircle1 = 0
displaycircle2 = 0
displaycircle3 = 0

intro_screen()
practice_screen()

while end_practice ==1:
    
    clock.reset()
    while clock.getTime() < default_time:

        prac1.draw()
        win.flip()
            
        allKeys = event.getKeys(keyList = ('escape'))
        for thisKey in allKeys:
            if thisKey == 'escape':
                win.close()
                core.quit()x
    
    clock.reset()
    while clock.getTime() < blank_time:
        
        win.flip()
        
    detection=1
    while detection==1:
                
        prac2.draw()
        prac_circle1.draw()
        prac_circle2.draw()
        prac_circle3.draw()
                
        user_circle.setPos(myMouse.getPos())
        user_circle.draw()
                
        mouse_loc = myMouse.getPos()
        buttons, times = myMouse.getPressed(getTime=True)
        
        if  prac_circle1.contains(myMouse.getPos()):
            if any(myMouse.getPressed()):
                displaycircle1 = 1
                if practice_gate1 == 0:
                    counter_practice += 1
                    practice_gate1 = 1
        else:
            pass
            
        if  prac_circle2.contains(myMouse.getPos()):
            if any(myMouse.getPressed()):
                displaycircle2 = 1
                if practice_gate2 == 0:
                    counter_practice += 1
                    practice_gate2 = 1
        else:
            pass
            
        if  prac_circle3.contains(myMouse.getPos()):
            if any(myMouse.getPressed()):
                displaycircle3 = 1
                if practice_gate3 == 0:
                    counter_practice += 1
                    practice_gate3 = 1
        else:
            pass
                
        allKeys = event.getKeys(keyList = ('escape','space'))
        for thisKey in allKeys:
            if thisKey == 'space':
                end_practice= 0
                detection=0
                
            if thisKey == 'escape':
                win.close()
                core.quit()
                
        if displaycircle1 == 1:
            prac_tick1.draw()
        if displaycircle2 == 1:
            prac_tick2.draw()
        if displaycircle3 == 1:
            prac_tick3.draw()
            
        if counter_practice == 3:
            detection = 0
            end_practice = 0

        win.flip()
    
    clock.reset()
    while clock.getTime() < blank_time:
        
        win.flip()
        

# -------------------- BEGIN EXPERIMENT --------------------

running = 1
displaycircle1 = 0
displaycircle2 = 0
displaycircle3 = 0
displaycircle4 = 0
displaycircle5 = 0

phase_screen()

while running:
    
    image1 = 1
    
    while image1:
        
        clock.reset()
        while clock.getTime() < default_time:

            learning_set[0].draw()
            win.flip()
                
            allKeys = event.getKeys(keyList = ('g','h','escape'))
            for thisKey in allKeys:
                if thisKey == 'escape':
                    win.close()
                    core.quit()
        
        clock.reset()
        while clock.getTime() < blank_time:
            
            win.flip()
            
        detection=1
        rt_clock.reset()
        while detection==1:
                    
            change_set[0].draw()
            circle1.draw()
            circle2.draw()
            circle3.draw()
            circle4.draw()
            circle5.draw()
                    
            user_circle.setPos(myMouse.getPos())
            user_circle.draw()
                    
            mouse_loc = myMouse.getPos()
            buttons, times = myMouse.getPressed(getTime=True)
            
            # check circles for keypress
            
            if  circle1.contains(myMouse.getPos()):
                if any(myMouse.getPressed()):
                    displaycircle1 = 1
                    if gate1 == 0:
                        counter1 += 1
                        gate1 = 1
            else:
                pass
                
            if  circle2.contains(myMouse.getPos()):
                if any(myMouse.getPressed()):
                    displaycircle2 = 1
                    if gate2 == 0:
                        counter1 += 1
                        gate2 = 1
            else:
                pass
                
            if  circle3.contains(myMouse.getPos()):
                if any(myMouse.getPressed()):
                    displaycircle3 = 1
                    if gate3 == 0:
                        counter1 += 1
                        gate3 = 1
            else:
                pass
                
            if  circle4.contains(myMouse.getPos()):
                if any(myMouse.getPressed()):
                    displaycircle4 = 1
                    if gate4 == 0:
                        counter1 += 1
                        gate4 = 1
            else:
                pass
                
            if  circle5.contains(myMouse.getPos()):
                if any(myMouse.getPressed()):
                    displaycircle5 = 1
                    if gate5 == 0:
                        counter1 += 1
                        gate5 = 1
            else:
                pass
                    
            allKeys = event.getKeys(keyList = ('escape','space'))
            for thisKey in allKeys:
                if thisKey == 'space':
                    rt_list.append(rt_clock.getTime())
                    rt_list1.append(rt_clock.getTime())
                    image1 = 0
                    detection = 0
                if thisKey == 'escape':
                    win.close()
                    core.quit()
                    
            if displaycircle1 == 1:
                tick1.draw()
            if displaycircle2 == 1:
                tick2.draw()
            if displaycircle3 == 1:
                tick3.draw()
            if displaycircle4 == 1:
                tick4.draw()
            if displaycircle5 == 1:
                tick5.draw()
                
            if counter1 == 5:
                rt_list.append(rt_clock.getTime())
                image1 = 0
                detection = 0

            win.flip()
        
        clock.reset()
        while clock.getTime() < blank_time:
            
            win.flip()
            
    change_set.pop(0)
    learning_set.pop(0)
    
    # ---------------------------------------- Image 2 ----------------------------------------
    
    image2 = 1
    
    displaycircle1 = 0
    displaycircle2 = 0
    displaycircle3 = 0
    displaycircle4 = 0
    displaycircle5 = 0
    
    while image2:
        
        clock.reset()
        while clock.getTime() < default_time:

            learning_set[0].draw()
            win.flip()
                
            allKeys = event.getKeys(keyList = ('escape'))
            for thisKey in allKeys:
                if thisKey == 'escape':
                    win.close()
                    core.quit()
        
        clock.reset()
        while clock.getTime() < blank_time:
            
            win.flip()
            
        detection=1
        rt_clock.reset()
        while detection==1:
                    
            change_set[0].draw()
            circle6.draw()
            circle7.draw()
            circle8.draw()
            circle9.draw()
            circle10.draw()
                    
            user_circle.setPos(myMouse.getPos())
            user_circle.draw()
                    
            mouse_loc = myMouse.getPos()
            buttons, times = myMouse.getPressed(getTime=True)
            
            # check circles for keypress
            
            if  circle6.contains(myMouse.getPos()):
                if any(myMouse.getPressed()):
                    displaycircle1 = 1
                    if gate6 == 0:
                        counter2 += 1
                        gate6 = 1
            else:
                pass
                
            if  circle7.contains(myMouse.getPos()):
                if any(myMouse.getPressed()):
                    displaycircle2 = 1
                    if gate7 == 0:
                        counter2 += 1
                        gate7 = 1
            else:
                pass
                
            if  circle8.contains(myMouse.getPos()):
                if any(myMouse.getPressed()):
                    displaycircle3 = 1
                    if gate8 == 0:
                        counter2 += 1
                        gate8 = 1
            else:
                pass
                
            if  circle9.contains(myMouse.getPos()):
                if any(myMouse.getPressed()):
                    displaycircle4 = 1
                    if gate9 == 0:
                        counter2 += 1
                        gate9 = 1
            else:
                pass
                
            if  circle10.contains(myMouse.getPos()):
                if any(myMouse.getPressed()):
                    displaycircle5 = 1
                    if gate10 == 0:
                        counter2 += 1
                        gate10 = 1
            else:
                pass
                    
            allKeys = event.getKeys(keyList = ('escape','space'))
            for thisKey in allKeys:
                if thisKey == 'space':
                    rt_list.append(rt_clock.getTime())
                    rt_list2.append(rt_clock.getTime())
                    image2 = 0
                    detection = 0
                if thisKey == 'escape':
                    win.close()
                    core.quit()
                    
            if displaycircle1 == 1:
                tick6.draw()
            if displaycircle2 == 1:
                tick7.draw()
            if displaycircle3 == 1:
                tick8.draw()
            if displaycircle4 == 1:
                tick9.draw()
            if displaycircle5 == 1:
                tick10.draw()
                
            if counter2 == 5:
                rt_list.append(rt_clock.getTime())
                image2 = 0
                detection = 0

            win.flip()
        
        clock.reset()
        while clock.getTime() < blank_time:
            
            win.flip()
            
    change_set.pop(0)
    learning_set.pop(0)
    
    # -------------------------------- Image3 ----------------------------------
    
    image3 = 1
    
    displaycircle1 = 0
    displaycircle2 = 0
    displaycircle3 = 0
    displaycircle4 = 0
    displaycircle5 = 0
    
    running = 0
    
    while image3:
        
        clock.reset()
        while clock.getTime() < default_time:

            learning_set[0].draw()
            win.flip()
                
            allKeys = event.getKeys(keyList = ('escape'))
            for thisKey in allKeys:
                if thisKey == 'escape':
                    win.close()
                    core.quit()
        
        clock.reset()
        while clock.getTime() < blank_time:
            
            win.flip()
            
        detection=1
        rt_clock.reset()
        while detection==1:
                    
            change_set[0].draw()
            circle11.draw()
            circle12.draw()
            circle13.draw()
            circle14.draw()
            circle15.draw()
                    
            user_circle.setPos(myMouse.getPos())
            user_circle.draw()
                    
            mouse_loc = myMouse.getPos()
            buttons, times = myMouse.getPressed(getTime=True)
            
            # check circles for keypress
            
            if  circle11.contains(myMouse.getPos()):
                if any(myMouse.getPressed()):
                    displaycircle1 = 1
                    if gate11 == 0:
                        counter3 += 1
                        gate11 = 1
            else:
                pass
                
            if  circle12.contains(myMouse.getPos()):
                if any(myMouse.getPressed()):
                    displaycircle2 = 1
                    if gate12 == 0:
                        counter3 += 1
                        gate12 = 1
            else:
                pass
                
            if  circle13.contains(myMouse.getPos()):
                if any(myMouse.getPressed()):
                    displaycircle3 = 1
                    if gate13 == 0:
                        counter3 += 1
                        gate13 = 1
            else:
                pass
                
            if  circle14.contains(myMouse.getPos()):
                if any(myMouse.getPressed()):
                    displaycircle4 = 1
                    if gate14 == 0:
                        counter3 += 1
                        gate14 = 1
            else:
                pass
                
            if  circle15.contains(myMouse.getPos()):
                if any(myMouse.getPressed()):
                    displaycircle5 = 1
                    if gate15 == 0:
                        counter3 += 1
                        gate15 = 1
            else:
                pass
                    
            allKeys = event.getKeys(keyList = ('escape','space'))
            for thisKey in allKeys:
                if thisKey == 'space':
                    rt_list.append(rt_clock.getTime())
                    rt_list3.append(rt_clock.getTime())
                    image3 = 0
                    detection = 0
                if thisKey == 'escape':
                    win.close()
                    core.quit()
                    
            if displaycircle1 == 1:
                tick11.draw()
            if displaycircle2 == 1:
                tick12.draw()
            if displaycircle3 == 1:
                tick13.draw()
            if displaycircle4 == 1:
                tick14.draw()
            if displaycircle5 == 1:
                tick15.draw()
                
            if counter3 == 5:
                rt_list.append(rt_clock.getTime())
                image3 = 0
                detection = 0

            win.flip()
        
        clock.reset()
        while clock.getTime() < blank_time:
            
            win.flip()
            
    change_set.pop(0)
    learning_set.pop(0)
    
    # -------------------------------- Image4 ----------------------------------
    
    image4 = 1
    
    displaycircle1 = 0
    displaycircle2 = 0
    displaycircle3 = 0
    displaycircle4 = 0
    displaycircle5 = 0
    
    running = 0
    
    while image4:
        
        clock.reset()
        while clock.getTime() < default_time:

            learning_set[0].draw()
            win.flip()
                
            allKeys = event.getKeys(keyList = ('escape'))
            for thisKey in allKeys:
                if thisKey == 'escape':
                    win.close()
                    core.quit()
        
        clock.reset()
        while clock.getTime() < blank_time:
            
            win.flip()
            
        detection=1
        rt_clock.reset()
        while detection==1:
                    
            change_set[0].draw()
            circle16.draw()
            circle17.draw()
            circle18.draw()
            circle19.draw()
            circle20.draw()
                    
            user_circle.setPos(myMouse.getPos())
            user_circle.draw()
                    
            mouse_loc = myMouse.getPos()
            buttons, times = myMouse.getPressed(getTime=True)
            
            # check circles for keypress
            
            if  circle16.contains(myMouse.getPos()):
                if any(myMouse.getPressed()):
                    displaycircle1 = 1
                    if gate16 == 0:
                        counter4 += 1
                        gate16 = 1
            else:
                pass
                
            if  circle17.contains(myMouse.getPos()):
                if any(myMouse.getPressed()):
                    displaycircle2 = 1
                    if gate17 == 0:
                        counter4 += 1
                        gate17 = 1
            else:
                pass
                
            if  circle18.contains(myMouse.getPos()):
                if any(myMouse.getPressed()):
                    displaycircle3 = 1
                    if gate18 == 0:
                        counter4 += 1
                        gate18 = 1
            else:
                pass
                
            if  circle19.contains(myMouse.getPos()):
                if any(myMouse.getPressed()):
                    displaycircle4 = 1
                    if gate19 == 0:
                        counter4 += 1
                        gate19 = 1
            else:
                pass
                
            if  circle20.contains(myMouse.getPos()):
                if any(myMouse.getPressed()):
                    displaycircle5 = 1
                    if gate20 == 0:
                        counter4 += 1
                        gate20 = 1
            else:
                pass
                    
            allKeys = event.getKeys(keyList = ('escape','space'))
            for thisKey in allKeys:
                if thisKey == 'space':
                    rt_list.append(rt_clock.getTime())
                    rt_list4.append(rt_clock.getTime())
                    image4 = 0
                    detection = 0
                if thisKey == 'escape':
                    win.close()
                    core.quit()
                    
            if displaycircle1 == 1:
                tick16.draw()
            if displaycircle2 == 1:
                tick17.draw()
            if displaycircle3 == 1:
                tick18.draw()
            if displaycircle4 == 1:
                tick19.draw()
            if displaycircle5 == 1:
                tick20.draw()

            if counter4 == 5:
                rt_list.append(rt_clock.getTime())
                image4 = 0
                detection = 0
                
            win.flip()
        
        clock.reset()
        while clock.getTime() < blank_time:
            
            win.flip()
            
myText = "Image  TIME"

avg_youtube = []
avg_youtube.append(rt_list[0])
avg_youtube.append(rt_list[1])
avg_youtube = sum(avg_youtube) / len(avg_youtube)
avg_youtube = str(round(avg_youtube, 2))

avg_allfour = []
avg_allfour.append(rt_list[2])
avg_allfour.append(rt_list[3])
avg_allfour = sum(avg_allfour) / len(avg_allfour)
avg_allfour = str(round(avg_allfour, 2))

rt_one = rt_list[0]
rt_two = rt_list[1]
rt_three = rt_list[2]
rt_four = rt_list[3]

rt_one=str(round(rt_one, 2))
rt_two=str(round(rt_two, 2))
rt_three=str(round(rt_three, 2))
rt_four=str(round(rt_four, 2))

percent_correct_list = counter1 + counter2 + counter3 + counter4

percent_correct = (percent_correct_list / float(20)) * 100
percent_correct = str(percent_correct)

Results_title = visual.TextStim(win, text=myText, color="red", pos=(0,6.5),antialias=True,wrapWidth=None)
rtone         = visual.TextStim(win,   text="1:       " + rt_one, color="black",   pos=(0,5),    antialias=True)
rtthree       = visual.TextStim(win, text="2:       " + rt_three, color="black", pos=(0,.5),    antialias=True)
average_youtube = visual.TextStim(win, text="Avg YouTube: " + avg_youtube, color="green", pos=(0,2),antialias=True,wrapWidth=None)

rttwo = visual.TextStim(win,   text="3:       " + rt_two, color="black",   pos=(0,3.5),  antialias=True)
rtfour = visual.TextStim(win,  text="4:       " + rt_four, color="black",  pos=(0,-1),  antialias=True)
average_allfour = visual.TextStim(win, text="Avg AllFour: " + avg_allfour, color="green", pos=(0,-2.5),antialias=True,wrapWidth=None)


percent_correct = visual.TextStim(win, text="Correct:      " + percent_correct + "%", color="blue", pos=(0,-4),antialias=True)

results_screen = 1
while results_screen:
    
    Results_title.draw()
    win.flip()
    core.wait(1)
    
    Results_title.draw()
    rtone.draw()
    win.flip()
    core.wait(1)
    
    Results_title.draw()
    rtone.draw()
    rtthree.draw()
    win.flip()
    core.wait(1)
    
    Results_title.draw()
    rtone.draw()
    average_youtube.draw()
    rtthree.draw()
    win.flip()
    core.wait(1)
    
    Results_title.draw()
    average_youtube.draw()
    rtone.draw()
    rttwo.draw()
    rtthree.draw()
    win.flip()
    core.wait(1)
    
    Results_title.draw()
    average_youtube.draw()
    rtone.draw()
    rttwo.draw()
    rtthree.draw()
    rtfour.draw()
    win.flip()
    core.wait(1)
    
    Results_title.draw()
    average_youtube.draw()
    rtone.draw()
    rttwo.draw()
    rtthree.draw()
    rtfour.draw()
    average_allfour.draw()
    win.flip()
    core.wait(1)
    
    wait_results = 1
    while wait_results == 1:
        Results_title.draw()
        average_youtube.draw()
        average_allfour.draw()
        rtone.draw()
        rttwo.draw()
        rtthree.draw()
        rtfour.draw()
        percent_correct.draw()
    
        allKeys = event.getKeys(keyList = ('escape','space'))
        for thisKey in allKeys:
            if thisKey == 'escape' or thisKey == 'space':
                wait_results = 0
                win.close()
                core.quit()
                
        win.flip()
