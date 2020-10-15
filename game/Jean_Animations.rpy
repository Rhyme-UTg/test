# Basic character Sprites

image Jean_Sprite:
    LiveComposite(                
        (516,954), 
        (160,0), "Jean_Sprite_HairBack",  
        (0,0), ConditionSwitch(
            #body
            "JeanX.ArmPose == 2", "images/JeanSprite/Jean_Sprite_Body2.png",         # right hand up/left down
            "True", "images/JeanSprite/Jean_Sprite_Body1.png", #if JeanX.Arms == 1   # right Hand on hip/left raised 
            ),  
#        (0,0), ConditionSwitch(
#            #Water effect 
#            "JeanX.Water and JeanX.ArmPose == 1", "images/JeanSprite/Jean_Sprite_Water1.png",   
#            "JeanX.Water", "images/JeanSprite/Jean_Sprite_Water2.png",   
#            "True", Null(),        
#            ),      
       
#        (145,560), ConditionSwitch(    #(225,560)                                                                     
#            #Personal Wetness            
#            "not JeanX.Wet", Null(),
#            "JeanX.Legs and JeanX.Legs != 'skirt' and not JeanX.Upskirt", Null(),   
#            "JeanX.Panties and not JeanX.PantiesDown and JeanX.Wet <= 1", Null(),   
#            "JeanX.Wet == 1", ConditionSwitch( #Wet = 1
#                    "JeanX.Panties and JeanX.PantiesDown", AlphaMask("Wet_Drip","Jean_Drip_MaskP"),  
#                    "JeanX.Legs and JeanX.Legs != 'skirt'", AlphaMask("Wet_Drip","Jean_Drip_MaskP"),
#                    "True", AlphaMask("Wet_Drip","Jean_Drip_Mask"), #only plays if nothing is in the way
#                    ),
#            "True", ConditionSwitch( #Wet = 2+
#                    "JeanX.Panties and JeanX.PantiesDown", AlphaMask("Wet_Drip2","Jean_Drip_MaskP"),
#                    "JeanX.Legs and JeanX.Legs != 'skirt'", AlphaMask("Wet_Drip2","Jean_Drip_MaskP"),
#                    "JeanX.Panties", AlphaMask("Wet_Drip","Jean_Drip_Mask"), #"Wet_Drip2",# 
#                    "True", AlphaMask("Wet_Drip2","Jean_Drip_Mask"), #only plays if nothing is in the way
#                    ),
#            ),
#        (145,560), ConditionSwitch(    #(225,560)                                                                     
#            #dripping spunk            
#            "'in' not in JeanX.Spunk and 'anal' not in JeanX.Spunk", Null(),
#            "JeanX.Legs and JeanX.Legs != 'skirt' and not JeanX.Upskirt", Null(),   
#            "JeanX.Panties and not JeanX.PantiesDown and JeanX.Wet <= 1", Null(),   
#            "True", ConditionSwitch( #Wet = 2+
#                    "JeanX.Panties and JeanX.PantiesDown", AlphaMask("Spunk_Drip2","Jean_Drip_MaskP"),
##                    "JeanX.Legs and JeanX.Legs != 'skirt'", AlphaMask("Spunk_Drip2","Jean_Drip_MaskP"), #add if pantes have down art
#                    "JeanX.Panties", AlphaMask("Spunk_Drip","Jean_Drip_Mask"), #"Wet_Drip2",# 
#                    "True", AlphaMask("Spunk_Drip2","Jean_Drip_Mask"), #only plays if nothing is in the way
#                    ),
#            ),
        (0,0), ConditionSwitch(
            #pubes 
            "JeanX.Pubes", "images/JeanSprite/Jean_Sprite_Pubes.png",   
            "True", Null(),        
            ),      
        (0,0), ConditionSwitch(
            #nude lower piercings        
            "not JeanX.Pierce", Null(),  
            "JeanX.Panties and not JeanX.PantiesDown", Null(), 
            "JeanX.Legs != 'skirt' and JeanX.Legs and not JeanX.Upskirt", Null(), #skirt if wearing a skirt
            "JeanX.Pierce == 'barbell'", "images/JeanSprite/Jean_Sprite_Barbell_Pussy.png",  
            "JeanX.Pierce == 'ring'", "images/JeanSprite/Jean_Sprite_Ring_Pussy.png",  
            "True", Null(), 
            ),  
        (0,0), ConditionSwitch(
            #stockings    
            "JeanX.Hose == 'stockings'", "images/JeanSprite/Jean_Sprite_Hose_Stockings.png",
            "JeanX.Hose == 'stockings and garterbelt'", "images/JeanSprite/Jean_Sprite_Hose_StockingsandGarter.png",
            #"JeanX.Hose == 'garterbelt'", "images/JeanSprite/Jean_Sprite_Garters.png",
            "True", Null(),
            ),   
        (0,0), ConditionSwitch(
            #Personal Wetness            
            "not JeanX.Wet", Null(),
            "JeanX.Legs and JeanX.Wet <= 1", Null(),
            "True", "images/JeanSprite/Jean_Sprite_Wetness.png",       #JeanX.Wet >1
            ),       
        (0,0), ConditionSwitch(
            #panties    
            "not JeanX.Panties", Null(),
            "JeanX.PantiesDown", ConditionSwitch(                   
                    #if the panties are down
                    "not JeanX.Legs or JeanX.Upskirt or JeanX.Legs == 'skirt'", ConditionSwitch(                   
                            #if she's wearing a skirt or nothing else                    
                            "JeanX.Panties == 'green panties' and JeanX.Wet", "images/JeanSprite/Jean_Sprite_Panties_Green_Down.png", #fix
                            "JeanX.Panties == 'green panties'", "images/JeanSprite/Jean_Sprite_Panties_Green_Down.png",                             
                            "JeanX.Panties == 'lace panties'", "images/JeanSprite/Jean_Sprite_Panties_Green_Down.png", 
                            "JeanX.Panties == 'bikini bottoms'", "images/JeanSprite/Jean_Sprite_Panties_Bikini_Down.png", 
                            "True", "images/JeanSprite/Jean_Sprite_Panties_Green_Down.png", #fix
                            ),         
                    "True", Null(),
                    ),                    
            "True", ConditionSwitch(                
                    #if she's got panties and they are not down
                    "JeanX.Wet", ConditionSwitch(   
                        #if she's  wet                            
                        "JeanX.Panties == 'green panties'", "images/JeanSprite/Jean_Sprite_Panties_Green.png",
                        "JeanX.Panties == 'lace panties'", "images/JeanSprite/Jean_Sprite_Panties_Lace.png", 
                        "JeanX.Panties == 'bikini bottoms'", "images/JeanSprite/Jean_Sprite_Panties_Bikini.png", 
                        "True", "images/JeanSprite/Jean_Sprite_Panties_Green.png", 
                        ),
                    "True", ConditionSwitch(   
                        #if she's not wet                            
                        "JeanX.Panties == 'green panties'", "images/JeanSprite/Jean_Sprite_Panties_Green.png",
                        "JeanX.Panties == 'lace panties'", "images/JeanSprite/Jean_Sprite_Panties_Lace.png", 
                        "JeanX.Panties == 'bikini bottoms'", "images/JeanSprite/Jean_Sprite_Panties_Bikini.png", 
                        "True", "images/JeanSprite/Jean_Sprite_Panties_Green.png", 
                        ),                    
                    ),    
            ),       
        
        (0,0), ConditionSwitch(
            #pantyhose    
            "JeanX.Hose == 'pantyhose' and not JeanX.PantiesDown", "images/JeanSprite/Jean_Sprite_Hose_Pantyhose.png",
            "True", Null(),
            ),    
        (0,0), ConditionSwitch(
            #pants    
            "not JeanX.Legs", Null(),
            "JeanX.Upskirt", ConditionSwitch(                
                        #if the skirt's up or pants down 
                        "JeanX.Legs == 'pants'", "images/JeanSprite/Jean_Sprite_Legs_Pants_Down.png",  
                        "JeanX.Legs == 'yoga pants'", "images/JeanSprite/Jean_Sprite_Legs_YogaPants_Down.png",       
                        "JeanX.Legs == 'skirt'", "images/JeanSprite/Jean_Sprite_Legs_Skirt_Up.png", 
                        "True", Null(),                       
                        ),                    
            "True", ConditionSwitch(                
                    #if it's the ring pericings
                    "JeanX.Wet", ConditionSwitch(   
                        #if she's not wet
                        "JeanX.Legs == 'pants'", "images/JeanSprite/Jean_Sprite_Legs_Pants.png",  
                        "JeanX.Legs == 'yoga pants'", "images/JeanSprite/Jean_Sprite_Legs_YogaPants.png",       
                        "JeanX.Legs == 'skirt'", "images/JeanSprite/Jean_Sprite_Legs_Skirt.png", 
                        "True", Null(),
                        ),                    
                    "True", ConditionSwitch(   
                        #if she's wet
                        "JeanX.Legs == 'pants'", "images/JeanSprite/Jean_Sprite_Legs_Pants.png",  
                        "JeanX.Legs == 'yoga pants'", "images/JeanSprite/Jean_Sprite_Legs_YogaPants.png",       
                        "JeanX.Legs == 'skirt'", "images/JeanSprite/Jean_Sprite_Legs_Skirt.png", 
                        "True", Null(),
                        ),                    
                    ),                  
            ),    
        (0,0), ConditionSwitch(
            #clothed lower piercings         
            "JeanX.Legs == 'skirt' or JeanX.Legs == 'pants'", Null(),
            "JeanX.Pierce == 'barbell'", ConditionSwitch(   
                    #if it's the barbell pericings 
                    "JeanX.Legs and not JeanX.Upskirt", "images/JeanSprite/Jean_Sprite_Barbell_PussyC.png",  
                    "JeanX.Panties and not JeanX.PantiesDown", "images/JeanSprite/Jean_Sprite_Barbell_PussyC.png", 
                    "True", Null(),
                    ),    
            "JeanX.Pierce == 'ring'", ConditionSwitch(   
                    #if it's the ring pericings
                    "JeanX.Legs and not JeanX.Upskirt", "images/JeanSprite/Jean_Sprite_Ring_PussyC.png",  
                    "JeanX.Panties and not JeanX.PantiesDown", "images/JeanSprite/Jean_Sprite_Ring_PussyC.png", 
                    "True", Null(),
                    ),
            "True", Null(), 
            ),    
        (0,0), ConditionSwitch(
            #pussy spunk 
            "JeanX.Legs and not JeanX.Upskirt", Null(),
            "'in' in JeanX.Spunk or 'anal' in JeanX.Spunk", "images/JeanSprite/Jean_Sprite_Spunk_Pussy.png",
            "True", Null(), 
            ),  
        (0,0), ConditionSwitch(
            #nude peircings      
            "not JeanX.Pierce or ((JeanX.Over or JeanX.Chest) and not JeanX.Uptop)", Null(),  
            "JeanX.Pierce == 'barbell'", "images/JeanSprite/Jean_Sprite_Barbell_Tits.png",   
            "JeanX.Pierce == 'ring'", "images/JeanSprite/Jean_Sprite_Ring_Tits.png",               
            "True", Null(),              
            ),    
#        (0,0), ConditionSwitch(               
#            #neck            
#            "JeanX.Neck == 'leash choker'", "images/JeanSprite/Jean_Sprite_Neck_Leash.png",       
#            "True", Null(), 
#            ),            
        (0,0), ConditionSwitch(
            #left arm
            "JeanX.ArmPose == 2", "images/JeanSprite/Jean_Sprite_2LeftArm.png", # right hand up/left down
            "True", "images/JeanSprite/Jean_Sprite_1LeftArm.png", # right Hand on hip/left raised 
            "True", Null(),     
            ), 
        
        (0,0), ConditionSwitch(
            #Water effect 
            "JeanX.Water and JeanX.ArmPose == 1", "images/JeanSprite/Jean_Sprite_Water1.png",   
            "JeanX.Water", "images/JeanSprite/Jean_Sprite_Water2.png",   
            "True", Null(),        
            ),   
        
        (0,0), ConditionSwitch(                                                                        
            #Chest layer
            "JeanX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "JeanX.Chest == 'green bra' and JeanX.ArmPose == 2", "images/JeanSprite/Jean_Sprite_Chest_GreenBra2_Up.png", 
                    "JeanX.Chest == 'green bra'", "images/JeanSprite/Jean_Sprite_Chest_GreenBra1_Up.png", 
                    "JeanX.Chest == 'lace bra' and JeanX.ArmPose == 2", "images/JeanSprite/Jean_Sprite_Chest_GreenBra2_Up.png", 
                    "JeanX.Chest == 'lace bra'", "images/JeanSprite/Jean_Sprite_Chest_GreenBra1_Up.png", 
                    "JeanX.Chest == 'corset'", "images/JeanSprite/Jean_Sprite_Chest_Corset_Up.png",   
                    "JeanX.Chest == 'sports bra' and JeanX.ArmPose == 2", "images/JeanSprite/Jean_Sprite_Chest_Sportsbra2_Up.png", 
                    "JeanX.Chest == 'sports bra'", "images/JeanSprite/Jean_Sprite_Chest_Sportsbra1_Up.png", 
                    "JeanX.Chest == 'bikini top' and JeanX.ArmPose == 2", "images/JeanSprite/Jean_Sprite_Chest_Bikini2_Up.png", 
                    "JeanX.Chest == 'bikini top'", "images/JeanSprite/Jean_Sprite_Chest_Bikini1_Up.png", 
                    #"JeanX.Chest == 'lace corset'", "images/JeanSprite/Jean_Sprite_Chest_Corset_Lace_Up.png",   
                    "True", Null(),     
                    ),     
            "JeanX.Chest == 'green bra' and JeanX.ArmPose == 2", "images/JeanSprite/Jean_Sprite_Chest_GreenBra2.png", 
            "JeanX.Chest == 'green bra'", "images/JeanSprite/Jean_Sprite_Chest_GreenBra1.png", 
            "JeanX.Chest == 'lace bra' and JeanX.ArmPose == 2", "images/JeanSprite/Jean_Sprite_Chest_LaceBra2.png", 
            "JeanX.Chest == 'lace bra'", "images/JeanSprite/Jean_Sprite_Chest_LaceBra1.png", 
            "JeanX.Chest == 'sports bra' and JeanX.ArmPose == 2", "images/JeanSprite/Jean_Sprite_Chest_Sportsbra2.png", 
            "JeanX.Chest == 'sports bra'", "images/JeanSprite/Jean_Sprite_Chest_Sportsbra1.png", 
            "JeanX.Chest == 'bikini top' and JeanX.ArmPose == 2", "images/JeanSprite/Jean_Sprite_Chest_Bikini2.png", 
            "JeanX.Chest == 'bikini top'", "images/JeanSprite/Jean_Sprite_Chest_Bikini1.png", 
            "JeanX.Chest == 'corset' and JeanX.ArmPose == 2", "images/JeanSprite/Jean_Sprite_Chest_Corset2.png",   
            "JeanX.Chest == 'corset'", "images/JeanSprite/Jean_Sprite_Chest_Corset1.png",   
            #"JeanX.Chest == 'lace corset'", "images/JeanSprite/Jean_Sprite_Chest_Corset_Lace.png",   
            "True", Null(),              
            ),     

        (0,0), ConditionSwitch(
            #Over
            "JeanX.Uptop", ConditionSwitch(
                    # if top is up. . .
                    "JeanX.Over == 'pink shirt' and JeanX.ArmPose == 2", "images/JeanSprite/Jean_Sprite_Over_PinkShirt2_Up.png",
                    "JeanX.Over == 'pink shirt'", "images/JeanSprite/Jean_Sprite_Over_PinkShirt1_Up.png",
                    "JeanX.Over == 'green shirt' and JeanX.ArmPose == 2", "images/JeanSprite/Jean_Sprite_Over_GreenShirt2_Up.png",
                    "JeanX.Over == 'green shirt'", "images/JeanSprite/Jean_Sprite_Over_GreenShirt1_Up.png",
#                    "JeanX.Over == 'towel'", "images/JeanSprite/Jean_Sprite_Towel.png",
                    "True", Null(),     
                    ),                
            "JeanX.Over == 'pink shirt' and JeanX.ArmPose == 2", "images/JeanSprite/Jean_Sprite_Over_PinkShirt2.png",   # right hand up/left down
            "JeanX.Over == 'pink shirt'", "images/JeanSprite/Jean_Sprite_Over_PinkShirt1.png",                          # right Hand on hip/left raised 
            "JeanX.Over == 'green shirt' and JeanX.ArmPose == 2", "images/JeanSprite/Jean_Sprite_Over_GreenShirt2.png",   # right hand up/left down
            "JeanX.Over == 'green shirt'", "images/JeanSprite/Jean_Sprite_Over_GreenShirt1.png",                          # right Hand on hip/left raised 
            "JeanX.Over == 'towel' and JeanX.ArmPose == 2", "images/JeanSprite/Jean_Sprite_Over_Towel2.png",
            "JeanX.Over == 'towel'", "images/JeanSprite/Jean_Sprite_Over_Towel1.png",
            "True", Null(),     
            ),         
        (0,0), ConditionSwitch(                                                                        
            #clothed peircings        
            "not JeanX.Pierce or (not JeanX.Over and not JeanX.Chest and not JeanX.Uptop)", Null(),  
            "JeanX.Pierce == 'barbell'",  "images/JeanSprite/Jean_Sprite_Barbell_TitsC.png", 
            "JeanX.Pierce == 'ring'", "images/JeanSprite/Jean_Sprite_Ring_TitsC.png", 
            "True", Null(), 
            ),   
                
        (0,0), ConditionSwitch(
            #belly spunk 
            "'belly' in JeanX.Spunk", "images/JeanSprite/Jean_Sprite_Spunk_Belly.png",
            "True", Null(), 
            ),    
        (0,0), ConditionSwitch(
            #breast spunk      
            "'tits' in JeanX.Spunk", "images/JeanSprite/Jean_Sprite_Spunk_Tits.png",  
            "True", Null(),  
            ),   
        #Head
#        (0,0), ConditionSwitch(
#            # head  
#            "True", "images/JeanSprite/Jean_Sprite_Headref.png",   
#            ),      
#        (0,0), "Jean_Sprite_Head", #(55,0)
        (160,0), ConditionSwitch(
            # head
#            "renpy.showing('Jean_BJ_Animation')", Null(),  
            "True", "Jean_Sprite_Head",   
            ),            
    #Left hand stuff
        (0,0), ConditionSwitch(
            #left arms toplayer
            "renpy.showing('Jean_HJ_Animation')", Null(), 
            "JeanX.ArmPose == 1", "images/JeanSprite/Jean_Sprite_1LeftHand.png", # right Hand on hip/left raised 
            "True", Null(),     
            ),                 
        (0,0), ConditionSwitch(
            #Water effect 
            "JeanX.Water and JeanX.ArmPose == 1", "images/JeanSprite/Jean_Sprite_Water1Arm.png",   
            "True", Null(),        
            ),   
        (0,0), ConditionSwitch(
            #over left arm toplayer
            "renpy.showing('Jean_HJ_Animation')", Null(), 
            "JeanX.Chest == 'sports bra' and JeanX.ArmPose == 1", "images/JeanSprite/Jean_Sprite_Chest_Sportsbra1_Arm.png", # right Hand on hip/left raised 
            "True", Null(),     
            ),    
        (0,0), ConditionSwitch(
            #over left arm toplayer
            "renpy.showing('Jean_HJ_Animation')", Null(), 
            "JeanX.Over == 'pink shirt' and JeanX.ArmPose == 1", "images/JeanSprite/Jean_Sprite_Over_PinkShirt1_Arm.png", # right Hand on hip/left raised 
            "True", Null(),     
            ),         
    #End Left hand stuff   
        (0,0), ConditionSwitch(
            #right arms toplayer
            "JeanX.ArmPose == 2", "images/JeanSprite/Jean_Sprite_2RightHand.png", # right hand up/left down
            "True", "images/JeanSprite/Jean_Sprite_1RightHand.png", # right Hand on hip/left raised 
            #"True", Null(),     
            ),       
