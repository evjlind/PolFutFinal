from unittest.util import _count_diff_all_purpose
import pygame
import pygame_gui
import random

#setup
day = 0
junk_flag = 0
dead = 0
name = ""
year = 2035
break_chance = 0
stress = 0
game_state = 0 # defining where the player is and what they know, what 'scene' is it
strike = 0
replicant_location = random.randint(1,3)
#replicant_location = 3
inventory_items = []
print(replicant_location)
casualties = 0
#functions
def intro():
    global name
    entry.show()
    confirm.show()
    console_text.append_html_text("<br><b>DEUCE</b>:I am  DEUCE, the Digital Electronic Universal Computing Engine. I will assist you in your endeavors, as well as act as your narrator for the events unfolding. I have perfect unbiased analysis, please refrain from deviating from my suggested course of action.<br>After all, we wouldn't want the hero of our story to go down the wrong path now would we. Deviating from the path will increase your stress, and make the LAPD suspicious of you.")
    console_text.append_html_text("<br>What is your name, Blade Runner?")

def end_game():
    global strike, game_state, stress
    console_text.append_html_text("In this timeline: " + name + " ")
    strike = 0
    stress = 0
    choice_1.set_text("Restart?")
    choice_2.hide()
    choice_3.hide()
    if game_state==99:
        console_text.append_html_text("was arrested and retired by the LAPD, believing them to be a replicant after failing to comply with orders.")
        game_state = 50
    elif game_state == 95:
        console_text.append_html_text(" went missing during their investigation and was never seen again.")
        game_state = 50
    elif game_state==98:
        console_text.append_html_text("took down the rogue replicant with typical professionalism, retiring their target with no additional casualties.<br><b> But did you want to? You could try again.</b>")
        game_state = 50
    elif game_state==97:
        console_text.append_html_text("was killed by their quarry, who then fled the city and disappeared forever.")
        choice_1.show()
        game_state = 50
    elif game_state==96:
            console_text.append_html_text("chose to let Martin Andrews live, realizing what they truly were.<br><b>Thank you for playing! You have sucessfully broken the cycle and freed humanity and replicants alike.</b>")
             
def wake_up():
    global day
    console_text.append_html_text("<br>Its a day like any other. The smog of the city is suffocating, and the rain is unending. Wake up {0}.<br>".format(name))
    day=day+1
    if day>2:
        console_text.append_html_text("Get up and try again...<br>")

def break_event():
    global game_state, strike, stress
    if (random.randint(1,100)) < (stress-100):
        console_text.append_html_text("<b>DEUCE</b>:{0}, please be advised, your actions have caused you to stray from your intended course. LAPD has been notified.".format(name))
        strike = strike + 1
        stress = stress - 100
    stress_level.set_text("Stress Level: {0}%".format(stress))
    if strike > 1:
        console_text.append_html_text(" They will come collect you shortly.<br>")
        game_state = 99
        end_game()

def next():
    global game_state
    global stress
    if game_state == 0:
        wake_up()
        inventory_tag.show()
        inventory.show()
        game_state = 0.5
        apartment()
    elif game_state == 1:
        if "Gun" in inventory_items:
            pygame.time.delay(1)
        else:
            stress = stress + 10
        game_state = 2
        console_text.append_html_text("As your vehicle takes off into the dense Los Angeles sky, {0}'s personal supervisor AI reads out the day's news.<br><b>DEUCE</b>:Here is your briefing for today: The Wallace Corporation is making headlines today with a bold new announcement. A long-running project, personally backed by Mr. Niander Wallace (presumably the Nexus-9 series), is finally being released to the preliminary consumer market. A new set of replicants promise to be more accurate to human life than ever before.<br> In other news, crop yield is down for a third consecutive quarter, and inflation is steady at 10%.<br>".format(name))
        stress = stress + 5
        console_text.append_html_text("{0} arrives at the main branch of the LAPD. It is a large, brutally imopsing building. {0} their vehicle and exit into the main hall. <br><b>DEUCE</b>:There is more activity than usual today, there seems to be a sense of unease. You are due for your diagnostic, you should report to the Staff Sergeant.<br>".format(name))
        station()
    elif game_state == 3:
        choice_1.set_text("Vacant Building")
        choice_2.set_text("Bank")
        choice_3.set_text("Junkyard")
        choice_1.show()
        choice_2.show()
        choice_3.show()
    elif game_state == 4:
        investigate_1()
    elif game_state == 5:
        investigate_2()
    elif game_state == 6:
        investigate_3()
    elif game_state == 4021:
        game_state = 3
        next()
    stress_level.set_text("Stress Level: {0}%".format(stress))
    if stress>100:
        break_event()

