﻿#This is the core game code


image title card = "images/titleimage.jpg"
image NightMask = "images/nightmask.png"

image Crossroads_E = "images/Crossroads_Evening.jpg"
image Crossroads_N = "images/Crossroads_Night.jpg"  
image Crossroads_D = "images/Crossroads_Day.jpg"

image UI_Backpack = "images/UI_Backpack_idle.png"
image UI_Dildo = "images/UI_Dildo.png"
image UI_VibA = "images/UI_VibA.png"
image UI_VibB = "images/UI_VibB.png"
image UI_Tongue = "images/UI_Tongue.png"
image UI_Finger = "images/UI_Finger.png"
image UI_Hand = "images/UI_Hand.png"
image UI_GirlFinger = "images/UI_GirlFinger.png" 
image UI_GirlHand = "images/UI_GirlHand.png" 


image blackscreen:
    Solid("#000000")
    on show:
        alpha 1.0
        linear 0.4 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.4 alpha 0.0

define ch_r = Character('[RogueX.Name]', color="#85bb65", image = "arrow", show_two_window=True)
define ch_p = Character('[Player.Name]', color="#87CEEB", show_two_window=True)
define ch_x = Character('Professor X', color="#a09400", image = "arrow", show_two_window=True)
define ch_k = Character('[KittyX.Name]', color="#F5A9D0", image = "arrow", show_two_window=True)
define ch_e = Character('[EmmaX.Name]', color="#98bee7", image = "arrow", show_two_window=True)
define ch_b = Character('Dr. McCoy', color="#1033b2", image = "arrow", show_two_window=True)
define ch_l = Character('[LauraX.Name]', color="#d8b600", image = "arrow", show_two_window=True)
define ch_j = Character('[JeanX.Name]', color="#b2d950", image = "arrow", show_two_window=True)
define ch_u = Character('???', color="#85bb65", image = "arrow", show_two_window=True)
define ch_n = Character('N', image = "arrow", show_two_window=True) #non-character, uses Ch_Focus #rmoved color, test that. . .
define ch_g = Character('[GwenName]', color="#F08080", image = "arrowG", show_two_window=True,background=Frame("images/WordballoonG.png",50,50))
define ch_usher = Character('Usher', color="#DF0174", show_two_window=True)
define ch_danger = Character('Danger Room:', color="#1033b2",what_color="#1033b2",what_font="dungeon.ttf",show_two_window=False)
#define e = Character("Eileen", what_color="#c8ffc8") #this sets the chat text color, handy


label splashscreen:
    if not config.developer:
        scene black onlayer backdrop
        with Pause(1)

        show image "images/Onirating.jpg"
        show text "This title is for ages 18 and up." with dissolve
        with Pause(2)
        
        show text "This is a very rough beta version of the game. It has limited function and has not been thoroughly tested. Please report any bugs you find." with dissolve
        with Pause(2)

        hide text with dissolve
        with Pause(1)

    return
    

init -1:  
#World Stats
    default SaveVersion = 991
    default Day = 1
    default Cheat = 0
    default Round = 100                 #Tracks time within a turn
    default Time_Options = ["Morning", "Midday", "Evening", "Night"]
    default Time_Count = 2
    default Current_Time = Time_Options[(Time_Count)]     
    default Week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    default Weekday = 6
    default DayofWeek = Week[Weekday]
    default bg_current = "bg study"
    default Ch_Focus = 0                
    default Party = []
    default TotalGirls = []
    default ActiveGirls = []
    default TotalSEXP = 0               #tallies the total combined SEXP daily
    default PersonalRooms = ["bg player"] #,"bg rogue","bg kitty","bg emma","bg laura"]
    default Taboo = 0
    default Rules = []
    default Digits = []
    default Keys = [] 
    default Line = 0
    default PassLine = 0                #used by AnyLine to pass lines around
    default Situation = 0               #Whether Auto/Shift
    default MultiAction = 1             #0 if the action cannot continue, 1 if it can
    default Trigger = 0                 #Mainhand
    default Trigger2 = 0                #Offhand
    default Trigger3 = 0                #Girl's offhand    
    default Trigger4 = 0                #this is the 4th sexual act performed by the second girl 
    default Trigger5 = 0                #this is the 5th sexual act performed by the second girl if masturbating
    default ThreeCount = 100              #This is a timer for changing sexual positions on auto
#    default Adjacent = []               #this is the girl you're sitting next to in class
    default Nearby = []                 #this tracks girls in the same room, but distant from you
    default Present = []                #This list tracks which girls are in this scene
    default Shop_Inventory = []         #These are updated with books available for purchase       ["DL","DL","DL","DL","G","G","G","G","G","A","A","A","A"]
    default Inventory_Count = 0         #used in screens to keep track of inventory
    default StackDepth = 0
#    default LesFlag = 0                #This is triggered if a lesbian action is occurring
    default Partner = 0                 #this is the second character involved in a sex act, make sure to set Partner to 0 after each sex act
    default Events = []  
    default PunishmentX = 0             #countdown on your punishment
    default Tempmod = 0
    default Approval = 0                #for approval checks
    default Count = 0                   #For within an event
    default Count2 = 0                  #For between several events
    default CountStore = 0              #Stores values for after an event ends
    default Cnt = 0                     #a mini Count variable for discrete operations
    default Stealth = 0                 #How careful you're being
    default Speed = 0                   #pace of sex acts
    default Achievements = []
    default Options = []
    default Vibration = 0
    default Psychic = 0                 #this is an animation toggle for psychic sex. hand/blow/tit/pussy/ass
    default RTR_Toggle = 1              #sets whether game asks if you want to return to your room when a girl asks you to
#    default UI_Girl = "Rogue"           #girl used in UI elements
    default TravelMode = 0              #used for wandering around, if 0, you use the worldmap
    default StageFarLeft = 150          #these are values for location points on the screen
    default StageLeft = 350     
    default StageCenter = 550           #This is the default position for the lead
    default StageRight = 715            #This is the default position for second girl
    default StageFarRight = 900         #these are values for location points on the screen
    default HolderCount = 1             #Used by the popup numbers