#        (0,0), ConditionSwitch( 
#            #hand spunk 
#            "JeanX.ArmPose == 2 or 'hand' not in JeanX.Spunk", Null(),  
#            "True", "images/JeanSprite/Jean_Sprite_Spunk_Hand.png",   
#            ),  
#        (0,0), ConditionSwitch(                                                                         #Props
#            "not JeanX.Held or JeanX.ArmPose != 2", Null(), 
#            "JeanX.ArmPose == 2 and JeanX.Held == 'phone'", "images/JeanSprite/Jean_held_phone.png",
#            "JeanX.ArmPose == 2 and JeanX.Held == 'dildo'", "images/JeanSprite/Jean_held_dildo.png",
#            "JeanX.ArmPose == 2 and JeanX.Held == 'vibrator'", "images/JeanSprite/Jean_held_vibrator.png",
#            "JeanX.ArmPose == 2 and JeanX.Held == 'panties'", "images/JeanSprite/Jean_held_panties.png",
#            "True", Null(), 
#            ),        
        (0,0), ConditionSwitch(
            #UI tool for When Jean is masturbating using Trigger3 actions
            "Trigger == 'lesbian' or not Trigger3 or Ch_Focus != JeanX", Null(),
            
            #this is not a lesbian thing, and a trigger is set, and Jean is the primary. . .
            "Trigger3 == 'fondle pussy'", "GirlGropePussy_JeanSelf",  
            "Trigger3 == 'fondle breasts'", ConditionSwitch(                                                                      
                    "Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts'", "GirlGropeLeftBreast_Jean", 
                        #When zero is working the right breast, fondle left
                    "Trigger == 'fondle breasts' or Trigger == 'suck breasts'", "GirlGropeRightBreast_Jean",   
                        #When zero is working the left breast, fondle right
                    "True", "GirlGropeBothBreast_Jean",
                        #else, fondle both
                    ),  
            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast_Jean",     
            "Trigger3 == 'vibrator pussy'", "VibratorPussy_Jean",
            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy_Jean",
            "Trigger3 == 'vibrator anal'", "VibratorAnal_Jean",
            "Trigger3 == 'vibrator anal insert'", "VibratorPussy_Jean",            
            "True", Null(),             
            ),                        
        (0,0), ConditionSwitch(  
            #UI tool for Trigger5(Threesome masutrbation) actions
            "not Trigger5 or Trigger4 != 'masturbation' or Ch_Focus == JeanX", Null(), 
            
            #Jean is not primary, and T4 is masturbation, and a T5 is selected
            "Trigger5 == 'fondle pussy' and Trigger != 'sex' and JeanX.Lust >= 70", "GirlFingerPussy_Jean",
            "Trigger5 == 'fondle pussy'", "GirlGropePussy_Jean",            
            "Trigger5 == 'fondle breasts'", "GirlGropeRightBreast_Jean",
            "Trigger5 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger5 == 'vibrator pussy'", "VibratorPussy",
            "Trigger5 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger5 == 'vibrator anal'", "VibratorAnal",
            "Trigger5 == 'vibrator anal insert'", "VibratorPussy",            
            "True", Null(), 
            ),                              
        (0,0), ConditionSwitch( 
            #UI tool for Trigger1(primary) actions
            #Jean is primary and a sex trigger is active
            "not Trigger or Ch_Focus != JeanX", Null(),            
            "Trigger == 'vibrator breasts'", "VibratorLeftBreast_Jean",
            "Trigger == 'fondle thighs'", "GropeThigh_Jean",            
            "Trigger == 'fondle breasts'", "GropeLeftBreast_Jean",
            "Trigger == 'suck breasts'", "LickRightBreast_Jean",
            "Trigger == 'fondle pussy' and Speed == 2", "FingerPussy_Jean",
            "Trigger == 'fondle pussy'", "GropePussy_Jean",
            "Trigger == 'lick pussy'", "Lickpussy_Jean",
            "Trigger == 'vibrator pussy'", "VibratorPussy_Jean",
            "Trigger == 'vibrator pussy insert'", "VibratorPussy_Jean",
            "Trigger == 'vibrator anal'", "VibratorAnal_Jean",
            "Trigger == 'vibrator anal insert'", "VibratorPussy_Jean",            
            "True", Null(), 
            ),            
        (0,0), ConditionSwitch(                
            #UI tool for Trigger2(secondary) actions
            "not Trigger2 or Ch_Focus != JeanX", Null(),
            
            #Jean is primary and an offhand trigger is active            
            "Trigger2 == 'fondle breasts'", ConditionSwitch(                                                                      
                    "Trigger2 == 'fondle breasts' and Trigger == 'suck breasts'", "GropeLeftBreast_Jean", 
                        #When zero is sucking on the right breast, fondle left
                    "True", "GropeRightBreast_Jean",
                        #else, fondle right
                    ),  
            "Trigger2 == 'vibrator breasts' and Trigger == 'suck breasts'", "VibratorLeftBreast_Jean",       
                #When sucking right breast, vibrator left            
            "Trigger2 == Trigger", Null(),
                #When both triggers are the same, do nothing              
            "Trigger2 == 'suck breasts'", "LickLeftBreast_Jean",        
            "Trigger2 == 'fondle pussy'", "GropePussy_Jean",
            "Trigger2 == 'lick pussy'", "Lickpussy_Jean",       
            "Trigger2 == 'vibrator breasts'", "VibratorRightBreast_Jean",
            "Trigger2 == 'vibrator pussy'", "VibratorPussy_Jean",
            "Trigger2 == 'vibrator pussy insert'", "VibratorPussy_Jean",
            "Trigger2 == 'vibrator anal'", "VibratorAnal_Jean",
            "Trigger2 == 'vibrator anal insert'", "VibratorPussy_Jean",            
            "True", Null(), 
            ),    
        (0,0), ConditionSwitch(  
            #UI tool for Trigger4(Threesome) actions (ie Rogue's hand on her)
            "not Trigger4 or Ch_Focus != JeanX", Null(),
            
            # There is a threesome trigger set and Jean is the target of it
            "Trigger4 == 'fondle pussy' and Trigger != 'sex' and JeanX.Lust >= 70", "GirlFingerPussy_Jean",
            "Trigger4 == 'fondle pussy'", "GirlGropePussy_Jean",            
            "Trigger4 == 'lick pussy'", "Lickpussy_Jean",
            "Trigger4 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_Jean", 
            "Trigger4 == 'suck breasts'", "LickRightBreast_Jean",      
            "Trigger4 == 'fondle breasts'", ConditionSwitch( 
                    "Trigger == 'fondle breasts' or Trigger == 'suck breasts'", "GirlGropeLeftBreast_Jean", #When zero is working the right breast, fondle left                                                  
#                    "Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts'", "GirlGropeRightBreast_Jean",  #When zero is working the left breast, fondle right                                         
#                    "Trigger3 == 'fondle breasts' or Trigger3 == 'suck breasts'", "GirlGropeRightBreast_Jean", #When zero is working the left breast, fondle right 
                    "True", "GirlGropeRightBreast_Jean",#else, fondle right
                    ),       
            "Trigger4 == 'vibrator breasts'", "VibratorRightBreast",     
            "Trigger4 == 'vibrator pussy'", "VibratorPussy",
            "Trigger4 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger4 == 'vibrator anal'", "VibratorAnal",
            "Trigger4 == 'vibrator anal insert'", "VibratorPussy",
            "True", Null(),             
            ),
        (0,0), ConditionSwitch(             
            #UI tool for Trigger3(lesbian) actions (ie Rogue's hand on her when Jean is secondary)
            "Trigger != 'lesbian' or Ch_Focus == JeanX or not Trigger3", Null(),            
            
            # If there is a Trigger3 and Jean is not the focus
            "Trigger3 == 'fondle pussy' and Trigger != 'sex' and JeanX.Lust >= 70", "GirlFingerPussy_Jean",
            "Trigger3 == 'fondle pussy'", "GirlGropePussy_Jean",            
            "Trigger3 == 'lick pussy'", "Lickpussy_Jean",
            "Trigger3 == 'suck breasts' and (Trigger2 != 'suck breasts' or Trigger == 'suck breasts')", "LickLeftBreast_Jean", 
            "Trigger3 == 'suck breasts'", "LickRightBreast_Jean",            
            "Trigger3 == 'fondle breasts'", ConditionSwitch( 
                    "Trigger == 'fondle breasts' or Trigger == 'suck breasts'", "GirlGropeLeftBreast_Jean",                    
                        #When zero is working the right breast, fondle left                                                  
                    "Trigger2 == 'fondle breasts' or Trigger2 == 'suck breasts'", "GirlGropeRightBreast_Jean", 
                        #When zero is working the left breast, fondle right                                         
                    "Trigger3 == 'fondle breasts' or Trigger3 == 'suck breasts'", "GirlGropeLeftBreast_Jean", 
                        #When zero is working the right breast, fondle left 
                    "True", "GirlGropeRightBreast_Jean",                    
                        #else, fondle right
                    ),                             
            "Trigger3 == 'vibrator breasts'", "VibratorRightBreast",               
            "Trigger3 == 'vibrator pussy'", "VibratorPussy",
            "Trigger3 == 'vibrator pussy insert'", "VibratorPussy",
            "Trigger3 == 'vibrator anal'", "VibratorAnal",
            "Trigger3 == 'vibrator anal insert'", "VibratorPussy",            
            "True", Null(),                
            ),   
        )      
    anchor (0.6, 0.0)               
    yoffset 15            
    zoom .75                

image Jean_Sprite_HairBack: 
    ConditionSwitch(
            #hair back 
            "not JeanX.Hair", Null(),
            "renpy.showing('Jean_BJ_Animation')", Null(), 
#            "renpy.showing('Jean_SexSprite')", "images/JeanSex/Jean_Sprite_Hair_Long_UnderSex.png",
            "JeanX.Hair == 'wet' or JeanX.Water", "images/JeanSprite/Jean_Sprite_Hair_Wet_Under.png",
            "JeanX.Hair", "images/JeanSprite/Jean_Sprite_Hair_Short_Under.png",   
            "True", Null(),        
            ),   
#    "images/JeanSprite/Jean_Sprite_Hair_Long_Under.png"       
    anchor (0.6, 0.0)                
    zoom .32                   

image Jean_Sprite_HairMid: 
    ConditionSwitch(
            #hair back 
            "not JeanX.Hair", Null(),
            "renpy.showing('Jean_BJ_Animation')", Null(), 
#            "renpy.showing('Jean_SexSprite')", "images/JeanSex/Jean_Sprite_Hair_Long_UnderSex.png",
            "JeanX.Hair == 'wet' or JeanX.Water", Null(),
            "JeanX.Hair", "images/JeanSprite/Jean_Sprite_Hair_Short_Mid.png",   
            "True", Null(),        
            ),     
    anchor (0.6, 0.0)                
    zoom .5 
 
image Jean_Sprite_HairTop: 
    ConditionSwitch(
            #hair back 
            "not JeanX.Hair", Null(),
            "renpy.showing('Jean_SexSprite')", "images/JeanSex/Jean_Sprite_Hair_Short_OverSex.png",
            "JeanX.Hair == 'wet' or JeanX.Water", "images/JeanSprite/Jean_Sprite_Hair_Wet_Over.png",
            "JeanX.Hair", "images/JeanSprite/Jean_Sprite_Hair_Short_Over.png",
            "True", Null(),        
            ),   
#    "images/JeanSprite/Jean_Sprite_Hair_Long_Under.png"       
    anchor (0.6, 0.0)                
    zoom .5                
            
image Jean_Sprite_Head:            
    LiveComposite(
        (900,900),      
#        (0,0), ConditionSwitch(
#                # hair behind face
#                "renpy.showing('Jean_SexSprite')", "images/JeanSex/Jean_Sprite_Hair_Long_UnderSex.png", 
#                "True", Null(),                        
#                ),         
        (0,0), ConditionSwitch(
                # Face background plate
                "JeanX.Blush >= 2", "images/JeanSprite/Jean_Sprite_Head_Blush2.png", 
                "JeanX.Blush", "images/JeanSprite/Jean_Sprite_Head_Blush.png",  
                "True", "images/JeanSprite/Jean_Sprite_Head.png",                        
                ),        
        (0,0), ConditionSwitch(#chin spunk
            "'chin' not in JeanX.Spunk", Null(),
            "renpy.showing('Jean_BJ_Animation') and Speed >= 2", Null(),
            "True", "images/JeanSprite/Jean_Sprite_Spunk_Chin.png",            
            ),                
#        (0,0), ConditionSwitch(#Mouths 
#            "renpy.showing('Jean_BJ_Animation')", "images/JeanSprite/Jean_Sprite_Mouth_SuckingBJ.png", #and Speed >= 2
#            "JeanX.Mouth == 'normal'", "images/JeanSprite/Jean_Sprite_Mouth_Normal.png",
#            "JeanX.Mouth == 'lipbite'", "images/JeanSprite/Jean_Sprite_Mouth_Lipbite.png",
#            "JeanX.Mouth == 'sucking'", "images/JeanSprite/Jean_Sprite_Mouth_Sucking.png",            
#            "JeanX.Mouth == 'kiss'", "images/JeanSprite/Jean_Sprite_Mouth_Kiss.png",
#            "JeanX.Mouth == 'sad'", "images/JeanSprite/Jean_Sprite_Mouth_Sad.png",
#            "JeanX.Mouth == 'smile'", "images/JeanSprite/Jean_Sprite_Mouth_Smile.png",
#            "JeanX.Mouth == 'surprised'", "images/JeanSprite/Jean_Sprite_Mouth_Surprised.png",            
#            "JeanX.Mouth == 'tongue'", "images/JeanSprite/Jean_Sprite_Mouth_Tongue.png",                
#            "JeanX.Mouth == 'grimace'", "images/JeanSprite/Jean_Sprite_Mouth_Smile.png",              
#            "JeanX.Mouth == 'smirk'", "images/JeanSprite/Jean_Sprite_Mouth_Smirk.png",           
#            "True", "images/JeanSprite/Jean_Sprite_Mouth_Normal.png",
#            ),         
        (0,0), ConditionSwitch(#Mouths
            "'mouth' in JeanX.Spunk", ConditionSwitch(
                    "JeanX.Mouth == 'normal'", "images/JeanSprite/Jean_Sprite_Mouth_Normal_Spunk.png",
                    "JeanX.Mouth == 'lipbite'", "images/JeanSprite/Jean_Sprite_Mouth_Lipbite_Spunk.png",
                    "JeanX.Mouth == 'sucking'", "images/JeanSprite/Jean_Sprite_Mouth_Tongue_Spunk.png",            
                    "JeanX.Mouth == 'kiss'", "images/JeanSprite/Jean_Sprite_Mouth_Kiss_Spunk.png",
                    "JeanX.Mouth == 'sad'", "images/JeanSprite/Jean_Sprite_Mouth_Sad_Spunk.png",
                    "JeanX.Mouth == 'smile'", "images/JeanSprite/Jean_Sprite_Mouth_Smile_Spunk.png",
                    "JeanX.Mouth == 'surprised'", "images/JeanSprite/Jean_Sprite_Mouth_Surprised_Spunk.png",            
                    "JeanX.Mouth == 'tongue'", "images/JeanSprite/Jean_Sprite_Mouth_Tongue_Spunk.png",                
                    "JeanX.Mouth == 'grimace'", "images/JeanSprite/Jean_Sprite_Mouth_Smile_Spunk.png",              
                    "JeanX.Mouth == 'smirk'", "images/JeanSprite/Jean_Sprite_Mouth_Smirk_Spunk.png",           
                    "True", "images/JeanSprite/Jean_Sprite_Mouth_Normal_Spunk.png",
                    ),
            "True", ConditionSwitch(
                    "JeanX.Mouth == 'normal'", "images/JeanSprite/Jean_Sprite_Mouth_Normal.png",
                    "JeanX.Mouth == 'lipbite'", "images/JeanSprite/Jean_Sprite_Mouth_Lipbite.png",
                    "JeanX.Mouth == 'sucking'", "images/JeanSprite/Jean_Sprite_Mouth_Tongue.png",            
                    "JeanX.Mouth == 'kiss'", "images/JeanSprite/Jean_Sprite_Mouth_Kiss.png",
                    "JeanX.Mouth == 'sad'", "images/JeanSprite/Jean_Sprite_Mouth_Sad.png",
                    "JeanX.Mouth == 'smile'", "images/JeanSprite/Jean_Sprite_Mouth_Smile.png",
                    "JeanX.Mouth == 'surprised'", "images/JeanSprite/Jean_Sprite_Mouth_Surprised.png",            
                    "JeanX.Mouth == 'tongue'", "images/JeanSprite/Jean_Sprite_Mouth_Tongue.png",                
                    "JeanX.Mouth == 'grimace'", "images/JeanSprite/Jean_Sprite_Mouth_Smile.png",              
                    "JeanX.Mouth == 'smirk'", "images/JeanSprite/Jean_Sprite_Mouth_Smirk.png",           
                    "True", "images/JeanSprite/Jean_Sprite_Mouth_Normal.png",
                    ),
            ),                                
        (0,0), ConditionSwitch(                                                                       
            #brows
            "JeanX.Blush >= 2", ConditionSwitch(
                    "JeanX.Brows == 'normal'", "images/JeanSprite/Jean_Sprite_Brows_Normal2.png",
                    "JeanX.Brows == 'angry'", "images/JeanSprite/Jean_Sprite_Brows_Angry2.png",
                    "JeanX.Brows == 'sad'", "images/JeanSprite/Jean_Sprite_Brows_Sad2.png",
                    "JeanX.Brows == 'surprised'", "images/JeanSprite/Jean_Sprite_Brows_Surprised.png",        
                    "JeanX.Brows == 'confused'", "images/JeanSprite/Jean_Sprite_Brows_Confused2.png",
                    "True", "images/JeanSprite/Jean_Sprite_Brows_Normal2.png",
                    ),
            "JeanX.Blush", ConditionSwitch(
                    "JeanX.Brows == 'normal'", "images/JeanSprite/Jean_Sprite_Brows_Normal1.png",
                    "JeanX.Brows == 'angry'", "images/JeanSprite/Jean_Sprite_Brows_Angry1.png",
                    "JeanX.Brows == 'sad'", "images/JeanSprite/Jean_Sprite_Brows_Sad1.png",
                    "JeanX.Brows == 'surprised'", "images/JeanSprite/Jean_Sprite_Brows_Surprised.png",        
                    "JeanX.Brows == 'confused'", "images/JeanSprite/Jean_Sprite_Brows_Confused1.png",
                    "True", "images/JeanSprite/Jean_Sprite_Brows_Normal1.png",
                    ),
            "True", ConditionSwitch(
                    "JeanX.Brows == 'normal'", "images/JeanSprite/Jean_Sprite_Brows_Normal.png",
                    "JeanX.Brows == 'angry'", "images/JeanSprite/Jean_Sprite_Brows_Angry.png",
                    "JeanX.Brows == 'sad'", "images/JeanSprite/Jean_Sprite_Brows_Sad.png",
                    "JeanX.Brows == 'surprised'", "images/JeanSprite/Jean_Sprite_Brows_Surprised.png",        
                    "JeanX.Brows == 'confused'", "images/JeanSprite/Jean_Sprite_Brows_Confused.png",
                    "True", "images/JeanSprite/Jean_Sprite_Brows_Normal.png",
                    ),
            ),        
        (0,0), "Jean Blink",     #Eyes           
#        (0,0), ConditionSwitch(
#            #Face Water
#            "not JeanX.Water", Null(),
#            "True", "images/JeanSprite/Jean_Sprite_Wet_Head.png",
#            ),  
        (0,0), ConditionSwitch(                                                                         
            #Hair over
            "not JeanX.Hair", Null(),
            "renpy.showing('Jean_TJ_Animation')", Null(),
#            "renpy.showing('Jean_SexSprite')", "images/JeanSex/Jean_Sprite_Hair_Long_OverSex.png",
            "JeanX.Hair == 'wet' or JeanX.Water", "images/JeanSprite/Jean_Sprite_Hair_Wet_Over.png",
            "JeanX.Hair", "images/JeanSprite/Jean_Sprite_Hair_Short_Over.png",
            "True", Null(),
            ),    
        (0,0), ConditionSwitch(
            #Hair Water
            "not JeanX.Water", Null(),
            "True", "images/JeanSprite/Jean_Sprite_Head_Wet.png",
#            "True", "images/JeanSprite/Jean_Sprite_Hair_Wet.png",
            ),
        (0,0), ConditionSwitch(
            #facial spunk               
            "'hair' in JeanX.Spunk", "images/JeanSprite/Jean_Sprite_Spunk_Facial2.png",  
            "'facial' in JeanX.Spunk", "images/JeanSprite/Jean_Sprite_Spunk_Facial1.png",            
            "True", Null(),            
            ),  
        )                
    anchor (0.6, 0.0)   
    #alpha 0.9
    zoom .32                      

image Jean Blink:            
    ConditionSwitch(
    "JeanX.Eyes == 'sexy'", "images/JeanSprite/Jean_Sprite_Eyes_Sexy.png",
    "JeanX.Eyes == 'side'", "images/JeanSprite/Jean_Sprite_Eyes_Side.png",
    "JeanX.Eyes == 'surprised'", "images/JeanSprite/Jean_Sprite_Eyes_Surprised.png",
    "JeanX.Eyes == 'normal'", "images/JeanSprite/Jean_Sprite_Eyes_Normal.png",    
    "JeanX.Eyes == 'stunned'", "images/JeanSprite/Jean_Sprite_Eyes_Stunned.png",
    "JeanX.Eyes == 'down'", "images/JeanSprite/Jean_Sprite_Eyes_Down.png",
    "JeanX.Eyes == 'closed'", "images/JeanSprite/Jean_Sprite_Eyes_Closed.png",
    "JeanX.Eyes == 'leftside'", "images/JeanSprite/Jean_Sprite_Eyes_Leftside.png",
    "JeanX.Eyes == 'manic'", "images/JeanSprite/Jean_Sprite_Eyes_Normal.png",
    "JeanX.Eyes == 'psychic'", "images/JeanSprite/Jean_Sprite_Eyes_Psychic.png",
    "JeanX.Eyes == 'squint'", "Jean_Squint",
    "True", "images/JeanSprite/Jean_Sprite_Eyes_Normal.png", 
    ),
    choice:
        3.5
    choice:
        3.25
    choice:
        3    
    "images/JeanSprite/Jean_Sprite_Eyes_Closed.png"
    .25
    repeat                

image Jean_Squint:       
    "images/JeanSprite/Jean_Sprite_Eyes_Normal.png"            
    choice:
        3.5
    choice:
        3.25
    choice:
        3    
    "images/JeanSprite/Jean_Sprite_Eyes_Sexy.png"
    .25
    repeat                         
            
            

image Jean_Drip_Mask:
    #This is the mask for her drip pattern
    contains:
        "images/JeanSprite/Jean_Sprite_WetMask.png"      
        offset (-145,-560)#(-225,-560)

image Jean_Drip_MaskP:
    #This is the mask for her drip pattern in panties down mode
    contains:
        "images/JeanSprite/Jean_Sprite_WetMaskP.png"      
        offset (-145,-560)#(-225,-560)
            
# End Jean Sprite / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /






# Start Jean Sex Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Jean Sex element //////////////////////////////////////////////////////////////////////////// / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /   