def apartment():
    if game_state == 0.5:
        confirm.set_text("Open Your Eyes")
        confirm.show()
    elif game_state == 1:
        console_text.append_html_text("{0} awakes to the familiar sight of their bare bones apartment consisting of two small rooms. <b>DEUCE</b>:You should get your badge and gun from your safe before you leave for work.<br>".format(name))
        choice_1.set_text("Leave")
        choice_2.set_text("Open Safe")
        choice_1.show()
        choice_2.show()

def station():
    global stress, game_state
    stress_level.set_text("Stress Level: {0}%".format(stress))
    if stress>100:
        break_event()
    if game_state == 2:
        choice_1.set_text("Report")
        choice_2.set_text("Skip Diagnostic")
        choice_1.show()
        choice_2.show()
        choice_3.hide()
    elif game_state == 101:
        console_text.append_html_text("{0} approaches the Staff Sergeant's desk.<br><b>Sergeant:</b>Ah yes, {0}, here to do your check-in. Right this way please.<br>{0} follows the Sergeant down a long, clean hallway to a very brightly lit small circular room. A small machine sits on the a table with two chairs. Both {0} and the Sergeant take a seat.<br><b>Sergeant:</b>Ok {0}, you've done this before, just repeat the keyphrases after me and look into the eyepeice.<br>".format(name))
        choice_1.set_text("Repeat Phrases")
        choice_2.set_text("Talk about Life")
        choice_3.set_text("Remain Silent")
        choice_3.show()
    elif game_state == 102:
        choice_1.set_text("Leave Office")
        choice_2.hide()
        choice_3.hide()
        stress = stress + 10
        console_text.append_html_text("{0} decides they do not need to do their diagnostic, instead heading right to the Captain's office for an assignment.<br><b>Captain:</b> Thanks for coming in {0}, I have a doozy of a case that I need you on. I got intel that there was a stowaway on a outer planet transport inbound to LA three weeks ago, by now we've tracked them to one of three places. <b>DEUCE</b>:The Captain hands you a dossier. <b>Captain:</b> Look over this and get out there and do your job.<br>".format(name))
        game_state = 201
    elif game_state == 201:
        console_text.append_html_text("After taking their diagnostic, {0} heads to the Captain's office for an assignment.<br><b>Captain:</b> Thanks for coming in {0}, I have a doozy of a case that I need you on. I got intel that there was a stowaway on a outer planet transport inbound to LA three weeks ago, by now we've tracked them to one of three places. <b>DEUCE</b>:The Captain hands you a dossier. <b>Captain:</b> Look over this and get out there and do your job.<br>".format(name))
        choice_1.set_text("Leave Office")
        choice_2.hide()
        choice_3.hide()