#Xavier Sprite Variables    
    default X_Brows = "happy"
    default X_Mouth = "happy"
    default X_Eyes = "happy"
    default X_Psychic = 0
    default X_Emote = "happy"
    default XSpriteLoc = StageCenter
    default GwenName = "????"
    
    
# Official game start  ////////////////////////////////////////////////////////////////////
label start: 
    # Intitializes classes              
    #$ import copy
    $ Player = PlayerClass()
    $ RogueX = GirlClass("Rogue",500,0,0,10)
    $ KittyX = GirlClass("Kitty",400,100,0,10)
    $ EmmaX = GirlClass("Emma",300,0,200,15)
    $ LauraX = GirlClass("Laura",400,0,200,10)
    $ JeanX = GirlClass("Jean",0,0,1000,10)
    
    $ RogueX.Introduction()
    $ KittyX.Introduction()
    $ EmmaX.Introduction()
    $ LauraX.Introduction()
    $ JeanX.Introduction()
    
    $ RogueX.OutfitChange(6,Changed=1)
    $ KittyX.OutfitChange(6,Changed=1)
    $ EmmaX.OutfitChange(6,Changed=1)
    $ LauraX.OutfitChange(6,Changed=1)
    $ JeanX.OutfitChange(6,Changed=1)
    
    $ Ch_Focus = RogueX
    show screen Status_Screen    
    show screen Inventorybutton            
        
    if config.developer:
        jump Dev_Room
    jump Prologue


# After loading, this runs ////////////////////////////////////////////////////////////////
label after_load: 
label VersionNumber: 
    $ SaveVersion = 0 if "SaveVersion" not in globals().keys() else SaveVersion    
    if SaveVersion == 975: #error correction, remove this eventually
            $ SaveVersion = 957  
        
    if SaveVersion >= 990:
        if SaveVersion < 992:    
            if SaveVersion <= 990:     
                if "RogueX" in globals().keys():
                            if RogueX.Hair == "wet":
                                    $ RogueX.Hair = "evo"
                            if RogueX.Casual1[1] == "gloved":
                                    $ RogueX.Casual1[1] == "gloves"
                            if RogueX.Casual2[1] == "gloved":
                                    $ RogueX.Casual2[1] == "gloves"
                            if RogueX.Gym[1] == "gloved":
                                    $ RogueX.Gym[1] == "gloves"
                            if RogueX.Arms == "gloved":
                                    $ RogueX.Arms = "gloves"
                            if RogueX in TotalGirls:
                                    while RogueX in TotalGirls:
                                        $ TotalGirls.remove(RogueX)
                                    $ TotalGirls.append(RogueX)
                            if RogueX in ActiveGirls:
                                    while RogueX in ActiveGirls:
                                        $ ActiveGirls.remove(RogueX)
                                    $ ActiveGirls.append(RogueX)
                            if not hasattr(RogueX,'Cheated'):
                                    $ setattr(RogueX,"Cheated",0)
                            if RogueX in Player.Harem:
                                    $ RogueX.AddWord(1,0,0,"dating",0)
                if "KittyX" in globals().keys():
                            if KittyX in TotalGirls:
                                    while KittyX in TotalGirls:
                                        $ TotalGirls.remove(KittyX)
                                    $ TotalGirls.append(KittyX)
                            if KittyX in ActiveGirls:
                                    while KittyX in ActiveGirls:
                                        $ ActiveGirls.remove(KittyX)
                                    $ ActiveGirls.append(KittyX)
                            if KittyX.Home in PersonalRooms:
                                    while KittyX.Home in PersonalRooms:
                                        $ PersonalRooms.remove(KittyX.Home)
                                    $ PersonalRooms.append(KittyX.Home)
                            if not hasattr(KittyX,'Cheated'):
                                    $ setattr(KittyX,"Cheated",0)
                            if KittyX in Player.Harem:
                                    $ KittyX.AddWord(1,0,0,"dating",0)
                if "EmmaX" in globals().keys():
                            if EmmaX in TotalGirls:
                                    while EmmaX in TotalGirls:
                                        $ TotalGirls.remove(EmmaX)
                                    $ TotalGirls.append(EmmaX)
                            if EmmaX in ActiveGirls:
                                    while EmmaX in ActiveGirls:
                                        $ ActiveGirls.remove(EmmaX)
                                    $ ActiveGirls.append(EmmaX)
                            if EmmaX.Home in PersonalRooms:
                                    while EmmaX.Home in PersonalRooms:
                                        $ PersonalRooms.remove(EmmaX.Home)
                                    $ PersonalRooms.append(EmmaX.Home)
                            if not hasattr(EmmaX,'Cheated'):
                                    $ setattr(EmmaX,"Cheated",0)
                            if EmmaX in Player.Harem:
                                    $ EmmaX.AddWord(1,0,0,"dating",0)
                if "LauraX" in globals().keys(): 
                            if LauraX in TotalGirls:
                                    while LauraX in TotalGirls:
                                        $ TotalGirls.remove(LauraX)
                                    $ TotalGirls.append(LauraX)
                            if LauraX in ActiveGirls:
                                    while LauraX in ActiveGirls:
                                        $ ActiveGirls.remove(LauraX)
                                    $ ActiveGirls.append(LauraX)
                            if LauraX.Home in PersonalRooms:
                                    while LauraX.Home in PersonalRooms:
                                        $ PersonalRooms.remove(LauraX.Home)
                                    $ PersonalRooms.append(LauraX.Home)
                            if not hasattr(LauraX,'Cheated'):
                                    $ setattr(LauraX,"Cheated",0)
                            if LauraX in Player.Harem:
                                    $ LauraX.AddWord(1,0,0,"dating",0)
                $ Player.StatPoints = 0 if Player.StatPoints < 0 else Player.StatPoints
                if "Emma stockings and garterbelt" in Player.Inventory:
                        $ Player.Inventory.remove("Emma stockings and garterbelt")
                        $ Player.Inventory.append("stockings and garterbelt")
                while 0 in Party:
                        $ Party.remove(0)
                hide Laura
                $ SaveVersion = 990    
                #End 0.990 updates
            if SaveVersion < 992: 
                #changes for version 991, adds Jean to the game
                if "JeanX" not in globals().keys():
                        $ JeanX = GirlClass("Jean",0,0,1000,10)
                        $ JeanX.Introduction()
                if "met" in JeanX.History and JeanX not in ActiveGirls: #remove once stable
                        $ ActiveGirls.Append(JeanX)
                    
                if "RogueX" in globals().keys() and "met" in RogueX.History: 
                            if RogueX not in TotalGirls:
                                    $ TotalGirls.append(RogueX)
                if "KittyX" in globals().keys() and "met" in KittyX.History:
                            if KittyX not in TotalGirls:
                                    $ TotalGirls.append(KittyX)
                            if KittyX.Pet == KittyX:
                                $ KittyX.Pet = "Kitty"
                if "EmmaX" in globals().keys() and "met" in EmmaX.History:
                            if EmmaX not in TotalGirls:
                                    $ TotalGirls.append(EmmaX)
                if "LauraX" in globals().keys() and "met" in LauraX.History: 
                            if LauraX not in TotalGirls:
                                    $ TotalGirls.append(LauraX)
                            if LauraX.Pet == LauraX:
                                    $ LauraX.Pet = "Laura"  
                            if LauraX.Casual2[4] == "jacket":
                                    $ LauraX.Casual1 = [2,"wrists","leather pants",0,"leash choker","leather bra","leather panties",0,0,0,0]
                                    $ LauraX.Casual2 = [2,0,"skirt","jacket","leash choker","corset","leather panties",0,0,0,0]
                if "JeanX" in globals().keys() and "met" in JeanX.History: 
                            if JeanX not in TotalGirls:
                                    $ TotalGirls.append(JeanX)
                            if JeanX.Pet == JeanX:
                                $ JeanX.Pet = "Jean"                                
                            if "exhibitionist" in JeanX.Traits and "nowhammy" not in JeanX.Traits:
                                    $ JeanX.Traits.remove("exhibitionist") 
                #$ SaveVersion = 991   
                #End 0.991 updates
        return
        #remove this later               #remove this later               #remove this later               #remove this later
    else:        
            
            $ renpy.scene("screens")    #removes old screens          
            $ Player = PlayerClass()
            $ RogueX = GirlClass("Rogue",500,0,0,10)
            $ KittyX = GirlClass("Kitty",400,100,0,10)
            $ EmmaX = GirlClass("Emma",300,0,200,15)
            $ LauraX = GirlClass("Laura",400,0,200,10)
            $ JeanX = GirlClass("Jean",0,0,1000,10)
            
            $ RogueX.Introduction()
            $ KittyX.Introduction()
            $ EmmaX.Introduction()
            $ LauraX.Introduction()
            $ JeanX.Introduction()
            
            $ Ch_Focus = RogueX
            show screen Status_Screen    
            show screen Inventorybutton    
                
            show blackscreen onlayer black
            if SaveVersion < 984:
                    "You are loading a save from a version earlier than 0.984."
                    "This will not work with this build, but please pick up a copy of version 0.984h."   
                    "Then move to the player's room, alone, and make a save file there."
                    "This save file -should- be able to be openned in version 0.990 and beyond."       
                    $ StackDepth = renpy.call_stack_depth() #Count = number of items in the call stack
                    while StackDepth > 0:
                        $ StackDepth -= 1
                        $ renpy.pop_call()  
                    return
            "You are loading a save from a version earlier than 0.990."
            if bg_current != "bg player":
                    "Your save is not in the player's room, which might cause errors due to missing local variables."
                    "You might want to load this save in version 0.984h, and move to the player's room before saving."
            "If you continue, know that this save migration is still being tested and may cause new errors."
            "Let me know if there are any clothing options behaving differently than expected, and stats that seem out of place,"
            "Anything unusual. I would recommend playing from this save file only a short distance, and not just continung forward indefinitely,"
            "until we're fairly certain that the migration process is fully functional. Be careful of where you save." 
            "that said, it shouldn't cause any harm to try it. :D"
            hide blackscreen onlayer black