image Jean_SexSprite:
    #core sex animation   
    contains:
        ConditionSwitch(                                                              
            # Jean's upper body
            "Player.Cock == 'in'", ConditionSwitch(                                                               
                    # If during sex
                    "Speed == 1", "Jean_Sex_Body_S1",#heading
                    "Speed == 2", "Jean_Sex_Body_S2",#slow
                    "Speed == 3", "Jean_Sex_Body_S3",#fast
                    "Speed >= 4", "Jean_Sex_Body_S4",#cumming
                    "True",       "Jean_Sex_Body_S0",#Static
                    ),
            "Player.Cock == 'anal'", ConditionSwitch(                                                              
#                    # If during Anal
                    "Speed == 1", "Jean_Sex_Body_A1",#heading
                    "Speed == 2", "Jean_Sex_Body_A2",#slow
                    "Speed == 3", "Jean_Sex_Body_A3",#fast
                    "Speed >= 4", "Jean_Sex_Body_A4",#cumming
                    "True",       "Jean_Sex_Body_A0",#Static
                    ),                    
            "Player.Cock == 'foot'", ConditionSwitch(                                      
                    # If during Footjob
                    "not Player.Sprite","Jean_Sex_Body_F0",#Static
                    "Speed == 1", "Jean_Sex_Body_F1",#heading
                    "Speed >= 4", "Jean_Sex_Body_F0",#cumming
                    "Speed >= 2", "Jean_Sex_Body_F2",#slow
                    "True",       "Jean_Sex_Body_F0",#Static
                    ),    
            
            "True", ConditionSwitch(                                                              
                    # If neither
                    "not Player.Sprite","Jean_Sex_Body_H0",#Static
                    "Speed == 1", "Jean_Sex_Body_H1",#slow
                    "Speed == 4", "Jean_Sex_Body_H0",#cumming
                    "Speed >= 2", "Jean_Sex_Body_H2",#fast
                    "True",       "Jean_Sex_Body_H0",#Static
                    ),
            )
    contains:
        ConditionSwitch(                                                               
            # Jean's lower body
            "Player.Cock == 'in'", ConditionSwitch(                                                               
                    # If during sex
                    "Speed == 1", "Jean_Sex_Legs_S1",#heading
                    "Speed == 2", "Jean_Sex_Legs_S2",#slow
                    "Speed == 3", "Jean_Sex_Legs_S3",#fast
                    "Speed >= 4", "Jean_Sex_Legs_S4",#cumming
                    "True", "Jean_Sex_Legs_S0",#Static
                    ),
            "Player.Cock == 'anal'", ConditionSwitch(                                                              
                    # If during Anal
                    "Speed == 1", "Jean_Sex_Legs_A1",#heading
                    "Speed == 2", "Jean_Sex_Legs_A2",#slow
                    "Speed == 3", "Jean_Sex_Legs_A3",#fast
                    "Speed >= 4", "Jean_Sex_Legs_A4",#cumming
                    "True", "Jean_Sex_Legs_A0",#Static
                    ),
            "Player.Cock == 'foot'", ConditionSwitch(                                      
                    # If during Footjob
                    "not Player.Sprite","Jean_Sex_Legs_F0",#Static
                    "Speed == 1", "Jean_Sex_Legs_F1",#heading
                    "Speed >= 4", "Jean_Sex_Legs_F0",#cumming
                    "Speed >= 2", "Jean_Sex_Legs_F2",#slow
                    "True",       "Jean_Sex_Legs_F0",#Static   
                    ),     
            "True", ConditionSwitch(                                                               
                    # If neither
                    "not Player.Sprite","Jean_Sex_Legs_H0",#Static
                    "Speed == 1", "Jean_Sex_Legs_H1",#heading
                    "Speed == 4", "Jean_Sex_Legs_H0",#cumming
                    "Speed >= 2", "Jean_Sex_Legs_H2",#slow
                    "True", "Jean_Sex_Legs_H0",#Static
                    ),
            )    
    zoom .6 #0.6
    transform_anchor True
    anchor (.5,.5)
#    rotate -30
    
image Jean_Sex_HairBack:
    #Hair underlay
    "Jean_Sprite_HairBack"
    transform_anchor True
    zoom 1.8
    anchor (0.5, 0.5)
    rotate 10
    pos (800,100)
  
image Jean_Sex_Head:
    #Hair underlay
    "Jean_Sprite_Head"
    transform_anchor True
    zoom 1.8
    anchor (0.5, 0.5)
    rotate 10
    pos (800,100)
                    


image Jean_Sex_Body:                                                                        
    #Her torso for the sex pose
    contains:
            "Jean_Sex_HairBack"        
    contains:
            # hand
#            "images/JeanSex/Jean_Sex_Hand.png"
                    
            ConditionSwitch(
                    "Player.Cock == 'foot'", Null(), 
                    "True", "images/JeanSex/Jean_Sex_Hand.png"       
                    ) 
    contains:
            # Over under layer
        ConditionSwitch(   
            "not JeanX.Over", Null(), 
            "JeanX.Uptop", ConditionSwitch(   
                    #if uptop                       
                    "JeanX.Over == 'jacket'", "images/JeanSex/Jean_Sex_Jacket_Back_Up.png",
                    "True", Null(),
                    ),                
            "True", ConditionSwitch(
                    #if not uptop        
                    "JeanX.Over == 'jacket'", "images/JeanSex/Jean_Sex_Jacket_Back.png",
                    "True", Null(),
                    ),    
            )
    contains:
            # body
            "images/JeanSex/Jean_Sex_Body.png"
    contains:
            # piercings tits
        ConditionSwitch(   
            "not JeanX.Pierce", Null(),
            "JeanX.Pierce == 'barbell'", "images/JeanSex/Jean_Sex_Barbell_Tits.png", 
            "JeanX.Pierce == 'ring'", "images/JeanSex/Jean_Sex_Ring_Tits.png", 
            "True", Null(), 
            )
    contains:
            # Chest clothing layer
        ConditionSwitch(    
            "JeanX.Neck == 'leash choker'", "images/JeanSex/Jean_Sex_Leash.png", 
            "True", Null(),  
            )
    contains:
            # garters
        ConditionSwitch(    
            "JeanX.Hose == 'stockings and garterbelt' or JeanX.Hose == 'garterbelt'", "images/JeanSex/Jean_Sex_Garter.png", 
            "True", Null(),  
            )
    contains:
            # Chest clothing layer
        ConditionSwitch(    
            "not JeanX.Chest", Null(),              
            "JeanX.Uptop",ConditionSwitch(  
                    #if the top is up. . .
                    "not JeanX.Chest", Null(),  
                    "JeanX.Chest == 'leather bra'", "images/JeanSex/Jean_Sex_Bra_Leather_Up.png", 
                    "JeanX.Chest == 'wolvie top'", "images/JeanSex/Jean_Sex_Top_Wolvie_Up.png", 
                    "JeanX.Chest == 'corset'", "images/JeanSex/Jean_Sex_Corset_Up.png",   
                    "JeanX.Chest == 'lace corset'", "images/JeanSex/Jean_Sex_Corset_Lace_Up.png",   
                    "JeanX.Chest == 'bikini top'", "images/JeanSex/Jean_Sex_Top_Bikini_Up.png",  
#                    "JeanX.Chest == 'sports bra'", "images/JeanSex/Jean_Sex_Bra_Sports_Up.png",  
#                    "JeanX.Chest == 'lace bra'", "images/JeanSex/Jean_Sex_Bra_Lace_Up.png",  
                    "True", Null(),  
                    ),     
            # else. . .
            "JeanX.Chest == 'leather bra'", "images/JeanSex/Jean_Sex_Bra_Leather.png", 
            "JeanX.Chest == 'wolvie top'", "images/JeanSex/Jean_Sex_Top_Wolvie.png", 
            "JeanX.Chest == 'corset'", "images/JeanSex/Jean_Sex_Corset.png",   
            "JeanX.Chest == 'lace corset'", "images/JeanSex/Jean_Sex_Corset_Lace.png",   
            "JeanX.Chest == 'bikini top'", "images/JeanSex/Jean_Sex_Top_Bikini.png",  
#            "JeanX.Chest == 'sports bra'", "images/JeanSex/Jean_Sex_Bra_Sports.png",  
#            "JeanX.Chest == 'lace bra'", "images/JeanSex/Jean_Sex_Bra_Lace.png",  
            "True", Null(),  
            )
    contains:
            # piercings tits over clothes
        ConditionSwitch(   
            "not JeanX.Pierce or JeanX.Uptop", Null(),
            "JeanX.Pierce == 'barbell'", "images/JeanSex/Jean_Sex_Barbell_Tits_C.png", 
            "JeanX.Pierce == 'ring'", "images/JeanSex/Jean_Sex_Ring_Tits_C.png", 
            "True", Null(), 
            )
    contains:
            # Over clothing layer
        ConditionSwitch(   
            "not JeanX.Over", Null(), 
            "JeanX.Uptop", ConditionSwitch(   
                    #if uptop                       
                    "JeanX.Over == 'jacket'", "images/JeanSex/Jean_Sex_Jacket_Up.png",
#                    "JeanX.Over == 'towel'", "images/JeanSex/Jean_Sex_Towel_Up.png",
                    "True", Null(),
                    ),                
            "True", ConditionSwitch(
                    #if not uptop        
                    "JeanX.Over == 'jacket'", "images/JeanSex/Jean_Sex_Jacket.png",
#                    "JeanX.Over == 'towel'", "images/JeanSex/Jean_Sex_Towel.png",
                    "True", Null(),
                    ),    
            )
    contains:
            # spunk
        ConditionSwitch(    
            "'belly' in JeanX.Spunk", "images/JeanSex/Jean_Sex_Spunk_Belly.png", 
            "True", Null(),
            ) 
    contains:
            # spunk on tits
            ConditionSwitch(    
                "'tits' not in JeanX.Spunk", Null(),
                "True", "images/JeanSex/Jean_Sex_Spunk_Tits.png",
                )     
    contains:
            "Jean_Sex_Head"
    transform_anchor True
    zoom .9 #1 
    offset (55,55)
#    rotate 30
#end Jean Body base

image Jean_Sex_Legs:                                                                        
    #Her Legs during sex             
    contains:
            # legs under
        ConditionSwitch(    
            "JeanX.Legs == 'skirt'", "images/JeanSex/Jean_Sex_Skirt_Back.png",  
            "True", Null(),
            )
#    contains:
#            # spunk
#        ConditionSwitch(    
#            "'anal' in JeanX.Spunk or 'in' in JeanX.Spunk", "images/JeanSex/Jean_Spunk_Sex.png", 
#            "True", Null(),
#            )
    contains:
            # Legs base
        ConditionSwitch(    
            "Player.Cock == 'foot'", "images/JeanSex/Jean_Sex_Legs_Foot.png", 
            "True", "images/JeanSex/Jean_Sex_Legs_High.png", 
            )
    contains:
            # anus
        ConditionSwitch(    
            "Player.Cock == 'anal' and Speed > 1", "images/JeanSex/Jean_Sex_Anus_L.png", #and speed above heading?
            "Player.Cock == 'anal' and Speed > 0", "images/JeanSex/Jean_Sex_Anus_M.png", #and speed above heading?
            "'anal' in JeanX.Spunk", "images/JeanSex/Jean_Sex_Anus_M.png", # If it's full. . .
            "True", "images/JeanSex/Jean_Sex_Anus_S.png", 
            )  
    contains:
            # anal spunk
        ConditionSwitch(    
            "'anal' not in JeanX.Spunk", Null(),
            "Player.Cock == 'anal' and Speed > 1", "images/JeanSex/Jean_Sex_Spunk_Anal_U.png", #speed above heading?
            "True", "images/JeanSex/Jean_Sex_Spunk_Anal.png", 
            ) 
    contains:
            # pussy
        ConditionSwitch(    
            "Player.Cock == 'in' and Speed > 1", "images/JeanSex/Jean_Sex_Pussy_Open.png", #and speed above heading?
            "Player.Cock == 'in' and Speed > 0", "images/JeanSex/Jean_Sex_Pussy_Mid.png", #and speed heading?
            "True", "images/JeanSex/Jean_Sex_Pussy_Closed.png", 
            )  
    contains:
            # pussy wetness
        ConditionSwitch(    
            "not JeanX.Wet", Null(),
            "True", "images/JeanSex/Jean_Sex_Wet.png", 
            ) 
    contains:
            # pussy spunk
        ConditionSwitch(    
            "'in' not in JeanX.Spunk", Null(),
            "Player.Cock == 'in' and Speed > 1", "images/JeanSex/Jean_Sex_Spunk_Pussy_Open.png", #and speed above heading?
            "True", "images/JeanSex/Jean_Sex_Spunk_Pussy.png", 
            ) 
    contains:
            # pubes
        ConditionSwitch(    
            "not JeanX.Pubes", Null(),
            "Player.Cock == 'in' and Speed > 1", "images/JeanSex/Jean_Sex_Pubes_Open.png", #and speed above heading?
            "Player.Cock == 'in' and Speed > 0", "images/JeanSex/Jean_Sex_Pubes_Mid.png", #and speed heading?
            "True", "images/JeanSex/Jean_Sex_Pubes_Closed.png", 
            )  
    contains:
            # piercings
        ConditionSwitch(    
            "JeanX.Pierce == 'barbell' and Player.Cock == 'in' and Speed > 1", "images/JeanSex/Jean_Sex_Barbell_Pussy_O.png", #and speed above heading?
            "JeanX.Pierce == 'barbell'", "images/JeanSex/Jean_Sex_Barbell_Pussy.png", 
            "JeanX.Pierce == 'ring' and Player.Cock == 'in' and Speed > 1", "images/JeanSex/Jean_Sex_Ring_Pussy_O.png", #and speed above heading?
            "JeanX.Pierce == 'ring'", "images/JeanSex/Jean_Sex_Ring_Pussy.png",
            "True", Null(), 
            )       
    contains:
            # panties
        ConditionSwitch(    
            "JeanX.PantiesDown", Null(),
#            "JeanX.Panties == 'wolvie panties' and JeanX.Wet", "images/JeanSex/Jean_Sex_Panties_Sport_SW.png", 
            "JeanX.Panties == 'bikini bottoms'", "images/JeanSex/Jean_Sex_Panties_Bikini.png", 
            "JeanX.Panties == 'wolvie panties'", "images/JeanSex/Jean_Sex_Panties_Wolvie.png", 
            "JeanX.Panties == 'lace panties'", "images/JeanSex/Jean_Sex_Panties_Lace.png", 
            "JeanX.Panties", "images/JeanSex/Jean_Sex_Panties_Black.png", 
            "True", Null(),
            )         
    contains:
            # hose base layer
        ConditionSwitch(    
            "Player.Cock == 'foot' and (JeanX.Hose == 'stockings and garterbelt' or JeanX.Hose == 'stockings')", "images/JeanSex/Jean_Sex_Stockings_Base_Foot.png", 
            "JeanX.Hose == 'stockings and garterbelt' or JeanX.Hose == 'stockings'", "images/JeanSex/Jean_Sex_Stockings_Base_Up.png", 
            "True", Null(),
            )              
    contains:
            # legs
        ConditionSwitch(    
            "JeanX.Legs == 'skirt'", "images/JeanSex/Jean_Sex_Skirt.png", 
            "JeanX.Upskirt", Null(),
            "JeanX.Legs == 'leather pants' and Player.Cock == 'foot'", "images/JeanSex/Jean_Sex_Pants_Base_Foot.png", 
            "JeanX.Legs == 'leather pants'", "images/JeanSex/Jean_Sex_Pants_Base_Up.png", 
            "True", Null(),
            )
    contains:
            # piercings
        ConditionSwitch(    
#            "JeanX.Panties and JeanX.PantiesDown", Null(), #don't show if panties are down
#            "JeanX.Legs == 'skirt' or (JeanX.Legs and JeanX.Upskirt)", Null(), #don't show if pants are down
            "JeanX.Pierce == 'barbell'", "images/JeanSex/Jean_Sex_Barbell_Pussy_C.png", 
            "JeanX.Pierce == 'ring'", "images/JeanSex/Jean_Sex_Ring_Pussy_C.png",
            "True", Null(), 
            ) 
#    contains:
#            # Over
#        ConditionSwitch(    
#            "JeanX.Over == 'nighty'", "images/JeanSex/Jean_Sex_Nighty_Pussy.png", 
#            "True", Null(),
#            )
    contains:
            # Feet
        ConditionSwitch(    
            "Player.Cock == 'foot'", "Jean_Footjob_Foot", 
            "True", "Jean_Sex_Foot", 
            )
    transform_anchor True
    zoom 1 
#    rotate 30
#    offset (0,0)
# End Jean Legs base


image Jean_Sex_Foot:
    #her vertical foot in the sex poses
#    contains:
#            # base
#            "images/JeanSex/Jean_Sex_FootHigh.png"
    contains:
            # hose/foot
        ConditionSwitch(    
            "JeanX.Hose == 'stockings and garterbelt' or JeanX.Hose == 'stockings'", "images/JeanSex/Jean_Sex_Stockings_Up.png", 
            "True", "images/JeanSex/Jean_Sex_FootHigh.png" #base
            )              
    contains:
            # legs
        ConditionSwitch(    
            "JeanX.Upskirt", Null(),
            "JeanX.Legs == 'leather pants'", "images/JeanSex/Jean_Sex_Pants_Up.png", 
            "True", Null(),
            )     
        xoffset  -2 #this shouldn't be needed, but otherwise there's a gap between the knee and leg. 
    transform_anchor True
    zoom 1 
#    alpha 0.2
    pos (988,-553)#(988,-553)

#image Jean_Footjob_Foot:
#    #her movable foot in the footjob poses
#    contains:
#            # hose/base
#        ConditionSwitch(    
#            "JeanX.Hose == 'stockings and garterbelt' or JeanX.Hose == 'stockings'", "images/JeanSex/Jean_Sex_Stockings_Foot.png", 
#            "True", "images/JeanSex/Jean_Sex_Foot.png"
#            )              
#    contains:
#            # legs
#        ConditionSwitch(    
#            "JeanX.Upskirt", Null(),
#            "JeanX.Legs == 'leather pants'", "images/JeanSex/Jean_Sex_Pants_Foot.png", 
#            "True", Null(),
#            )      
#    transform_anchor True
#    zoom 1 

image Jean_CockRef:
    "images/JeanSex/Jean_Sex_Cocktest.png"
    alpha 0.8
   
   
# Sex Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Sex Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jean_SexMask:                    
    transform_anchor True
    contains:
        "images/JeanSex/Jean_Sex_MaskPussyX.png"
        pos (200,303)#(0,0)#(-300,-300) #303
        anchor (.5,.5)
    zoom 1 
    anchor (0.5,0.5)
                    
# Start S0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Jean_Sex_Body_S0:                                                                        
    #Her Body in the sex pose, static
    contains:
        "Jean_Sex_Body"      
        subpixel True       
        pos (0,0) #top (0,-10)
        block:#total 2s
            pause 0.15
            ease 0.6 ypos -5 #in
            pause 0.65
            ease .6 ypos 0 #out
            repeat

image Jean_Sex_Legs_S0:
    # Her Legs in the Sex pose, static
    contains:
            #Body
            "Jean_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2s
                pause 0.1
                ease 0.5 ypos -5 #in -25
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat                    
    contains:
            AlphaMask("Jean_Sex_Zero_Anim_S0", "Jean_SexMask")
            subpixel True
            pos (525,465)
            block:#total 2s
                pause 0.1
                ease 0.5 ypos 460 #in 470
                easeout 0.5 ypos 461 #471
                easein 0.9 ypos 465 #out 475                 
                repeat
    # End Legs Sex static
                    
image Jean_Sex_Zero_Anim_S0:
    #this is the cock for Jean's sex animation, Speed0 (static)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        alpha 0.8
        pos (125,170)#125,75
        block: #total 4s
                ease 2 ypos 115#-50
                easeout .5 ypos 120#60
                easein 1.5 ypos 170
                repeat
    
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True
                    
# End S0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

# Start S1 (Heading) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Jean_Sex_Body_S1:                                                                        
    #Her Body in the sex pose, heading
    contains:
        "Jean_Sex_Body"      
        subpixel True       
        pos (0,0) #top (0,-10)
        block:#total 2s
            pause 0.15
            ease 0.6 ypos -5 #in
            pause 0.65
            ease .6 ypos 0 #out
            repeat

image Jean_Sex_Legs_S1:
    # Her Legs in the Sex pose, heading
    contains:
            #Body
            "Jean_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2s
                pause 0.1
                ease 0.5 ypos -5 #in -25
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat                    
    contains:
            AlphaMask("Jean_Sex_Zero_Anim_S1", "Jean_SexMask")
            subpixel True
            pos (525,485)
            block:#total 2s
                pause 0.1
                ease 0.5 ypos 480 #in 450
                easeout 0.5 ypos 481 #455
                easein 0.9 ypos 485 #out    #475              
                repeat
    # End Legs Sex heading
                    
image Jean_Sex_Zero_Anim_S1:
    #this is the cock for Jean's sex animation, Speed1 (heading)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,115)#125,75
        block: #total 2s
                ease .5 ypos 90#-50
                easeout .5 ypos 100#60
                easein 1 ypos 115
                repeat
    
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True
                    
# End S1 (Heading) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

# Start S2 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Jean_Sex_Body_S2:                                                                        
    #Her Body in the sex pose, slow
    contains:
        "Jean_Sex_Body"      
        subpixel True       
        pos (0,10) #top (0,-10)
        block:
            pause 0.3
            ease 0.3 ypos -10 #in
            pause 0.20
            ease 1.70 ypos 10 #out
            repeat

image Jean_Sex_Legs_S2:
    # Her Legs in the Sex pose, slow
    contains:
            #Body
            "Jean_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:
                pause 0.25
                ease 0.3 ypos -25 #in
                easeout 0.45 ypos -20
                easein 1.5 ypos 0 #out
                repeat                    
    contains:
            AlphaMask("Jean_Sex_Zero_Anim_S2", "Jean_SexMask")
            subpixel True
            pos (525,478)
            block:
                pause 0.25
                ease 0.3 ypos 453 #in
                easeout 0.45 ypos 458 
                easein 1.5 ypos 478 #out                    
                repeat
    contains:
            # spunk
            ConditionSwitch(    
                "'in' not in JeanX.Spunk", Null(),
                "True", "images/JeanSex/Jean_Sex_Spunk_Anal_O.png", 
                ) 
            subpixel True                
            pos (-15,-105) #top
            block:
                pause 0.25
                ease 0.3 ypos -130 #in 
                easeout 0.45 ypos -125
                easein 1.5 ypos -105 #out
                repeat         
    # End Legs Sex slow
                    
image Jean_Sex_Zero_Anim_S2:
    #this is the cock for Jean's sex animation, Speed 1 (slow)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,75)#130,75
        block: #total 2.5s
                ease .5 ypos -50#-50
                easeout 1.5 ypos 60#100
                easein .5 ypos 75
                repeat
    
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True
# End S2 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <


# Start S3 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Jean_Sex_Body_S3:                                                                        
    #Her Body in the sex pose, fast
    contains:
        "Jean_Sex_Body"      
        subpixel True       
        pos (0,10) #top (0,-10)
        block:#total 2.5s > 1.75 > 1.2
            pause 0.1
            ease 0.2 ypos -50 #in -10
            pause 0.2
            ease .7 ypos 10 #out
            repeat

image Jean_Sex_Legs_S3:
    # Her Legs in the Sex pose, slow
    contains:
            #Body
            "Jean_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos -45 #in -25
                easeout 0.45 ypos -40 #-50
                easein .5 ypos 0 #out
                repeat                    
    contains:
            AlphaMask("Jean_Sex_Zero_Anim_S3", "Jean_SexMask")
            subpixel True
            pos (525,478) #(525,475)
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos 433 #in 450
                easeout 0.45 ypos 438 #455
                easein .5 ypos 478 #out                  
                repeat