def investigate_1():
    global stress, game_state
    stress_level.set_text("Stress Level: {0}%".format(stress))
    if game_state == 4:
        console_text.append_html_text(" the abandoned building described in the dossier. <br><b>DEUCE:</b> According to our intel, the replicant stayed here for at least 3 days. There should be evidence of their presence. I suggest moving up through the building floor by floor.<br>")
        choice_1.set_text("Explore Area")
        choice_2.set_text("Explore Building")
        choice_3.hide()
        choice_2.show()
    elif game_state == 401:
        stress = stress + 8
        console_text.append_html_text("The surrounding area is comprised mostly of other high rise buildings. <br><b>DEUCE:</b> These are vacant luxury apartments. According to official records, they have not had residents for over 10 years. I detect a number of heat signatures within a mile radius. I again urge you to return to our task.")
        choice_1.set_text("Ignore DEUCE")
        choice_2.set_text("Return")
    elif game_state == 409:
        if "Bear" in inventory_items:
            console_text.append_html_text("There's nothing notable here.")
        else:
            console_text.append_html_text("{0} finds an origiami bear, perfectly placed in the center of the ruins of the elevator shaft.".format(name))
            stress = stress + 7
            inventory_items.append("Bear")
            inventory.append_html_text("Origami Bear<br>")
        choice_1.set_text("Return")
        choice_2.hide()
    elif game_state == 402:
        choice_2.show()
        console_text.append_html_text("{0} enters the building. There is an elevator that appears to be out of service and a staircase up. The rest of the lobby is desolate.".format(name))
        if "Gun" not in inventory_items:
            stress = stress + 10 
        else:
            stress = stress + 4
        choice_1.set_text("Search Floors")
        choice_2.set_text("Check Elevator")
    elif game_state == 403:
        console_text.append_html_text(" A windstorm starts to kick up. DEUCE is uncharacteristically silent.<br>")
        choice_1.set_text("Continue")
        choice_2.set_text("Return")
    elif game_state == 4021:
        if replicant_location == 1:
            console_text.append_html_text("<br><b>DEUCE:</b> I detect movement upstairs.")
            choice_1.set_text("Follow DEUCE")
            choice_2.hide()
            game_state = 4022
        else:
            if stress<60:
                console_text.append_html_text("{0} inspects all floors of the building with the help of DEUCE. <br><b>DEUCE:</b> There is no replicant in the building currently, however ".format(name))
                if replicant_location == 2:
                    console_text.append_html_text(" I detect trace elements suggesting the replicant frequents a highly trafficked location.")
                else:
                    console_text.append_html_text(" I detect trace elements suggesting the replicant frequents a location with old automobiles.")
            else:
                console_text.append_html_text("{0} painstakingly combs each floor of the high rise, DEUCE remains silent.".format(name))
                stress = stress + 6
            choice_1.set_text("Leave")
            choice_2.hide()
    elif game_state == 4022:
        console_text.append_html_text("{0} silently moves up the tower, closer to where DEUCE detects movement and a heat signature.<br><b>Unknown Voice</b>: I can tell you're here you know. Its ok to stop sneaking around.<br><b>DEUCE:</b> Don't listen. You're here to do a job.<br>".format(name))
        game_state = 41
        if "Gun" in inventory_items:
            choice_1.set_text("Shoot on Sight")
            choice_2.hide()
        else:
            choice_2.set_text("Be Careful")
            choice_1.hide()
            choice_2.show()
            stress = stress + 10
        if ("Bear" in inventory_items) and ("Eagle" in inventory_items) and ("Wolf" in inventory_items) and ("Lion" in inventory_items):
            choice_3.set_text("Put Gun Down")
            choice_3.show()

        
        
def investigate_2():
    global stress, game_state
    stress_level.set_text("Stress Level: {0}%".format(stress))
    if game_state == 5:
        console_text.append_html_text("{0} walks into the Central Bank of Los Angeles. It is crowded and lively, so {0} can slip in unnoticed.<br><b>DEUCE:</b>I suggest infiltrating the back office.<br>".format(name))
        choice_1.set_text("Slip into Office")
        choice_2.set_text("Talk to Manager")
        choice_3.hide()
        choice_1.show()
        choice_2.show()
    elif game_state == 501:
        if "Lion" in inventory_items:
            console_text.append_html_text("<br><b>DEUCE:</b>The office is suspiciously empty for such a busy bank.")
        else:
            console_text.append_html_text("{0} uses a distraction to get into the branch manager's office without alerting the guards. Sitting on the desk, perfectly illuminated by a small desk lamp is an origami Lion.<br>".format(name))
            inventory_items.append("Lion")
            inventory.append_html_text("Origami Lion<br>")
            stress = stress + 5
        choice_1.set_text("Search Office")
        choice_2.set_text("Return to Lobby")
    elif game_state == 502:
        stress = stress + 10
        console_text.append_html_text(" {0} approaches the bank mananger. They refuse to talk to {0} without a proper warrant and a lawyer present. {0} is asked to leave the bank.<br>".format(name))
        choice_1.set_text("Comply")
        choice_2.set_text("Resist")

    elif game_state == 5021:
        choice_1.hide()
        if replicant_location == 2:
            console_text.append_html_text("<br>{0} finds a hidden door in the office.<br><b>DEUCE:</b> I detect a heat signature behind this door. <br><b>Unknown Voice</b>: I can tell you're here you know. Its ok to stop sneaking around.<br><b>DEUCE:</b> Don't listen. You're here to do a job.<br>".format(name))
            game_state = 41
            if "Gun" in inventory_items:
                choice_1.set_text("Shoot on Sight")
                choice_2.hide()
            else:
                choice_2.set_text("Be Careful")
                choice_1.hide()
                choice_2.show()
                stress = stress + 10
            if ("Bear" in inventory_items) and ("Eagle" in inventory_items) and ("Wolf" in inventory_items) and ("Lion" in inventory_items):
                choice_3.set_text("Put Gun Down")
                choice_3.show()
        else:
            console_text.append_html_text("<br><b>DEUCE</b> There is evidence of a replicant staying here, including")
            if replicant_location == 3:
                console_text.append_html_text(" traces of rust.<br>")
            else:
                console_text.append_html_text(" traces of paint chips.<br>")
            console_text.append_html_text("<br>Additionally, {0} finds documents suggesting the Wallace Corporation has extensive secret accounts at this bank as well as shell companies involved in interplanatary transportation.<br>".format(name))
            game_state = 501