#    if not config.developer:
#            show blackscreen onlayer black 
            
#            "You are loading a save from a version earlier than 0.990."
#            "This will not work with this build, but will hopefully work with a future build of the game."         
#            $ StackDepth = renpy.call_stack_depth() #Count = number of items in the call stack
#            while StackDepth > 0:
#                $ StackDepth -= 1
#                $ renpy.pop_call()  
#            return
#            #$ SaveVersion = 990
     
    call Failsafe                #fix                #fix                #fix                #fix
    return                #fix                #fix                #fix                #fix
    
    if SaveVersion < 990:
        if SaveVersion < 984:
                "You are loading a save from a version earlier than 0.984."
                "This will not work with this build, but please pick up a copy of version 0.984h."   
                "Then move to the player's room, alone, and make a save file there."
                "This save file -should- be able to be openned in version 0.990 and beyond."
                if SaveVersion < 94:
                    $ R_Love = R_Love * 10
                    $ R_Inbt = R_Inbt * 10
                    $ R_Obed = R_Obed * 10
                    $ SaveVersion = 940
                    $ R_Under = 0        
                    $ R_OutfitShame[0] = 50
                if SaveVersion < 95:
                    $ R_Event[3] = 0
                    if "hungry" in R_Traits:
                        while "hungry" in R_Traits:
                            $ R_Traits.remove("hungry")  
                        $ R_Traits.append("hungry")
                    $ SaveVersion = 950
                if SaveVersion < 955:
                    if R_Schedule[7] == 4:
                        $ R_Schedule[7] = 0
                    $ R_Schedule[8] = 4     #changes which slot is in gym clothes
                    $ SaveVersion = 955    
                if SaveVersion < 957:
                    $ R_OutfitShame[4] = 20
                    $ SaveVersion = 957    
                if SaveVersion < 960:
                    $ R_Schedule[0] = R_Schedule[1]
                    $ R_Schedule[1] = R_Schedule[2]
                    $ R_Schedule[2] = R_Schedule[3]
                    $ R_Schedule[3] = R_Schedule[4]
                    $ R_Schedule[4] = R_Schedule[5]
                    $ R_Schedule[5] = R_Schedule[6]
                    $ R_Schedule[6] = R_Schedule[7]
                    $ R_Schedule[7] = 0   
                    $ R_Hose = "stockings" if R_Hose == 1 else 0            
                    $ R_Custom[9] = "stockings" if R_Custom[9] == 1 else 0
                    $ R_Sleepwear[6] = "stockings" if R_Sleepwear[6] == 1 else 0    
                    $ TravelMode = 0 if "TravelMode" not in globals().keys() else TravelMode         
                    $ P_RecentActions = [] if "P_RecentActions" not in globals().keys() else P_RecentActions
                    $ P_DailyActions = [] if "P_DailyActions" not in globals().keys() else P_DailyActions         
                    $ R_RecentActions = [] if "R_RecentActions" not in globals().keys() else R_RecentActions
                    $ R_DailyActions = [] if "R_DailyActions" not in globals().keys() else R_DailyActions
                    $ SaveVersion = 960      
                if SaveVersion < 966:
                    $ K_History = []
                    $ K_Arms = Kitty_Arms
                    $ StageFarLeft = 150
                    $ SaveVersion = 966  
                    while len(R_OutfitShame) < 15:
                        $ R_OutfitShame.append(0)  
                if SaveVersion < 970:        
                    hide screen roguebutton
                    hide screen statbutton  
                    $ R_Sperm = []  
                    while len(Event) < 4:
                        $ Event.append(0)
                    while len(R_Chat) < 6:
                        $ R_Chat.append(0)
                    while len(R_Event) < 11:
                        $ R_Event.append(0)
                    while len(R_Custom) < 11:
                        $ R_Custom.append(0)
                    while len(R_Custom2) < 11:
                        $ R_Custom2.append(0)
                    while len(R_Custom3) < 11:
                        $ R_Custom3.append(0)
                    while len(R_Gym) < 11:
                        $ R_Gym.append(0)
                    while len(R_Sleepwear) < 7:
                        $ R_Sleepwear.append(0)
                    while len(R_Schedule) < 10:
                        $ R_Schedule.append(0)
                    while len(K_Custom) < 10:
                        $ K_Custom.append(0)  
                    $ K_Spunk = []            
                    $ K_Custom = [0,0,0,0,0,0,0,0,0,0]
                    $ K_Custom2 = [0,0,0,0,0,0,0,0,0,0,0]
                    $ K_Custom3 = [0,0,0,0,0,0,0,0,0,0,0]        
                    $ K_Gym = [0,0,"shorts",0,0,"sports bra","panties",0,0,0,0]
                    $ K_Sleepwear = [0,0,0,0,"tank","green panties",0]
                    $ K_Schedule = [0,0,0,0,0,0,0,0,4,0]                      #chooses when she wears what
                    $ K_Chat = [0,0,0,0,0,0]
                    $ K_Event = [0,0,0,0,0,0,0,0,0,0,0]  
                    $ K_Todo = []
                    $ SaveVersion = 970  
                if SaveVersion < 971:      
                    $ K_Gym = [1,0,"shorts",0,0,"sports bra","green panties",0,0,0,0]
                    $ K_Sleepwear = [0,"shorts",0,0,"cami","green panties",0]
                
                    $ R_Gym = [0,"gloves",0,"hoodie",0,"sports bra","shorts",0,0,0,0]
                    $ R_Sleepwear = [0,0,0,0,"tank","green panties",0] 
                    $ R_LikeKitty = 600
                    $ K_Traits = []
                    $ K_Petname = Playername[:1]    
                    $ K_Petnames = ["sweetie"]
                    $ K_Pet = "Kitty"       
                    $ K_Pets = ["Kitty"]
                    $ K_Loose = 0
                    $ K_PantiesDown = 0
                    $ K_Water = 0
                    $ K_Pierce = 0
                    $ K_ForcedCount = 0
                    $ R_ForcedCount = 0
                    $ SaveVersion = 971         
                if SaveVersion < 972:            
                    $ RogueLayer = 50
                    $ KittyLayer = 100
                                
                    if Current_Time == 'Night':
                        show NightMask onlayer nightmask      
                    if K_Over == "pink top":
                        $ K_Neck = "gold necklace"
                    else:
                        $ K_Neck = 0
                    $ R_Spunk = R_Sperm
                    if renpy.showing("setting", layer='master'):
                        scene setting onlayer backdrop
                        hide setting
                    if renpy.showing("bg_entry", layer='master'):
                        scene bg_entry onlayer backdrop
                        hide bg_entry
                    $ SaveVersion = 972 
                if SaveVersion < 973:
                    $ K_Pierce = 0 if "K_Pierce" not in globals().keys() else K_Pierce  
                    $ Trigger4 = 0                #this is the 4th sexual act performed by the second girl  
                    $ Trigger5 = 0                #this is the 5th sexual act performed by the second girl if masturbating 
                    $ Partner = 0                 #this is the second character involved in a sex act, make sure to set Partner to 0 after each sex act
                    $ K_Sleepwear[3] = 0
                    
                    if R_Custom[1] == "collargloved":
                            $ R_Custom[1] = "gloves"
                            $ R_Custom[4] = "spiked collar"
                    elif R_Custom[1] == "collarbare":  
                            $ R_Custom[1] = 0
                            $ R_Custom[4] = "spiked collar"
                    elif R_Custom[1] == "gloved":
                            $ R_Custom[1] = "gloved"
                            $ R_Custom[4] = 0
                    else:
                            $ R_Custom[1] = 0
                            $ R_Custom[4] = 0
                            
                    if R_Custom2[1] == "collargloved":
                            $ R_Custom2[1] = "gloved"
                            $ R_Custom2[4] = "spiked collar"
                    elif R_Custom2[1] == "collarbare":  
                            $ R_Custom2[1] = 0
                            $ R_Custom2[4] = "spiked collar"
                    elif R_Custom2[1] == "gloved":
                            $ R_Custom2[1] = "gloved"
                            $ R_Custom2[4] = 0
                    else:
                            $ R_Custom2[1] = 0
                            $ R_Custom2[4] = 0
                    
                    if R_Custom3[1] == "collargloved":
                            $ R_Custom3[1] = "gloved"
                            $ R_Custom3[4] = "spiked collar"
                    elif R_Custom3[1] == "collarbare":  
                            $ R_Custom3[1] = 0
                            $ R_Custom3[4] = "spiked collar"
                    elif R_Custom3[1] == "gloved":
                            $ R_Custom3[1] = "gloved"
                            $ R_Custom3[4] = 0
                    else:
                            $ R_Custom3[1] = 0
                            $ R_Custom3[4] = 0
                            
                    if R_Gym[1] == "collargloved":
                            $ R_Gym[1] = "gloved"
                            $ R_Gym[4] = "spiked collar"
                    elif R_Gym[1] == "collarbare":  
                            $ R_Gym[1] = 0
                            $ R_Gym[4] = "spiked collar"
                    elif R_Gym[1] == "gloved":
                            $ R_Gym[1] = "gloved"
                            $ R_Gym[4] = 0
                    else:
                            $ R_Gym[1] = 0
                            $ R_Gym[4] = 0
                    
                    if R_Sleepwear[0] == "collargloved":
                            $ R_Sleepwear[0] = "gloved"
                            $ R_Sleepwear[3] = "spiked collar"
                    elif R_Sleepwear[0] == "collarbare":  
                            $ R_Sleepwear[0] = 0
                            $ R_Sleepwear[3] = "spiked collar"
                    elif R_Sleepwear[0] == "gloved":
                            $ R_Sleepwear[0] = "gloved"
                            $ R_Sleepwear[3] = 0
                    else:
                            $ R_Sleepwear[0] = 0
                            $ R_Sleepwear[3] = 0
                            
                    if R_Arms == "collargloved":
                            $ R_Arms = "gloved"
                            $ R_Neck = "spiked collar"
                    elif R_Arms == "collarbare":    
                            $ R_Arms = 0
                            $ R_Neck = "spiked collar"
                    elif R_Arms == "gloved":    
                            $ R_Arms = "gloved"
                            $ R_Neck = 0            
                    else:  
                            $ R_Arms = 0
                            $ R_Neck = 0
                    
                    $ P_Rep = 600
                    $ R_Rep = R_Rep * 10
                    $ K_Rep = K_Rep * 10
                    $ R_History = []            
                    $ R_PlayerFav = 0
                    $ R_Favorite = 0
                    $ K_PlayerFav = 0
                    $ K_Favorite = 0   
                    $ R_SeenPeen = 0   
                    $ K_SeenPeen = 0
                    $ R_Les = 0    
                    $ R_SexKitty = 0
                    $ K_Les = 0    
                    $ K_SexRogue = 0
                    $ R_SEXP += 5 if R_LickA else 0
                    $ Trigger = "fondle pussy" if Trigger == "insert pussy" else Trigger
                    $ Trigger2 = "fondle pussy" if Trigger2 == "insert pussy" else Trigger2
                    $ Trigger2 = "jackin" if Trigger2 == "masturbation" else Trigger2
                    $ R_SeenPeen = R_Sex + R_Anal + R_Hotdog + R_Blow + R_Hand + R_Tit    
                    $ K_SeenPeen = K_Sex + K_Anal + K_Hotdog + K_Blow + K_Hand + K_Tit                  
                    if "around" in R_Traits:
                        while "around" in R_Traits:
                            $ R_Traits.remove("around") 
                    if "around" in K_Traits:
                        while "around" in K_Traits:
                            $ K_Traits.remove("around") 
                    $ R_OutfitDay = R_Outfit
                    $ K_OutfitDay = K_Outfit
                    $ SaveVersion = 973 
                if SaveVersion < 974:
                    $ Adjacent = 0    
                    $ R_Resistance = 1 if R_Resistance >= 1 else 0
                    $ K_Resistance = 1 if K_Resistance >= 1 else 0
                    $ Week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
                    if "All" in Keys and "Kitty" not in Keys:
                        $ Keys.append("Kitty")
                    $ Present = []
                    $ R_Date = 0 
                    $ K_Date = 0 
                    $ SaveVersion = 974 
        if SaveVersion < 976:
            if R_History == 0: 
                $ R_History = []
            if K_History == 0: 
                $ K_History = []
            if "saw with Kitty" in R_Traits:
                while "saw with Kitty" in R_Traits:
                        $ R_Traits.remove("saw with Kitty") 
            if "saw with Rogue" in K_Traits:
                while "saw with Rogue" in K_Traits:
                        $ K_Traits.remove("saw with Rogue") 
            $ R_Gag = 0   
            $ K_Gag = 0  
            $ SaveVersion = 976 
        if SaveVersion < 977:
            if K_Rep <= 400:
                $ P_Rep -= 100
            if R_Rep <= 400:
                $ P_Rep -= 100
            $ SaveVersion = 977 
        if SaveVersion < 978:            
            if "stockings and garterbelt" not in R_Inventory and ApprovalCheck("Rogue", 1500):
                    $ R_Inventory.append("stockings and garterbelt")
            $ E_Loose = 2
            $ SaveVersion = 978
        if SaveVersion < 979:      
            $ StageFarRight = 900            #these are values for location points on the screen
            $ StageRight = 715            #these are values for location points on the screen
            $ StageCenter = 550
            $ StageLeft = 350
            $ StageFarLeft = 150
            #make sure to set K_SpriteLoc etc. to new values, 
            # $ K_SpriteLoc = 200 if K_SpriteLoc = 550 else K_SpriteLoc
            if "exhibitionist" in E_Traits:
                    $ E_Traits.remove("exhibitionist")
            if len(R_Sleepwear) <= 9: #this should be the case on any busted-ass og versions
                    $ R_Sleepwear.append(0)
                    $ R_Sleepwear.append(0)
                    $ R_Sleepwear.append(0)
                    $ R_Sleepwear[9] = R_Sleepwear[6] #Hose 6>9
                    $ R_Sleepwear[8] = "evo"            #Hair
                    $ R_Sleepwear[6] = R_Sleepwear[5] #Panties 5>6
                    $ R_Sleepwear[5] = R_Sleepwear[4] #Chest 4>5
                    $ R_Sleepwear[4] = R_Sleepwear[3] #Neck 3>4 "choker"  
                    $ R_Sleepwear[3] = R_Sleepwear[2] #Over 2>3
                    $ R_Sleepwear[2] = R_Sleepwear[1] #Legs 1>2
                    $ R_Sleepwear[1] = R_Sleepwear[0] #Arms 0>1
                    $ R_Sleepwear[0] = 1                #new toggle
                    
                    $ K_Sleepwear.append(0)
                    $ K_Sleepwear.append(0)
                    $ K_Sleepwear.append(0)
                    $ K_Sleepwear[9] = K_Sleepwear[6] #Hose 6>9
                    $ K_Sleepwear[8] = "long"           #Hair
                    $ K_Sleepwear[6] = K_Sleepwear[5] #Panties 5>6
                    $ K_Sleepwear[5] = K_Sleepwear[4] #Chest 4>5
                    $ K_Sleepwear[4] = K_Sleepwear[3] #Neck 3>4 "choker"  
                    $ K_Sleepwear[3] = K_Sleepwear[2] #Over 2>3
                    $ K_Sleepwear[2] = K_Sleepwear[1] #Legs 1>2
                    $ K_Sleepwear[1] = K_Sleepwear[0] #Arms 0>1
                    $ K_Sleepwear[0] = 1                #new toggle
                    
                    $ E_Sleepwear.append(0)
                    $ E_Sleepwear.append(0)
                    $ E_Sleepwear.append(0)
                    $ E_Sleepwear[9] = E_Sleepwear[6] #Hose 6>9
                    $ E_Sleepwear[8] = E_Hair          #Hair
                    $ E_Sleepwear[6] = E_Sleepwear[5] #Panties 5>6
                    $ E_Sleepwear[5] = E_Sleepwear[4] #Chest 4>5
                    $ E_Sleepwear[4] = E_Sleepwear[3] #Neck 3>4 "choker"  
                    $ E_Sleepwear[3] = E_Sleepwear[2] #Over 2>3
                    $ E_Sleepwear[2] = E_Sleepwear[1] #Legs 1>2
                    $ E_Sleepwear[1] = E_Sleepwear[0] #Arms 0>1
                    $ E_Sleepwear[0] = 1                #new toggle
            #end of sleepwear overhaul
            
                
            if Trigger == "kissing": #add to update
                    if Trigger5 == "kiss girl":
                        $ Trigger = "kiss girl"
                    elif Trigger5 == "kiss both":
                        $ Trigger = "kiss both"
                    else:
                        $ Trigger = "kiss you"
            if Trigger2 == "kissing":
                        $ Trigger2 = "kiss you"        
            if Trigger3 == "kissing": #add to update
                    if Trigger5 == "kiss both":
                        $ Trigger3 = "kiss both"
                    elif Trigger5 == "kiss girl" or Trigger == "lesbian":
                        $ Trigger3 = "kiss girl"
                    else:
                        $ Trigger3 = "kiss you"
            if Trigger4 == "kissing": #add to update
                    if Trigger5 == "kiss both":
                        $ Trigger4 = "kiss both"
                    elif Trigger5 == "kiss girl" or Trigger == "lesbian":
                        $ Trigger4 = "kiss girl"
                    else:
                        $ Trigger4 = "kiss you"
            if Trigger5 in ("kiss you", "kiss girl", "kiss both"):
                    $ Trigger5 = 0 #Clear out Trigger 5 if it's for kissing.  
            $ E_Caught = 0
            if Rules == 1:
                $ Rules = []
            elif Rules == 0:
                $ Rules = ["rules"]
            if "exhibitionist" in E_Traits:  
                    $ E_Traits.remove("exhibitionist")
            $ E_Gym = [2,0,0,0,0,"sports bra","sports panties",0,0,0,0]                        
            $ SaveVersion = 979   
            
        if SaveVersion < 980:                     
            $ SaveVersion = 980   
            if "met" not in K_History:
                $ K_Loc = 0
            if "met" not in E_History:
                $ E_Loc = 0
            if "vocal" not in R_Traits:
                    $ R_Traits.append("vocal")
            if "vocal" not in K_Traits:
                    $ K_Traits.append("vocal")
            if "vocal" not in E_Traits:
                    $ E_Traits.append("vocal")
            if bg_current in ("date","bg restaurant","bg movies"):
                    #this should reset dates. 
                    show blackscreen onlayer black 
                    $ bg_current = "bg player"
                    call Wait
                    call Wait
                    call Set_The_Scene(Dress=0)
                    "You wake up in your room, you had a weird dream, apparently."
                    jump Player_Room   
        if SaveVersion < 981:                     
            $ SaveVersion = 981   
            if Trigger == "kissing": #add to update
                    if Trigger5 == "kiss girl":
                        $ Trigger = "kiss girl"
                    elif Trigger5 == "kiss both":
                        $ Trigger = "kiss both"
                    else:
                        $ Trigger = "kiss you"
            if Trigger2 == "kissing":
                        $ Trigger2 = "kiss you"        
            if Trigger3 == "kissing": #add to update
                    if Trigger5 == "kiss both":
                        $ Trigger3 = "kiss both"
                    elif Trigger5 == "kiss girl" or Trigger == "lesbian":
                        $ Trigger3 = "kiss girl"
                    else:
                        $ Trigger3 = "kiss you"
            if Trigger4 == "kissing": #add to update
                    if Trigger5 == "kiss both":
                        $ Trigger4 = "kiss both"
                    elif Trigger5 == "kiss girl" or Trigger == "lesbian":
                        $ Trigger4 = "kiss girl"
                    else:
                        $ Trigger4 = "kiss you"
            if Trigger5 in ("kiss you", "kiss girl", "kiss both"):
                    $ Trigger5 = 0 #Clear out Trigger 5 if it's for kissing.  
            if "nighty" in P_Inventory: 
                $ P_Inventory.remove("nighty")
                $ P_Cash += 75
            if "lace bra" in P_Inventory: 
                $ P_Inventory.remove("lace bra")
                $ P_Cash += 90  
            if "lace panties" in P_Inventory: 
                $ P_Inventory.remove("lace panties")
                $ P_Cash += 110   
            if E_Schedule[8] == 4:
                $ E_Schedule[8] = 0
            if "locked" in E_RecentActions:
                $ P_RecentActions.append("lockedclass")
                $ E_RecentActions.remove("locked")
            if ("movie" in P_DailyActions or "dinner" in P_DailyActions) and not Party:
                    #this should reset dates. 
                    $ Primary = 0 if "Primary" not in locals().keys() else Primary 
                    $ Secondary = 0 if "Secondary" not in locals().keys() else Secondary
                    $ Party = [Primary,Secondary]

            if Adjacent:
                $ X_Psychic = Adjacent
                $ Adjacent = [X_Psychic]                
                $ X_Psychic = 0
            else:
                $ Adjacent = [] 
            if "dating" in R_Traits and "Rogue" not in P_Harem:
                $ P_Harem.append("Rogue")
            if "dating" in K_Traits and "Kitty" not in P_Harem:
                $ P_Harem.append("Kitty")    
        if SaveVersion < 982:        
            #this bit removes the annoying leftover 
            if Time_Count > 0 or Round < 90:
                    #should only apply after morning or after a little time has passed
                    if "sleepover" in R_Traits and R_Loc != bg_current: 
                            $ R_Traits.remove("sleepover")
                    if "sleepover" in K_Traits and K_Loc != bg_current: 
                            $ K_Traits.remove("sleepover")
                    if "sleepover" in E_Traits and E_Loc != bg_current: 
                            $ E_Traits.remove("sleepover")
                    if "sleepover" in L_Traits and L_Loc != bg_current: 
                            $ L_Traits.remove("sleepover")
            $ L_Pubes = 1
            if "passive" in R_Traits:
                    while "passive" in R_Traits:
                        $ R_Traits.remove("passive")     
                    $ R_Traits.append("passive") 
            if P_Harem:
                $ X_Psychic = P_Harem[0] 
                
                while P_Harem.count("Rogue") > 1:
                        $ P_Harem.remove("Rogue")    
                while P_Harem.count("Kitty") > 1:
                        $ P_Harem.remove("Kitty")       
                while P_Harem.count("Emma") > 1:
                        $ P_Harem.remove("Emma") 
                if P_Harem[0] != X_Psychic:                                    
                        $ P_Harem.remove(X_Psychic)    
                        $ P_Harem.insert(0,X_Psychic) 
                $ X_Psychic = 0  
            if "saw with kitty" in R_Traits:
                    $ R_Traits.append("saw with Kitty")
                    $ R_Traits.remove("saw with kitty")
            if "saw with kitty" in E_Traits:
                    $ E_Traits.append("saw with Kitty")
                    $ E_Traits.remove("saw with kitty")                    
            if "saw with rogue" in K_Traits:
                    $ K_Traits.append("saw with Rogue")
                    $ K_Traits.remove("saw with rogue")
            if "saw with rogue" in E_Traits:
                    $ E_Traits.append("saw with Rogue")
                    $ E_Traits.remove("saw with rogue")                    
            if "saw with emma" in R_Traits:
                    $ R_Traits.append("saw with Emma")
                    $ R_Traits.remove("saw with emma")
            if "saw with emma" in K_Traits:
                    $ K_Traits.append("saw with Emma")
                    $ K_Traits.remove("saw with emma")
            # / / / / / /        
            if "poly kitty" in R_Traits:
                    $ R_Traits.append("poly Kitty")
                    $ R_Traits.remove("poly kitty")
            if "poly kitty" in E_Traits:
                    $ E_Traits.append("poly Kitty")
                    $ E_Traits.remove("poly kitty")                    
            if "poly rogue" in K_Traits:
                    $ K_Traits.append("poly Rogue")
                    $ K_Traits.remove("poly rogue")
            if "poly rogue" in E_Traits:
                    $ E_Traits.append("poly Rogue")
                    $ E_Traits.remove("poly rogue")                    
            if "poly emma" in R_Traits:
                    $ R_Traits.append("poly Emma")
                    $ R_Traits.remove("poly emma")
            if "poly emma" in K_Traits:
                    $ K_Traits.append("poly Emma")
                    $ K_Traits.remove("poly emma")
            # / / / / / /        
            if "noticed kitty" in R_RecentActions:
                    $ R_RecentActions.append("noticed Kitty")
                    $ R_RecentActions.remove("noticed kitty")
            if "noticed kitty" in E_RecentActions:
                    $ E_RecentActions.append("noticed Kitty")
                    $ E_RecentActions.remove("noticed kitty")                    
            if "noticed rogue" in K_RecentActions:
                    $ K_RecentActions.append("noticed Rogue")
                    $ K_RecentActions.remove("noticed rogue")
            if "noticed rogue" in E_RecentActions:
                    $ E_RecentActions.append("noticed Rogue")
                    $ E_RecentActions.remove("noticed rogue")                 
            if "noticed emma" in K_RecentActions:
                    $ K_RecentActions.append("noticed Emma")
                    $ K_RecentActions.remove("noticed emma")
            if "noticed emma" in R_RecentActions:
                    $ R_RecentActions.append("noticed Emma")
                    $ R_RecentActions.remove("noticed emma")
            # / / / / / /        
            if "ask kitty" in R_RecentActions:
                    $ R_RecentActions.append("ask Kitty")
                    $ R_RecentActions.remove("ask kitty")
            if "ask kitty" in E_RecentActions:
                    $ E_RecentActions.append("ask Kitty")
                    $ E_RecentActions.remove("ask kitty")                    
            if "ask rogue" in K_RecentActions:
                    $ K_RecentActions.append("ask Rogue")
                    $ K_RecentActions.remove("ask rogue")
            if "ask rogue" in E_RecentActions:
                    $ E_RecentActions.append("ask Rogue")
                    $ E_RecentActions.remove("ask rogue")                 
            if "ask emma" in K_RecentActions:
                    $ K_RecentActions.append("ask Emma")
                    $ K_RecentActions.remove("ask emma")
            if "ask emma" in R_RecentActions:
                    $ R_RecentActions.append("ask Emma")
                    $ R_RecentActions.remove("ask emma")
                    
            if "lockedclass" in P_RecentActions:
                $ P_RecentActions.remove("lockedclass")
                $ P_Traits.append("locked")
            $ SaveVersion = 982
            #end Save 982 prep          
            
        if SaveVersion < 983:        
            $ Kitty_Arms = K_Arms   
            call Clothing_Schedule_Check("Rogue",3,1)  
            call Clothing_Schedule_Check("Rogue",4,1) 
            call Clothing_Schedule_Check("Rogue",5,1) 
            call Clothing_Schedule_Check("Rogue",6,1) 
            call Clothing_Schedule_Check("Kitty",3,1)  
            call Clothing_Schedule_Check("Kitty",4,1) 
            call Clothing_Schedule_Check("Kitty",5,1) 
            call Clothing_Schedule_Check("Kitty",6,1) 
            call Clothing_Schedule_Check("Emma",3,1)  
            call Clothing_Schedule_Check("Emma",4,1) 
            call Clothing_Schedule_Check("Emma",5,1) 
            call Clothing_Schedule_Check("Emma",6,1) 
            call Clothing_Schedule_Check("Laura",3,1)  
            call Clothing_Schedule_Check("Laura",4,1) 
            call Clothing_Schedule_Check("Laura",5,1) 
            call Clothing_Schedule_Check("Laura",6,1) 