#            block:#total 2.5s > 1.75 > 1.2
#                pause 0.05
#                ease 0.2 ypos 430 #in 450
#                easeout 0.45 ypos 435 #455
#                easein .5 ypos 475 #out                  
#                repeat
    contains:
            # spunk
            ConditionSwitch(    
                "'in' not in JeanX.Spunk", Null(),
                "True", "images/JeanSex/Jean_Sex_Spunk_Anal_O.png", 
                ) 
            subpixel True                
            pos (-15,-105) #top(-15,-105)   
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos -150 #in -45
                easeout 0.45 ypos -145 #-40
                easein .5 ypos -105 #out
                repeat     
    # End Legs Sex fast
                    
image Jean_Sex_Zero_Anim_S3:
    #this is the cock for Jean's sex animation, Speed3 (fast)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,75)#130,75
        block: #total 2.5s > 1.75 > 1.2
                ease .2 ypos -70#-50
                easeout .5 ypos 0#60
                easein .5 ypos 75
                repeat
    
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True                    
# End S3 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

# Start S4 (cumming) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Jean_Sex_Body_S4:                                                                        
    #Her Body in the sex pose, cumming
    contains:
        "Jean_Sex_Body"      
        subpixel True       
        pos (0,10) #top (0,10)
        block:#total 2.5s > 1.75 > 1.2
            pause 0.1
            ease 0.2 ypos 0 #in
            pause 0.2
            ease 1.7 ypos 10 #out
            repeat

image Jean_Sex_Legs_S4:
    # Her Legs in the Sex pose, slow
    contains:
            #Body
            "Jean_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos -15 #in -25
                easeout 0.45 ypos -10 #-50
                easein 1.5 ypos 0 #out
                repeat                   
    contains:
            AlphaMask("Jean_Sex_Zero_Anim_S4", "Jean_SexMask")
            subpixel True
            pos (525,475)
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos 460 #in 450
                easeout 0.45 ypos 465 #455
                easein 1.5 ypos 475 #out                  
                repeat
    contains:
            # spunk
            ConditionSwitch(    
                "'in' not in JeanX.Spunk", Null(),
                "True", "images/JeanSex/Jean_Sex_Spunk_Anal_O.png", 
                ) 
            subpixel True
            pos (-15,-105) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos -120 #in -15
                easeout 0.45 ypos -115 #-10
                easein 1.5 ypos -105 #out
                repeat 
    # End Legs Sex fast
                    
image Jean_Sex_Zero_Anim_S4:
    #this is the cock for Jean's sex animation, Speed4 (cumming)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,-60)#130,75
        block: #total 
                ease .2 ypos -70
                easeout .5 ypos -68
                easein 1.5 ypos -60
                repeat
    
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True
    
# End S4 (cumming) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

# Anal Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start A0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
 
image Jean_Sex_Body_A0:                                                                        
    #Her Body in the anal pose, static
    contains:
        "Jean_Sex_Body"      
        subpixel True       
        pos (0,0) #top (0,-10)
        block:#total 2s
            pause 1.15
            ease 0.6 ypos -5 #in
            pause 0.65
            ease .6 ypos 0 #out
            repeat
            
image Jean_Sex_Legs_A0:
    # Her Legs in the anal pose, static
    contains:
            #Body
            "Jean_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2s
                pause 0.6
                easeout 0.8 ypos -2 #-50
                easein 0.2 ypos -5 #out
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat                  
    contains:
            AlphaMask("Jean_Sex_Zero_Anim_A0", "Jean_AnalMask")
            subpixel True
            pos (533,587) #538,580
            block:#total 2.5s > 1.75 > 1.2
                pause 0.6
                easeout 0.8 ypos 585 #578
                easein 0.2 ypos 582 #out  575
                easeout 0.5 ypos 583 #576
                easein 0.9 ypos 587 #out  580                
                repeat
    # End Legs anal static
    
image Jean_Sex_Zero_Anim_A0:
    #this is the cock for Jean's anal animation, Speed0 (static)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,115)#125,115
        block: #total 3s
                ease 1.5 ypos 110
                pause .5
                ease 1.0 ypos 115
                repeat         
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True
    
# End A0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

# Start A1 (heading) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

                
image Jean_Sex_Body_A1:                                                                        
    #Her Body in the anal pose, heading
    contains:
        "Jean_Sex_Body"      
        subpixel True       
        pos (0,0) #top (0,-10)
        block:#total 2s
            pause 1.15
            ease 0.6 ypos -5 #in
            pause 0.65
            ease .6 ypos 0 #out
            repeat
            
image Jean_Sex_Legs_A1:
    # Her Legs in the anal pose, heading
    contains:
            #Body
            "Jean_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2s
                pause 0.6
                easeout 0.8 ypos -2 #-50
                easein 0.2 ypos -5 #out
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat                  
    contains:
            AlphaMask("Jean_Sex_Zero_Anim_A1", "Jean_AnalMask")
            subpixel True
            pos (538,583) #525,475
            block:#total 2.5s > 1.75 > 1.2
                pause 0.6
                easeout 0.8 ypos 581 #455
                easein 0.2 ypos 578 #out  
                easeout 0.5 ypos 579 #455
                easein 0.9 ypos 583 #out                  
                repeat
    # End Legs anal heading
                    
image Jean_Sex_Zero_Anim_A1:
    #this is the cock for Jean's anal animation, Speed1 (heading)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,115)#125,75
        block: #total 3s
                easeout 1.2 ypos 100
                easein .3 ypos 90
                easeout .5 ypos 100
                easein 1 ypos 115
                repeat         
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True
    
# End A1 (heading) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
# Start A2 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
 
image Jean_Sex_Body_A2:                                                                        
    #Her Body in the anal pose, slow
    contains:
        "Jean_Sex_Body"      
        subpixel True       
        pos (0,0) #top (0,-10)
        block:#total 2.5s > 1.75 > 1.2
            pause 0.3
            ease 0.3 ypos -20 #in
            pause 0.20
            ease 1.70 ypos 20 #out
            repeat
            
image Jean_Sex_Legs_A2:
    # Her Legs in the anal pose, slow
    contains:
            #Body
            "Jean_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.25
                ease 0.3 ypos -35 #in
                easeout 0.45 ypos -30
                easein 1.5 ypos 0 #out
                repeat            
    contains:
            AlphaMask("Jean_Sex_Zero_Anim_A2", "Jean_AnalMask")
            subpixel True
            pos (538,580) #525,475
            block:#total 2.5s > 1.75 > 1.2
                pause 0.25
                ease 0.3 ypos 545 #in 450
                easeout 0.45 ypos 550 #455
                easein 1.5 ypos 580 #out                  
                repeat
    contains:
            # spunk
            ConditionSwitch(    
                "'anal' not in JeanX.Spunk", Null(),
                "True", "images/JeanSex/Jean_Sex_Spunk_Anal_O.png", 
                ) 
            subpixel True
            pos (0,0) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.25
                ease 0.3 ypos -35 #in
                easeout 0.45 ypos -30
                easein 1.5 ypos 0 #out
                repeat 
    # End Legs anal slow
                    
image Jean_Sex_Zero_Anim_A2:
    #this is the cock for Jean's anal animation, Speed2 (slow)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,75)#130,75
        block: #total 2.5s > 1.75 > 1.2
                ease .5 ypos -50#-50
                easeout 1.5 ypos 60#60
                easein .5 ypos 75
                repeat                
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True
    
# End A2 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
# Start A3 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Jean_Sex_Body_A3:                                                                        
    #Her Body in the anal pose, fast
    contains:
        "Jean_Sex_Body"      
        subpixel True       
        pos (0,0) #top (0,-10)
        block:#total 2.5s > 1.75 > 1.2
            pause 0.1
            ease 0.2 ypos -50 #in
            pause 0.2
            ease .7 ypos 00 #out
            repeat
                            
image Jean_Sex_Legs_A3:
    # Her Legs in the anal pose, fast
    contains:
            #Body
            "Jean_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos -55 #in -25
                easeout 0.45 ypos -40 #-50
                easein .5 ypos 0 #out
                repeat                      
    contains:
            AlphaMask("Jean_Sex_Zero_Anim_A3", "Jean_AnalMask")
            subpixel True
            pos (538,580) #525,475
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos 525 #in 450
                easeout 0.45 ypos 540 #455
                easein .5 ypos 580 #out                  
                repeat
    contains:
            # Spunk
            ConditionSwitch(    
                "'anal' not in JeanX.Spunk", Null(),
                "True", "images/JeanSex/Jean_Sex_Spunk_Anal_O.png", 
                ) 
            subpixel True
            pos (0,0) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos -55 #in -25
                easeout 0.45 ypos -40 #-50
                easein .5 ypos 0 #out
                repeat  
    # End Legs Anal fast
                    
image Jean_Sex_Zero_Anim_A3:
    #this is the cock for Jean's anal animation, Speed3 (fast)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,75)#130,75
        block: #total 2.5s > 1.75 > 1.2
                ease .2 ypos -70#-50
                easeout .7 ypos 0#60
                easein .3 ypos 75
                repeat
    
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True
    
# End A3 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
# Start A4 (cumming) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Jean_Sex_Body_A4:                                                                        
    #Her Body in the anal pose, cumming
    contains:
        "Jean_Sex_Body"      
        subpixel True       
        pos (0,20) #top (0,-10)
        block:#total 2.5s > 1.75 > 1.2
            pause 0.1
            ease 0.2 ypos 00 #in
            pause 0.2
            ease 1.7 ypos 20 #out
            repeat

image Jean_Sex_Legs_A4:
    # Her Legs in the anal pose, cumming
    contains:
            #Body
            "Jean_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos -15 #in -25
                easeout 0.45 ypos -10 #-50
                easein 1.5 ypos 0 #out
                repeat                   
    contains:
            AlphaMask("Jean_Sex_Zero_Anim_A4", "Jean_AnalMask")
            subpixel True
            pos (538,583) #525,475
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos 568 #in 450
                easeout 0.45 ypos 573 #455
                easein 1.5 ypos 583 #out                  
                repeat
    contains:
            # spunk
            ConditionSwitch(    
                "'anal' not in JeanX.Spunk", Null(),
                "True", "images/JeanSex/Jean_Sex_Spunk_Anal_O.png", 
                ) 
            subpixel True
            pos (0,0) #top
            block:#total 2.5s > 1.75 > 1.2
                pause 0.05
                ease 0.2 ypos -15 #in -25
                easeout 0.45 ypos -10 #-50
                easein 1.5 ypos 0 #out
                repeat 
    # End Legs Anal cumming
                    
image Jean_Sex_Zero_Anim_A4:
    #this is the cock for Jean's anal animation, Speed4 (cumming)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,-60)#130,75
        block: #total 
                ease .2 ypos -70
                easeout .5 ypos -68
                easein 1.5 ypos -60
                repeat
    
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True
# End A4 (cumming) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <


# Start H0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
   
image Jean_Sex_Body_H0:                                                                        
    #Her Body in the hotdogging pose, static
    contains:
        "Jean_Sex_Body"      
        subpixel True       
        pos (0,0) #top (0,-10)
        block:#total 2s
            pause 1.15
            ease 0.6 ypos -5 #in
            pause 0.65
            ease .6 ypos 0 #out
            repeat
            
image Jean_Sex_Legs_H0:
    # Her Legs in the hotdogging pose, static
    contains:
            #Body
            "Jean_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2s
                pause 0.6
                easeout 0.8 ypos -2 #-50
                easein 0.2 ypos -5 #out
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat                  
    contains:
            "Jean_Sex_Zero_Anim_H0"
#            AlphaMask("Jean_Sex_Zero_Anim_H0", "Jean_AnalMask")
            subpixel True
            pos (558,580) #538,475
            block:#total 2.5s > 1.75 > 1.2
                pause 0.6
                easeout 0.8 ypos 578 #455
                easein 0.2 ypos 575 #out  
                easeout 0.5 ypos 576 #455
                easein 0.9 ypos 580 #out                  
                repeat
    # End Legs hotdogging static
                    
image Jean_Sex_Zero_Anim_H0:
    #this is the cock for Jean's hotdogging animation, Speed0 (static)
    contains:
        subpixel True
        ConditionSwitch(            
            "Player.Sprite", "Zero_Doggy_Insert",# Zero's cock, changes color and properties
            "True", Null(),
            )    
        
#        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        pos (125,115)#125,75
        alpha 0.8    
        block: #total 3s
                ease 1.5 ypos 110
                pause .5
                ease 1.0 ypos 115
                repeat         
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True
    
# End H0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

# Start H1 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
        
image Jean_Sex_Body_H1:                                                                        
    #Her Body in the hotdogging pose, slow
    contains:
        "Jean_Sex_Body"      
        subpixel True       
        pos (0,0) #top (0,-10)
        block:#total 2s
            pause 1.15
            ease 0.6 ypos -5 #in
            pause 0.65
            ease .6 ypos 0 #out
            repeat
            
image Jean_Sex_Legs_H1:
    # Her Legs in the hotdogging pose, slow
    contains:
            #Body
            "Jean_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 2s
                pause 0.6
                ease 1 ypos -10 #-50
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat                  
    contains:
            "Jean_Sex_Zero_Anim_H1"
#            AlphaMask("Jean_Sex_Zero_Anim_H0", "Jean_AnalMask")
            subpixel True
            pos (558,580) #538,475
            block:#total 2.5s > 1.75 > 1.2
                pause 0.6
                ease 1 ypos 570 #-50 
                easeout 0.5 ypos 576 #455
                easein 0.9 ypos 580 #out                  
                repeat
    # End Legs hotdogging slow
                    
image Jean_Sex_Zero_Anim_H1:
    #this is the cock for Jean's hotdogging animation, Speed1 (slow)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        alpha 0.8    
        pos (125,250)#125,75
        block: #total 3s
                ease 1.5 ypos 90 #110
                pause .5
                ease 1.0 ypos 250
                repeat         
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True
    
# End H1 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
                
# Start H2 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

image Jean_Sex_Body_H2:                                                                        
    #Her Body in the hotdogging pose, fast
    contains:
        "Jean_Sex_Body"      
        subpixel True       
        pos (0,0) #top (0,-10)
        block:#total .75s
            pause .3
            ease .5 ypos -5 #in
            pause 0.3
            ease .4 ypos 0 #out
            repeat
            
image Jean_Sex_Legs_H2:
    # Her Legs in the hotdogging pose, fast
    contains:
            #Body
            "Jean_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total .75s
                pause 0.1
                ease .25 ypos -20 #-50
                easeout 0.15 ypos -18 #-50
                easein 0.25 ypos 0 #out
                repeat                  
    contains:
            "Jean_Sex_Zero_Anim_H2"
#            AlphaMask("Jean_Sex_Zero_Anim_H0", "Jean_AnalMask")
            subpixel True
            pos (558,580) #538,475
            block:#total 2.5s > 1.75 > 1.2
                pause 0.1
                ease .25 ypos 560 #-50
                easeout 0.15 ypos 562 #455
                easein 0.25 ypos 580 #out                  
                repeat
    # End Legs anal fast
                    
image Jean_Sex_Zero_Anim_H2:
    #this is the cock for Jean's hotdogging animation, Speed1 (fast)
    contains:
        subpixel True
        "Zero_Doggy_Insert" # Zero's cock, changes color and properties
        zoom 1.7 #1.6
        alpha 0.8    
        pos (125,230)#125,75
        block: #total .75s
                ease .25 ypos 150 #110
                easeout 0.25 ypos 170 
                easein 0.25 ypos 230   
                repeat         
    size (401,606)
    anchor (0.1,0.5)
    transform_anchor True
    
# End H2 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
                
             
image Jean_AnalMask:                    
    transform_anchor True
    contains:
        "images/JeanSex/Jean_Sex_MaskAnalX.png"
        pos (200,366)#(0,0)#(-300,-300) #323 -70
        anchor (.5,.5)
    zoom 1 
    anchor (0.5,0.5)
   
   

# Jean Footjob  Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

image Jean_Footjob_Foot:
    #her movable foot in the footjob poses
    contains:
            # hose/base
        ConditionSwitch(    
            "JeanX.Hose == 'stockings and garterbelt' or JeanX.Hose == 'stockings'", "images/JeanSex/Jean_Sex_Stockings_Foot.png", 
            "True", "images/JeanSex/Jean_Sex_Foot.png"
            )              
    contains:
            # legs
        ConditionSwitch(    
            "JeanX.Upskirt", Null(),
            "JeanX.Legs == 'leather pants'", "images/JeanSex/Jean_Sex_Pants_Foot.png", 
            "True", Null(),
            )      
    offset (1105,140) #
    zoom 1 
    
image Jean_Sex_Zero_Anim_F:
            #cock used in laura's sex pose
            "Zero_Blowcock"
            zoom .7
            anchor (0.5, 0.9)
            offset (270,650)#(220,350)
            rotate 0
            
# Start F1 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
   
image Jean_Sex_Body_F0:                                                                        
    #Her Body in the hotdogging pose, static
    contains:
        "Jean_Sex_Body"      
        subpixel True       
        pos (0,0) #top (0,-10)
        block:#total 2s
            pause 1.15
            ease 0.6 ypos -5 #in
            pause 0.65
            ease .6 ypos 0 #out
            repeat
    yoffset -100
            
image Jean_Sex_Legs_F0:
    # Her Legs in the hotdogging pose, static
    contains:
            #Body
            "Jean_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 3s
                pause 0.6
                easeout 0.8 ypos -2 #-50
                easein 0.2 ypos -5 #out
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat         
    contains:
            #Foot
            "Jean_Footjob_Foot"
            subpixel True  
            anchor (1100,140)
            transform_anchor True       
            pos (0,0) #top 
            rotate 0
            parallel:#total 3s
                pause 0.6
                easeout 0.8 ypos -2 #-2
                easein 0.2 ypos -5 #out
                easeout 0.5 ypos -4 #-4
                easein 0.9 ypos 0 #out
                repeat  
            parallel:#total 3s
                ease 2 rotate 5 #20  
                ease 2 rotate -5 #0   
                pause .5
                repeat    
    contains:
            "Jean_Sex_Zero_Anim_F"
            subpixel True
            transform_anchor True  
            pos (558,580) #538,475
            rotate -5
            parallel:#total 3s
                pause 0.6
                easeout 0.8 ypos 578 #578
                easein 0.2 ypos 575 #out 575 
                easeout 0.5 ypos 576 #575
                easein 0.9 ypos 580 #out  580                
                repeat
            parallel:#total 3s
                easeout 1 rotate -5 #-20  
                easein 1 rotate -10 #-28  
                pause .2
                easeout .8 rotate -5 #-20   
                easein 1 rotate 0 #-5  
                pause .5
                repeat   
    
    yoffset -100
    # End Legs hotdogging static
                    
            
# End F0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <


# Start F1 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
   
image Jean_Sex_Body_F1:                                                                        
    #Her Body in the hotdogging pose, static
    contains:
        "Jean_Sex_Body"      
        subpixel True       
        pos (0,0) #top (0,-10)
        block:#total 2s
            pause 1.15
            ease 0.6 ypos -5 #in
            pause 0.65
            ease .6 ypos 0 #out
            repeat
    yoffset -100
            
image Jean_Sex_Legs_F1:
    # Her Legs in the hotdogging pose, static
    contains:
            #Body
            "Jean_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 3s
                pause 0.6
                easeout 0.8 ypos -2 #-50
                easein 0.2 ypos -5 #out
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat            
    contains:
            "Jean_Sex_Zero_Anim_F"
            subpixel True
            transform_anchor True  
            pos (558,580) #538,475
            rotate -5
            parallel:#total 3s
                pause 0.6
                easeout 0.8 ypos 578 #455
                easein 0.2 ypos 575 #out  
                easeout 0.5 ypos 576 #455
                easein 0.9 ypos 580 #out                  
                repeat
            parallel:#total 3s
                easeout 1 rotate -20 #-50  
                easein 1 rotate -28 #-50  
                pause .2
                easeout .8 rotate -20 #-50   
                easein 1 rotate -5 #-50  
                pause .5
                repeat  
    contains:
            #Foot
            "Jean_Footjob_Foot"
            subpixel True  
            anchor (1100,140)
            transform_anchor True       
            pos (0,0) #top 
            rotate 0
            parallel:#total 3s
                pause 0.6
                easeout 0.8 ypos -2 #-50
                easein 0.2 ypos -5 #out
                easeout 0.5 ypos -4 #-50
                easein 0.9 ypos 0 #out
                repeat  
            parallel:#total 3s
                ease 2 rotate 20 #-50  
                ease 2 rotate 0 #-50   
                pause .5
                repeat  
    
    yoffset -100
    # End Legs hotdogging static
                              
# End F1 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <


# Start F2 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
   
image Jean_Sex_Body_F2:                                                                        
    #Her Body in the hotdogging pose, fast
    contains:
        "Jean_Sex_Body"      
        subpixel True       
        pos (0,0) #top (0,-10)
        block:#total 2s
            ease .7 ypos -10 #in
            ease .7 ypos 0 #out
            repeat
    rotate 15
    yoffset -250
    xoffset 500#400
    xzoom -1
                
image Jean_Sex_Legs_F2:
    # Her Legs in the hotdogging pose, fast
    contains:
            #Body
            "Jean_Sex_Legs"
            subpixel True
            pos (0,0) #top
            block:#total 3
                ease 0.5 ypos -2 #-50
                ease 1 ypos -10 #-50
                pause .1
                repeat                      
    contains:
            "Jean_Sex_Zero_Anim_F"
            subpixel True
            transform_anchor True  
            pos (808,380) #(558,580)
            rotate -55
            parallel:#total 3s
                easeout .25 rotate -58 #-20  
                easein .25 rotate -60 #-28  
                pause .1
                easeout .4 rotate -58 #-20   
                easein .5 rotate -55 #-5  
                pause .1#.25
                repeat  
    contains:
            #Foot
            "Jean_Footjob_Foot"
            subpixel True  
            anchor (1100,140)
            transform_anchor True       
            pos (0,0) #top 
            rotate 0
            parallel:#total 3s
                pause 0.15
                easeout 0.2 ypos -2 #-50
                easein 0.05 ypos -5 #out
                easeout 0.25 ypos -4 #-50
                easein 0.45 ypos 0 #out
                repeat  
            parallel:#total 3s
                ease .5 rotate 20 #-50  top
                ease 1 rotate 0 #-50   
                pause .1#.25
                repeat  
    
    yoffset -400
    xoffset 300#200
    rotate 50
    # End Legs hotdogging fast
                               
            