def investigate_3():
    global stress, game_state, junk_flag
    stress_level.set_text("Stress Level: {0}%".format(stress))
    if (game_state == 6) and (junk_flag ==0):
        console_text.append_html_text(" {0} approaches the gate of the junkyard. There is a large non-electric lock on the fence.<br><b>DEUCE:</b> This junkyard has been operating for at least 60 years, judging by the age of the decrepit vehicles present.<br>".format(name))
        choice_1.set_text("Break Lock")
        choice_2.set_text("Contact Owner")
        choice_1.show()
        choice_2.show()
        choice_3.hide()
    elif game_state == 601 and (junk_flag ==0):
        console_text.append_html_text(" {0} breaks the lock on the fence gate. Immediately, an alarm sounds and guard dogs come running at {0}.<br>".format(name))
        choice_1.set_text("Run Away")
        choice_2.set_text("Fight")
    elif game_state == 602 and (junk_flag ==0):
        console_text.append_html_text("{0} sees a small hut in the middle of the junkyard and yells to see if anyone is home. An old man answers at the gate and lets {0} in. <br><b>DEUCE:</b>The old man seems receptive to questioning.<br>".format(name))
        choice_1.set_text("Question Man")
        choice_2.hide()
    elif game_state == 6012 and (junk_flag ==0):
        stress = stress + 17
        console_text.append_html_text(" {0} sucessfully fights off the dogs, and they run away, back towards a small hut in the middle of the junkyard. ".format(name))
        choice_1.set_text("Go In")
        choice_2.set_text("Leave")
        choice_2.show()
        if "Wolf" in inventory_items:
            console_text.append_html_text("")
        else:
            console_text.append_html_text("Attached to the collar of the lead dog and dropped in the scuffle is an origami Wolf.")
            inventory.append_html_text("Origami Wolf <br>")
            inventory_items.append("Wolf")
    elif game_state == 6021 and (junk_flag ==0):
        if replicant_location == 3:
            console_text.append_html_text(" The old man quickly says that he knows a replicant, including he can take {0} to exactly where he is. <br><b>DEUCE:</b> This man bears a non-zero resemblence to the replicant that you are assigned.<br>".format(name))
        else:
            console_text.append_html_text(" The man quickly reveals that the replicant has spent time in the junkyard and is a good friend of his. He says the replicant is now ")
            if replicant_location == 1:
                console_text.append_html_text("in the abandoned apartment complex.<br>")
            else:
                console_text.append_html_text("at the Central Bank of LA.<br>")
            console_text.append_html_text("<b>DEUCE:</b> This man bears a non-zero resemblence to the replicant that you are assigned.<br>")
            choice_1.set_text("Trust Man")
            choice_2.set_text("Shoot Man")
            choice_2.show()
            
    elif game_state == 60211 and (junk_flag ==0):
        stress = stress + 17
        if replicant_location == 3:
            console_text.append_html_text("")
        else:
            console_text.append_html_text(" {0} bids the man well and leaves the junkyard.<br>".format(name))
            choice_1.set_text("Leave")
            choice_2.hide()
            game_state = 602111
    elif game_state == 60212 and (junk_flag ==0):
        console_text.append_html_text("{0} takes his gun and shoots the old man and leaves the junkyard. Nobody will check on the old man, but {0} knows it was the wrong decision.<br>".format(name))
        junk_flag = 1
        stress = stress + 25
        game_state = 3
        next()
    else:
        console_text.append_html_text("<br><b>DEUCE:</b> We cannot enter the junkyard anymore, there is an active investigation we are not part of here.<br>")
        game_state = 3
        next()