#            $ K_Arms = 0
            $ SaveVersion = 983
            #end Save 983 prep          
                    
        if SaveVersion < 984:   
            #shifts case of these words. . .
            if "les kitty" in R_History:
                    $ R_History.remove("les kitty")
                    if "les Kitty" not in R_History:
                        $ R_History.append("les Kitty")
            if "les emma" in R_History:
                    $ R_History.remove("les emma")                    
                    if "les Emma" not in R_History:
                        $ R_History.append("les Emma")
            if "les laura" in R_History:
                    $ R_History.remove("les laura")
                    if "les Laura" not in R_History:
                        $ R_History.append("les Laura")                    
            if "les rogue" in K_History:
                    $ K_History.remove("les rogue")
                    if "les Rogue" not in K_History:
                        $ K_History.append("les Rogue")
            if "les emma" in K_History:
                    $ K_History.remove("les emma")
                    if "les Emma" not in K_History:
                        $ K_History.append("les Emma")
            if "les laura" in K_History:
                    $ K_History.remove("les laura")
                    if "les Laura" not in K_History:
                        $ K_History.append("les Laura")                    
            if "les rogue" in E_History:
                    $ E_History.remove("les rogue")
                    if "les Rogue" not in E_History:
                        $ E_History.append("les Rogue")
            if "les kitty" in E_History:
                    $ E_History.remove("les kitty")
                    if "les Kitty" not in E_History:
                        $ E_History.append("les Kitty")
            if "les laura" in E_History:
                    $ E_History.remove("les laura")
                    if "les Laura" not in E_History:
                        $ E_History.append("les Laura")                    
            if "les rogue" in L_History:
                    $ L_History.remove("les rogue")
                    if "les Rogue" not in L_History:
                        $ L_History.append("les Rogue")
            if "les kitty" in L_History:
                    $ L_History.remove("les kitty")
                    if "les Kitty" not in L_History:
                        $ L_History.append("les Kitty")
            if "les emma" in L_History:
                    $ L_History.remove("les emma")
                    if "les Emma" not in L_History:
                        $ L_History.append("les Emma")
            #end shifts case of these words. . .
             
            if "locked" in P_RecentActions:
                $ P_RecentActions.remove("locked")
                if "locked" not in P_Traits:
                        $ P_Traits.append("locked")       
                    
            if "Dazzler and Longshot" in P_Inventory and "DL" in Shop_Inventory:
                $ Shop_Inventory.remove("DL")    
            if "Avengers Tower Penthouse" in P_Inventory and "A" in Shop_Inventory:
                $ Shop_Inventory.remove("A")
            if "256 Shades of Grey" in P_Inventory and "G" in Shop_Inventory:
                $ Shop_Inventory.remove("G")
                
            if "Dazzler and Longshot" in R_Inventory and "DL" in Shop_Inventory:
                $ Shop_Inventory.remove("DL")    
            if "Avengers Tower Penthouse" in R_Inventory and "A" in Shop_Inventory:
                $ Shop_Inventory.remove("A")
            if "256 Shades of Grey" in R_Inventory and "G" in Shop_Inventory:
                $ Shop_Inventory.remove("G")
                
            if "Dazzler and Longshot" in K_Inventory and "DL" in Shop_Inventory:
                $ Shop_Inventory.remove("DL")    
            if "Avengers Tower Penthouse" in K_Inventory and "A" in Shop_Inventory:
                $ Shop_Inventory.remove("A")
            if "256 Shades of Grey" in K_Inventory and "G" in Shop_Inventory:
                $ Shop_Inventory.remove("G")
                
            if "Dazzler and Longshot" in E_Inventory and "DL" in Shop_Inventory:
                $ Shop_Inventory.remove("DL")    
            if "Avengers Tower Penthouse" in E_Inventory and "A" in Shop_Inventory:
                $ Shop_Inventory.remove("A")
            if "256 Shades of Grey" in E_Inventory and "G" in Shop_Inventory:
                $ Shop_Inventory.remove("G")
                
            if "Dazzler and Longshot" in L_Inventory and "DL" in Shop_Inventory:
                $ Shop_Inventory.remove("DL")    
            if "Avengers Tower Penthouse" in L_Inventory and "A" in Shop_Inventory:
                $ Shop_Inventory.remove("A")
            if "256 Shades of Grey" in L_Inventory and "G" in Shop_Inventory:
                $ Shop_Inventory.remove("G")
                
            $ SaveVersion = 984
            #end Save 983 prep  
            
            
            #when new girl added. . .
            #$ Shop_Inventory.extend(["A","DL","G"]) #adds a new one for each
            
    call Failsafe                     
    return



return