# End F2 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
                    
#End Footjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

#End Sex Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


image Jean_SexMaskX:                    
    transform_anchor True
    contains:
        "images/JeanSex/Jean_Sex_MaskPussyX.png"
        pos (200,303)#(0,0)#(-300,-300) #
        anchor (.5,.5)
    zoom 1 
#    transform_anchor True
    anchor (0.5,0.5)
#    rotate 30
                    
image Jean_Sex_Zero_AnimX:
        #this is the cock for Jean's sex animation, Speed 0 (static)
        contains: 
            Solid("#159457", xysize=(401,606))#(1264,1061))
            alpha 0.9
        contains:
            subpixel True
#            anchor (0.5,0)
            "Zero_Doggy_Insert" # Zero's cock, changes color and properties
#            pos (498,530) #X less is left, Y less is up (498,520)
            zoom 1.6
            alpha 0.5
            pos (130,100)#(390,550)#(350,250) #466
#            rotate -30
            block:
                    ease 1.25 ypos -50#630
                    ease 1.25 ypos 100#480
                    repeat
        
        size (401,606)#(88,266)(1264,1061)#(1119,1186)
        anchor (0.1,0.5)
        transform_anchor True
#        rotate 30


image Jean_Mega_Mask2:
    # giant green brick for use in finding where a mask is
    contains:
        "images/JeanSex/Jean_Sex_PussyMaskTest2.png"
#        Solid("#159457", xysize=(500,500))
#        offset (-100,100)
#        anchor (0.5,0.5)
#        zoom 1.0
#        alpha .5
#        pos (200,0)#(26,350)#(-175,450)
#        block:
#                    ease .25 offset(0,-500)
#                    ease .25 offset(0,1000)
#                    ease .25 offset(200,-500)
#                    ease .25 offset(200,1000)
#                    ease .25 offset(400,-500)
#                    ease .25 offset(400,1000)
#                    ease .25 offset(600,-500)
#                    ease .25 offset(600,1000)
#                    ease 1.5 offset(-800,-1000)
#                    ease 1.5 offset(-200,-100)
#                    ease .25 offset(-400,-500)
#                    ease .25 offset(-400,1000)
#                    ease .25 offset(-200,-500)
#                    ease .25 offset(-200,1000)
#                    repeat
    transform_anchor True
    zoom 1 
    rotate 30
#    block:
#                    ease 1 rotate 0
#                    ease 1 rotate 30
#                    repeat

image Jean_Mega_Mask:
    # giant green brick for use in finding where a mask is
    contains:
        "images/JeanSex/Jean_Sex_PussyMaskTestB.png"
#        Solid("#159457", xysize=(500,500))
#        offset (-100,100)
#        anchor (0.5,0.5)
#        zoom 1.0
        alpha .5
#        pos (200,0)#(26,350)#(-175,450)
#        block:
#                    ease 1.5 offset(-800,-1200)
#                    ease 1.5 offset(-200,-100)
#                    ease 1.5 offset(-600,-1200)
#                    ease 1.5 offset(-600,-600)
#                    ease 1.5 offset(-200,-1200)
#                    ease 1.5 offset(-200,-600)
#                    repeat
    transform_anchor True
    zoom 1 
    rotate 30
                    
# end Jean's Sex Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Jean_Sex_Launch(Line = "solo"): 
        if Line == "sex":        
            $ Player.Cock = "in"
        elif Line == "anal":
            $ Player.Cock = "anal"
        elif Line == "solo":   
            $ Player.Sprite = 0
            $ Player.Cock = "out"
        elif Line == "hotdog":          
            $ Player.Cock = "out"
        elif Line == "foot":          
            $ Player.Cock = "foot"
        if not Trigger:
            $ Trigger = Line
        if renpy.showing("Jean_SexSprite"):
            return 
        $ Player.Sprite = 1
        hide Jean_Sprite      
        if renpy.showing("Jean_BJ_Animation"):
            hide Jean_BJ_Animation
        if renpy.showing("Jean_HJ_Animation"):
            hide Jean_HJ_Animation
        if renpy.showing("Jean_TJ_Animation"):
            hide Jean_TJ_Animation
        call Speed_Shift(0) 
        
        if Trigger == "in" or Trigger == "anal": 
                if JeanX.Legs or JeanX.HoseNum() >= 5:      
                    $ JeanX.Upskirt = 1
                if JeanX.Panties:     
                    $ JeanX.PantiesDown = 1
                            
        show Jean_SexSprite zorder 150:
            pos (450,500)
        with dissolve
        return
    
label Jean_Sex_Reset:
        if not renpy.showing("Jean_SexSprite"):
            return
        $ JeanX.ArmPose = 2     
        hide Jean_SexSprite  
        call Jean_Hide 
        show Jean_Sprite at SpriteLoc(JeanX.SpriteLoc) zorder JeanX.Layer:
            alpha 1
            zoom 1 offset (0,0) 
            anchor (0.5, 0.0)
        with dissolve
        $ Speed = 0
        return
label Jean_Doggy_Reset:
        return


# Jean's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
            
            
            
            
# Jean's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
                                                 

              
image Jean_BJ_Animation:                
    #core blowjob animation   
    contains:
        ConditionSwitch(
            # Jean's upper body
#            "Player.Sprite", ConditionSwitch(                                                               
#                    # If during sex
            "Speed == 1", "Jean_BJ_Body_1",#Licking
            "Speed == 2", "Jean_BJ_Body_2",#Heading
            "Speed == 3", "Jean_BJ_Body_3",#Sucking
            "Speed == 4", "Jean_BJ_Body_4",#Deepthroat
            "Speed == 5", "Jean_BJ_Body_5",#Cumming high
            "Speed == 6", "Jean_BJ_Body_6",#Cumming deep
#                    "True",     "Jean_BJ_Body_0",#Static
#                    ),
            "True","Jean_BJ_Body_0",#Static
            )   
    zoom 1.35            
    anchor (.5,.5)                 
    pos (600,605)            
                 

#  BJ animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

                
#image Jean_Sprite_BJ_SuckingMask:
#    contains:
#            "images/JeanSprite/Jean_Sprite_SuckingMask.png"
##            pos (200,50)
#    contains:
#            "images/JeanSprite/Jean_Sprite_SpunkSuckingO.png"
#    pos (100,150)
#    alpha .8
            
image Jean_Sprite_BJ_HairBack:          
    #This is the version of the hair back used in the BJ pose
#    "images/JeanSprite/Jean_Sprite_Hair_Long_Under.png"      
    ConditionSwitch(                                                                         
            #Hair over
            "not JeanX.Hair", Null(),
            "JeanX.Hair == 'wet' or JeanX.Water", "images/JeanSprite/Jean_Sprite_Hair_Wet_Under.png",
            "JeanX.Hair", "images/JeanSprite/Jean_Sprite_Hair_Short_Under.png",
            "True", Null(),
            )        
                    
image Jean_Sprite_BJ_Head:
    #This is the version of the head used in the BJ pose
    LiveComposite(
        (806,806),         
        (0,0), ConditionSwitch(
                # Face background plate
                "JeanX.Blush == 2", "images/JeanSprite/Jean_Sprite_Head_Blush2.png", 
                "JeanX.Blush", "images/JeanSprite/Jean_Sprite_Head_Blush.png",  
                "True", "images/JeanSprite/Jean_Sprite_Head.png",                        
                ),        
        (0,0), ConditionSwitch(#chin spunk
            "'chin' not in JeanX.Spunk", Null(),
            "Speed >= 2", Null(),
            "True", "images/JeanSprite/Jean_Sprite_Spunk_Chin.png",
            ),    
        (0,0), ConditionSwitch(#Mouths 
            "Speed >= 2", "images/JeanSprite/Jean_Sprite_Mouth_SuckingBJ.png",   #sucking       
            "Speed == 1", "images/JeanSprite/Jean_Sprite_Mouth_Tongue.png",     #licking 
            "JeanX.Mouth == 'normal'", "images/JeanSprite/Jean_Sprite_Mouth_Normal.png",
            "JeanX.Mouth == 'lipbite'", "images/JeanSprite/Jean_Sprite_Mouth_Lipbite.png",
            "JeanX.Mouth == 'sucking'", "images/JeanSprite/Jean_Sprite_Mouth_Sucking.png",            
            "JeanX.Mouth == 'kiss'", "images/JeanSprite/Jean_Sprite_Mouth_Kiss.png",
            "JeanX.Mouth == 'sad'", "images/JeanSprite/Jean_Sprite_Mouth_Sad.png",
            "JeanX.Mouth == 'smile'", "images/JeanSprite/Jean_Sprite_Mouth_Smile.png",
            "JeanX.Mouth == 'surprised'", "images/JeanSprite/Jean_Sprite_Mouth_Surprised.png",            
            "JeanX.Mouth == 'tongue'", "images/JeanSprite/Jean_Sprite_Mouth_Tongue.png",                
            "JeanX.Mouth == 'grimace'", "images/JeanSprite/Jean_Sprite_Mouth_Smile.png",              
            "JeanX.Mouth == 'smirk'", "images/JeanSprite/Jean_Sprite_Mouth_Smirk.png",                    
#            "JeanX.Mouth == 'smirk'", "images/JeanSprite/Jean_Sprite_Mouth_Normal.png",         
            "True", "images/JeanSprite/Jean_Sprite_Mouth_Normal.png",
            ),         
        (0,0), ConditionSwitch(#Mouth spunk 
            "'mouth' not in JeanX.Spunk", Null(),
            "Speed >= 2", "images/JeanSprite/Jean_Sprite_Spunk_MouthSuck.png",   #sucking       
            "Speed == 1", "images/JeanSprite/Jean_Sprite_Spunk_MouthTongue.png",     #licking             
            "JeanX.Mouth == 'normal'", "images/JeanSprite/Jean_Sprite_Spunk_MouthNeutral.png",
            "JeanX.Mouth == 'lipbite'", "images/JeanSprite/Jean_Sprite_Spunk_MouthSmirk.png",
            "JeanX.Mouth == 'sucking'", "images/JeanSprite/Jean_Sprite_Spunk_MouthTongue.png",            
            "JeanX.Mouth == 'kiss'", "images/JeanSprite/Jean_Sprite_Spunk_MouthKiss.png",
            "JeanX.Mouth == 'sad'", "images/JeanSprite/Jean_Sprite_Spunk_MouthSad.png",
            "JeanX.Mouth == 'smile'", "images/JeanSprite/Jean_Sprite_Spunk_MouthSmile.png",
            "JeanX.Mouth == 'surprised'", "images/JeanSprite/Jean_Sprite_Spunk_MouthSad.png",            
            "JeanX.Mouth == 'tongue'", "images/JeanSprite/Jean_Sprite_Spunk_MouthTongue.png",                
            "JeanX.Mouth == 'grimace'", "images/JeanSprite/Jean_Sprite_Spunk_MouthSmile.png",              
            "JeanX.Mouth == 'smirk'", "images/JeanSprite/Jean_Sprite_Spunk_MouthSmirk.png",      
            "True", "images/JeanSprite/Jean_Sprite_Spunk_MouthNeutral.png",
            ),     
        (0,0), ConditionSwitch(#Mouth spunk over 
            "Speed >= 2 and 'mouth' in JeanX.Spunk", "images/JeanSprite/Jean_Sprite_SpunkSuckingO.png",   #sucking  
            "True", Null(),
            ),    
        (0,0), ConditionSwitch(#wet tongue
            "Speed == 1", "images/JeanSprite/Jean_Sprite_Wet_Tongue.png",     #licking   
            "True", Null(),
            ),                                                              
        (0,0), ConditionSwitch(                                                                       
            #brows
            "JeanX.Blush >= 2", ConditionSwitch(
                    "JeanX.Brows == 'normal'", "images/JeanSprite/Jean_Sprite_Brows_Normal_B.png",
                    "JeanX.Brows == 'angry'", "images/JeanSprite/Jean_Sprite_Brows_Angry_B.png",
                    "JeanX.Brows == 'sad'", "images/JeanSprite/Jean_Sprite_Brows_Sad_B.png",
                    "JeanX.Brows == 'surprised'", "images/JeanSprite/Jean_Sprite_Brows_Surprised_B.png",        
                    "JeanX.Brows == 'confused'", "images/JeanSprite/Jean_Sprite_Brows_Confused_B.png",
                    "True", "images/JeanSprite/Jean_Sprite_Brows_Normal_B.png",
                    ),
            "True", ConditionSwitch(
                    "JeanX.Brows == 'normal'", "images/JeanSprite/Jean_Sprite_Brows_Normal.png",
                    "JeanX.Brows == 'angry'", "images/JeanSprite/Jean_Sprite_Brows_Angry.png",
                    "JeanX.Brows == 'sad'", "images/JeanSprite/Jean_Sprite_Brows_Sad.png",
                    "JeanX.Brows == 'surprised'", "images/JeanSprite/Jean_Sprite_Brows_Surprised.png",        
                    "JeanX.Brows == 'confused'", "images/JeanSprite/Jean_Sprite_Brows_Confused.png",
                    "True", "images/JeanSprite/Jean_Sprite_Brows_Normal.png",
                    ),
            ),        
        (0,0), "Jean Blink",     #Eyes    
#        (0,0), ConditionSwitch(                
#            #Hair mid
#            "JeanX.Over == 'jacket'", Null(),
#            "JeanX.Hair == 'wet' or JeanX.Water", Null(),
#            "JeanX.Hair", "images/JeanSprite/Jean_Sprite_Hair_Long_Mid.png",
#            "True", Null(),
#            ),       
#        (0,0), ConditionSwitch(
#            #Face Water
#            "not JeanX.Water", Null(),
#            "True", "images/JeanSprite/Jean_Sprite_Wet_Head.png",
#            ),
        (0,0), ConditionSwitch(                                                                         
            #Hair over
            "not JeanX.Hair", Null(),
            "JeanX.Hair == 'wet' or JeanX.Water", "images/JeanSprite/Jean_Sprite_Hair_Wet_Over.png",
            "JeanX.Hair", "images/JeanSprite/Jean_Sprite_Hair_Short_Over.png",
            "True", Null(),
            ),        
        (0,0), ConditionSwitch(
            #Hair Water
            "not JeanX.Water", Null(),
            "True", "images/JeanSprite/Jean_Sprite_Head_Wet.png",
#            "True", "images/JeanSprite/Jean_Sprite_Hair_Wet.png",
            ),
        (0,0), ConditionSwitch(
            #facial spunk               
            "'hair' in JeanX.Spunk", "images/JeanSprite/Jean_Sprite_Spunk_Facial2.png",  
            "'facial' in JeanX.Spunk", "images/JeanSprite/Jean_Sprite_Spunk_Facial1.png",            
            "True", Null(),
            ),  
        )                
#    anchor (0.6, 0.0)                
#    zoom .5      
        
image Jean_BlowCock_Mask:   
    #This is a mask used by the blockcock during the Speed 3 sucking animation
    #it is a block moving in and out to prevent the cock sticking out the back. 
    contains:
        Solid("#159457", xysize=(190,950))
        offset (0,0)#(640,198)# top
#        block:
#                pause 0.1
#                ease 1.6 offset (0,300)# bottom
#                pause 0.1
#                ease 1.4 offset (0,0)# top
#                repeat                    


#image Jean_BlowCock_Mask_3:   
#    This is a mask used by the blockcock during the Speed 4 deep throat animation
#    it is a block moving in and out to prevent the cock sticking out the back. 
#    contains:
#        Solid("#159457", xysize=(190,950))
#        offset (0,0)#(640,198)# top
#        block:
#                pause 0.1
#                ease 1.6 offset (0,300)# bottom
#                pause 0.1
#                ease 1.4 offset (0,0)# top
#                repeat   

image Jean_BJ_Body_0:                                                                        
    #Her Body in the BJ pose, static
    contains:
            #Hair underlay
            "Jean_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (490,400) #(535,340) #top
            rotate 0 #-30
            parallel:
                ease 1.1 ypos 405 #bottom
                pause 0.2
                ease 1.1 ypos 400 #top
                pause 0.2
                repeat           
    contains:       
            #base body
            "Jean_Sprite"   
            subpixel True   
            pos (650,800)#(673,740) #top
            zoom 2.2 #.75                    
            anchor (0.5, 0.5)
            rotate -20
            parallel:
                pause 0.1
                ease 1.1 ypos 810 #bottom
                pause 0.2
                ease 1 ypos 800 #top
                pause 0.1
                repeat    
    contains:
            #base head under cock
            subpixel True
            "Jean_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (490,400) #(535,340) #top
            rotate 0 #-30    
            parallel:
                ease 1.1 ypos 405 #bottom
                pause 0.2
                ease 1.1 ypos 400 #top
                pause 0.2
                repeat    
    contains:
            #zero's cock
#            ConditionSwitch(    
#                "Player.Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Jean_BlowCock_Mask"), #Null(),
#                )      
            AlphaMask("Blowcock", "Jean_BlowCock_Mask")
            subpixel True
            pos (412,292) #tilted/top #(640,198)
            zoom 0.4  
            alpha 1
            rotate 10    
            parallel:
                pause 0.1
#                easeout .1 rotate 1 #bottom .6
                ease .15 rotate -5 #bottom
                pause 0.4
                ease 1.95 rotate 10 #top
                repeat
            parallel:
                pause 0.1
#                easeout .1 pos (407,262) #bottom(637,168)
                ease .15 pos (405,255) #bottom(637,168)
                pause 0.4
                ease 1.95 pos (420,292) #top 412
                repeat
    #End BJ animation Speed 0
    

image Jean_BJ_Body_1:                                                                        
    #Her Body in the BJ pose, licking
    contains:
            #Hair underlay
            "Jean_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (535,340) #(523,380) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                ease 1.4 rotate -50 #bottom
                pause 0.3
                ease 1.4 rotate -30 #top
                repeat  
            parallel:
                pause 0.1
                easeout 1.2 xpos 470 #bottom
                easein .2 xpos 460 #bottom 481 
                pause 0.3
                easeout .75 xpos 500 #top
                easein .65 xpos 535 #top
                repeat    
            parallel:
                pause 0.1
                ease 1.4 ypos 500 #bottom
                pause 0.3
                ease 1.4 ypos 340 #top
                repeat            
    contains:       
            #base body
            "Jean_Sprite"      
            pos (673,740)#(680,755) #top
            zoom 2.2 #.75                    
            anchor (0.5, 0.5)
            rotate -20
            subpixel True
            parallel:
                pause 0.15
                ease 1.25 rotate -40 #bottom
                pause 0.45
                ease 1.35 rotate -20 #top
                repeat 
            parallel:
                pause 0.15
                easeout .9 xpos 740 #bottom
                easein .35 xpos 740 #bottom 481 
                pause 0.5
                easeout .65 xpos 710 #top
                easein .65 xpos 673 #top
                repeat   
            parallel:
                pause 0.15
                ease 1.25 ypos 830 #bottom
                pause 0.45
                ease 1.35 ypos 740 #top
                repeat    
    contains:
            #base head under cock
            subpixel True
            "Jean_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (535,340) #(523,380) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                ease 1.4 rotate -50 #bottom
                pause 0.3
                ease 1.4 rotate -30 #top
                repeat  
            parallel:
                pause 0.1
                easeout 1.2 xpos 470 #bottom
                easein .2 xpos 460 #bottom 481 
                pause 0.3
                easeout .75 xpos 500 #top
                easein .65 xpos 535 #top
                repeat    
            parallel:
                pause 0.1
                ease 1.4 ypos 500 #bottom
                pause 0.3
                ease 1.4 ypos 340 #top
                repeat    
    contains:
            #zero's cock
#            ConditionSwitch(    
#                "Player.Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Jean_BlowCock_Mask"), #Null(),
#                )      
            AlphaMask("Blowcock", "Jean_BlowCock_Mask")
            subpixel True
            pos (412,292) #tilted/top #(640,198)
            zoom 0.4  
            alpha 1
            rotate 10    
            parallel:
                pause 0.1
                easeout 1.2 rotate 1 #bottom
                easein .3 rotate -1 #bottom
                pause 0.4
                ease 1.2 rotate 10 #top
                repeat
            parallel:
                pause 0.1
                easeout 1.2 pos (407,262) #bottom(637,168)
                easein .3 pos (405,255) #bottom(637,168)
                pause 0.4
                ease 1.2 pos (412,292) #top
                repeat
    #End BJ animation Speed 1
    
image Jean_BJ_Body_2:                                                                        
    #Her Body in the BJ pose, heading
    contains:
            #Hair underlay
            "Jean_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (530,355) #(530,355) #top
            rotate -30 #-30            
            parallel:
                pause 0.1
                easeout 1.2 rotate -40 #bottom
                ease .6 rotate -32 #bottom
                pause 0.1
                ease 1.2 rotate -30 #top
                repeat  
            parallel:
                pause 0.1
                easeout 1.2 xpos 510 #bottom 510
                ease .7 xpos 520 #bottom
                pause 0.1
                ease 1.1 xpos 530 #top
                repeat  
            parallel:
                pause 0.1
                ease 1.6 ypos 400 #bottom
                pause 0.1
                ease 1.4 ypos 355 #top
                repeat   
    contains:       
            #base body
            "Jean_Sprite"      
            pos (680,755)#(680,755) #top
            zoom 2.2 #.75                    
            anchor (0.5, 0.5)
            rotate -20
            subpixel True
            parallel:
                pause 0.15
                ease 1.55 rotate -30 #bottom
                pause 0.15
                ease 1.35 rotate -20 #top
                repeat 
            parallel:
                pause 0.15   
                ease 1.35 xpos 730 #bottom 760
                pause 0.25
                ease 1.45 xpos 680 #top                    
                repeat   
            parallel:
                pause 0.15
                ease 1.55 ypos 780 #bottom
                pause 0.15
                ease 1.35 ypos 755 #top
                repeat   
    contains:
            #base head under cock
            subpixel True
            "Jean_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (530,355) #(530,355) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                easeout 1.2 rotate -40 #bottom
                ease .6 rotate -32 #bottom
                pause 0.1
                ease 1.2 rotate -30 #top
                repeat  
            parallel:
                pause 0.1
                easeout 1.2 xpos 510 #bottom 510
                ease .7 xpos 520 #bottom
                pause 0.1
                ease 1.1 xpos 530 #top
                repeat  
            parallel:
                pause 0.1
                ease 1.6 ypos 400 #bottom
                pause 0.1
                ease 1.4 ypos 355 #top
                repeat    
    contains:
            #zero's cock