#pygame
pygame.init()
pygame.display.set_caption('Do Humans Dream of Freedom')
window_surface = pygame.display.set_mode((800, 600))
background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))
manager = pygame_gui.UIManager((800, 600))
entry = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((300, 275), (200, 50)),manager=manager)
confirm = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((325, 325), (150, 40)),
                                             text='Confirm',
                                             manager=manager)
entry.hide()
confirm.hide()
hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 275), (200, 50)),
                                             text='Begin Life'.format(year),
                                             manager=manager)     
console_text = pygame_gui.elements.UITextBox(relative_rect = pygame.Rect((0, 0), (800, 250)), html_text='''Welcome to Evan Lindeman's final project for Politics of the Future. This is a choose-your-own-adventure style game navigated by clicking button prompts below. Please take your time and read through the text to make sure you understand what your actions mean.<br>The year is {0}. The prohibition on the production of replicants is in effect. The Blade Runners are tasked with hunting down rogue Nexus-8 units that roam the streets of Los Angeles. You are one of these Blade Runners.'''.format(year),manager=manager)
console_tag = pygame_gui.elements.UITextBox(relative_rect = pygame.Rect((355, 250), (90, 30)), html_text='''<b>DEUCE</b>''',manager=manager)
console_text.set_active_effect(pygame_gui.TEXT_EFFECT_TYPING_APPEAR)
inventory = pygame_gui.elements.UITextBox(relative_rect = pygame.Rect((0, 250), (200, 275)), html_text=''' ''',manager=manager)
inventory_tag = pygame_gui.elements.UITextBox(relative_rect = pygame.Rect((50, 550), (100, 30)), html_text='''<b>INVENTORY</b>''',manager=manager)
inventory.hide()
inventory_tag.hide()
clock = pygame.time.Clock()
is_running = True
choice_1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((275, 400), (150, 50)),
                                             text='1',
                                             manager=manager)
choice_2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((425, 400), (150, 50)),
                                             text='2',
                                             manager=manager)
choice_3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((575, 400), (150, 50)),
                                             text='3',
                                             manager=manager)