#            ConditionSwitch(    
#                "Player.Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Jean_BlowCock_Mask"), #Null(),
#                )      
            AlphaMask("Blowcock", "Jean_BlowCock_Mask")
            subpixel True
            pos (412,292) #tilted/top #(640,198)
            zoom 0.4  
            alpha 1
            rotate 10    
            parallel:
                pause 1.3
                ease .4 rotate 8 #bottom
                pause .2
                ease 1 rotate 10 #top
                pause .3
                repeat
            parallel:
                pause 1.3
                ease .4 pos (410,285) #bottom(407,262)
                pause .2
                ease 1 pos (412,292) #top
                pause .3
                repeat
    contains:
            #head masked portion
            subpixel True
            AlphaMask("Jean_Sprite_BJ_Head", "images/JeanSprite/Jean_Sprite_SuckingMask.png")
            zoom 0.81
            anchor (0.5, 0.5)
            pos (530,355) #(530,355) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                easeout 1.2 rotate -40 #bottom
                ease .6 rotate -32 #bottom
                pause 0.1
                ease 1.2 rotate -30 #top
                repeat  
            parallel:
                pause 0.1
                easeout 1.2 xpos 510 #bottom 510
                ease .7 xpos 520 #bottom
                pause 0.1
                ease 1.1 xpos 530 #top
                repeat  
            parallel:
                pause 0.1
                ease 1.6 ypos 400 #bottom
                pause 0.1
                ease 1.4 ypos 355 #top
                repeat   
    #End BJ animation Speed 2
    


image Jean_BlowCock_Mask_3:   
    #This is a mask used by the blockcock during the Speed 3 sucking animation
    #it is a block moving in and out to prevent the cock sticking out the back. 
    contains:
        Solid("#159457", xysize=(190,950))
        offset (0,100)#(640,198)# top
#        block:
#                pause 0.1
#                ease 1.6 offset (0,300)# bottom
#                pause 0.1
#                ease 1.4 offset (0,0)# top
#                repeat   

image Jean_BJ_Body_3:                                                                        
    #Her Body in the BJ pose, sucking
    contains:
            #Hair underlay
            "Jean_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (523,380) #(530,355) #top
            rotate -30 #-30
            parallel:
#                pause 0.2
                ease .7 rotate -50 #bottom
#                pause 0.1
                ease 1 rotate -30 #top
                repeat  
            parallel:
#                pause 0.2
                easeout .3 xpos 500 #bottom .7
                easein .4 xpos 481 #bottom .9
#                pause 0.1
                easeout .55 xpos 500 #top .75
                easein .45 xpos 523 #top .65
                repeat    
            parallel:
#                pause 0.2
                ease .7 ypos 450 #bottom
#                pause 0.1
                ease 1 ypos 380 #top
                repeat                  
    contains:       
            #base body
            "Jean_Sprite"      
            pos (673,780)#(680,755) #top
            zoom 2.2 #.75                    
            anchor (0.5, 0.5)
            rotate -20
            subpixel True
            parallel:
#                pause 0.15
                ease .7 rotate -40 #bottom
#                pause 0.15
                ease 1.0 rotate -20 #top
                repeat 
            parallel:
#                pause 0.15   
                easeout .3 xpos 710 #bottom
                easein .4 xpos 760 #bottom
#                pause 0.15
                easeout .55 xpos 710 #top
                easein .45 xpos 673 #top                    
                repeat   
            parallel:
#                pause 0.15
                ease .7 ypos 780 #bottom 830
#                pause 0.15
                ease 1.0 ypos 780 #top
                repeat   
    contains:
            #base head under cock
            subpixel True
            "Jean_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (523,380) #(530,355) #top
            rotate -30 #-30
            parallel:
#                pause 0.2
                ease .7 rotate -50 #bottom
#                pause 0.1
                ease 1 rotate -30 #top
                repeat  
            parallel:
#                pause 0.2
                easeout .3 xpos 500 #bottom .7
                easein .4 xpos 481 #bottom .9
#                pause 0.1
                easeout .55 xpos 500 #top .75
                easein .45 xpos 523 #top .65
                repeat    
            parallel:
#                pause 0.2
                ease .7 ypos 450 #bottom
#                pause 0.1
                ease 1 ypos 380 #top
                repeat    
    contains:
            #zero's cock
#            ConditionSwitch(    
#                "Player.Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Jean_BlowCock_Mask"), #Null(),
#                )      
            AlphaMask("Blowcock", "Jean_BlowCock_Mask_3")
            subpixel True
            pos (412,292) #tilted/top #(640,198)
            zoom 0.4  
            alpha 1
            rotate 10    
            parallel:
#                pause 0.2
                ease .7 rotate 0 #bottom
#                pause 0.1
                ease 1 rotate 10 #top
                repeat
            parallel:
#                pause 0.2
                ease .7 pos (407,262) #bottom(637,168)
#                pause 0.1
                ease 1 pos (412,292) #top
                repeat
    contains:
            #head masked portion
            subpixel True
            AlphaMask("Jean_Sprite_BJ_Head", "images/JeanSprite/Jean_Sprite_SuckingMask.png")   
            zoom 0.81
            anchor (0.5, 0.5)
            pos (523,380) #(530,355) #top
            rotate -30 #-30
            parallel:
#                pause 0.2
                ease .7 rotate -50 #bottom
#                pause 0.1
                ease 1 rotate -30 #top
                repeat  
            parallel:
#                pause 0.2
                easeout .3 xpos 500 #bottom .7
                easein .4 xpos 481 #bottom .9
#                pause 0.1
                easeout .55 xpos 500 #top .75
                easein .45 xpos 523 #top .65
                repeat    
            parallel:
#                pause 0.2
                ease .7 ypos 450 #bottom
#                pause 0.1
                ease 1 ypos 380 #top
                repeat   
    #End BJ animation Speed 3
    
    
image Jean_BlowCock_Mask_4:   
    #This is a mask used by the blockcock during the Speed 4 deep throat animation
    #it is a block moving in and out to prevent the cock sticking out the back. 
    contains:
        Solid("#159457", xysize=(190,950))
        offset (0,0)#(640,198)# top
        block:
                pause 0.1
                ease 1.6 offset (0,300)# bottom
                pause 0.1
                ease 1.4 offset (0,0)# top
                repeat   

image Jean_BJ_Body_4:                                                                        
    #Her Body in the BJ pose, deep throat
    contains:
            #Hair underlay
            "Jean_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (523,380) #(530,355) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                ease 1.6 rotate -50 #bottom
                pause 0.1
                ease 1.4 rotate -30 #top
                repeat  
            parallel:
                pause 0.1
                easeout .7 xpos 500 #bottom
                easein .9 xpos 481 #bottom
                pause 0.1
                easeout .75 xpos 500 #top
                easein .65 xpos 523 #top
                repeat    
            parallel:
                pause 0.1
                ease 1.6 ypos 500 #bottom
                pause 0.1
                ease 1.4 ypos 380 #top
                repeat                
    contains:       
            #base body
            "Jean_Sprite"      
            pos (673,780)#(680,755) #top
            zoom 2.2 #.75                    
            anchor (0.5, 0.5)
            rotate -20
            subpixel True
            parallel:
                pause 0.15
                ease 1.55 rotate -40 #bottom
                pause 0.15
                ease 1.35 rotate -20 #top
                repeat 
            parallel:
                pause 0.15   
                easeout .65 xpos 710 #bottom
                easein .9 xpos 760 #bottom
                pause 0.15
                easeout .70 xpos 710 #top
                easein .65 xpos 673 #top                    
                repeat   
            parallel:
                pause 0.15
                ease 1.55 ypos 830 #bottom
                pause 0.15
                ease 1.35 ypos 780 #top
                repeat   
    contains:
            #base head under cock
            subpixel True
            "Jean_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (523,380) #(530,355) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                ease 1.6 rotate -50 #bottom
                pause 0.1
                ease 1.4 rotate -30 #top
                repeat  
            parallel:
                pause 0.1
                easeout .7 xpos 500 #bottom
                easein .9 xpos 481 #bottom
                pause 0.1
                easeout .75 xpos 500 #top
                easein .65 xpos 523 #top
                repeat    
            parallel:
                pause 0.1
                ease 1.6 ypos 500 #bottom
                pause 0.1
                ease 1.4 ypos 380 #top
                repeat    
    contains:
            #zero's cock
#            ConditionSwitch(    
#                "Player.Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Jean_BlowCock_Mask"), #Null(),
#                )      
            AlphaMask("Blowcock", "Jean_BlowCock_Mask_4")
            subpixel True
            pos (412,292) #tilted/top #(640,198)
            zoom 0.4  
            alpha 1
            rotate 10    
            parallel:
                pause 0.1
                ease 1.6 rotate 0 #bottom
                pause 0.1
                ease 1.4 rotate 10 #top
                repeat
            parallel:
                pause 0.1
                ease 1.6 pos (407,262) #bottom(637,168)
                pause 0.1
                ease 1.4 pos (412,292) #top
                repeat
    contains:
            #head masked portion
            subpixel True
            AlphaMask("Jean_Sprite_BJ_Head", "images/JeanSprite/Jean_Sprite_SuckingMask.png")
            zoom 0.81
            anchor (0.5, 0.5)
            pos (523,380) #(530,355) #top
            rotate -30 #-30
            parallel:
                pause 0.1
                ease 1.6 rotate -50 #bottom
                pause 0.1
                ease 1.4 rotate -30 #top
                repeat  
            parallel:
                pause 0.1
                easeout .7 xpos 500 #bottom
                easein .9 xpos 481 #bottom
                pause 0.1
                easeout .75 xpos 500 #top
                easein .65 xpos 523 #top
                repeat    
            parallel:
                pause 0.1
                ease 1.6 ypos 500 #bottom
                pause 0.1
                ease 1.4 ypos 380 #top
                repeat  
    #End BJ animation Speed 4
    
    
image Jean_BJ_Body_5:                                                                        
    #Her Body in the BJ pose, high cumming
    contains:
            #Hair underlay
            "Jean_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (520,375) #(530,355) #bottom
            rotate -50 #-30
            parallel:
                pause 1
                ease .3 rotate -30 #top
                easeout .3 rotate -32 #bottom
                easein .5 rotate -35 #bottom
                pause .5
                repeat  
            parallel:
                pause 1 
                easein .3 xpos 530 #top
                easeout .3 xpos 525 #bottom
                easein .5 xpos 520 #bottom
                pause .5
                repeat    
            parallel:
                pause 1
                ease .3 ypos 355 #top
                easeout .3 ypos 365 #bottom
                easein .5 ypos 375 #bottom
                pause .5
                repeat              
    contains:       
            #base body
            "Jean_Sprite"      
            subpixel True
            zoom 2.2 #.75                    
            anchor (0.5, 0.5)
            rotate -30
            pos (730,760)#(680,755) #bottom                
            parallel:
                pause 1
                ease .3 rotate -26 #top
                easeout .3 rotate -28 #bottom
                easein .5 rotate -30 #bottom
                pause .5
                repeat  
            parallel:
                pause 1 
                easein .3 xpos 710 #top 680
                easeout .3 xpos 720 #bottom
                easein .5 xpos 730 #bottom
                pause .5
                repeat    
            parallel:
                pause 1
                ease .3 ypos 750 #top 755
                easeout .3 ypos 755 #bottom
                easein .5 ypos 760 #bottom
                pause .5
                repeat                  
    contains:
            #base head under cock
            subpixel True
            "Jean_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (520,375) #(530,355) #bottom
            rotate -35 #-30
            parallel:
                pause 1
                ease .3 rotate -30 #top
                easeout .3 rotate -32 #bottom
                easein .5 rotate -35 #bottom
                pause .5
                repeat  
            parallel:
                pause 1 
                easein .3 xpos 530 #top
                easeout .3 xpos 525 #bottom
                easein .5 xpos 520 #bottom
                pause .5
                repeat    
            parallel:
                pause 1
                ease .3 ypos 355 #top
                easeout .3 ypos 365 #bottom
                easein .5 ypos 375 #bottom
                pause .5
                repeat                   
    contains:
            #zero's cock
#            ConditionSwitch(    
#                "Player.Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Jean_BlowCock_Mask"), #Null(),
#                )      
            AlphaMask("Blowcock", "Jean_BlowCock_Mask")
            subpixel True
            pos (410,292) #bottom
            zoom 0.4  
            alpha 1
            rotate 12    
            parallel:
                pause 1
                ease .3 rotate 10 #top
                ease .3 rotate 12 #bottom
                pause 1
                repeat
            parallel:
                pause 1
                ease .3 pos (412,285) #top
                ease .3 pos (410,292) #bottom(637,168)
                pause 1
                repeat
    contains:
            #head masked portion
            subpixel True
            AlphaMask("Jean_Sprite_BJ_Head", "images/JeanSprite/Jean_Sprite_SuckingMask.png")
            zoom 0.81
            anchor (0.5, 0.5)
            pos (520,375) #(530,355) #bottom
            rotate -35 #-30
            parallel:
                pause 1
                ease .3 rotate -30 #top
                easeout .3 rotate -32 #bottom
                easein .5 rotate -35 #bottom
                pause .5
                repeat  
            parallel:
                pause 1 
                easein .3 xpos 530 #top
                easeout .3 xpos 525 #bottom
                easein .5 xpos 520 #bottom
                pause .5
                repeat    
            parallel:
                pause 1
                ease .3 ypos 355 #top
                easeout .3 ypos 365 #bottom
                easein .5 ypos 375 #bottom
                pause .5
                repeat   
    #End BJ animation Speed 5
    
image Jean_BlowCock_Mask_6:   
    #This is a mask used by the blockcock during the Speed 4 deep throat animation
    #it is a block moving in and out to prevent the cock sticking out the back. 
    contains:
        Solid("#159457", xysize=(190,950))
        offset (0,300)#(640,198)# top
#        block:
#                pause 0.1
#                ease 1.6 offset (0,300)# bottom
#                pause 0.1
#                ease 1.4 offset (0,0)# top
#                repeat   
                
image Jean_BJ_Body_6:                                                                        
    #Her Body in the BJ pose, deep throat cumming
    contains:
            #Hair underlay
            "Jean_Sprite_BJ_HairBack"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (481,500) #(530,355) #bottom
            rotate -50 #-30
            parallel:
                pause 1
                ease .3 rotate -45 #top
                easeout .3 rotate -48 #bottom
                easein .5 rotate -50 #bottom
                pause .5
                repeat  
            parallel:
                pause 1 
                easein .3 xpos 490 #top
                easeout .3 xpos 485 #bottom
                easein .5 xpos 481 #bottom
                pause .5
                repeat    
            parallel:
                pause 1
                ease .3 ypos 490 #top
                easeout .3 ypos 496 #bottom
                easein .5 ypos 500 #bottom
                pause .5
                repeat                 
    contains:       
            #base body
            "Jean_Sprite"      
            subpixel True
            zoom 2.2 #.75                    
            anchor (0.5, 0.5)
            rotate -40
            pos (760,830)#(680,755) #bottom                
            parallel:
                pause 1
                ease .3 rotate -38 #top
                easeout .3 rotate -39 #bottom
                easein .5 rotate -40 #bottom
                pause .5
                repeat  
            parallel:
                pause 1 
                easein .3 xpos 750 #top
                easeout .3 xpos 756 #bottom
                easein .5 xpos 760 #bottom
                pause .5
                repeat    
            parallel:
                pause 1
                ease .3 ypos 835 #top
                easeout .3 ypos 830 #bottom
                easein .5 ypos 830 #bottom
                pause .5
                repeat  
    contains:
            #base head under cock
            subpixel True
            "Jean_Sprite_BJ_Head"
            zoom 0.81
            anchor (0.5, 0.5)
            pos (481,500) #(530,355) #bottom
            rotate -50 #-30
            parallel:
                pause 1
                ease .3 rotate -45 #top
                easeout .3 rotate -48 #bottom
                easein .5 rotate -50 #bottom
                pause .5
                repeat  
            parallel:
                pause 1 
                easein .3 xpos 490 #top
                easeout .3 xpos 485 #bottom
                easein .5 xpos 481 #bottom
                pause .5
                repeat    
            parallel:
                pause 1
                ease .3 ypos 490 #top
                easeout .3 ypos 496 #bottom
                easein .5 ypos 500 #bottom
                pause .5
                repeat   
    contains:
            #zero's cock
#            ConditionSwitch(    
#                "Player.Sprite", "Blowcock",
#                "True", AlphaMask("Blowcock", "Jean_BlowCock_Mask"), #Null(),
#                )      
            AlphaMask("Blowcock", "Jean_BlowCock_Mask_6")
            subpixel True
            pos (407,262) #bottom
            zoom 0.4  
            alpha 1
            rotate 0    
            parallel:
                pause 1
                ease .3 rotate 2 #top
                ease .3 rotate 0 #bottom
                pause 1
                repeat
            parallel:
                pause 1
                ease .3 pos (409,268) #top
                ease .3 pos (407,262) #bottom(637,168)
                pause 1
                repeat
    contains:
            #head masked portion
            subpixel True
            AlphaMask("Jean_Sprite_BJ_Head", "images/JeanSprite/Jean_Sprite_SuckingMask.png")
            zoom 0.81
            anchor (0.5, 0.5)
            pos (481,500) #(530,355) #bottom
            rotate -50 #-30
            parallel:
                pause 1
                ease .3 rotate -45 #top
                easeout .3 rotate -48 #bottom
                easein .5 rotate -50 #bottom
                pause .5
                repeat  
            parallel:
                pause 1 
                easein .3 xpos 490 #top
                easeout .3 xpos 485 #bottom
                easein .5 xpos 481 #bottom
                pause .5
                repeat    
            parallel:
                pause 1
                ease .3 ypos 490 #top
                easeout .3 ypos 496 #bottom
                easein .5 ypos 500 #bottom
                pause .5
                repeat  
    #End BJ animation Speed 6
#Head and Body Animations for Jean's BJ Scenes / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
                                                               #BJ Launchers  
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                               #BJ Launchers  
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Jean_BJ_Launch(Line = 0):    
    # The sequence to launch the Jean BJ animations                     
    call expression Girl.Tag + "_Kissing_Launch" pass (Trigger)  
    
    return                      #fix, remove this once the pose is done
    $ JeanX.ArmPose = 1
    if renpy.showing("Jean_BJ_Animation"):
        return
    
    call Jean_Hide
    if Line == "L" or Line == "cum":
        show Jean_Sprite at SpriteLoc(StageCenter) zorder JeanX.Layer:
            alpha 1
            ease 1 zoom 2.5 offset (150,80) 
        with dissolve
    else:
        show Jean_Sprite at SpriteLoc(StageCenter) zorder JeanX.Layer:
            alpha 1
            zoom 2.5 offset (150,80) 
        with dissolve
        
    $ Speed = 0
    if Line == "L": # Jean gets started. . .
            if Taboo: 
                if len(Present) >= 2:
                    if Present[0] != JeanX:
                            "[JeanX.Name] looks back at [Present[0].Name] to see if she's watching."
                    elif Present[1] != JeanX:
                            "[JeanX.Name] looks back at [Present[1].Name] to see if she's watching."
                else:
                            "[JeanX.Name] casually glances around to see if anyone can see her."
            "[JeanX.Name] smoothly bends down and places your cock against her cheek."   
            
    if Line != "cum":
        $ Trigger = "blow"
    
    show Jean_Sprite zorder JeanX.Layer:
        alpha 0
    show Jean_BJ_Animation zorder 150: 
        pos (645,510) 
    return
    
label Jean_BJ_Reset: # The sequence to the Jean animations from BJ to default
    if not renpy.showing("Jean_BJ_Animation"):
        return
#    hide Jean_BJ_Animation
    call Jean_Hide 
    $ Speed = 0
    
    show Jean_Sprite at SpriteLoc(StageCenter) zorder JeanX.Layer:
        alpha 1
        zoom 2.5 offset (150,80) 
    with dissolve
    
    show Jean_Sprite zorder JeanX.Layer:
        alpha 1
        ease 1 zoom 1.5 offset (-50,50)
        pause .5
        ease .5 zoom 1 offset (0,0)      
    show Jean_Sprite at SpriteLoc(JeanX.SpriteLoc) zorder JeanX.Layer:
        alpha 1
        zoom 1 offset (0,0)    
    return  

# End Jean Blowjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



# Start Jean Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Jean Handjob element //////////////////////////////////////////////////////////////////////   

image Jean_Hand_Under:
    "images/JeanSprite/handjean2.png"
    anchor (0.5,0.5)
    pos (-10,0)
    offset (0,130)
            
image Jean_Hand_Over:
    "images/JeanSprite/handjean1.png"    
    anchor (0.5,0.5)
    pos (-10,0)
    offset (0,130)
        
transform Jean_Hand_1():
    subpixel True
    pos (-20,-100) 
    rotate 5
    block:
        ease .5 pos (0,150) rotate -5 #ypos 150 rotate 5 Bottom
        pause 0.25
        ease 1.0 pos (-20,-100) rotate 5 #250#-150 #rotate -10#  Top
        pause 0.1
        repeat

transform Jean_Hand_2():
    subpixel True    
    pos (-15,-120) 
    rotate 10 
    block:
        ease 0.2 pos (-15,0) rotate 0   
        pause 0.1
        ease 0.4 pos (-15,-120) rotate 10 
        pause 0.1
        repeat

#transform Handcock_3():
#    subpixel True
#    rotate_pad False    
#    ypos 400 
#    rotate 0 #400
#    block:
#        ease .5 ypos 450 rotate -2 #450
#        pause 0.25
#        ease 1.0 ypos 400 rotate 0 #400
#        pause 0.1
#        repeat

#transform Handcock_4():
#    subpixel True
#    rotate_pad False    
#    ypos 400 
#    rotate 0
#    block:
#        ease .2 ypos 430 rotate -3 #410
#        ease .5 ypos 400 rotate 0
#        pause 0.1
#        repeat
     
transform Handcock_1J():
    subpixel True
    rotate_pad False    
    ypos 400 
    rotate 0 #400
    block:
        ease .5 ypos 450 rotate -2 #450
        pause 0.25
        ease 1.0 ypos 400 rotate 0 #400
        pause 0.1
        repeat

transform Handcock_2J():
    subpixel True
    rotate_pad False
    ypos 400 
    rotate 0
    block:
        ease .2 ypos 430 rotate -3 #410
        ease .5 ypos 400 rotate 0
        pause 0.1
        repeat
    