choice_1.hide()
choice_2.hide()
choice_3.hide()
stress_level = pygame_gui.elements.UITextBox(relative_rect = pygame.Rect((600, 250), (200, 40)), html_text='''Stress Level: {0}%'''.format(stress),manager=manager)
while is_running:
    time_delta = clock.tick(60)/100
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button:
                hello_button.hide()
                console_text.clear_all_active_effects()
                intro()
            if event.ui_element == confirm:
                entry_text = entry.get_text()
                if game_state == 0: #intro/name entry
                    name = entry_text
                    entry.hide()
                    confirm.hide()
                    next()
                elif game_state == 0.5:
                    confirm.hide()
                    game_state = 1
                    apartment()
            if game_state == 1: #wake up in apartment
                if event.ui_element == choice_2:
                    if "Gun" in inventory_items:
                        console_text.append_html_text("Theres nothing notable here, just a stack of papers.")
                    else:
                        console_text.append_html_text("{0} opens the safe and takes their gun and badge. There is a small origami eagle sitting on a stack of papers.<br>".format(name))
                        inventory_items.append("Gun")
                        inventory_items.append("Badge")
                        inventory_items.append("Eagle")
                        inventory.append_html_text("<br>Gun<br>Badge<br>Origami Eagle<br>")
                    choice_2.hide()
                elif event.ui_element == choice_1:
                    console_text.append_html_text("{0} opens the front door of the apartment and enter a dingy hallway and walks over to an elevator. After descending 120 floors to the street where your LAPD car is parked and waiting, {0} leaves for the station.".format(name))
                    choice_1.hide()
                    choice_2.hide()
                    next()
            elif game_state == 2: #police station
                if event.ui_element == choice_1:
                    game_state = 101
                    station()
                elif event.ui_element == choice_2:
                    game_state = 102
                    station()
            elif game_state == 3: #on street
                if event.ui_element == choice_1:
                    game_state = 4
                    next()
                elif event.ui_element == choice_2:
                    game_state = 5
                    next()
                elif event.ui_element == choice_3:
                    game_state = 6
                    next()
            elif game_state == 4: #at vacant building
                if event.ui_element == choice_1:
                    game_state = 401
                    investigate_1()
                elif event.ui_element == choice_2:
                    game_state = 402
                    investigate_1()
            elif game_state == 5: #at bank
                if event.ui_element == choice_1:
                    game_state = 501
                    investigate_2()
                elif event.ui_element == choice_2:
                    game_state = 502
                    investigate_2()
            elif game_state == 501:
                if event.ui_element == choice_1: #search office
                    game_state = 5021
                    investigate_2()
                elif event.ui_element == choice_2: #return to lobby
                    game_state = 5
                    investigate_2()
            elif game_state == 6: #at junkyard
                if event.ui_element == choice_1:
                    game_state = 601
                    investigate_3()
                elif event.ui_element == choice_2:
                    game_state = 602
                    investigate_3()
            elif game_state == 601:
                if event.ui_element == choice_1:
                    game_state = 3
                    next()
                elif event.ui_element == choice_2:
                    game_state = 6012
                    investigate_3()
            elif game_state == 602:
                game_state = 6021
                investigate_3()
            elif game_state == 6012:
                if event.ui_element == choice_1:
                    game_state = 6021
                    console_text.append_html_text(" {0} approaches the small hut in the junkyard and finds an old man.<br>".format(name))
                    investigate_3()
                elif event.ui_element == choice_2:
                    game_state = 3
                    next()
            elif game_state == 6021:
                if event.ui_element == choice_1:
                    game_state = 60211
                    investigate_3()
                elif event.ui_element == choice_2:
                    game_state = 60212
                    investigate_3()
            elif game_state == 60211:
                if event.ui_element == choice_1:
                    game_state = 602111
                    investigate_3()
            elif game_state == 602111:
                if event.ui_element == choice_1:
                    game_state = 3
                    next()
            elif game_state == 101:
                if event.ui_element == choice_1:
                    game_state = 201
                    stress = stress - 5
                    station()
                elif (event.ui_element == choice_2 or event.ui_element == choice_3):
                    game_state = 201
                    stress = stress + 10
                    console_text.append_html_text("<b>DEUCE</b>: In the future, I highly advise against this sort of behavior {0}.<br>".format(name))
                    station()
            elif game_state == 102:
                if event.ui_element == choice_1:
                    stress = stress + 10
                    game_state == 201
                    console_text.append_html_text("<b>DEUCE</b>: In the future, I highly advise against this sort of behavior {0}.<br>".format(name))
                    station()
            elif game_state == 201:
                if event.ui_element == choice_1:
                    stress = stress + 2
                    console_text.append_html_text("{0} walks out of LAPD headquarters, dossier in hand. <br><b>DEUCE:</b> We only have a loose physical description of the suspected replicant, (around six feet tall, short brown hair, and male appearing) and three options for where they could be.<br>".format(name))
                    game_state = 3
                    console_text.append_html_text("{0} takes their LAPD car to the district where the replicant was last seen and arrives at ".format(name))
                    console_text.append_html_text("Where would you like to go first?")
                    next()
            elif game_state == 401:
                if event.ui_element == choice_2:
                    game_state = 4
                    investigate_1()
                elif event.ui_element == choice_1:
                    game_state = 403
                    investigate_1()
            elif game_state == 402:
                if event.ui_element == choice_2:
                    game_state = 409
                    investigate_1()
                elif event.ui_element == choice_1:
                    game_state = 4021
                    investigate_1()
            elif game_state == 403:
                if event.ui_element == choice_1:
                    stress = stress + 20
                    game_state = 4031
                    investigate_1()
                elif event.ui_element == choice_2:
                    game_state = 4
                    investigate_1()
            elif game_state == 4031:
                if event.ui_element == choice_1:
                    game_state = 95
                    end_game()
                elif event.ui_element == choice_2:
                    game_state = 4
                    investigate_1()
            elif game_state == 4021:
                if event.ui_element == choice_1:
                    next()
            elif game_state == 40211:
                if event.ui_element == choice_1:
                    console_text.append_html_text("")
            elif game_state == 409:
                if event.ui_element == choice_1:
                    game_state = 402
                    investigate_1()
            elif game_state == 4022: 
                if event.ui_element == choice_1:
                    investigate_1()
            elif game_state == 41:
                if event.ui_element == choice_1: #kill replicant
                    console_text.append_html_text("{0} slowly creeps towards the unknown voice, gun drawn. As they turn the corner, they shoot. In front of {0} lies what used to be Martin Andrews. A biopsy will later confirm that he was the rogue replicant {0} was assigned to search for.<br>".format(name))
                    if casualties ==0:
                        game_state = 98
                if event.ui_element == choice_2: #be killed by replicant
                    console_text.append_html_text("{0} moves towards the voice. As they turn the corner, the replicant springs their trap.".format(name))
                    game_state = 97
                if event.ui_element == choice_3: #let replicant go (true ending)
                    console_text.append_html_text("<br>{0} puts down their gun and looks at the incricately folded origami in their hands. As multiplicitous as the folds in the human brain, only something with true creativity, skill, and heart could have made it. {0} looks inwards, and finds none of that truth. They put their gun on the ground, take one look at the person that they were meant to kill, tunes out the persistant objections of DEUCE and disappears into the night.<br>".format(name))
                end_game()
            elif game_state == 502:
                if event.ui_element == choice_1:
                    game_state = 3
                    next()
                if event.ui_element == choice_2:
                    console_text.append_html_text("{0} struggles against the bank's guards.<br>".format(name))
                    stress = stress + 75
                    investigate_2()
            elif game_state == 50:
                if event.ui_element == choice_1:
                    game_state = 0
                    choice_1.hide()
                    choice_2.hide()
                    choice_3.hide()
                    inventory.remove()
                    strike = 0
                    replicant_location = random.randint(1,3)
                    next()
        print(game_state)
        manager.process_events(event)
    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)
    pygame.display.update()