image Jean_HJ_Animation:  
    contains:
        ConditionSwitch(                                                
            # backside of the hand
            "not Speed", Transform("Jean_Hand_Under"), 
            "Speed == 1", At("Jean_Hand_Under", Jean_Hand_1()),
            "Speed >= 2", At("Jean_Hand_Under", Jean_Hand_2()),            
            "Speed", Null(),
            ),  
    contains:
        ConditionSwitch(                                                
            # cock
            "not Speed", Transform("Zero_Handcock"), 
            "Speed == 1", At("Zero_Handcock", Handcock_1J()),
            "Speed >= 2", At("Zero_Handcock", Handcock_2J()), 
            "Speed", Null(),
            ),  
        offset (0,0)
    contains:
        ConditionSwitch(                                               
            # fingers of the hand
            "not Speed", Transform("Jean_Hand_Over"), 
            "Speed == 1", At("Jean_Hand_Over", Jean_Hand_1()),
            "Speed >= 2", At("Jean_Hand_Over", Jean_Hand_2()), 
            "Speed", Null(),
            ),   
    anchor (0.51, -1.3)
    zoom 0.4#0.6
        
        
label Jean_HJ_Launch(Line = 0): 
    if renpy.showing("Jean_HJ_Animation"):        
        $ Trigger = "hand"
        return
    call Jean_Hide
    $ JeanX.ArmPose = 1
    if Line == "L":      
        show Jean_Sprite at SpriteLoc(StageRight) zorder JeanX.Layer:
            alpha 1
            ease 1 zoom 1.7 offset (-150,350)#(-180,350)
    else:     
        show Jean_Sprite at SpriteLoc(StageRight) zorder JeanX.Layer:
            alpha 1
            ease 1 zoom 1.7 offset (-150,350)#(-180,350)
        with dissolve
            
    $ Speed = 0
    if Line != "cum":
        $ Trigger = "hand"
    else:
        $ Speed = 1
    pause .5
    show Jean_HJ_Animation at SpriteLoc(StageCenter) zorder 150 with easeinbottom:
        #xoffset 150
        offset (250,250)#(100,250)        
    show Jean_Sprite at SpriteLoc(StageRight) zorder JeanX.Layer:
        alpha 1
        ease .5 zoom 1.7 offset (-150,200)#(-180,200)
    return
    
label Jean_HJ_Reset: # The sequence to the Jean animations from handjob to default
    if not renpy.showing("Jean_HJ_Animation"):
        return    
    $ Speed = 0            
    $ JeanX.ArmPose = 1
    hide Jean_HJ_Animation with easeoutbottom
    call Jean_Hide 
    show Jean_Sprite at SpriteLoc(JeanX.SpriteLoc) zorder JeanX.Layer:
        alpha 1
        zoom 1.7 offset (-150,200)
    show Jean_Sprite at SpriteLoc(JeanX.SpriteLoc) zorder JeanX.Layer:
        alpha 1
        ease 1 zoom 1.5 offset (-150,50)
        pause .5
        ease .5 zoom 1 offset (0,0) 
        pause.5
    show Jean_Sprite at SpriteLoc(JeanX.SpriteLoc) zorder JeanX.Layer:
        alpha 1
        zoom 1 offset (0,0)     
    return
    
# End Jean Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    


# Start Jean Psychic Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Core Jean Psychic Handjob element //////////////////////////////////////////////////////////////////////   

image Jean_Hand_Psychic:    
    ConditionSwitch(    
#        "Psychic == 'mouth'", "images/JeanSprite/handjeanP.png", 
#        "Psychic == 'pussy'", "images/JeanSprite/handjeanP.png", 
#        "Psychic == 'anus'", "images/JeanSprite/handjeanP.png", 
#        "Psychic == 'tits'", "images/JeanSprite/handjeanP.png", 
        "True", "images/JeanSprite/handjeanP.png", 
        )         
        
#    "images/JeanSprite/handjeanP.png"    
    anchor (0.5,0.5)
    pos (-10,0)
    offset (0,130)
    block:
        ease 3 alpha 0.7
        ease 3 alpha 1
        repeat
        
image Jean_PJ_Animation:  
#    contains:
#        ConditionSwitch(                                                
#            # backside of the hand
#            "not Speed", Transform("Jean_Hand_Under"), 
#            "Speed == 1", At("Jean_Hand_Under", Jean_Hand_1()),
#            "Speed >= 2", At("Jean_Hand_Under", Jean_Hand_2()),            
#            "Speed", Null(),
#            ),  
    contains:
        ConditionSwitch(                                                
            # cock
#            "True", Transform("Zero_Handcock"), #remove?
            "not Speed", Transform("Zero_Handcock"), 
            "Speed == 1", At("Zero_Handcock", Handcock_1J()),
            "Speed >= 2", At("Zero_Handcock", Handcock_2J()), 
            "Speed", Null(),
            ),  
        offset (0,0)
    contains:
        ConditionSwitch(                                               
            # fingers of the hand
            "not Speed", Transform("Jean_Hand_Psychic"), 
            "Speed == 1", At("Jean_Hand_Psychic", Jean_Hand_1()),
            "Speed >= 2", At("Jean_Hand_Psychic", Jean_Hand_2()), 
            "Speed", Null(),
            ),   
    anchor (0.51, -1.3)
    zoom 0.4#0.6
        
        
label Jean_PJ_Launch(Line = 0): 
    if renpy.showing("Jean_PJ_Animation"):        
        $ Trigger = "psy"
        return
    show Jean_PJ_Animation at SpriteLoc(StageCenter) zorder 150 with easeinbottom:
        #xoffset 150
        offset (250,250)#(100,250)      
    return
    
label Jean_PJ_Reset: # The sequence to the Jean animations from handjob to default
    if not renpy.showing("Jean_PJ_Animation"):
        return    
    $ Speed = 0            
    $ JeanX.ArmPose = 1
    hide Jean_PJ_Animation with easeoutbottom
    return
    
# End Jean Psychic Handjob Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
    


# Jean's TJ animations start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# Animation components / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# start base animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
image Jean_TJ_Animation:
            #core TJ animation   
            contains:
                ConditionSwitch(                                                              
                    # Jean's upper body     
                    "not Player.Sprite","Jean_TJ_0",#Static
                    "Speed == 1", "Jean_TJ_1",#slow
                    "Speed == 4", "Jean_TJ_4",#cumming high
                    "Speed == 5", "Jean_TJ_5",#cumming low
                    "Speed >= 2", "Jean_TJ_2",#fast
                    "True",       "Jean_TJ_0",#Static
                    )
            zoom .7 #0.6
            transform_anchor True
            anchor (.5,.5)
# end base animation / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
            
            
    
image Jean_TJ_HairBack:
            #Hair underlay
            "Jean_Sprite_HairBack"
            transform_anchor True
            zoom 2.5
            anchor (0.5, 0.5)
            offset (320,100)
            rotate 0
  
image Jean_TJ_Head:
            #Hair underlay
            "Jean_Sprite_Head"
            transform_anchor True
            zoom 2.5
            anchor (0.5, 0.5)
            offset (320,100)
            rotate 0
    
image Jean_TJ_HairMid:
            #Hair midlayer
            "Jean_Sprite_HairMid"
            transform_anchor True
            zoom 2.5
            anchor (0.5, 0.5)
            rotate 20
            offset (320,100)
            rotate 0

image Jean_TJ_HairTop:
            #Hair overlay
            "Jean_Sprite_HairTop"
            transform_anchor True
            zoom 2.5 #2.1
            anchor (0.5, 0.5)
            offset (320,100) # (300,275)
            rotate 0

image Jean_TJ_ZeroCock:
            #cock used in laura's sex pose
            "Zero_Blowcock"
            transform_anchor True
            zoom .7
            anchor (0.5, 0.5)
            offset (220,670)#(300,750)
            rotate 0

image Jean_TJ_Body:
            #body underlay
            contains:
                "images/JeanSex/Jean_Titjob_Body.png"  
            contains:               
                ConditionSwitch(
                        "not JeanX.Neck",Null(),                                
                        "True",       "images/JeanSex/Jean_Titjob_Neck_[JeanX.Neck].png",
                        )      
            contains:               
                ConditionSwitch(
                        "'tits' not in JeanX.Spunk",Null(),                                
                        "True",       "images/JeanSex/Jean_Titjob_Spunk_Chest.png",
                        )                 
            transform_anchor True
            zoom 1
            anchor (0.4, 1.0)
            offset (410,770) # (300,275)
            rotate 0
    
  
image Jean_TJ_LeftArm:
            #left arm
            contains:
                "images/JeanSex/Jean_Titjob_LeftHand.png" 
            contains:               
                ConditionSwitch(
                        "not JeanX.Arms",Null(),                                
                        "True",       "images/JeanSex/Jean_Titjob_[JeanX.Arms].png",
                        )   
            contains:
                # Left Piercings
                ConditionSwitch(
                        "not JeanX.Pierce",Null(),        
                        "True",       "images/JeanSex/Jean_Titjob_Left_[JeanX.Pierce].png",
                        )    
    
# Animations start / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Start 0 (static) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Jean_TJ_0:                                                                        
        #Her Body in the TJ pose, static
        contains:
                #hairback
                "Jean_TJ_HairBack"   
                subpixel True       
                pos (0,0) #top (0,-10)
                transform_anchor True
                rotate 0
                parallel:
                    ease 2 ypos -20
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat  
                parallel:
                    pause .1
                    ease 2 rotate -5
                    pause .1
                    ease 2 rotate 0
                    repeat  
        contains:
                #base body test
                "Jean_TJ_Body"  
                subpixel True       
                pos (0,0) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos -20
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat 
        contains:
                #right hand backside
                "images/JeanSex/Jean_Titjob_RightHandBack.png"      
                subpixel True       
                pos (0,-15) #top (0,-10)    
                transform_anchor True 
                parallel:
                    ease 2 ypos -5
                    pause .1
                    ease 2 ypos -15
                    pause .1
                    repeat 
        contains:
                contains:
                    "images/JeanSex/Jean_Titjob_RightTit.png"            
                contains:
                    ConditionSwitch(
                            "'tits' not in JeanX.Spunk",Null(),                                
                            "True",       "images/JeanSex/Jean_Titjob_Spunk_Right.png",
                            )      
                subpixel True       
                pos (0,-15) #top (0,-10)
                transform_anchor True 
                parallel:
                    pause .1
                    ease 2 ypos -5
                    pause .1
                    ease 2 ypos -15
                    repeat 
        contains:
                #right hand
                contains:
                    "images/JeanSex/Jean_Titjob_RightHand.png"    
                contains:
                    # Right Piercings                    
                    ConditionSwitch(
                            "not JeanX.Pierce",Null(),                                
                            "True",       "images/JeanSex/Jean_Titjob_Right_[JeanX.Pierce].png",
                            )                           
                subpixel True     
                pos (0,-15) #top (0,-10)  
                transform_anchor True 
                parallel:
                    ease 2 ypos -5
                    pause .1
                    ease 2 ypos -15
                    pause .1
                    repeat 
        contains:
                #head
                "Jean_TJ_Head"   
                subpixel True       
                pos (0,0) #top (0,-10)
                transform_anchor True
                rotate 0
                parallel:
                    ease 2 ypos -20
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat  
                parallel:
                    pause .1
                    ease 2 rotate -5
                    pause .1
                    ease 2 rotate 0
                    repeat  
        contains:
                #zero cock
                subpixel True
                "Jean_TJ_ZeroCock"
                pos (0,30) #top (0,-10)
                transform_anchor True
                rotate -2
                parallel:
                    ease 2 rotate -2
                    pause .1
                    ease 2 rotate 3
                    pause .1
                    repeat      
        contains:
                #left tit
                contains:
                    "images/JeanSex/Jean_Titjob_LeftTit.png"    
                contains:
                    ConditionSwitch(
                            "'tits' not in JeanX.Spunk",Null(),                                
                            "True",       "images/JeanSex/Jean_Titjob_Spunk_Left.png",
                            )                            
                subpixel True       
                pos (0,0) #top (0,-10)
                transform_anchor True
                parallel:
                    pause .1
                    ease 2 ypos -40
                    pause .1
                    ease 2 ypos 0
                    repeat 
        contains:
                #left hand
                "Jean_TJ_LeftArm"
#                contains:
#                    "images/JeanSex/Jean_Titjob_LeftHand.png"    
#                contains:
#                    # Left Piercings
#                    ConditionSwitch(
#                            "not JeanX.Pierce",Null(),        
#                            "True",       "images/JeanSex/Jean_Titjob_Left_[JeanX.Pierce].png",
#                            )  
                subpixel True       
                pos (0,0) #top (0,-10)   
                transform_anchor True
                parallel:
                    ease 2 ypos -40
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat 
        contains:
                #mid hair
                "Jean_TJ_HairMid"   
                subpixel True       
                pos (0,0) #top (0,+10)
                transform_anchor True
                rotate 0
                parallel:
                    ease 2 ypos -20
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat  
                parallel:
                    pause .1
                    ease 2 rotate -5
                    pause .1
                    ease 2 rotate 0
                    repeat   
        contains:
                #head
                "Jean_TJ_HairTop"   
                subpixel True       
                pos (0,0) #top (0,-10)
                transform_anchor True
                rotate 0
                parallel:
                    ease 2 ypos -20
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat    
                parallel:
                    pause .1
                    ease 2 rotate -5
                    pause .1
                    ease 2 rotate 0
                    repeat  
# End Jean TJ Pose 0 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start 1 (slow) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Jean_TJ_1:                                                                        
        #Her Body in the TJ pose, slow
        contains:
                #hairback
                "Jean_TJ_HairBack"   
                subpixel True       
                pos (0,150) #top (0,-10)
                transform_anchor True
                rotate -5
                parallel:
                    ease 2 ypos 0
                    pause .2
                    ease 2 ypos 150
                    pause .5
                    repeat    
                parallel:
                    ease 2 rotate 0
                    pause .2
                    ease 2 rotate -5
                    pause .5
                    repeat  
        contains:
                #base body
                "Jean_TJ_Body"      
                subpixel True       
                pos (0,150) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos 0
                    pause .2
                    ease 2 ypos 150
                    pause .5
                    repeat  
        contains:
                #right hand backside
                "images/JeanSex/Jean_Titjob_RightHandBack.png"      
                subpixel True       
                pos (0,150) #top (0,-10)    
                transform_anchor True  
                block:
                    ease 2 ypos -20
                    pause .4
                    ease 1.8 ypos 150
                    pause .5
                    repeat  
        contains:
                contains:
                    "images/JeanSex/Jean_Titjob_RightTit.png"            
                contains:
                    ConditionSwitch(
                            "'tits' not in JeanX.Spunk",Null(),                                
                            "True",       "images/JeanSex/Jean_Titjob_Spunk_Right.png",
                            )        
                subpixel True       
                pos (0,150) #top (0,-10)
                transform_anchor True
                block:
                    pause .1
                    ease 1.9 ypos -20
                    pause .4
                    ease 1.8 ypos 150
                    ease .5 ypos 140   
                    repeat
        contains:
                #right hand
                contains:
                    "images/JeanSex/Jean_Titjob_RightHand.png"    
                contains:
                    # Right Piercings                    
                    ConditionSwitch(
                            "not JeanX.Pierce",Null(),                                
                            "True",       "images/JeanSex/Jean_Titjob_Right_[JeanX.Pierce].png",
                            )                           
                subpixel True     
                pos (0,150) #top (0,-10)  
                transform_anchor True 
                block:
                    ease 2 ypos -20                    
                    pause .4
                    ease 1.8 ypos 150
                    pause .5
                    repeat  
        contains:
                #head
                "Jean_TJ_Head"   
                subpixel True       
                pos (0,150) #top (0,-10)
                transform_anchor True
                rotate -5
                parallel:
                    ease 2 ypos 0
                    pause .2
                    ease 2 ypos 150
                    pause .5
                    repeat    
                parallel:
                    ease 2 rotate 0
                    pause .2
                    ease 2 rotate -5
                    pause .5
                    repeat  
        contains:
                #zero cock
                subpixel True
                "Jean_TJ_ZeroCock"
                pos (0,25) #top (0,-10)
                transform_anchor True
                rotate -5
                parallel:                  
                    ease 2 ypos 0
                    pause .4
                    ease 1.8 ypos 25
                    pause .5
                    repeat     
                parallel:
                    ease 2 rotate 0
                    pause .2
                    ease 2 rotate -5
                    pause .5
                    repeat      
        contains:
                #left tit
                contains:
                    "images/JeanSex/Jean_Titjob_LeftTit.png"      
                contains:
                    ConditionSwitch(
                            "'tits' not in JeanX.Spunk",Null(),                                
                            "True",       "images/JeanSex/Jean_Titjob_Spunk_Left.png",
                            )                           
                subpixel True       
                pos (0,150) #top (0,-10)
                transform_anchor True
                block:
                    pause .1
                    ease 1.9 ypos -20
                    pause .4
                    ease 1.8 ypos 150
                    ease .5 ypos 140    
                    repeat
        contains:
                #left hand
                "Jean_TJ_LeftArm"
                subpixel True       
                pos (0,150) #top (0,-10)   
                transform_anchor True
                block:
                    ease 2 ypos -20
                    pause .4
                    ease 1.8 ypos 150
                    pause .5
                    repeat  
        contains:
                #mid hair
                "Jean_TJ_HairMid"   
                subpixel True       
                pos (0,160) #top (0,150)
                transform_anchor True
                rotate -5
                parallel:
                    ease 2 ypos -20#-20
                    pause .4
                    ease 1.8 ypos 160
                    pause .5
                    repeat   
                parallel:
                    ease 2 rotate 0
                    pause .2
                    ease 2 rotate -5
                    pause .5
                    repeat  
        contains:
                #head
                "Jean_TJ_HairTop"   
                subpixel True       
                pos (0,150) #top (0,-10)
                transform_anchor True
                rotate -5
                parallel:
                    ease 2 ypos 0
                    pause .2
                    ease 2 ypos 150
                    pause .5
                    repeat    
                parallel:
                    ease 2 rotate 0
                    pause .2
                    ease 2 rotate -5
                    pause .5
                    repeat  
# End Jean TJ Pose 1 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
             
 
# Start 2 (fast) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Jean_TJ_2:                                                                        
        #Her Body in the TJ pose, fast
        contains:
                #hairback
                "Jean_TJ_HairBack"   
                subpixel True       
                pos (0,80) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 1 ypos -20
                    pause .1
                    ease .5 ypos 80
                    repeat    
                parallel:
                    ease 1 rotate 0
                    pause .1
                    ease .5 rotate -5
                    repeat  
        contains:
                #base body
                "Jean_TJ_Body"      
                subpixel True       
                pos (0,80) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 1 ypos -20
                    pause .1
                    ease .5 ypos 80
                    repeat   
        contains:
                #right hand backside
                "images/JeanSex/Jean_Titjob_RightHandBack.png"      
                subpixel True       
                pos (0,80) #top (0,-10)    
                transform_anchor True  
                block:
                    ease 1 ypos -40
                    pause .2
                    ease .4 ypos 80
                    repeat  
        contains:
                contains:
                    "images/JeanSex/Jean_Titjob_RightTit.png"            
                contains:
                    ConditionSwitch(
                            "'tits' not in JeanX.Spunk",Null(),                                
                            "True",       "images/JeanSex/Jean_Titjob_Spunk_Right.png",
                            )      
                subpixel True       
                pos (0,80) #top (0,-10)
                transform_anchor True                
                block:
                    ease .3 ypos 40  
                    ease .7 ypos -40
                    pause .2
                    ease .4 ypos 80
                    repeat
        contains:
                #right hand
                contains:
                    "images/JeanSex/Jean_Titjob_RightHand.png"    
                contains:
                    # Right Piercings                    
                    ConditionSwitch(
                            "not JeanX.Pierce",Null(),                                
                            "True",       "images/JeanSex/Jean_Titjob_Right_[JeanX.Pierce].png",
                            )                           
                subpixel True     
                pos (0,80) #top (0,-10)  
                transform_anchor True 
                block:
                    ease 1 ypos -40
                    pause .2
                    ease .4 ypos 80
                    repeat  
        contains:
                #head
                "Jean_TJ_Head"   
                subpixel True       
                pos (0,80) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 1 ypos -20
                    pause .1
                    ease .5 ypos 80
                    repeat    
                parallel:
                    ease 1 rotate 0
                    pause .1
                    ease .5 rotate -5
                    repeat  
        contains:
                #zero cock
                subpixel True
                "Jean_TJ_ZeroCock"
                pos (0,30) #top (0,-10)
                transform_anchor True
                rotate -2
                parallel:                  
                    ease 1 ypos 0
                    pause .2
                    ease .4 ypos 30
                    repeat     
                parallel:
                    ease 1 rotate 0
                    pause .1
                    ease .5 rotate -2
                    repeat      
        contains:
                #left tit
                contains:
                    "images/JeanSex/Jean_Titjob_LeftTit.png"        
                contains:
                    ConditionSwitch(
                            "'tits' not in JeanX.Spunk",Null(),                                
                            "True",       "images/JeanSex/Jean_Titjob_Spunk_Left.png",
                            )                         
                subpixel True       
                pos (0,80) #top (0,-10)
                transform_anchor True
                block:
                    ease .3 ypos 40  
                    ease .7 ypos -40
                    pause .2
                    ease .4 ypos 80   
                    repeat
        contains:
                #left hand
                "Jean_TJ_LeftArm"
                subpixel True       
                pos (0,80) #top (0,-10)   
                transform_anchor True
                block:
                    ease 1 ypos -40
                    pause .2
                    ease .4 ypos 80
                    repeat  
        contains:
                #mid hair
                "Jean_TJ_HairMid"   
                subpixel True       
                pos (0,90) #top (0,+10)
                transform_anchor True
                rotate -5
                parallel:
                    ease 1 ypos -40#-20
                    pause .2
                    ease .4 ypos 90
                    repeat   
                parallel:
                    ease 1 rotate 0
                    pause .2
                    ease .4 rotate -5
                    repeat  
        contains:
                #head
                "Jean_TJ_HairTop"   
                subpixel True       
                pos (0,80) #top (0,-10)
                transform_anchor True
                rotate -5
                parallel:
                    ease 1 ypos -20
                    pause .1
                    ease .5 ypos 80
                    repeat    
                parallel:
                    ease 1 rotate 0
                    pause .1
                    ease .5 rotate -5
                    repeat  
# End Jean TJ Pose 2 / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
                   
                   
# Start 4 (cumming high) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Jean_TJ_4:                                                                        
        #Her Body in the TJ pose, cumming
        contains:
                #hairback
                "Jean_TJ_HairBack"   
                subpixel True       
                pos (0,0) #top (0,-10)
                transform_anchor True
                rotate 0
                parallel:
                    ease 2 ypos -20
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat  
                parallel:
                    pause .1
                    ease 2 rotate -5
                    pause .1
                    ease 2 rotate 0
                    repeat  
        contains:
                #base body
                "Jean_TJ_Body"      
                subpixel True       
                pos (0,0) #top (0,-10)
                transform_anchor True
                parallel:
                    ease 2 ypos -20
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat 
        contains:
                #right hand backside
                "images/JeanSex/Jean_Titjob_RightHandBack.png"      
                subpixel True       
                pos (0,0) #top (0,-10)    
                transform_anchor True 
                parallel:
                    ease 2 ypos -30
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat  
        contains:
                contains:
                    "images/JeanSex/Jean_Titjob_RightTit.png"            
                contains:
                    ConditionSwitch(
                            "'tits' not in JeanX.Spunk",Null(),                                
                            "True",       "images/JeanSex/Jean_Titjob_Spunk_Right.png",
                            )        
                subpixel True       
                pos (0,5) #top (0,-10)
                transform_anchor True 
                parallel:
                    pause .2
                    ease 1.9 ypos -30
                    pause .2
                    ease 1.9 ypos 5
                    repeat  
        contains:
                #right hand
                contains:
                    "images/JeanSex/Jean_Titjob_RightHand.png"    
                contains:
                    # Right Piercings                    
                    ConditionSwitch(
                            "not JeanX.Pierce",Null(),                                
                            "True",       "images/JeanSex/Jean_Titjob_Right_[JeanX.Pierce].png",
                            )                           
                subpixel True     
                pos (0,0) #top (0,-10)  
                transform_anchor True 
                parallel:
                    ease 2 ypos -30
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat  
        contains:
                #head
                "Jean_TJ_Head"   
                subpixel True       
                pos (0,0) #top (0,-10)
                transform_anchor True
                rotate 0
                parallel:
                    ease 2 ypos -20
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat  
                parallel:
                    pause .1
                    ease 2 rotate -5
                    pause .1
                    ease 2 rotate 0
                    repeat  
        contains:
                #zero cock
                subpixel True
                "Jean_TJ_ZeroCock"
                pos (0,20) #top (0,-10)
                transform_anchor True
                rotate 2
                parallel:                  
                    ease 2 ypos 0    
                    pause .1
                    ease 2 ypos 20
                    pause .1
                    repeat         
        contains:
                #left tit
                contains:
                    "images/JeanSex/Jean_Titjob_LeftTit.png"        
                contains:
                    ConditionSwitch(
                            "'tits' not in JeanX.Spunk",Null(),                                
                            "True",       "images/JeanSex/Jean_Titjob_Spunk_Left.png",
                            )                         
                subpixel True       
                pos (0,5) #top (0,-10)
                transform_anchor True
                parallel:
                    pause .2
                    ease 1.9 ypos -30
                    pause .2
                    ease 1.9 ypos 5
                    repeat  
        contains:
                #left hand
                "Jean_TJ_LeftArm"
                subpixel True       
                pos (0,0) #top (0,-10)   
                transform_anchor True
                parallel:
                    ease 2 ypos -30
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat  
        contains:
                #mid hair
                "Jean_TJ_HairMid"   
                subpixel True       
                pos (0,0) #top (0,+10)
                transform_anchor True
                rotate 0
                parallel:
                    ease 2 ypos -15
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat  
                parallel:
                    pause .1
                    ease 2 rotate -5
                    pause .1
                    ease 2 rotate 0
                    repeat   
        contains:
                #head
                "Jean_TJ_HairTop"   
                subpixel True       
                pos (0,0) #top (0,-10)
                transform_anchor True
                rotate 0
                parallel:
                    ease 2 ypos -20
                    pause .1
                    ease 2 ypos 0
                    pause .1
                    repeat    
                parallel:
                    pause .1
                    ease 2 rotate -5
                    pause .1
                    ease 2 rotate 0
                    repeat  
# End Jean TJ Pose 4 cumming / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


# Start 5 (cumming low) < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <
image Jean_TJ_5:                                                                        
        #Her Body in the TJ pose, cumming low
        contains:
                #hairback
                "Jean_TJ_HairBack"   
                subpixel True    
                pos (-30,155)
                transform_anchor True
                rotate -20
                parallel:
                    ease 2 ypos 140
                    pause .1
                    ease 2 ypos 155
                    pause .1
                    repeat
#        contains:
#                #base body
#                contains:
#                    "images/JeanSex/Jean_Titjob_Body.png"      
#                subpixel True   
#                pos (-80,-200)
#                transform_anchor True
#                rotate -20
#                parallel:
#                    ease 2 ypos -220
#                    pause .1
#                    ease 2 ypos -200
#                    pause .1
#                    repeat 
        contains:
                #base body 
                "Jean_TJ_Body"      
                subpixel True        
                pos (185,70)
                transform_anchor True
                rotate -20
                parallel:
                    ease 2 ypos 50
                    pause .1
                    ease 2 ypos 70
                    pause .1
                    repeat                   
        contains:
                #right hand backside
                contains:
                    "images/JeanSex/Jean_Titjob_RightHandBack.png"      
                subpixel True     
                pos (-80,-180)
                transform_anchor True
                rotate -10
                parallel:
                    ease 2 ypos -200
                    pause .1
                    ease 2 ypos -180
                    pause .1
                    repeat  
        contains:
                #right tit
                contains:
                    "images/JeanSex/Jean_Titjob_RightTit.png"            
                contains:
                    ConditionSwitch(
                            "'tits' not in JeanX.Spunk",Null(),                                
                            "True",       "images/JeanSex/Jean_Titjob_Spunk_Right.png",
                            )       
                subpixel True       
                pos (-80,-160)
                transform_anchor True
                rotate -10
                parallel:
                    ease .4 ypos -170
                    ease 1.7 ypos -190
                    pause .1
                    ease 2 ypos -160
                    repeat  
        contains:
                #right hand
                contains:
                    "images/JeanSex/Jean_Titjob_RightHand.png"    
                contains:
                    # Right Piercings                    
                    ConditionSwitch(
                            "not JeanX.Pierce",Null(),                                
                            "True",       "images/JeanSex/Jean_Titjob_Right_[JeanX.Pierce].png",
                            )                           
                subpixel True     
                pos (-80,-180)
                transform_anchor True
                rotate -10
                parallel:
                    ease 2 ypos -200
                    pause .1
                    ease 2 ypos -180
                    pause .1
                    repeat   
        contains:
                #head
                "Jean_TJ_Head"   
                subpixel True       
                pos (-30,155)
                transform_anchor True
                rotate -20
                parallel:
                    ease 2 ypos 140
                    pause .1
                    ease 2 ypos 155
                    pause .1
                    repeat 
        contains:
                #zero cock
                subpixel True
                "Jean_TJ_ZeroCock"
                pos (0,20) #top (0,-10)
                transform_anchor True
                rotate 2  
                parallel:                  
                    ease 2 ypos 0    
                    pause .1
                    ease 2 ypos 20
                    pause .1
                    repeat 
        contains:
                #left tit
                contains:
                    "images/JeanSex/Jean_Titjob_LeftTit.png"         
                contains:
                    ConditionSwitch(
                            "'tits' not in JeanX.Spunk",Null(),                                
                            "True",       "images/JeanSex/Jean_Titjob_Spunk_Left.png",
                            )                           
                subpixel True   
                pos (-80,-160)
                transform_anchor True
                rotate -10
                parallel:
                    ease .4 ypos -170
                    ease 1.7 ypos -190
                    pause .1
                    ease 2 ypos -160
                    repeat  
        contains:
                #left hand
                "Jean_TJ_LeftArm"
                subpixel True     
                pos (-80,-180)
                transform_anchor True
                rotate -10
                parallel:
                    ease 2 ypos -200
                    pause .1
                    ease 2 ypos -180
                    pause .1
                    repeat  
        contains:
                #mid hair
                "Jean_TJ_HairMid"   
                subpixel True   
                pos (-30,115)
                transform_anchor True
                rotate -10
                parallel:
                    ease 2 ypos 95
                    pause .1
                    ease 2 ypos 115
                    pause .1
                    repeat  
        contains:
                #head
                "Jean_TJ_HairTop"   
                subpixel True    
                pos (-30,155)
                transform_anchor True
                rotate -20
                parallel:
                    ease 2 ypos 140
                    pause .1
                    ease 2 ypos 155
                    pause .1
                    repeat  
# End Jean TJ Pose 5 cumming / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

# Jean's TJ animations end / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Jean_TJ_Launch(Line = 0):    # The sequence to launch the Jean Titfuck animations   
    if renpy.showing("Jean_TJ_Animation"):
        return
    call Jean_Hide
    show Jean_Sprite at SpriteLoc(JeanX.SpriteLoc) zorder JeanX.Layer:
        alpha 1
        ease 1 zoom 2.3 xpos 750 yoffset -100
    if Line == "L": # Jean gets started. . .
            if Taboo: 
                if len(Present) >= 2:
                    if Present[0] != JeanX:
                            "[JeanX.Name] looks back at [Present[0].Name] to see if she's watching."
                    elif Present[1] != JeanX:
                            "[JeanX.Name] looks back at [Present[1].Name] to see if she's watching."
                else:
                            "[JeanX.Name] casually glances around to see if anyone can see her."
            "[JeanX.Name] bends over and places your cock between her breasts."   
    
    if JeanX.Chest and JeanX.Over:
        "She throws off her [JeanX.Over] and her [JeanX.Chest]."                
    elif JeanX.Over:
        "She throws off her [JeanX.Over], baring her breasts underneath."
    elif JeanX.Chest:
        "She tugs off her [JeanX.Chest] and throws it aside."
    $ JeanX.Over = 0
    $ JeanX.Chest = 0
    $ JeanX.ArmPose = 0
    
    call Jean_First_Topless           
     
    show blackscreen onlayer black with dissolve   
    show Jean_Sprite zorder JeanX.Layer:
        alpha 0
    $ Speed = 0
    if Line != "cum":
        $ Trigger = "titjob"
    show Jean_TJ_Animation zorder 150:
        pos (700,520) #700,420)
    $ Player.Sprite = 1
    hide blackscreen onlayer black with dissolve
    return
    
label Jean_TJ_Reset: 
    # The sequence to the Jean animations from Titfuck to default
    if not renpy.showing("Jean_TJ_Animation"):
        return
#    hide Jean_TJ_Animation
    call Jean_Hide 
    $ Player.Sprite = 0
    
    show Jean_Sprite at SpriteLoc(JeanX.SpriteLoc) zorder JeanX.Layer:
        zoom 2.3 xpos 750 yoffset -100
    show Jean_Sprite zorder JeanX.Layer:
        alpha 1
        ease 1 zoom 1.5 xpos 700 yoffset 50
        pause .5
        ease .5 zoom 1 xpos JeanX.SpriteLoc yoffset 0         
    "[JeanX.Name] pulls back"
    show Jean_Sprite at SpriteLoc(JeanX.SpriteLoc) zorder JeanX.Layer:
        alpha 1
        zoom 1 offset (0,0) xpos JeanX.SpriteLoc  
    return
            
# End Jean TJ Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /







# Jean Misc Animations / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
       
        
        
label Jean_Kissing_Launch(T = Trigger):    
    call Jean_Hide
    $ Trigger = T
    show Jean_Sprite at SpriteLoc(JeanX.SpriteLoc) zorder JeanX.Layer
    show Jean_Sprite at SpriteLoc(StageCenter) zorder JeanX.Layer:
        ease 0.5 offset (0,0) zoom 2 alpha 1
    return
    
label Jean_Kissing_Smooch:   
    $ JeanX.FaceChange("kiss")
    show Jean_Sprite at SpriteLoc(StageCenter) zorder JeanX.Layer:
        ease 0.5 xpos StageCenter offset (0,0) zoom 2 alpha 1
        pause 1
        ease 0.5 xpos JeanX.SpriteLoc zoom 1      
    show Jean_Sprite at SpriteLoc(JeanX.SpriteLoc) zorder JeanX.Layer:
        zoom 1
    $ JeanX.FaceChange("sexy") 
    return
            
label Jean_Breasts_Launch(T = Trigger):    
    call Jean_Hide
    $ Trigger = T
    show Jean_Sprite at SpriteLoc(JeanX.SpriteLoc) zorder JeanX.Layer:
#        ease 0.5 offset (-100,-200) zoom 2
        ease 0.5 pos (700,-50) offset (0,0) zoom 2 alpha 1
    return
     
label Jean_Middle_Launch(T = Trigger):    
    call Jean_Hide
    $ Trigger = T
    show Jean_Sprite at SpriteLoc(JeanX.SpriteLoc) zorder JeanX.Layer:
#        ease 0.5 offset (-100,-200) zoom 2
        ease 0.5 pos (700,-50) offset (0,0) zoom 1.5 alpha 1
    return
    
label Jean_Pussy_Launch(T = Trigger):
    call Jean_Hide    
    $ Trigger = T
    show Jean_Sprite at SpriteLoc(JeanX.SpriteLoc) zorder JeanX.Layer:
        ease 0.5 pos (700,-400) offset (0,0) zoom 2 alpha 1
    return
        
label Jean_Pos_Reset(Pose = 0):  
    if JeanX.Loc != bg_current:
            return
    call Jean_Hide 
    show Jean_Sprite at SpriteLoc(JeanX.SpriteLoc) zorder JeanX.Layer:
            ease .5 offset (0,0) anchor (0.5, 0.0) zoom 1 alpha 1 xzoom 1 yzoom 1
    show Jean_Sprite zorder JeanX.Layer:
            offset (0,0) 
            anchor (0.5, 0.0)
            zoom 1  
            xzoom 1 
            yzoom 1 
            alpha 1
            pos (JeanX.SpriteLoc,50)
    $ Trigger = Pose
    return
    
label Jean_Hide(Sprite=0):
        if renpy.showing("Jean_SexSprite"):
            call Jean_Sex_Reset
        hide Jean_SexSprite
        hide Jean_HJ_Animation
        hide Jean_BJ_Animation
        hide Jean_TJ_Animation 
        if Sprite:
                hide Jean_Sprite    
        return

# Interface items //////////////////////////////////////////////////////////////////////////////

image GropeRightBreast_Jean:    
    contains:
        subpixel True
        "UI_Hand"
        yzoom 0.65
        xzoom -0.65
        pos (185,340)#(110,380)#(120,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -60
        block: 
            ease 1 rotate -30 #-30
            ease 1 rotate -60 #-60 
            repeat

image GropeLeftBreast_Jean:    
    contains:
        subpixel True
        "UI_Hand"
        zoom 0.65#.7
        pos (290,340)#(195,380)#(215,400)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 60
        block: 
            ease 1 rotate 30
            ease 1 rotate 60
            repeat
                        
image LickRightBreast_Jean:   
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5 
        xzoom -0.45
        pos (175,325)#(195,360) #(200,410)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block: 
            ease .5 rotate -40 pos (150,300)#(190,380)            
            pause .5
            ease 1.5 rotate 30 pos (175,325)#(200,410)
            repeat

#image GropeBreast:
image LickLeftBreast_Jean:   
    contains:
        subpixel True
        "UI_Tongue"
        yzoom 0.45#0.5 
        xzoom -0.45
        pos (275,330)#(95,355)#(105,375)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 30
        block: 
            ease .5 rotate -40 pos (255,310)#(85,345)  top         
            pause .5
            ease 1.5 rotate 30 pos (275,330)#(105,375) bottom
            repeat
            
image GropeThigh_Jean: 
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (245,630)#(115,690)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 100
        block:
            pause .5
            ease 1 rotate 110 pos (255,700) #(150,750) bottom
            ease 1 rotate 100 pos (245,630)   
            repeat

image GropePussy_Jean: 
    contains:
        subpixel True
        "UI_Hand"
        zoom .65
        pos (245,560)#(120,620)#(200,600) -20
        anchor (0.5,0.5)
        alpha 0.5
        rotate 170
        block:
            choice: 
                ease .5 rotate 190 pos (245,545)#pos (120,605) #(200,585)
                ease .75 rotate 170 pos (245,560)#pos (120,620)   
            choice: 
                ease .5 rotate 190 pos (245,545)#pos (120,605)
                pause .25
                ease 1 rotate 170 pos (245,560)#pos (120,620)             
            repeat

image FingerPussy_Jean: 
    contains:
        subpixel True
        "UI_Finger"       
        zoom 0.65
        pos (265,640)#(140,700)#(210,665)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 40
        block:
            choice: 
                ease 1 rotate 40 pos (275,615)#(150,665)#(220,640)
                pause .5
                ease 1 rotate 50 pos (265,640)#(140,700)  #(210,665)     
            choice:                          
                ease .5 rotate 40 pos (275,615)
                pause .5
                ease 1.75 rotate 50 pos (265,640) 
            choice:                          
                ease 2 rotate 40 pos (275,615)
                pause .5
                ease 1 rotate 50 pos (265,640) 
            choice:                          
                ease .25 rotate 40 pos (275,615)
                ease .25 rotate 50 pos (265,640)
                ease .25 rotate 40 pos (275,615)
                ease .25 rotate 50 pos (265,640)
            repeat
            
image Lickpussy_Jean:   
    contains:
        subpixel True
        "UI_Tongue"        
        yzoom 0.45
        xzoom -0.45
        pos (275,595)#(155,650)#(230,625)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 10
        block: 
            easeout .5 rotate -50 pos (265,575)#(145,630) #(210,605)
            linear .5 rotate -60 pos (255,585)#(135,640) #(200,615)
            easein 1 rotate 10 pos (275,595)#(155,650) #(230,625)
            repeat

image VibratorRightBreast_Jean: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (165,310)#(150,380)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            ease .9 rotate 35 ypos 300
            pause .25
            ease .7 rotate 55 ypos 310           
            pause .25
            repeat

image VibratorLeftBreast_Jean: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (270,310)#(270,400)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 55
        block:
            ease 1.1 rotate 35 ypos 300
            pause .25
            ease .9 rotate 55 ypos 310           
            pause .25
            repeat
            
image VibratorPussy_Jean: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (265,580)#(240,665)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 70
        block:
            ease 1 rotate 35 xpos 250 #230
            pause .25
            ease 1 rotate 70 xpos 265 #240          
            pause .25
            repeat

image VibratorAnal_Jean: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (295,570)#(270,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 10
        block:
            ease 1 rotate 0 xpos 290
            pause .25
            ease 1 rotate 10 xpos 300       
            pause .25
            repeat
            
image VibratorPussyInsert_Jean: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (240,645)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.5
        rotate 0

image VibratorAnalInsert_Jean: 
    contains:
        subpixel True
        "UI_Vibrator"  
        pos (250,640)
        zoom 0.5
        anchor (0.5,0.5)
        alpha 0.3
        rotate 0



#Lesbian action animations.
image GirlGropeBothBreast_Jean: 
    contains:
        "GirlGropeLeftBreast_Jean"
    contains:
        "GirlGropeRightBreast_Jean"
    
image GirlGropeLeftBreast_Jean:  
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        pos (290,340)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10
        block: 
            ease 1 rotate 10 pos (290,350)#(220,380)
            ease 1 rotate -10 pos (290,340)#(220,370)
            repeat
#(185,340)(290,340)
image GirlGropeRightBreast_Jean:    
    contains:
        subpixel True
        "UI_GirlHand"
        yzoom 0.6
        xzoom -0.6
        pos (170,340)#(90,380)
        anchor (0.5,0.5)
        alpha 0.5
        rotate -10#-30
        block: 
            ease 1 rotate -40 pos (170,350)#(90,380)
            ease 1 rotate -10 pos (170,340)#(90,370)
            repeat

image GirlGropeThigh_Jean: 
    contains:
        subpixel True
        "UI_GirlHand"
        zoom .6
        anchor (0.5,0.5)
        pos (0,0)#(240,540)#(210,730)
        alpha 0.5
        rotate 100
#        parallel: 
#            pause .5
#            ease 1 ypos 780
#            ease 1 ypos 730            
#            repeat
#        parallel:            
#            pause .5
#            ease .5 xpos 213
#            ease .5 xpos 210
#            ease .5 xpos 213
#            ease .5 xpos 210
#            repeat

image GirlGropePussy_JeanSelf:
    contains:
        "GirlGropePussy_Jean"
        anchor (0.5,0.5)
        rotate -40
#        yzoom -1
        pos (200,510)#(100,500)
    
image GirlGropePussy_Jean: 
    contains:
        subpixel True
        "UI_GirlHand"
        zoom 0.6
        pos (240,540)#(130,595)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 pos (240,535)#(130,590)
                ease .5 rotate 195 
                ease .75 rotate 210 
                ease .5 rotate 195 
            choice: #slow rub
                ease .5 rotate 210 pos (240,535)#(130,590)#-10+20
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 pos (240,535)#(130,590)
                ease .75 rotate 200 pos (240,540)#(130,595) 
                ease .5 rotate 205 pos (240,535)
                ease .75 rotate 200 pos (240,540)
            choice: #Fast stroke
                ease .3 rotate 205 pos (240,535)#(130,590)
                ease .3 rotate 200 pos (240,545)#(130,600)
                ease .3 rotate 205 pos (240,535)
                ease .3 rotate 200 pos (240,545)
            repeat

image GirlFingerPussy_Jean: 
    contains:
        subpixel True
        "UI_GirlFinger"       
        zoom .6
        pos (250,550)#(140,605)
        anchor (0.5,0.5)
        alpha 0.5
        rotate 200
        block:
            choice: #fast rub
                ease .75 rotate 210 pos (250,555)#(140,610)
                ease .5 rotate 195 
                ease .75 rotate 210 
                ease .5 rotate 195 
            choice: #slow rub
                ease .5 rotate 210 pos (250,555)
                ease 1 rotate 195
                pause .25
                ease .5 rotate 210
                ease 1 rotate 195
                pause .25
            choice: #slow stroke
                ease .5 rotate 205 ypos 565#620
                ease .75 rotate 200 ypos 570#625
                ease .5 rotate 205 ypos 565
                ease .75 rotate 200 ypos 570
            choice: #Fast stroke
                ease .3 rotate 205 ypos 565#620
                ease .3 rotate 200 ypos 575#630
                ease .3 rotate 205 ypos 565
                ease .3 rotate 200 ypos 575
            repeat