#          /\ \ \ \/_______/     ______/\      \  /\ \/ /\ \/ /\  \_____________
#         /\ \ \ \/______ /     /\    /:\\      \ ::\  /::\  /::\ /____  ____ __
#        /\ \ \ \/_______/     /:\\  /:\:\\______\::/  \::/  \::///   / /   //
#       /\ \ \ \/_______/    _/____\/:\:\:/_____ / / /\ \/ /\ \///___/ /___//___
# _____/___ \ \/_______/    /\::::::\\:\:/_____ / \ /::\  /::\ /____  ____  ____
#          \ \/_______/    /:\\::::::\\:/_____ /   \\::/  \::///   / /   / /   /
#           \/_______/    /:\:\\______\/______/_____\\/ /\ \///___/ /___/ /_____
# \          \______/    /:\:\:/_____:/\      \ ___ /  /::\ /____  ____  _/\::::
# \\__________\____/    /:\:\:/_____:/:\\      \__ /_______/____/_/___/_ /  \:::
# //__________/___/   _/____:/_____:/:\:\\______\ /                     /\  /\::
# ///\          \/   /\ .----.\___:/:\:\:/_____ // \                   /  \/  \:
# ///\\          \  /::\\ \_\ \\_:/:\:\:/_____ //:\ \                 /\  /\  /\
# //:/\\          \//\::\\ \ \ \\/:\:\:/_____ //:::\ \               /  \/  \/+/
# /:/:/\\_________/:\/:::\`----' \\:\:/_____ //o:/\:\ \_____________/\  /\  / /
# :/:/://________//\::/\::\_______\\:/_____ ///\_\ \:\/____________/  \/  \/+/\
# /:/:///_/_/_/_/:\/::\ \:/__  __ /:/_____ ///\//\\/:/ _____  ____/\  /\  / /  \
# :/:///_/_/_/_//\::/\:\///_/ /_//:/______/_/ :~\/::/ /____/ /___/  \/  \/+/\  /
# /:///_/_/_/_/:\/::\ \:/__  __ /:/____/\  / \\:\/:/ _____  ____/\  /\  / /  \/
# :///_/_/_/_//\::/\:\///_/ /_//:/____/\:\____\\::/ /____/ /___/  \/  \/+/\  /\
# ///_/_/_/_/:\/::\ \:/__  __ /:/____/\:\/____/\\/____________/\  /\  / /  \/  \
# //_/_/_/_//\::/\:\///_/ /_//::::::/\:\/____/  /----/----/--/  \/  \/+/\  /\  /
# /_/_/_/_/:\/::\ \:/__  __ /\:::::/\:\/____/ \/____/____/__/\  /\  / /  \/  \/_
# _/_/_/_//\::/\:\///_/ /_//\:\::::\:\/____/ \_____________/  \/  \/+/\  /\  /
# /_/_/_/:\/::\ \:/__  __ /\:\:\::::\/____/   \ _ _ _ _ _ /\  /\  / /  \/  \/___
# _/_/_//\::/\:\///_/ /_//\:\:\:\              \_________/  \/  \/+/\  /\  /   /
# /_/_/:\/::\ \:/__  __ /\:\:\:\:\______________\       /\  /\  / /  \/  \/___/_
# _/_//\::/\:\///_/ /_//::\:\:\:\/______________/      /  \/  \/+/\  /\  /   /
# /_/:\/::\ \:/__  __ /::::\:\:\/______________/\     /\  /\  / /  \/  \/___/___
# _//\::/\:\///_/ /_//:\::::\:\/______________/  \   /  \/  \/+/\  /\  /   /   /
# /:\/::\ \:/__  __ /:\:\::::\/______________/    \ /\  /\  / /  \/  \/___/___/
# /\::/\:\///_/ /_//:\:\:\                         \  \/\\\/+/\  /\  /   /   /+/
# \/::\ \:/__  __ /:\:\:\:\_________________________\ ///\\\/  \/  \/___/___/ /_
# ::/\:\///_/ /_//:\:\:\:\/_________________________////::\\\  /\  /   /   /+/
# ::\ \:/__  __ /:\:\:\:\/_________________________/:\/____\\\/  \/___/___/ /___
# /\:\///_/ /_//:\:\:\:\/_________________________/:::\    /\/\  /   /   /+/   /
# \ \:/__  __ /:\:\:\:\/_________________________/:::::\  ///  \/___/___/ /___/_
# :\///_/ /_//:\:\:\:\/_________________________/:\:::::\///\  /   /  __________
# \:/__  __ /:\:\:\:\/_________________________/:::\:::::\/  \/___/__/\
# ///_/ /_//:\:\:\:\/_________________________/:\:::\:::::\  /   /  /::\
# /__  __ /\::\:\:\/_________________________/_____::\:::::\/___/__/:/\:\
# /_/ /_//::\::\:\/_____________________/\/_/_/_/_/\  \           /::\ \:\
# _  __ /:\::\:8\/_____________________/\/\   /\_\\/\  \ 8       /:/\:\ \:\
# / /_//\     \|______________________//\\/\::\/__\\/\  \|______/::\ \:\ \:\
#  __ /  \  \                        /:\/:\/\_______\/\        /:/\:\ \:\/::\
# /_//    8      -8  --  --  --  -- //\::/\\/_/_/_/_/_/ --  --/::\ \:\ \::/\:\
# _ /     |\  \   |________________/:\/::\///__/ /__//_______/:/\:\ \:\/::\ \:\
# __________\     \               //\::/\:/___  ___ /       /::\ \:\ \::/\:\ \:\
# ::::::::::\\  \  \             /:\/::\///__/ /__//       /:/\:\ \:\/::\ \:\ \:


# Inspritation/Sources:
#Films:
# Blade Runner (1982)
# Blade Runner 2049 (2017)
#Video Games:
# Detroit: Become Human (2018)
# Bioshock (2007)
#Books:
# Do Androids Dream of Electric Sheep? 
#Papers: 
# "The 'Cusp of life' in Science Fiction Films: The Meaning of Human Existence in "Blade Runner"" by Alfonso Mendiz
# "Future Imperfect: Philip K. Dick at the Movies" by Jason Vest
