﻿# star Jean chat interface
#Jean Relationship ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////  

label Jean_Relationship: #rkelj 
    while True:
        menu:
            ch_j "What did you want to talk about?"            
            "Do you want to be my girlfriend?" if "dating" not in JeanX.Traits and "ex" not in JeanX.Traits:
                    $ JeanX.DailyActions.append("relationship")
                    if "asked boyfriend" in JeanX.DailyActions and "angry" in JeanX.DailyActions:
                            $ JeanX.FaceChange("angry", 1)
                            ch_j "Again with this? No!"
                            return
                    elif "asked boyfriend" in JeanX.DailyActions:
                            $ JeanX.FaceChange("angry", 1)
                            ch_j "Still no."
                            return
                    elif JeanX.Break[0]:
                            $ JeanX.FaceChange("angry", 1)
                            ch_j "You have to be kidding."
                            if Player.Harem:   
                                    $ JeanX.DailyActions.append("asked boyfriend")
                                    return
                            else:
                                    ch_p "I'm serious."
                    
                    $ JeanX.DailyActions.append("asked boyfriend")
                    
                    if Player.Harem and "JeanYes" not in Player.Traits:  
                        if len(Player.Harem) >= 2:
                            ch_j "Hey, apparently it's those other girls' problem, [JeanX.Petname]."
                        else:
                            ch_j "Hey, apparently it's [Player.Harem[0].Name]'s problem, [JeanX.Petname]."
                        return
                                        
                    if JeanX.Event[5]:
                            $ JeanX.FaceChange("bemused", 1)
                            ch_j "Hey, you were the one that said \"no\". . ."
                    else:
                            $ JeanX.FaceChange("surprised", 2)
                            ch_j "What? Why?" 
                            $ JeanX.FaceChange("smile", 1)
                        
                    call Jean_OtherWoman
                    
                    if JeanX.Love >= 800:
                            $ JeanX.FaceChange("surprised", 1)
                            $ JeanX.Mouth = "smile"
                            $ JeanX.Statup("Love", 200, 40)
                            ch_j "Huh. Ok."
                            if "boyfriend" not in JeanX.Petnames:
                                    $ JeanX.Petnames.append("boyfriend")                
                            $ JeanX.Traits.append("dating") 
                            if "JeanYes" in Player.Traits:       
                                    $ Player.Traits.remove("JeanYes")
                                    $ Player.Harem.append(JeanX)
                                    call Harem_Initiation
                            "[JeanX.Name] floats in and kisses you deeply."
                            $ JeanX.FaceChange("kiss", 1) 
                            $ JeanX.Kissed += 1
                    elif JeanX.Obed >= 500:
                            $ JeanX.FaceChange("perplexed")
                            ch_j "\"Dating\". . . I mean. . ."
                            ch_j "That's not really what this is. . ."
                    elif JeanX.Inbt >= 500:
                            $ JeanX.FaceChange("smile")                
                            ch_j "-No-."
                    else:
                            $ JeanX.FaceChange("perplexed", 1)
                            ch_j "Relax there, [JeanX.Petname]."
                      
            "Do you want to get back together?" if "ex" in JeanX.Traits:
                    $ JeanX.DailyActions.append("relationship")
                    if "asked boyfriend" in JeanX.DailyActions and "angry" in JeanX.DailyActions:
                            $ JeanX.FaceChange("angry", 1)
                            ch_j "Again with this? No!"
                            return
                    elif "asked boyfriend" in JeanX.DailyActions:
                            $ JeanX.FaceChange("angry", 1)
                            ch_j "Still no."
                            return
                            
                    $ JeanX.DailyActions.append("asked boyfriend")
                    
                    if Player.Harem and "JeanYes" not in Player.Traits:
                            if len(Player.Harem) >= 2:
                                ch_j "Hey, apparently it's those other girls' problem, [JeanX.Petname]."
                            else:
                                ch_j "Hey, apparently it's [Player.Harem[0].Name]'s problem, [JeanX.Petname]."
                            return
                        
                    $ Cnt = 0
                    call Jean_OtherWoman
                                            
                    if JeanX.Love >= 800:
                            $ JeanX.FaceChange("surprised", 1)
                            $ JeanX.Mouth = "smile"
                            $ JeanX.Statup("Love", 90, 5)
                            ch_j "Oh, fine, whatever."
                            if "boyfriend" not in JeanX.Petnames:
                                        $ JeanX.Petnames.append("boyfriend")                
                            $ JeanX.Traits.append("dating")          
                            $ JeanX.Traits.remove("ex")
                            if "JeanYes" in Player.Traits:       
                                        $ Player.Traits.remove("JeanYes")
                                        $ Player.Harem.append(JeanX)
                                        call Harem_Initiation
                            "[JeanX.Name] floats in and kisses you."
                            $ JeanX.FaceChange("kiss", 1) 
                            $ JeanX.Kissed += 1
                    elif JeanX.Love >= 600 and ApprovalCheck(JeanX, 1500):
                            $ JeanX.FaceChange("smile", 1)
                            $ JeanX.Statup("Love", 90, 5)
                            ch_j "Sure, whatever."
                            if "boyfriend" not in JeanX.Petnames:
                                    $ JeanX.Petnames.append("boyfriend")                
                            $ JeanX.Traits.append("dating")             
                            $ JeanX.Traits.remove("ex")    
                            if "JeanYes" in Player.Traits:       
                                    $ Player.Traits.remove("JeanYes")
                                    $ Player.Harem.append(JeanX)
                                    call Harem_Initiation
                            $ JeanX.FaceChange("kiss", 1) 
                            "[JeanX.Name] gives you a quick kiss."
                            $ JeanX.FaceChange("sly", 1) 
                            $ JeanX.Kissed += 1
                    elif JeanX.Obed >= 500:
                            $ JeanX.FaceChange("sad")
                            ch_j "That's not really where we're at."   
                    elif JeanX.Inbt >= 500:
                            $ JeanX.FaceChange("perplexed")                
                            ch_j "That's no fun."
                    else:
                            $ JeanX.FaceChange("perplexed", 1)
                            ch_j "Um, no."
                        
                    # End Back Together
                 
            "I wanted to ask about [[another girl]" if JeanX in Player.Harem:
                            call AskDateOther
                                   
            "I think we should break up." if "dating" in JeanX.Traits or JeanX in Player.Harem: 
                            if "breakup talk" in JeanX.RecentActions:
                                    ch_j "I'm pretty sure we already covered that."
                            elif "breakup talk" in JeanX.DailyActions:
                                    ch_j "Silly rabbit." 
                                    ch_j "Not today, [JeanX.Petname]."
                            else:
                                    call Breakup(JeanX)
            
            "About that talk we had before. . .":
                menu:
#                    "When you said you loved me. . ." if "lover" not in JeanX.Traits and JeanX.Event[6] >= 20 and JeanX.Event[6] != 23:
#                            call Jean_Love_Redux
                            
#                    "When you were telling me all that stuff about yourself. . ." if "lover" not in JeanX.Traits and JeanX.Event[6] == 23:
#                            call Jean_Love_Redux
                            
#                    "You said you wanted me to be more in control?" if "sir" not in JeanX.Petnames and "sir" in JeanX.History:
#                            if "asked sub" in JeanX.RecentActions:
#                                    ch_j "I'm pretty sure we already covered that."
#                            elif "asked sub" in JeanX.DailyActions:
#                                    ch_j "Maybe later. . ."            
#                            else:
#                                    call Jean_Sub_Asked
#                    "You said you wanted me to be your Master?" if "master" not in JeanX.Petnames and "master" in JeanX.History:
#                            if "asked sub" in JeanX.RecentActions:
#                                    ch_j "I'm pretty sure we already covered that."
#                            elif "asked sub" in JeanX.DailyActions:
#                                    ch_j "Maybe later. . ."                     
#                            else:
#                                    call Jean_Sub_Asked
                    "Never mind":
                            pass       
                            
            "Never Mind":
                return
                  
    return
 
label Jean_OtherWoman(Cnt = 0):
    #Other is the other woman, Poly is whether she'd be cool with a threesome
    if not Player.Harem:
            return      
    $ Cnt = int((JeanX.GirlLikeCheck(Player.Harem[0]) - 500)/2)      
        
    $ JeanX.FaceChange("perplexed")
    if len(Player.Harem) >= 2:
        ch_j "Aren't you hanging out with. . . [Player.Harem[0].Name] right now?"
        ch_j "And that's not all, if I'm reading the room right."
    else:    
        ch_j "Aren't you hanging out with. . . [Player.Harem[0].Name] right now?"
    menu: 
        extend ""
        "She said I can be with you too." if "JeanYes" in Player.Traits:
                if ApprovalCheck(JeanX, 1800, Bonus = Cnt):
                    $ JeanX.FaceChange("smile", 1)
                    if JeanX.Love >= JeanX.Obed:
                            ch_j "Oh, well ok then."
                    elif JeanX.Obed >= JeanX.Inbt:
                            ch_j "Smooth."
                    else:
                            ch_j "Oh, cool.."
                else:
                    $ JeanX.FaceChange("smile", 1)
                    ch_j "Lol, cuck."  
                    #$ renpy.pop_call()                                          
                    #This causes it to jump past the previous menu on the return, disabled on Jean
        
        "I could ask if she'd be ok with me dating you both." if "JeanYes" not in Player.Traits:
                if ApprovalCheck(JeanX, 1800, Bonus = Cnt):
                        $ JeanX.FaceChange("smile", 1)
                        if JeanX.Love >= JeanX.Obed:
                            ch_j "Probably a good idea."
                        elif JeanX.Obed >= JeanX.Inbt:
                            ch_j "Uh-huh. . ."
                        else:
                            ch_j "bawk, bawkbawk baawk."    
                        ch_j "Fine, ask her and let me know in the morning."
                else:
                        $ JeanX.FaceChange("smile", 1)
                        ch_j "Lol, I bet she would. . ."  
                $ renpy.pop_call()
        
        "What she doesn't know won't hurt her.":
#                if not ApprovalCheck(JeanX, 1800, Bonus = -Cnt): #checks if Jean likes you more than the other girl
#                        $ JeanX.FaceChange("angry", 1)
#                        if not ApprovalCheck(JeanX, 1800):
#                                ch_j "Well it'd hurt me."
#                        else:
#                                ch_j "I don't like the sound of that."                    
#                        $ renpy.pop_call() 
#                else:
                        $ JeanX.FaceChange("smile", 1)
                        if JeanX.Love >= JeanX.Obed:
                                ch_j "True. . ."
                        elif JeanX.Obed >= JeanX.Inbt:
                                ch_j "Hmm. . ."
                        else:
                                ch_j "Lol, true."
                        $ JeanX.Traits.append("downlow")
                
        "I can break it off with her.":
                    $ JeanX.FaceChange("sad")
                    ch_j "Yeah, get on that."
                    $ renpy.pop_call()
            
        "You're right, I was dumb to ask.":
                    $ JeanX.FaceChange("sad")
                    ch_j "Definitely."                    
                    $ renpy.pop_call()                   
                
    return
    
    
label Jean_About(Check=0): #rkelj 
    if Check not in TotalGirls:
            ch_j "Who?"
            return
    ch_j "What do I think about [Check.Name]? Huh. . ."    
    if Check == RogueX:    
            if "poly Rogue" in JeanX.Traits:  
                ch_j "I mean, she's a pretty good lay. . ."    
            elif JeanX.LikeRogue >= 900:
                ch_j "She is kinda sexy. . ."
            elif JeanX.LikeRogue >= 800:
                ch_j "I don't know, she's fine. . ."    
            elif JeanX.LikeRogue >= 700:
                ch_j "She's good in class or something?"
            elif JeanX.LikeRogue >= 600:
                ch_j "She's the one with the white stripe, right?"
            elif JeanX.LikeRogue >= 500:
                ch_j "Who?"
            elif JeanX.LikeRogue >= 400:
                ch_j "I don't spend much time thinking about her."
            elif JeanX.LikeRogue >= 300:
                ch_j "She can go to hell." 
            else:
                ch_j "Bitch."
    elif Check == KittyX:    
            if "poly Kitty" in JeanX.Traits:  
                ch_j "I mean, she's a pretty good lay. . ."     
            elif JeanX.LikeKitty >= 900:
                ch_j "She is kinda cute. . ."
            elif JeanX.LikeKitty >= 800:
                ch_j "I don't know, she's fine. . ."    
            elif JeanX.LikeKitty >= 700:
                ch_j "She's, uh, a jock or something?"
            elif JeanX.LikeKitty >= 600:
                ch_j "she's the one with the tiny tits, right? Ghost girl?"
            elif JeanX.LikeKitty >= 500:
                ch_j "Who?"
            elif JeanX.LikeKitty >= 400:
                ch_j "I don't spend much time thinking about her."
            elif JeanX.LikeKitty >= 300:
                ch_j "She can go to hell." 
            else:
                ch_j "Bitch."
    elif Check == EmmaX:    
            if "poly Emma" in JeanX.Traits:  
                ch_j "I mean, she's an amazing lay. . ."    
            elif JeanX.LikeEmma >= 900:
                ch_j "She is pretty thicc. . ."
            elif JeanX.LikeEmma >= 800:
                ch_j "I don't know, she's fine. . ."     
            elif JeanX.LikeEmma >= 700:
                ch_j "She's prety hot, for an old."
            elif JeanX.LikeEmma >= 600:
                ch_j "She's the teacher, right?"
            elif JeanX.LikeEmma >= 500:
                ch_j "Who? Oh, the teacher, right?"
            elif JeanX.LikeEmma >= 400:
                ch_j "I could do with less of her attitude."
            elif JeanX.LikeEmma >= 300:
                ch_j "She needs to mind her business." 
            else:
                ch_j "Grrrrr."   
    elif Check == LauraX:    
            if "poly Laura" in JeanX.Traits:  
                ch_j "I mean, she's a pretty good lay. . ."    
            elif JeanX.LikeLaura >= 900:
                ch_j "She is pretty fit. . ."
            elif JeanX.LikeLaura >= 800:
                ch_j "I don't know, she's fine. . ."    
            elif JeanX.LikeLaura >= 700:
                ch_j "She's good in class or something?"
            elif JeanX.LikeLaura >= 600:
                ch_j "She's the one with the claws, right?"
            elif JeanX.LikeLaura >= 500:
                ch_j "Who?"
            elif JeanX.LikeLaura >= 400:
                ch_j "I don't spend much time thinking about her."
            elif JeanX.LikeLaura >= 300:
                ch_j "She can go to hell." 
            else:
                ch_j "Bitch."
    return    
#End Jean_AboutEmma   

label Jean_Monogamy:  #rkelj 
        #called from Jean_Settings to ask her not to hook up with other girls    
        menu:
            "Could you not hook up with other girls?" if "mono" not in JeanX.Traits:
                    if JeanX.Thirst >= 60 and not ApprovalCheck(JeanX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ JeanX.FaceChange("sly",1) 
                            if "mono" not in JeanX.DailyActions:                                                         
                                    $ JeanX.Statup("Obed", 90, -2) 
                            ch_j "Sorry, I've got plans later."
                            return
                    elif ApprovalCheck(JeanX, 1200, "LO", TabM=0) and JeanX.Love >= JeanX.Obed:
                            #she cares
                            $ JeanX.FaceChange("sly",1) 
                            if "mono" not in JeanX.DailyActions:                                                         
                                    $ JeanX.Statup("Love", 90, 1) 
                            ch_j "Oh, jealous?" 
                            ch_j "Ok, fine, but you owe me. . ."
                    elif ApprovalCheck(JeanX, 700, "O", TabM=0):
                            #she is obedient
                            $ JeanX.FaceChange("sly",1,Eyes="side") 
                            ch_j "Well. . . ok, fine."
                    else:   
                            #she doesn't care
                            $ JeanX.FaceChange("sly",1) 
                            ch_j "Ha!" 
                            return                       
                    if "mono" not in JeanX.DailyActions:                                                         
                            $ JeanX.Statup("Obed", 90, 3) 
                    $ JeanX.AddWord(1,0,"mono") #Daily
                    $ JeanX.Traits.append("mono")   
            "Don't hook up with other girls." if "mono" not in JeanX.Traits:
                    if ApprovalCheck(JeanX, 900, "O", TabM=0):
                            #she is obedient
                            $ JeanX.FaceChange("sly",1,Eyes="side")
                            ch_j "Well. . . ok, fine."
                    elif JeanX.Thirst >= 60 and not ApprovalCheck(JeanX, 1700, "LO", TabM=0):
                            #she's too thirsty
                            $ JeanX.FaceChange("sly",1) 
                            if "mono" not in JeanX.DailyActions:                                                         
                                    $ JeanX.Statup("Obed", 90, -2) 
                            ch_j "Sorry, I've got plans later."
                            return
                    elif ApprovalCheck(JeanX, 600, "O", TabM=0):
                            #she is obedient
                            $ JeanX.FaceChange("sly",1,Eyes="side") 
                            ch_j "Well. . . ok, fine."
                    elif ApprovalCheck(JeanX, 1400, "LO", TabM=0):
                            #she cares
                            $ JeanX.FaceChange("sly",1) 
                            ch_j "Oh, jealous?" 
                            ch_j "Ok, fine, but you owe me. . ."
                    else:   
                            #she doesn't care
                            $ JeanX.FaceChange("sly",1,Brows="confused") 
                            ch_j "Ha!" 
                            return                 
                    if "mono" not in JeanX.DailyActions:                                                         
                            $ JeanX.Statup("Obed", 90, 3) 
                    $ JeanX.AddWord(1,0,"mono") #Daily
                    $ JeanX.Traits.append("mono")   
            "It's ok if you hook up with other girls." if "mono" in JeanX.Traits:
                    if ApprovalCheck(JeanX, 700, "O", TabM=0):
                            $ JeanX.FaceChange("sly",1,Eyes="side") 
                            ch_j ". . . good."
                    elif ApprovalCheck(JeanX, 800, "L", TabM=0):
                            $ JeanX.FaceChange("sly",1) 
                            ch_j "Ok. . ." 
                    else:
                            $ JeanX.FaceChange("sly",1,Brows="confused") 
                            if "mono" not in JeanX.DailyActions:                                                         
                                    $ JeanX.Statup("Love", 90, -2)
                            ch_j "Good to know. . ." 
                    if "mono" not in JeanX.DailyActions:                                                         
                            $ JeanX.Statup("Obed", 90, 3) 
                    if "mono" in JeanX.Traits:
                            $ JeanX.Traits.remove("mono")   
                    $ JeanX.AddWord(1,0,"mono") #Daily
            "Never mind.":
                pass
        return
        
# end Jean monogamy <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

label Jean_Jumped: #rkelj 
        #called from Jean_Settings to ask her not to jump you  
        ch_p "Hey, Remember that time you threw yourself at me?" 
        $ JeanX.FaceChange("sly",1,Brows="confused") 
        ch_j "I'm not sure I'd put it like that, but. . . yeah?"
        menu:
            ch_j ". . . yeah?"
            "Could you maybe just ask instead?" if "chill" not in JeanX.Traits:
                    if JeanX.Thirst >= 60 and not ApprovalCheck(JeanX, 1500, "LO", TabM=0):
                            #she's too thirsty
                            $ JeanX.FaceChange("sly",1) 
                            if "chill" not in JeanX.DailyActions:                                                         
                                    $ JeanX.Statup("Obed", 90, -2) 
                            ch_j "Why waste the time?"
                            ch_j "It's not like you'd say \"no.\""
                            return
                    elif ApprovalCheck(JeanX, 1000, "LO", TabM=0) and JeanX.Love >= JeanX.Obed:
                            #she cares
                            $ JeanX.FaceChange("surprised",1) 
                            if "chill" not in JeanX.DailyActions:                                                         
                                    $ JeanX.Statup("Love", 90, 1) 
                            ch_j "I was really horny though. . ." 
                            $ JeanX.FaceChange("sly",1,Eyes="side") 
                            ch_j "I'll give it some thought. . ."
                    elif ApprovalCheck(JeanX, 500, "O", TabM=0):
                            #she is obedient
                            $ JeanX.FaceChange("sly",1,Eyes="side") 
                            ch_j "Maybe. . ."
                    else:   
                            #she doesn't care
                            $ JeanX.FaceChange("sly",1) 
                            ch_j "Why waste the time?"
                            ch_j "It's not like you'd say \"no.\""
                            return                    
                    if "chill" not in JeanX.DailyActions:                                                         
                            $ JeanX.Statup("Obed", 90, 3) 
                    $ JeanX.AddWord(1,0,"chill") #Daily
                    $ JeanX.Traits.append("chill")   
            "Don't bother me like that." if "chill" not in JeanX.Traits:
                    if ApprovalCheck(JeanX, 800, "O", TabM=0):
                            #she is obedient
                            $ JeanX.FaceChange("sly",1,Eyes="side") 
                            ch_j ". . . fine. . ."
                    elif JeanX.Thirst >= 60 and not ApprovalCheck(JeanX, 500, "O", TabM=0):
                            #she's too thirsty
                            $ JeanX.FaceChange("sly",1) 
                            if "chill" not in JeanX.DailyActions:                                                         
                                    $ JeanX.Statup("Obed", 90, -2) 
                            ch_j "Why waste the time?"
                            ch_j "It's not like you'd say \"no.\""
                            return
                    elif ApprovalCheck(JeanX, 400, "O", TabM=0):
                            #she is obedient
                            $ JeanX.FaceChange("sly",1,Eyes="side") 
                            ch_j "Well. . . ok. . ."
                    elif ApprovalCheck(JeanX, 500, "LO", TabM=0) and not ApprovalCheck(JeanX, 500, "I", TabM=0):
                            #she cares
                            $ JeanX.FaceChange("sly",1) 
                            ch_j "Rude." 
                            ch_j "I guess I cna try though. . ."
                    else:   
                            #she doesn't care
                            $ JeanX.FaceChange("sly",1) 
                            ch_j "Why waste the time?"
                            ch_j "It's not like you'd say \"no.\""
                            return                     
                    if "chill" not in JeanX.DailyActions:                                                         
                            $ JeanX.Statup("Obed", 90, 3) 
                    $ JeanX.AddWord(1,0,"chill") #Daily
                    $ JeanX.Traits.append("chill")   
            "Knock yourself out.":
                    if ApprovalCheck(JeanX, 800, "L", TabM=0):
                            $ JeanX.FaceChange("sly",1) 
                            ch_j "Heh, you know how I think. . ." 
                    elif ApprovalCheck(JeanX, 700, "O", TabM=0):
                            $ JeanX.FaceChange("sly",1,Eyes="side") 
                            ch_j "Good to know."
                    else:
                            $ JeanX.FaceChange("sly",1,Brows="confused") 
                            if "chill" not in JeanX.DailyActions:                                                         
                                    $ JeanX.Statup("Love", 90, -2)
                            ch_j "We'll see. . ." 
                    if "chill" not in JeanX.DailyActions:                                                         
                            $ JeanX.Statup("Obed", 90, 3) 
                    if "chill" in JeanX.Traits:
                            $ JeanX.Traits.remove("chill")  
                    $ JeanX.AddWord(1,0,"chill") #Daily 
            "Um, never mind.":
                pass
        return
        
# end Jean jumped <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# start laura hungry //////////////////////////////////////////////////////////
label Jean_Hungry: #rkelj 
    if JeanX.Chat[3]:
        ch_j "Hey, gimme a taste. . ."
    elif JeanX.Chat[2]:
        ch_j "Hey, I could use some of that. . . serum. . ."
    else:
        ch_j "I really like. . . your flavor. . ."
    $ JeanX.Traits.append("hungry")
return


# end laura hungry //////////////////////////////////////////////////////////

# Jean Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
label Jean_SexChat: #rkelj 
    $ Line = "Yeah, what did you want to talk about?" if not Line else Line
    while True:
            menu:
                ch_j "[Line]"                
                "My favorite thing to do is. . .":
                    if "setfav" in JeanX.DailyActions:
                        ch_j "I remember."
                    else:
                        menu:
                            "Sex.":
                                        $ JeanX.FaceChange("sly")
                                        if JeanX.PlayerFav == "sex":
                                            $ JeanX.Statup("Lust", 80, 5)
                                            ch_j "Yeah, I know that. . ."                                
                                        elif JeanX.Favorite == "sex":
                                            $ JeanX.Statup("Love", 90, 5)
                                            $ JeanX.Statup("Lust", 80, 10)
                                            ch_j "I really like it too!"
                                        elif JeanX.Sex >= 5:
                                            ch_j "Well I don't mind that."
                                        elif not JeanX.Sex:
                                            $ JeanX.FaceChange("perplexed")
                                            ch_j "Oh? Who with?"
                                        else:
                                            $ JeanX.FaceChange("bemused")
                                            ch_j "Heh, um, yeah, it's nice. . ."
                                        $ JeanX.PlayerFav = "sex"
                                        
                            "Anal.":
                                        $ JeanX.FaceChange("sly")
                                        if JeanX.PlayerFav == "anal":
                                            $ JeanX.Statup("Lust", 80, 5)
                                            ch_j "So you've said. . ."                                
                                        elif JeanX.Favorite == "anal":
                                            $ JeanX.Statup("Love", 90, 5)
                                            $ JeanX.Statup("Lust", 80, 10)
                                            ch_j "I love it too!"
                                        elif JeanX.Anal >= 10:
                                            ch_j "Yeah, it's. . . nice. . ."
                                        elif not JeanX.Anal:
                                            $ JeanX.FaceChange("perplexed")
                                            ch_j "Oh? Who with?"
                                        else:
                                            $ JeanX.FaceChange("bemused",Eyes="side")
                                            ch_j "Heh, heh, yeah, um, it's ok. . ."
                                        $ JeanX.PlayerFav = "anal"
                                        
                            "Blowjobs.":   
                                        $ JeanX.FaceChange("sly")
                                        if JeanX.PlayerFav == "blow":
                                            $ JeanX.Statup("Lust", 80, 3)
                                            ch_j "Yeah, I know."                                
                                        elif JeanX.Favorite == "blow":
                                            $ JeanX.Statup("Love", 90, 5)
                                            $ JeanX.Statup("Lust", 80, 5)
                                            ch_j "I can't say I hate it either. . ."
                                        elif JeanX.Blow >= 10:
                                            ch_j "Yeah, you're surprisingly tasty."
                                        elif not JeanX.Blow:
                                            $ JeanX.FaceChange("perplexed")
                                            ch_j "Oh? Who with?"
                                        else:
                                            $ JeanX.FaceChange("bemused")
                                            ch_j "You're lucky you taste so good."
                                        $ JeanX.PlayerFav = "blow"     
                                        
                            "Titjobs.":
                                        $ JeanX.FaceChange("sly")   
                                        if JeanX.PlayerFav == "titjob":
                                            $ JeanX.Statup("Lust", 80, 5)
                                            ch_j "Yeah, you've said that before. . ."                           
                                        elif JeanX.Favorite == "titjob":
                                            $ JeanX.Statup("Love", 90, 5)
                                            $ JeanX.Statup("Lust", 80, 7)
                                            ch_j "Yeah, I enjoy that too. . ."
                                        elif JeanX.Tit >= 10:
                                            ch_j "Nice, right?"
                                        elif not JeanX.Tit:
                                            $ JeanX.FaceChange("perplexed")
                                            ch_j "Oh? Who with?"
                                        else:
                                            $ JeanX.FaceChange("bemused")
                                            ch_j "They are pretty nice. . ."
                                            $ JeanX.Statup("Love", 80, 5)
                                            $ JeanX.Statup("Inbt", 50, 10)
                                        $ JeanX.PlayerFav = "titjob"   
                                        
                            "Footjobs.":
                                        $ JeanX.FaceChange("sly")
                                        if JeanX.PlayerFav == "foot":
                                            $ JeanX.Statup("Lust", 80, 5)
                                            ch_j "Yeah, you've said that. . ."                                 
                                        elif JeanX.Favorite == "foot":
                                            $ JeanX.Statup("Love", 90, 5)
                                            $ JeanX.Statup("Lust", 80, 7)
                                            ch_j "I do like using my feet. . ."
                                        elif JeanX.Foot >= 10:
                                            ch_j "I like it too . . ."
                                        elif not JeanX.Foot:
                                            $ JeanX.FaceChange("perplexed")
                                            ch_j "Oh? Who with?"
                                        else:
                                            $ JeanX.FaceChange("bemused")
                                            ch_j "Yeah, it's nice. . ."
                                        $ JeanX.PlayerFav = "foot"  
                                        
                            "Handjobs.":
                                        $ JeanX.FaceChange("sly")
                                        if JeanX.PlayerFav == "hand":
                                            $ JeanX.Statup("Lust", 80, 5)
                                            ch_j "Yeah, you've said that. . ."                                
                                        elif JeanX.Favorite == "hand":
                                            $ JeanX.Statup("Love", 90, 5)
                                            $ JeanX.Statup("Lust", 80, 7)
                                            ch_j "I do have quite the touch. . ."
                                        elif JeanX.Hand >= 10:
                                            ch_j "I like it too . . ."
                                        elif not JeanX.Hand:
                                            $ JeanX.FaceChange("perplexed")
                                            ch_j "Oh? Who with?"
                                        else:
                                            $ JeanX.FaceChange("bemused")
                                            ch_j "Yeah, it's nice. . ."
                                        $ JeanX.PlayerFav = "hand"  
                                        
                            "Feeling you up.":
                                        $ Cnt = JeanX.FondleB + JeanX.FondleT + JeanX.SuckB + JeanX.Hotdog
                                        $ JeanX.FaceChange("sly")
                                        if JeanX.PlayerFav == "fondle":
                                            $ JeanX.Statup("Lust", 80, 3)
                                            ch_j "Yeah, I think we're clear on that. . ."                                
                                        elif JeanX.Favorite in ("hotdog","suck breasts","fondle breasts","fondle thighs"):
                                            $ JeanX.Statup("Love", 90, 5)
                                            $ JeanX.Statup("Lust", 80, 5)
                                            ch_j "I love when you touch me. . ."
                                        elif Cnt >= 10:
                                            ch_j "Yeah, it's really nice . . ."
                                        elif not Cnt:
                                            $ JeanX.FaceChange("perplexed")
                                            ch_j "Oh? Who with?"
                                        else:
                                            $ JeanX.FaceChange("bemused")
                                            ch_j "I do like how that feels. . ."
                                        $ JeanX.PlayerFav = "fondle"  
                                        $ Cnt = 0
                                
                            "Kissing you.":
                                        $ JeanX.FaceChange("sly")
                                        if JeanX.PlayerFav == "kiss you":
                                            $ JeanX.Statup("Love", 90, 3)
                                            ch_j "Dork. . ."                                
                                        elif JeanX.Favorite == "kiss you":
                                            $ JeanX.Statup("Love", 90, 5)
                                            $ JeanX.Statup("Lust", 80, 5)
                                            ch_j "I. . . do too, ok? . ."
                                        elif JeanX.Kissed >= 10:
                                            ch_j "Yeah, it's fun . . ."
                                        elif not JeanX.Kissed:
                                            $ JeanX.FaceChange("perplexed")
                                            ch_j "Oh? Who with?"
                                        else:
                                            $ JeanX.FaceChange("bemused")
                                            ch_j "I do too. . ."
                                        $ JeanX.PlayerFav = "kiss you" 
                                
                        $ JeanX.DailyActions.append("setfav") 
                            
                "What's your favorite thing to do?":
                                if not ApprovalCheck(JeanX, 800):
                                        $ JeanX.FaceChange("perplexed")
                                        ch_j ". . ."                                    
                                else:
                                        if JeanX.SEXP >= 50:
                                            $ JeanX.FaceChange("perplexed")
                                            ch_j "You should know that by now. . ."   
                                        else:                 
                                            $ JeanX.FaceChange("bemused")
                                            $ JeanX.Eyes = "side"
                                            ch_j "Hmm. . ."
                                            
                                            
                                        if not JeanX.Favorite or JeanX.Favorite == "kiss":
                                            ch_j "Kissing?"  
                                        elif JeanX.Favorite == "anal":
                                                ch_j "Probably anal."  
                                        elif JeanX.Favorite == "lick ass":
                                                ch_j "When you lick my ass." 
                                        elif JeanX.Favorite == "insert ass":
                                                ch_j "Fingering my asshole, probably." 
                                        elif JeanX.Favorite == "sex":
                                                ch_j "Just stick it in me." 
                                        elif JeanX.Favorite == "lick pussy":
                                                ch_j "When you lick my pussy." 
                                        elif JeanX.Favorite == "fondle pussy":
                                                ch_j "When you finger me." 
                                        elif JeanX.Favorite == "blow":
                                                ch_j "I do like how your cock tastes. . ." 
                                        elif JeanX.Favorite == "tit":
                                                ch_j "When I use my tits." 
                                        elif JeanX.Favorite == "foot":
                                                ch_j "Footjobs are pretty fun." 
                                        elif JeanX.Favorite == "hand":
                                                ch_j "I like to jerk you off." 
                                        elif JeanX.Favorite == "hotdog":
                                                ch_j "When you grind against me." 
                                        elif JeanX.Favorite == "suck breasts":
                                                ch_j "When you suck my tits."  
                                        elif JeanX.Favorite == "fondle breasts":
                                                ch_j "When you massage my tits." 
                                        elif JeanX.Favorite == "fondle thighs":
                                                ch_j "When you massage my thighs."
                                        else:
                                                ch_j "I don't know, surprise me."    
                                                
                                # End Jean's favorite things.
                    
                "Don't talk as much during sex." if "vocal" in JeanX.Traits:
                        if "setvocal" in JeanX.DailyActions:
                                $ JeanX.FaceChange("perplexed")
                                ch_j "Don't jerk me around, [Girl.Petname]."
                        else:              
                            if ApprovalCheck(JeanX, 1000) and JeanX.Obed <= JeanX.Love:
                                $ JeanX.FaceChange("bemused")
                                $ JeanX.Statup("Obed", 90, 1)
                                ch_j ". . . fine."
                                $ JeanX.Traits.remove("vocal")   
                            elif ApprovalCheck(JeanX, 700, "O"):
                                $ JeanX.FaceChange("sadside")
                                $ JeanX.Statup("Obed", 90, 1)
                                ch_j ". . ."
                                $ JeanX.Traits.remove("vocal")   
                            elif ApprovalCheck(JeanX, 600):
                                $ JeanX.FaceChange("sly")
                                $ JeanX.Statup("Love", 90, -3)
                                $ JeanX.Statup("Obed", 50, -1)
                                $ JeanX.Statup("Inbt", 90, 5)
                                ch_j "Oh, I'll talk and you'll listen, [JeanX.Petname]."
                            else:
                                $ JeanX.FaceChange("angry")
                                $ JeanX.Statup("Love", 90, -5)
                                $ JeanX.Statup("Obed", 60, -3)
                                $ JeanX.Statup("Inbt", 90, 10)
                                ch_j "Yeah, that'll be the day. . ."
                                                
                            $ JeanX.DailyActions.append("setvocal")   
                "Talk dirty to me during sex." if "vocal" not in JeanX.Traits:
                        if "setvocal" in JeanX.DailyActions:
                                $ JeanX.FaceChange("perplexed")
                                ch_j "Don't jerk me around, [Girl.Petname]."
                        else:     
                            if ApprovalCheck(JeanX, 1000) and JeanX.Obed <= JeanX.Love:
                                $ JeanX.FaceChange("sly")
                                $ JeanX.Statup("Obed", 90, 2)
                                ch_j "I think that can be arranged. . ."
                                $ JeanX.Traits.append("vocal")   
                            elif ApprovalCheck(JeanX, 700, "O"):
                                $ JeanX.FaceChange("sadside")
                                $ JeanX.Statup("Obed", 90, 2)
                                ch_j "I'll see what I can do, [JeanX.Petname]."
                                $ JeanX.Traits.append("vocal")   
                            elif ApprovalCheck(JeanX, 600):
                                $ JeanX.FaceChange("sly")
                                $ JeanX.Statup("Obed", 90, 3)
                                ch_j "Sure, whatever."
                                $ JeanX.Traits.append("vocal")   
                            else:
                                $ JeanX.FaceChange("angry")
                                $ JeanX.Statup("Inbt", 90, 5)
                                ch_j ". . ."  
                                
                            $ JeanX.DailyActions.append("setvocal")  
                        # End Jean Dirty Talk
                    
                "Don't do your own thing as much during sex." if "passive" not in JeanX.Traits:
                        if "initiative" in JeanX.DailyActions:
                                $ JeanX.FaceChange("perplexed")
                                ch_j "Don't jerk me around, [Girl.Petname]."
                        else:       
                            if ApprovalCheck(JeanX, 1200) and JeanX.Obed <= JeanX.Love:
                                $ JeanX.FaceChange("bemused")
                                $ JeanX.Statup("Obed", 90, 1)
                                ch_j "Like me \"passive?\" I'll see what I can do. . ."     
                                $ JeanX.Traits.append("passive")                  
                            elif ApprovalCheck(JeanX, 700, "O"):
                                $ JeanX.FaceChange("sadside")
                                $ JeanX.Statup("Obed", 90, 1)
                                ch_j ". . . yeah, ok. . ."
                                $ JeanX.Traits.append("passive")
                            elif ApprovalCheck(JeanX, 600):
                                $ JeanX.FaceChange("sly")
                                $ JeanX.Statup("Love", 90, -3)
                                $ JeanX.Statup("Obed", 50, -1)
                                $ JeanX.Statup("Inbt", 90, 5)
                                ch_j "Hm, -NO.-"
                            else:
                                $ JeanX.FaceChange("angry")
                                $ JeanX.Statup("Love", 90, -5)
                                $ JeanX.Statup("Obed", 60, -3)
                                $ JeanX.Statup("Inbt", 90, 10)
                                ch_j "You wish."
                                
                            $ JeanX.DailyActions.append("initiative")  
                "Take more initiative during sex." if "passive" in JeanX.Traits:
                        if "initiative" in JeanX.DailyActions:
                                $ JeanX.FaceChange("perplexed")
                                ch_j "Don't jerk me around, [Girl.Petname]."
                        else:   
                            if ApprovalCheck(JeanX, 1000) and JeanX.Obed <= JeanX.Love:
                                $ JeanX.FaceChange("bemused")
                                $ JeanX.Statup("Obed", 90, 1)
                                ch_j "Damned right I will."    
                                $ JeanX.Traits.remove("passive")                   
                            elif ApprovalCheck(JeanX, 700, "O"):
                                $ JeanX.FaceChange("sadside")
                                $ JeanX.Statup("Obed", 90, 1)
                                ch_j ". . . fine. . ."
                                $ JeanX.Traits.remove("passive")    
                            elif ApprovalCheck(JeanX, 600):
                                $ JeanX.FaceChange("sly")
                                $ JeanX.Statup("Obed", 90, 3)
                                ch_j "Sure."
                                $ JeanX.Traits.remove("passive")  
                            else:
                                $ JeanX.FaceChange("angry")
                                $ JeanX.Statup("Inbt", 90, 5)
                                ch_j "Ugh, don't bother me with that, figure it out yourself."  
                                
                            $ JeanX.DailyActions.append("initiative")   
                                
                "About getting Jumped" if "jumped" in JeanX.History:
                        call Jean_Jumped
                
                "About that \"mind screen\"" if "screen" in JeanX.Traits or "noscreen" in JeanX.Traits:
                        ch_j "You mean how I can make Chuck ignore us a sometimes?"
                        menu:
                            extend ""
                            "Yeah, do that." if "noscreen" in JeanX.Traits:
                                ch_j "Nice. . ."
                                $ JeanX.Traits.append("screen")
                            "Don't do that anymore, I want him to know." if "screen" in JeanX.Traits:
                                ch_j "So naughty. . ."
                                if ApprovalCheck(JeanX, 900, "OI"):
                                        $ JeanX.FaceChange("sad")
                                        ch_j "Fine, I can leave it down."
                                        $ JeanX.FaceChange("bemused")
                                        $ JeanX.Traits.append("noscreen")
                                else:
                                        ch_j "Still, I don't like him bothering us."
                                        ch_j "I'll keep the screen up anyway."
                            "Never mind.":
                                pass                          
                #end mental screen talk  
                                
                "About that \"whammy\" you do?" if "whammy" in JeanX.Traits or "nowhammy" in JeanX.Traits:
                        ch_j "You mean how I mind wipe the other students so they don't know what a freak I am?"
                        menu:
                            extend ""
                            "That is so cool":
                                if "whammytalk" not in JeanX.Chat: 
                                        $ JeanX.Statup("Love", 60, 10)
                                        $ JeanX.Statup("Love", 90, 5)
                                        $ JeanX.Statup("Obed", 60, 10)
                                        $ JeanX.Statup("Obed", 80, 5)
                                        $ JeanX.Statup("Inbt", 90, 10)
                                ch_j "I know, right?"
                                $ JeanX.Chat.append("whammytalk")
                            "Yeah, can should start doing that again." if "nowhammy" in JeanX.Traits:
                                ch_j "Oh, well. . ."                                
                                if "Alpha" not in Player.Traits:
                                            #you haven't done the Plan Alpha yet
                                            $ JeanX.FaceChange("sad")
                                            ch_j "I'd love to, but Chuck'd have my ovaries over it. . ."                                        
                                elif ApprovalCheck(JeanX, 800, "I"): 
                                    if "whammytalk" not in JeanX.DailyActions: 
                                            $ JeanX.Statup("Love", 80, 10)
                                            $ JeanX.Statup("Obed", 60, 5)
                                            $ JeanX.Statup("Inbt", 90, 10)
                                    if not ApprovalCheck(JeanX, 800, "LO"):
                                            #she's sluttier than she likes you
                                            $ JeanX.FaceChange("sad")
                                            ch_j "Actually, I like it that way."
                                    else:
                                            #she's slutty but likes you enough to stop
                                            $ JeanX.FaceChange("sad")
                                            ch_j "Ok, fine. . ."
                                            $ JeanX.FaceChange("bemused")
                                            ch_j "I did kind of enjoy the thrill though. . ."
                                else:
                                            #she's not that slutty
                                            if "whammytalk" not in JeanX.DailyActions: 
                                                    $ JeanX.Statup("Love", 90, 5)
                                                    $ JeanX.Statup("Obed", 60, 3)
                                            ch_j "Ok, thanks. . ."
                                            $ JeanX.Traits.append("whammy")
                                $ JeanX.DailyActions.append("whammytalk")
                            "Don't do that anymore, I want them to remember." if "whammy" in JeanX.Traits:
                                if "whammytalk" not in JeanX.DailyActions: 
                                            $ JeanX.Statup("Obed", 60, 5)
                                            $ JeanX.Statup("Obed", 85, 5)
                                            $ JeanX.Statup("Inbt", 90, 10)
                                ch_j "Oh, well. . ." 
                                if ApprovalCheck(JeanX, 1500):
                                            $ JeanX.FaceChange("sad")
                                            ch_j "Ok, I guess I can. . ."
                                            $ JeanX.Traits.append("nowhammy")
                                else:
                                            $ JeanX.FaceChange("bemused")
                                            ch_j "Well too bad for you. . ."
                                $ JeanX.DailyActions.append("whammytalk")
                            "Never mind.":
                                pass                            
                #end Whammy talk
                
                "About when you masturbate":
                    call NoFap(JeanX)
                    
                "Never Mind" if Line == "Yeah, what did you want to talk about?":
                        return
                "That's all." if Line != "Yeah, what did you want to talk about?":
                        return
            if Line == "Yeah, what did you want to talk about?":
                $ Line = "Anything else?"
    return
# End Jean Sexchat <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


## Jean Chitchat /////////////////// #Work in progress
label Jean_Chitchat(O=0, Options = ["default","default","default"]): #rkel 
    $ Round -= 3 if Round > 3 else (Round-1)
    if O:                                               #adds only a specific option that was sent
        $ Options = [O]
    else:
        
        if JeanX not in Digits:
                if ApprovalCheck(JeanX, 500, "L") or ApprovalCheck(JeanX, 250, "I"):
                    ch_j "Oh, here's my number, gimme a call some time."
                    $ Digits.append(JeanX)  
                    return
                elif ApprovalCheck(JeanX, 250, "O"):
                    ch_j "I guess you should have my number. . ."             
                    $ Digits.append(JeanX)
                    return
                
        if "hungry" not in JeanX.Traits and (JeanX.Swallow + JeanX.Chat[2]) >= 10 and JeanX.Loc == bg_current:  #She's swallowed a lot        
                    call Jean_Hungry
                    return  
        
        if not Taboo or ApprovalCheck(JeanX, 800, "I"):
                    if JeanX.Loc == bg_current and JeanX.Thirst >= 30 and "refused" not in JeanX.DailyActions and "quicksex" not in JeanX.DailyActions: 
                            $ JeanX.FaceChange("sly",1)    
                            ch_j "I could use some stress relief, you busy?"
                            call Quick_Sex(JeanX)
                            return
#        $ Options = ["default","default","default"]
        #adds options based on accomplishments
#        if PunishmentX and "caught chat" not in JeanX.DailyActions:
#            $ Options.append("caught")
        if JeanX.Event[0] and "key" not in JeanX.Chat:
            $ Options.append("key")
              
        if "mandrill" in Player.Traits and "cologne chat" not in JeanX.DailyActions:
            $ Options.append("mandrill")        
        if "purple" in Player.Traits and "cologne chat" not in JeanX.DailyActions:
            $ Options.append("purple")        
        if "corruption" in Player.Traits and "cologne chat" not in JeanX.DailyActions:
            $ Options.append("corruption")
                    
        if JeanX.Date >= 1:
            #if you've dated before
            $ Options.append("dated")
#        if "cheek" in JeanX.DailyActions and "cheek" not in JeanX.Chat:
#            #If you've touched her cheek today
#            $ Options.append("cheek")
        if JeanX.Kissed >= 5:
            #if you've kissed a few times
            $ Options.append("kissed")
        if "dangerroom" in Player.DailyActions:
            #If you've been in the danger room today
            $ Options.append("dangerroom")
        if "showered" in JeanX.DailyActions:
            #If you've caught Jean showering today
            $ Options.append("showercaught")
        if "fondle breasts" in JeanX.DailyActions or "fondle pussy" in JeanX.DailyActions or "fondle ass" in JeanX.DailyActions:
            #If you've fondled Jean today
            $ Options.append("fondled")
        if "Dazzler and Longshot" in JeanX.Inventory and "256 Shades of Grey" in JeanX.Inventory and "Avengers Tower Penthouse" in JeanX.Inventory:   
            #If you've given Jean the books
            if "book" not in JeanX.Chat:
                $ Options.append("booked")
        if "lace bra" in JeanX.Inventory or "lace panties" in JeanX.Inventory:   
            #If you've given Jean the lingerie
            if "lingerie" not in JeanX.Chat:
                $ Options.append("lingerie")
        if JeanX.Hand:   
            #If Jean's given a handjob
            $ Options.append("handy")
        if JeanX.Swallow:   
            #If Jean's swallowed before
            $ Options.append("swallowed")
        if "cleaned" in JeanX.DailyActions or "painted" in JeanX.DailyActions:
            #If Jean's been facialed
            $ Options.append("facial")
        if JeanX.Sleep:
            #If Jean's slept over
            $ Options.append("sleep")
        if JeanX.CreamP or JeanX.CreamA:
            #If Jean's been creampied
            $ Options.append("creampie")
        if JeanX.Sex or JeanX.Anal:
            #If Jean's been sexed
            $ Options.append("sexed")
        if JeanX.Anal:
            #If Jean's been analed
            $ Options.append("anal")
            
        if "seenpeen" in JeanX.History:
            $ Options.append("seenpeen")  
        if "topless" in JeanX.History:
            $ Options.append("topless")  
        if "bottomless" in JeanX.History:
            $ Options.append("bottomless")  
                    
        if not ApprovalCheck(JeanX, 300):            #She dislikes you
            $ Options.append("hate") 
    
    $ renpy.random.shuffle(Options)             #shuffles options and picks out the first one
    
    if Options[0] == "mandrill":                             
        $ JeanX.DailyActions.append("cologne chat") 
        $ JeanX.FaceChange("confused")
        ch_j "(sniff, sniff). . . have you been fucking Hank? . ."
        $ JeanX.FaceChange("sexy", 2)
        ch_j ". . . still, you do smell kinda good. . ."    
    elif Options[0] == "purple":              
        $ JeanX.DailyActions.append("cologne chat") 
        $ JeanX.FaceChange("sly",1)
        ch_j "(sniff, sniff). . . what is that? . ."
        $ JeanX.FaceChange("normal",0)
        ch_j ". . . what was it you wanted?"    
    elif Options[0] == "corruption":              
        $ JeanX.DailyActions.append("cologne chat") 
        $ JeanX.FaceChange("confused")
        ch_j "(sniff, sniff). . . that's a strong scent. . ."
        $ JeanX.FaceChange("angry")
        ch_j ". . . a dangerous scent. . ."
        $ JeanX.FaceChange("sly")
                
    elif Options[0] == "caught": # Xavier's caught you
            $ JeanX.FaceChange("angry")
            if "caught chat" in JeanX.Chat:
                    ch_j "That asshole Chuck."
                    ch_j "I'm tired of him sticking his nose in where it doesn't belong."                            
            else:   
                    ch_j "That asshole Chuck."
                    ch_j "I'm tired of him sticking his nose in where it doesn't belong."
                    $ JeanX.FaceChange("surprised")
                    ch_j "Oh!"
                    $ JeanX.FaceChange("sly")
                    ch_j "I've got an idea." 
                    ch_j "I could use my own powers to jam out his a little bit, make it more likely that he'll ignore us."
                    menu:
                        "Sure, that sounds good.":
                            ch_j "Excellent. . ."
                            $ JeanX.Traits.append("screen")
                        "Nah, I want him to know.":
                            ch_j "Heh, you're naughty."
                            if ApprovalCheck(JeanX, 900, "OI"):
                                    $ JeanX.FaceChange("sad")
                                    ch_j "Ok, fine, we won't do that."
                                    $ JeanX.FaceChange("bemused")
                                    $ JeanX.Traits.append("noscreen")
                            else:
                                    ch_j "Still, I don't like him sticking his nose in."
                                    ch_j "I think I'll use the screen anyway."
                                    $ JeanX.Traits.append("screen")
                    $ JeanX.Chat.append("caught chat") 
    elif Options[0] == "key": # you have her key
            if JeanX.SEXP <= 15:
                ch_j "Don't use that key too freely. . ."
            else:
                ch_j "You have my key, but don't visit enough. . ."
            $ JeanX.Chat.append("key") 
        
#    elif Options[0] == "cheek":
#            #Jean's response to having her cheek touched.
#            ch_j "So,[JeanX.Petname]. . .y'know how you[JeanX.like]kinda just brushed my cheek before?"
#            ch_p "Yeah?  Was that okay?"
#            $ JeanX.FaceChange("smile",1)
#            ch_j "More than just {i}okay{/i}."
#            $ JeanX.Chat.append("cheek") 
                                                
    elif Options[0] == "dated":
            #Jean's response to having gone on a date with the Player.
            ch_j "I had fun the other night, we should do that again some time."

    elif Options[0] == "kissed":
            #Jean's response to having been kissed by the Player.
            $ JeanX.FaceChange("normal",1)
            ch_j "I have to say, you are a good kisser, [JeanX.Petname]."
            menu:
                extend ""
                "Hey. . .I'm the best there is at what I do.":
                        $ JeanX.FaceChange("smile",1)
                        ch_j "I've heard that one before. . ."
                "No. You think?":
                        ch_j "I wouldn't say it otherwise."

    elif Options[0] == "dangerroom":
            #Jean's response to Player working out in the Danger Room while Jean is present
            $ JeanX.FaceChange("sly",1)
            ch_j "Hey,[JeanX.Petname]. I saw you in the Danger Room, earlier."
            ch_j "You're going surprisingly well for someone with your. . . limitations."

    elif Options[0] == "showercaught":
            #Jean's response to being caught in the shower.
            if "shower" in JeanX.Chat: 
                ch_j "I saw you in the showers again. . ."                       
            else:
                ch_j "So do you always just bust into the showers?"            
                $ JeanX.Chat.append("shower") 
                menu:
                    extend ""
                    "It was a total accident! I promise!":             
                            $ JeanX.Statup("Love", 50, 5)    
                            $ JeanX.Statup("Love", 90, 2) 
                            if ApprovalCheck(JeanX, 1200):
                                $ JeanX.FaceChange("sly",1)
                                ch_j "Well, it's not like I minded."
                            $ JeanX.FaceChange("smile")
                            ch_j "I guess we can all make mistakes. . ."
                    "Just with you.":        
                            $ JeanX.Statup("Obed", 40, 5)   
                            if ApprovalCheck(JeanX, 1000) or ApprovalCheck(JeanX, 700, "L"):      
                                    $ JeanX.Statup("Love", 90, 3)    
                                    $ JeanX.FaceChange("sly",1)
                                    ch_j "Oh, a charmer. . ."
                            else:                
                                    $ JeanX.Statup("Love", 70, -5) 
                                    $ JeanX.FaceChange("angry")
                                    ch_j "I'll bet. . ."                                                       
                    "Totally on purpose. I regret nothing.":
                            if ApprovalCheck(JeanX, 800):                          
                                    $ JeanX.Statup("Obed", 60, 5)            
                                    $ JeanX.Statup("Inbt", 50, 5) 
                                    $ JeanX.FaceChange("perplexed",2)
                                    ch_j "fair"
                                    $ JeanX.Blush = 1
                            else:                
                                    $ JeanX.Statup("Love", 50, -10) 
                                    $ JeanX.Statup("Love", 80, -10)          
                                    $ JeanX.Statup("Obed", 50, 10)  
                                    $ JeanX.FaceChange("angry")
                                    ch_j "Perv."

    elif Options[0] == "fondled":
            #Jean's response to being felt up.
            if JeanX.FondleB + JeanX.FondleP + JeanX.FondleA >= 15:
                ch_j "Hey, give me a nice, hard, rubdown. . ." 
            else:                
                ch_j "Hey, gimme another massage. . . "
                ch_j ". . . the good kind. . ." 

    elif Options[0] == "booked":
            #Jean's response after a Player gives her the books from the shop.
            ch_j "Hey, I read those books you gave me."
            menu:
                extend ""
                "Yeah?  Did you like them?":
                        $ JeanX.FaceChange("sly",2)
                        ch_j "They were pretty hot."
                "Good.  You looked like you could use to learn a thing or two from them.":  
                        $ JeanX.Statup("Obed", 70, 5)            
                        $ JeanX.Statup("Inbt", 50, 5) 
                        $ JeanX.FaceChange("angry")
                        ch_j "Yeah right."                
            $ JeanX.Blush = 1
            $ JeanX.Chat.append("book") 

    elif Options[0] == "lingerie":
            #Jean's response to being given lingerie.
            $ JeanX.FaceChange("sly",2)
            ch_j "I really enjoy those silky underthings you got me. . ."
            $ JeanX.Blush = 1
            $ JeanX.Chat.append("lingerie") 

    elif Options[0] == "handy":
            #Jean's response after giving the Player a handjob.
            $ JeanX.FaceChange("sly",1)
            ch_j "I was thinking about your cock in my hand. . ."
            ch_j "I think we should do that again some time. . ."
            $ JeanX.Blush = 0

    elif Options[0] == "blow":
            if "blow" not in JeanX.Chat:
                    #Jean's response after giving the Player a blowjob.
                    $ JeanX.FaceChange("sly",2)
                    ch_j "Hey, so did you enjoy that blowjob?"
                    menu:
                        extend ""
                        "You were totally amazing.":                            
                                    $ JeanX.Statup("Love", 90, 5)            
                                    $ JeanX.Statup("Obed", 60, 15)          
                                    $ JeanX.Statup("Inbt", 60, 10) 
                                    $ JeanX.FaceChange("normal",1)
                                    ch_j "You know it."
                                    $ JeanX.FaceChange("sexy",1)
                                    ch_j "I wouldn't mind having another taste. . ."
                        "Honestly? It was good. . .but you could use a little practice, I think.":
                                if ApprovalCheck(JeanX, 300, "I") or not ApprovalCheck(JeanX, 800):                     
                                    $ JeanX.Statup("Love", 90, -5)          
                                    $ JeanX.Statup("Obed", 60, 10)            
                                    $ JeanX.Statup("Inbt", 50, 10) 
                                    $ JeanX.FaceChange("perplexed",1)
                                    ch_j "Really? I'd never gotten any complaints before. . ."
                                else:                              
                                    $ JeanX.Statup("Obed", 70, 15)            
                                    $ JeanX.Statup("Inbt", 50, 5) 
                                    $ JeanX.FaceChange("sexy",1)
                                    ch_j "You just don't know quality when you feel it."                                  
                        "I guess. If you're into weird sounds and too much teeth. Spoiler, I'm not.":                     
                                $ JeanX.Statup("Love", 90, -10)          
                                $ JeanX.Statup("Obed", 60, -5)   
                                $ JeanX.FaceChange("angry",2)
                                ch_j "You just don't know quality."
                    $ JeanX.Blush = 1
                    $ JeanX.Chat.append("blow") 
            else:
                    $ Line = renpy.random.choice(["I gotta tell you, your dick tastes great.", 
                            "I think I nearly dislocated my jaw last time.", 
                            "Let me know if you'd like another blowjob sometime.",
                            "Hmmm. . . [she mimes her tongue knocking against her cheek.]"])
                    ch_j "[Line]"

    elif Options[0] == "swallowed":
            #Jean's response after swallowing the Player's cum.
            if "swallow" in JeanX.Chat:                
                ch_j "Hey, I wouldn't mind another taste. . ."
            else:
                ch_j "Hey. . . the other day. . ."
                ch_j "Your jiz tasted really good."
                ch_j "Like -really- good." 
                $ JeanX.FaceChange("sly",1)
                ch_j "Weird."
                $ JeanX.Chat.append("swallow") 

    elif Options[0] == "facial":
            #Jean's response after taking a facial from the Player.
            ch_j "Ok, so. . ."
            ch_j "You know how you came on my face?"
            $ JeanX.FaceChange("sexy",2)
            ch_j "That just felt -so- good for some reason. . ."
            $ JeanX.Blush = 1

    elif Options[0] == "sleepover":
            #Jean's response after sleeping with the Player.
            ch_j "I really enjoyed the other night."
            ch_j "I really enjoyed the company."

    elif Options[0] == "creampie":
            #Another of Jean's responses after having sex with the Player.
            "[JeanX.Name] draws close to you so she can whisper into your ear."
            ch_j "I still ave some of you spilling out of me. . ."

    elif Options[0] == "sexed":
            #A final response from Jean after having sex with the Player.
            ch_j "So. . . you should know. . ."
            $ JeanX.FaceChange("sexy",2)
            ch_j ". . .lately when I've been schlicking. . ."
            ch_j "I've been thinking about you inside of me."
            $ JeanX.Blush = 1

    elif Options[0] == "anal":
            #Jean's response after getting anal from the Player.
            $ JeanX.FaceChange("sly")
            ch_j "I'm not much of a fan of anal."
            $ JeanX.FaceChange("sexy",1)
            ch_j "Still, with you it's pretty fun."
        
    elif Options[0] == "seenpeen": # first seen peen skipped
            $ JeanX.FaceChange("sly",1, Eyes="down")  
            ch_j "Oh, I forgot to mention, congrats on that package you're swinging. . ."
            $ JeanX.FaceChange("bemused",1)  
            $ JeanX.Statup("Love", 50, 5) 
            $ JeanX.Statup("Love", 60, 10) 
            $ JeanX.History.remove("seenpeen")  
    elif Options[0] == "topless": # first seen breasts skipped
            ch_j "So you got a good look at my tits earlier, Pretty great, right?"
            call Jean_First_TMenu
            $ JeanX.History.remove("topless")  
    elif Options[0] == "bottomless": # first seen pussy skipped
            ch_j "So you got a good look at my pussy earlier, not bad, right?"
            call Jean_First_BMenu
            $ JeanX.History.remove("bottomless")  
            
#    elif Options[0] == "boyfriend?":
#        call Jean_BF
#    elif Options[0] == "lover?":
#        call Jean_Love
#    elif Options[0] == "sir?":
#        call Jean_Sub
#    elif Options[0] == "master?":
#        call Jean_Master
#    elif Options[0] == "sexfriend?":
#        call Jean_Sexfriend
#    elif Options[0] == "fuckbuddy?":
#        call Jean_Fuckbuddy 
#    elif Options[0] == "daddy?":
#        call Jean_Daddy  
        
    elif Options[0] == "hate": # trinty lower then 50:
        $ Line = renpy.random.choice(["Get away from me.", 
                "I don't want to smell you near me.", 
                "Back off.",
                "Buzz off."])
        ch_j "[Line]"
        
    else: #all else fell through. . .
            ch_j "Oh, did you have something interesting to say?"
            
#            $ D20 = renpy.random.randint(1, 15)        
#            if D20 == 1:
#                    $ JeanX.FaceChange("smile")
#                    ch_j "I got a good grade on that bio test."
#            elif D20 == 2:
#                    $ JeanX.FaceChange("annoyed")
#                    ch_j "If I have to hear him say \"I'm the best there is\" one more time, I swear I'm going ..."
#            elif D20 == 3:
#                    $ JeanX.FaceChange("surprised")
#                    ch_j "Huh? Oh, sorry. I sort of spaced out. That's not like me."
#            elif D20 == 4:
#                    $ JeanX.FaceChange("sad")
#                    ch_j "Oh, [JeanX.Petname]. I was just remembering something. Don't worry about it."
#            elif D20 == 5:
#                    $ JeanX.FaceChange("smile")
#                    ch_j "I had a good nap. It's nice to be somewhere I can just doze off without worry."
#            elif D20 == 6:
#                    $ JeanX.FaceChange("perplexed")
#                    ch_j "Oh, [JeanX.Petname]. I think I just saw Emma Frost staring at Cyclops. That's... wierd."
#            elif D20 == 7:
#                    $ JeanX.FaceChange("smile")
#                    ch_j "I just got a new personal best time in the Danger Room."
#            elif D20 == 8:
#                    $ JeanX.FaceChange("sad")
#                    ch_j "I like being here, but sometimes there's just so much noise..."
#            elif D20 == 9:
#                    $ JeanX.FaceChange("confused")
#                    ch_j "I'm still trying to figure out what the mystery meat in the cafeteria was today."
#                    ch_j "I have enhanced senses, this shouldn't be so difficult!"
#            elif D20 == 10:
#                    $ JeanX.FaceChange("smile")
#                    ch_j "Kitty, Rogue and some of the others asked me if I wanted to go grab some ice cream with them tomorrow."
#            elif D20 == 11:
#                    $ JeanX.FaceChange("smile")
#                    ch_j "I tried out a dance class like Kitty said. Apparently I'm good at it."
#            elif D20 == 12:
#                    $ JeanX.FaceChange("sad")
#                    ch_j "I like talking to Kitty and the others. It makes me feel, I don't know. . ."
#                    ch_j "{i}not{/i} like a really dangerous mutant who could kill everyone around me if I flipped out."
#            elif D20 == 13:
#                    $ JeanX.FaceChange("smile")
#                    ch_j "Kitty and Rogue dared me to call Logan \"Dad\". I think we might've given him a heart attack."
#            elif D20 == 14:
#                    $ JeanX.FaceChange("sad")
#                    ch_j "I like going out on missions, but catching up with what's been going on while I'm gone is always a pain."
#            elif D20 == 15:
#                    $ JeanX.FaceChange("perplexed")
#                    ch_j "So they're called the \"Avengers\", but do they ever do any avenging?"
#                    ch_j "At least the Fantastic Four really do things that are strange and fantastic."
#            elif D20 == 16:
#                    $ JeanX.FaceChange("perplexed")
#                    ch_j "Have you ever been to New York? Sometimes I'm surprised anyone still wants to live there."
#            elif D20 == 17:
#                    $ JeanX.FaceChange("perplexed")
#                    ch_j "Logan just walked up and told me that if I ever meet someone called. . ."
#                    ch_j "\"Dead...Poole?\"...I should just go ahead and stab him in the face."
#                    ch_j "What's up with that?"
#            elif D20 == 18:
#                    $ JeanX.FaceChange("smile")
#                    ch_j "Don't tell anyone this, but I think Cyclops is kind of wound up tight."
#            elif D20 == 19:
#                    $ JeanX.FaceChange("confused")
#                    ch_j "Do you smell something? Is that... nachos and... chocolate syrup?!"
#            elif D20 == 20:
#                    $ JeanX.FaceChange("smile")
#                    ch_j "I like being able to just talk about nothing in particular. It's... nice."
#            else:
#                    $ JeanX.FaceChange("smile")
#                    ch_j "You're fun to hang with."
        
    $ Line = 0
    return

# start Jean_Names//////////////////////////////////////////////////////////
label Jean_Names:     #rkelj 
    menu:
        ch_j "Oh? What would you like me to call you?"
        "My initial's fine.":            
            $ JeanX.Petname = Player.Name[:1]  #fix test this
            ch_j "You got it, [JeanX.Petname]."
        "Call me by my name.":
            if Player.Name in JeanX.Petnames:                
                    $ JeanX.Petname = Player.Name
                    ch_j "Sure, [JeanX.Petname]."
            else:
                    ch_j "Sure, [JeanX.Petname]."
                    menu:
                        extend ""
                        "Fine, whatever.":
                                pass
                        "No, my -real- name, [Player.Name].":
                                if ApprovalCheck(JeanX, 700, "LO"): 
                                        $ JeanX.Petname = Player.Name
                                        $ JeanX.Petnames.append(Player.Name)
                                        ch_j "Ok, fine, I'mm remember that one. . . [JeanX.Petname]."
                                else:                 
                                        call JeanName(1) #picks a random new name
                                        ch_j "Right, right. . . [JeanX.Petname]!"
                                        menu:
                                            extend ""
                                            "Fine, whatever.":
                                                    pass
                                            "No, [Player.Name]!":
                                                    call JeanName #picks a random new name
                                                    ch_j "Ok, don't shout. . . [JeanX.Petname], got it."
            #end real name
        "Call me \"boyfriend\"." if "boyfriend" in JeanX.Petnames:
            $ JeanX.Petname = "boyfriend"
            ch_j ". .  . ok, [JeanX.Petname]."
        "Call me \"lover\"." if "lover" in JeanX.Petnames:
            $ JeanX.Petname = "lover"
            ch_j ". . ."
            ch_j ". . . ok, [JeanX.Petname]."
        "Call me \"sir\"." if "sir" in JeanX.Petnames:
            $ JeanX.Petname = "sir"
            ch_j "Lol, sure, [JeanX.Petname]."
        "Call me \"master\"." if "master" in JeanX.Petnames:
            $ JeanX.Petname = "master"
            ch_j "Um. . yes, [JeanX.Petname]."
        "Call me \"sex friend\"." if "sex friend" in JeanX.Petnames:
            $ JeanX.Petname = "sex friend"
            ch_j "Lol, ok, [JeanX.Petname]."
        "Call me \"fuck buddy\"." if "fuck buddy" in JeanX.Petnames:
            $ JeanX.Petname = "fuck buddy"
            ch_j "Heh, ok, [JeanX.Petname]."        
        "Call me \"daddy\"." if "daddy" in JeanX.Petnames:
            $ JeanX.Petname = "daddy"
            ch_j "Hmm. . . [JeanX.Petname]."   
        "Nevermind.":
            return
    return
# end Jean_Names//////////////////////////////////////////////////////////

label Jean_Pet: #rkelj 
    while True:
        menu:
            extend ""
            "Polite":
                menu:
                    extend ""
                    "I think I'll just call you Jean.":
                        $ JeanX.Pet = "Jean"
                        ch_j "Ok."
                                                
                    "I think I'll call you \"girl\".":
                        $ JeanX.Pet = "girl"
                        if "boyfriend" in JeanX.Petnames or ApprovalCheck(JeanX, 600, "L"):
                            $ JeanX.FaceChange("sexy", 1) 
                            ch_j "Yeah, ok, [JeanX.Petname]."
                        else:      
                            $ JeanX.FaceChange("angry")           
                            ch_j "I'm NOT your girl, [JeanX.Petname]." 
                            
                    "I think I'll call you \"boo\".":
                        $ JeanX.Pet = "boo"
                        if "boyfriend" in JeanX.Petnames or ApprovalCheck(JeanX, 700, "L"):
                            $ JeanX.FaceChange("sexy", 1) 
                            ch_j "I guess I am your boo, [JeanX.Petname]."
                        else:     
                            $ JeanX.FaceChange("angry")            
                            ch_j "I'm NOT your boo,  [JeanX.Petname]."
                            
                    "I think I'll call you \"bae\".":
                        $ JeanX.Pet = "bae"
                        if "boyfriend" in JeanX.Petnames or ApprovalCheck(JeanX, 600, "L"):
                            $ JeanX.FaceChange("sexy", 1) 
                            ch_j "I guess I am your bae, [JeanX.Petname]."
                        else:     
                            $ JeanX.FaceChange("angry")            
                            ch_j "I'm NOT your bae,  [JeanX.Petname]."
                            
                    "I think I'll call you \"baby\".":
                        $ JeanX.Pet = "baby"
                        if "boyfriend" in JeanX.Petnames or ApprovalCheck(JeanX, 500, "L"):
                            $ JeanX.FaceChange("sexy", 1) 
                            ch_j "Cute, [JeanX.Petname]."
                        else:     
                            $ JeanX.FaceChange("angry")            
                            ch_j "I am not a baby." 
                            
                            
                    "I think I'll call you \"sweetie\".":
                        $ JeanX.Pet = "sweetie"
                        if "boyfriend" in JeanX.Petnames or ApprovalCheck(JeanX, 600, "L"):
                            ch_j "Sounds good, [JeanX.Petname]."
                        else:     
                            $ JeanX.FaceChange("angry", 1)            
                            ch_j "Too sweet, [JeanX.Petname]."
                            
                    "I think I'll call you \"sexy\".":
                        $ JeanX.Pet = "sexy"
                        if "lover" in JeanX.Petnames or ApprovalCheck(JeanX, 800):
                            $ JeanX.FaceChange("sexy", 1) 
                            ch_j "You know it, [JeanX.Petname]."
                        else:        
                            $ JeanX.FaceChange("angry", 1)         
                            ch_j "True, but a little rude, [JeanX.Petname]."  
                            
                    "I think I'll call you \"lover\".":
                        $ JeanX.Pet = "lover"
                        if "lover" in JeanX.Petnames or ApprovalCheck(JeanX, 1200):
                            $ JeanX.FaceChange("sexy", 1) 
                            ch_j "Heh, ok."
                        else:      
                            $ JeanX.FaceChange("angry", 1)           
                            ch_j "I don't think so, [JeanX.Petname]."  
                    
                    "Back":
                        pass
            
            "Risky":
                menu:                        
                    "I think I'll call you \"slave\".":
                        $ JeanX.Pet = "slave"
                        if "master" in JeanX.Petnames or ApprovalCheck(JeanX, 800, "O"):
                            $ JeanX.FaceChange("bemused", 1) 
                            ch_j ". . . ok, [JeanX.Petname]."
                        else:      
                            $ JeanX.FaceChange("angry", 1)           
                            ch_j "I am not your slave, [JeanX.Petname]."
                                            
                    "I think I'll call you \"pet\".":
                        $ JeanX.Pet = "pet"
                        if "master" in JeanX.Petnames or ApprovalCheck(JeanX, 650, "O"):
                            $ JeanX.FaceChange("bemused", 1) 
                            ch_j ". . . fine, [JeanX.Petname]."
                        else:             
                            $ JeanX.FaceChange("angry", 1)    
                            ch_j "I'm not your -pet,- [JeanX.Petname]."
                            
                    "I think I'll call you \"slut\".":
                        $ JeanX.Pet = "slut"
                        if "sex friend" in JeanX.Petnames or ApprovalCheck(JeanX, 900, "OI"):
                            $ JeanX.FaceChange("sexy") 
                            ch_j "Well. . . yeah."
                        else:                
                            $ JeanX.FaceChange("angry", 1) 
                            $ JeanX.Mouth = "surprised"
                            ch_j "How attached are you to having a vocabulary?" 
                            
                    "I think I'll call you \"whore\".":
                        $ JeanX.Pet = "whore"
                        if "fuckbuddy" in JeanX.Petnames or ApprovalCheck(JeanX, 1000, "OI"):
                            $ JeanX.FaceChange("sly") 
                            ch_j ". . ."
                        else:        
                            $ JeanX.FaceChange("angry", 1)         
                            ch_j "You'd better not. . ." 
                                                   
                    "I think I'll call you \"sugartits\".":
                        $ JeanX.Pet = "sugartits"
                        if "sex friend" in JeanX.Petnames or ApprovalCheck(JeanX, 1400):
                            $ JeanX.FaceChange("sly", 1) 
                            ch_j ". . . ok."
                        else:     
                            $ JeanX.FaceChange("angry", 1)            
                            ch_j "Not cool." 
                            
                    "I think I'll call you \"sex friend\".":
                        $ JeanX.Pet = "sex friend"
                        if "sex friend" in JeanX.Petnames or ApprovalCheck(JeanX, 600, "I"):
                            $ JeanX.FaceChange("sly") 
                            ch_j "Yeah. . ."
                        else:                
                            $ JeanX.FaceChange("angry", 1) 
                            ch_j "Keep it down, [JeanX.Petname]." 
                            
                    "I think I'll call you \"fuckbuddy\".":
                        $ JeanX.Pet = "fuckbuddy"
                        if "fuckbuddy" in JeanX.Petnames or ApprovalCheck(JeanX, 700, "I"):
                            $ JeanX.FaceChange("sly") 
                            ch_j "Yup."
                        else:                
                            $ JeanX.FaceChange("angry", 1)
                            $ JeanX.Mouth = "surprised"
                            ch_j "Don't even joke, [JeanX.Petname]." 
                        
                    "I think I'll call you \"baby girl\".":
                        $ JeanX.Pet = "baby girl"
                        if "daddy" in JeanX.Petnames or ApprovalCheck(JeanX, 1200):
                            $ JeanX.FaceChange("smile", 1) 
                            ch_j "I guess?"
                        else:                
                            $ JeanX.FaceChange("angry", 1) 
                            ch_j "Weirdo." 
                            
                    "Back":
                        pass
                    
            "Nevermind.":
                return
    return
    
#label Jean_Namecheck(JeanX.Pet = JeanX.Pet, Cnt = 0, Ugh = 0): #replaced with $ Girl.NameCheck() #checks reaction to petname
  
  
# start Jean_Rename//////////////////////////////////////////////////////////
label Jean_Rename:   #rkelj 
        #Sets alternate names from Jean
        $ JeanX.Mouth = "smile"
        ch_j "Yeah?"
        menu:
            extend ""
            "I think \"Jean's\" a pretty name." if JeanX.Name != "Jean" and "Jean" in JeanX.Names:
                    $ JeanX.Name = "Jean"
                    ch_j "Well, yeah. I like it."
            "Nevermind.":
                    pass                    
        $ JeanX.AddWord(1,0,"namechange")
        return
# end Jean_Rename//////////////////////////////////////////////////////////


# start Jean_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
label Jean_Personality(Cnt = 0):    #rkelj 
    if not JeanX.Chat[4] or Cnt:
        "Since you're doing well in one area, you can convince Jean to focus on one of the others."
        "Any time you go over the limit in a given stat, the excess will spill over into the chosen stat instead."
        "This will also impact which personality trait takes priority in dialog."
    menu:
        ch_j "Yeah?"
        "More Obedient. [[Love to Obedience]" if JeanX.Love > 900:
            ch_p "If you really love me, could you please just do what I say?"
            ch_j "Oh, fine, I'll try. . ."
            $ JeanX.Chat[4] = 1
        "Less Inhibited. [[Love to Inhibition]" if JeanX.Love > 900:
            ch_p "If you really love me, could lighten up a bit, just have some fun?"
            ch_j "Oh, you like it kinky then? . ."
            $ JeanX.Chat[4] = 2
        
        "Less Inhibited. [[Obedience to Inhibition]" if JeanX.Obed > 900:
            ch_p "I want you to be less inhibited."
            ch_j "I'll give it a try. . ."
            $ JeanX.Chat[4] = 3
        "More Loving. [[Obedience to Love]" if JeanX.Obed > 900:
            ch_p "I'd like you to learn to love me."
            ch_j "Well. . . ok. . ."
            $ JeanX.Chat[4] = 4
            
        "More Obedient. [[Inhibition to Obedience]" if (JeanX.Inbt - JeanX.IX) > 900:
            ch_p "I know we're having fun, but couldn't you listen to me sometimes?"
            ch_j "Hmm. . . kinky. . ."
            $ JeanX.Chat[4] = 5
            
        "More Loving. [[Inhibition to Love]" if (JeanX.Inbt - JeanX.IX) > 900:
            ch_p "I know we're having fun, but do you even care about me?"
            ch_j "Oh, fine. . ."
            $ JeanX.Chat[4] = 6
            
        "I guess just do what you like. . .[[reset]" if JeanX.Chat[4]:
            ch_p "You know what we talked about before? Nevermind that stuff."
            ch_j "Um, sure. . ."
            $ JeanX.Chat[4] = 0
        "Repeat the rules":
            $ Cnt = 1
            jump Jean_Personality
        "Nevermind.":
            return
    return
# end Jean_Personality / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /




# Jean_Summon / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Jean_Summon(Tempmod=Tempmod): #rkelj 
    $ JeanX.OutfitChange()  
    if "no summon" in JeanX.RecentActions:
                if "angry" in JeanX.RecentActions:
                    ch_j "Go away!"
                elif JeanX.RecentActions.count("no summon") > 1:
                    ch_j "Give me some space!"
                    $ JeanX.RecentActions.append("angry") 
#                elif Current_Time == "Night": 
#                    ch_j "Like I said, it's too late for that."
                else:
                    ch_j "I told you I'm busy!"   
                $ JeanX.RecentActions.append("no summon")
                return
                           
    $ D20 = renpy.random.randint(1, 20) 
    $ Line = 0
    if JeanX.Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = -10
    elif JeanX.Loc == "bg jean":    
        $ Tempmod = -10
    elif JeanX.Loc == "bg showerroom":    
        $ Tempmod = -30
        
    if D20 <= 3:                                                                        
        #unlucky refusal
        $ Line = "no"       
    if Current_Time == "Night": 
                if ApprovalCheck(JeanX, 500, "L") or ApprovalCheck(JeanX, 400, "O"):                             
                        #It's night time but she likes you.
                        ch_j "You're up too? Yeah, that's fine."
                        $ JeanX.Loc = bg_current 
                        call Set_The_Scene
                else:                                                           
                        #It's night time and she isn't into you
                        ch_j "I'd rather not. . ."       
                        $ JeanX.RecentActions.append("no summon")         
                return                  
    elif "les" in JeanX.RecentActions:
            #if she's with another girl. . .
            if ApprovalCheck(JeanX, 2000):
                    ch_j "I'm getting off with one of the girls. Wanna come over?"
                    menu:
                        extend ""
                        "Sure":
                            $ Line = "go to"
                        "No thanks.":
                            ch_j "Heh, ok. . ."
                            return
            else:            
                    ch_j "I'm a little. . . tied up at the moment."   
                    ch_j "We can talk later."      
                    $ JeanX.RecentActions.append("no summon") 
                    return   
    elif not ApprovalCheck(JeanX, 700, "L") or not ApprovalCheck(JeanX, 600, "O"):                       
        #It's not night time, but she's busy 
        if not ApprovalCheck(JeanX, 300):
                ch_j "I'm busy, [JeanX.Petname]."       
                $ JeanX.RecentActions.append("no summon")         
                return    
            
            
        if "summoned" in JeanX.RecentActions:
                pass
        elif "goto" in JeanX.RecentActions:
                ch_j "You just left. . ."
        elif JeanX.Loc == "bg classroom":
                ch_j "I'm in class right now."
        elif JeanX.Loc == "bg dangerroom": 
                ch_j "I'm in the Danger Room, [JeanX.Petname]."    
        elif JeanX.Loc == "bg campus": 
                ch_j "I'm relaxing in the quad right now." 
        elif JeanX.Loc == "bg jean": 
                ch_j "I'm in my room, [JeanX.Petname]." 
        elif JeanX.Loc == "bg player": 
                ch_j "I'm in your room, [JeanX.Petname], where are you?"   
        elif JeanX.Loc == "bg showerroom":    
            if ApprovalCheck(JeanX, 1600):
                ch_j "I'm in the shower right now."
            else:            
                ch_j "I'm in the shower right now, [JeanX.Petname]." 
                ch_j "Don't come knocking."
                $ JeanX.RecentActions.append("no summon")         
                return      
        elif JeanX.Loc == "hold":
                ch_j "I'm busy at the moment."       
                $ JeanX.RecentActions.append("no summon") 
                return      
        else:        
                ch_j "Why don't you come to me?"    
           
           
        if "summoned" in JeanX.RecentActions:
            ch_j "Again? Ok, fine."           
            $ Line = "yes"            
        elif "goto" in JeanX.RecentActions:
            menu:
                extend ""
                "You're right, be right back.":
                                ch_j "Ok then."
                                $ Line = "go to"                    
                "Nah, it's better here.":    
                                ch_j "Ok then."                    
                "But I'd {i}really{/i} like to see you over here.":
                        if ApprovalCheck(JeanX, 600, "L") or ApprovalCheck(JeanX, 1400):
                                $ Line = "lonely"
                        else: 
                                $ Line = "no"                        
                "I said come over here.":
                        if ApprovalCheck(JeanX, 600, "O"):                                    
                                #she is obedient
                                $ Line = "command"                        
                        elif D20 >= 7 and ApprovalCheck(JeanX, 1400):                         
                                #she is generally favorable 
                                ch_j "Well. . ."              
                                $ Line = "yes"                        
                        elif ApprovalCheck(JeanX, 200, "O"):                                  
                                #she is not obedient  
                                ch_j "Whatever."    
                        else:                                                                   
                                #she is obedient, but you failed to meet the checks                     
                                $ Line = "no" 
        else:  
            menu:
                extend ""
                "Ok, I'll be right there.":
                    $ JeanX.Statup("Love", 55, 1) 
                    $ JeanX.Statup("Inbt", 30, 1)
                    ch_j "Good."
                    $ Line = "go to"
                    
                "Ok, we can talk later then.":
                    $ JeanX.Statup("Obed", 50, 1)                            
                    $ JeanX.Statup("Obed", 30, 2)
                    ch_j "Ok."
                    
                "Could you please come visit me? I'm lonely.":
                    if ApprovalCheck(JeanX, 650, "L") or ApprovalCheck(JeanX, 1500):
                        $ JeanX.Statup("Love", 70, 1)                   
                        $ JeanX.Statup("Obed", 50, 1)
                        $ Line = "lonely"
                    else: 
                        $ JeanX.Statup("Inbt", 30, 1)
                        $ Line = "no"
                        ch_j "Needy much?"
                        
                "Come on, it'll be fun.":
                    if ApprovalCheck(JeanX, 400, "L") and ApprovalCheck(JeanX, 800):
                        $ JeanX.Statup("Love", 70, 1)                   
                        $ JeanX.Statup("Obed", 50, 1)
                        $ Line = "fun"
                    else: 
                        $ JeanX.Statup("Inbt", 30, 1)
                        $ Line = "no"
                        
                "I said come over here.":
                    if ApprovalCheck(JeanX, 600, "O"):                              
                        #she is obedient
                        $ JeanX.Statup("Love", 50, 1, 1)    
                        $ JeanX.Statup("Love", 40, -1)                
                        $ JeanX.Statup("Obed", 90, 1)    
                        $ Line = "command"
                        
                    elif D20 >= 7 and ApprovalCheck(JeanX, 1500):       
                        #she is generally favorable
                        $ JeanX.Statup("Love", 70, -2)  
                        $ JeanX.Statup("Love", 90, -1)  
                        $ JeanX.Statup("Obed", 50, 2)                                
                        $ JeanX.Statup("Obed", 90, 1)  
                        ch_j "Ok, fine."              
                        $ Line = "yes"
                        
                    elif ApprovalCheck(JeanX, 200, "O"):                                         
                        #she is not obedient   
                        $ JeanX.Statup("Love", 60, -4)  
                        $ JeanX.Statup("Love", 90, -3)   
                        ch_j "And I said \"no.\""                             
                        $ JeanX.Statup("Inbt", 40, 2)
                        $ JeanX.Statup("Inbt", 60, 1)    
                        $ JeanX.Statup("Obed", 70, -3)
                        ch_j "I'm staying here."                    
                    else:                                                                   
                        #she is obedient, but you failed to meet the checks
                        $ JeanX.Statup("Inbt", 30, 1)
                        $ JeanX.Statup("Inbt", 50, 1)                                    
                        $ JeanX.Statup("Love", 50, -1, 1)
                        $ JeanX.Statup("Obed", 70, -1)  
                        $ Line = "no" 
                    #end "ordered"
    else:                                                                               
        #automatic acceptance
        if JeanX.Love > JeanX.Obed:
            ch_j "Ok, fine."
        else:
            ch_j "Ok, if you insist. . ."
        $ Line = "yes" 
        
    $ Tempmod = 0
    
    if not Line:                                                                        
            #You end the dialog neutrally               
            $ JeanX.RecentActions.append("no summon")         
            return
        
    if Line == "no":                                                                    
            # She's refused, context based dialog
            ch_j "Sorry, [JeanX.Petname], I'm kinda busy."          
            $ JeanX.RecentActions.append("no summon")         
            return
        
    elif Line == "go to":                                                                 
            #You agreed to go to her instead        
            $ renpy.pop_call()
            $ JeanX.RecentActions.append("goto")  
            $ Player.RecentActions.append("goto")  
            $ Line = 0
            if JeanX.Loc == "bg classroom":
                    ch_j "Ok then."
                    jump Class_Room 
            elif JeanX.Loc == "bg dangerroom": 
                    ch_j "I'll try not to finish the exercise myself."
                    jump Danger_Room
            elif JeanX.Loc == "bg jean":    
                    ch_j "Don't keep me waiting."
                    jump Jean_Room
            elif JeanX.Loc == "bg player": 
                    ch_j "Don't keep me waiting."
                    jump Player_Room                
            elif JeanX.Loc == "bg showerroom": 
                    ch_j "I'll see you then."
                    jump Shower_Room
            elif JeanX.Loc == "bg campus": 
                    ch_j "Ok."
                    jump Campus            
            elif JeanX.Loc in PersonalRooms: 
                    ch_j "Yeah, see you."
                    $ bg_current = JeanX.Loc
                    jump Misplaced
            else:
                    ch_j "Um, I'll just meet you in my room."
                    $ JeanX.Loc = "bg jean"
                    jump Jean_Room
            
    #She's agreed to come over    
    elif Line == "lonely":
            ch_j "Oh. . . fine. . ."
    elif Line == "command": 
            ch_j "Fine, [JeanX.Petname]."
        
    $ JeanX.RecentActions.append("summoned")  
    $ Line = 0
    if "locked" in Player.Traits:
            call Locked_Door(JeanX)
            return                 
    $ JeanX.Loc = bg_current 
    call Taboo_Level(0)
    $ JeanX.OutfitChange()
    call Set_The_Scene
    return

# End Jean Summon  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /


label Jean_Leave(Tempmod=Tempmod, GirlsNum = 0):   #rkelj       
    if "leaving" in JeanX.RecentActions:
        $ JeanX.DrainWord("leaving")
    else:
        return
    
    if JeanX.Loc == "hold":   
            # Activates if she's being moved out of play
            ch_j "Ok, I've got work to do, apparently." 
            return
            
    if JeanX in Party or "lockedtravels" in JeanX.Traits:           
            #If she's in your party or if you've told her not to leave you
            #It resets her to your location
            $ JeanX.Loc = bg_current 
            return
      
    elif "freetravels" in JeanX.Traits or not ApprovalCheck(JeanX, 700):
            #If you've told her to go wherever, or she just doesn't care what you think.   
            $ JeanX.OutfitChange()           
            if GirlsNum: #if someone left before her
                        ch_j "I'm leaving too."
                        
            if JeanX.Loc == "bg classroom":
                        ch_j "I've got class."
            elif JeanX.Loc == "bg dangerroom": 
                        ch_j "I'm getting some exercise."   
            elif JeanX.Loc == "bg campus": 
                        ch_j "I'm taking a break in the quad." 
            elif JeanX.Loc == "bg laura": 
                        ch_j "I'm going back to my room." 
            elif JeanX.Loc == "bg player": 
                        ch_j "I'm hanging out in your room for a bit."   
            elif JeanX.Loc == "bg pool": 
                        ch_j "I going to hit the pool."  
            elif JeanX.Loc == "bg showerroom":    
                if ApprovalCheck(JeanX, 1400):
                        ch_j "I'm hitting the showers."
                else:            
                        ch_j "I'm headed out."
            else:        
                        ch_j "I'm headed out."   
            hide Jean_Sprite
            return     
            #End Free Travels
    
    if bg_current == "bg dangerroom":   
            call Gym_Clothes("exit")
            
    $ JeanX.OutfitChange()  
    
    if "follow" not in JeanX.Traits:
            # Sets a key to show that she's asked you to follow her at least once
            $ JeanX.Traits.append("follow")   
        
    $ D20 = renpy.random.randint(1, 20) 
    $ Line = 0
    # Sets her preferences
    if JeanX.Loc == "bg classroom": #fix change these if changed function
        $ Tempmod = 10
    elif JeanX.Loc == "bg showerroom":    
        $ Tempmod = 40
    
    
    if GirlsNum: #if someone left before her
                ch_j "Yeah, I'm headed out too."
                
    if JeanX.Loc == "bg classroom":
        ch_j "I've got class."
    elif JeanX.Loc == "bg dangerroom": 
        ch_j "I've got some Danger Room time scheduled."    
    elif JeanX.Loc == "bg campus": 
        ch_j "I'm hanging out on the quad." 
    elif JeanX.Loc == "bg jean": 
        ch_j "I'm headed back to my room." 
    elif JeanX.Loc == "bg player": 
        ch_j "I'm going to hang out in your room for a bit."   
    elif JeanX.Loc == "bg showerroom":    
        if ApprovalCheck(JeanX, 1600):
            ch_j "I'm hitting the showers."
        else:            
            ch_j "I'm hitting the showers, maybe hang back for a bit."
            return      
    elif JeanX.Loc == "bg pool": 
            ch_j "I was hitting the pool."   
    else:       
            ch_j "Are you coming with?"    
    
    
    menu:
        extend ""
        "Ok, I'll catch up.":
                if "followed" not in JeanX.RecentActions:
                    $ JeanX.Statup("Love", 55, 1) 
                    $ JeanX.Statup("Inbt", 30, 1)
                $ Line = "go to"
            
        "Ok, we can talk later.":
                if "followed" not in JeanX.RecentActions:
                    $ JeanX.Statup("Obed", 50, 1)                            
                    $ JeanX.Statup("Obed", 30, 2)
                ch_j "Fine, whatever."
            
        "Could you please stay with me? I'll get lonely.":
                if ApprovalCheck(JeanX, 650, "L") or ApprovalCheck(JeanX, 1500):                
                    if "followed" not in JeanX.RecentActions:
                        $ JeanX.Statup("Love", 70, 1)                   
                        $ JeanX.Statup("Obed", 50, 1)
                    $ Line = "lonely"
                else: 
                    if "followed" not in JeanX.RecentActions:
                        $ JeanX.Statup("Inbt", 30, 1)
                    $ Line = "no"
                    ch_j "Needy much?"
                
        "Come on, it'll be fun.":
                if ApprovalCheck(JeanX, 400, "L") and ApprovalCheck(JeanX, 800):
                    $ JeanX.Statup("Love", 70, 1)                   
                    $ JeanX.Statup("Obed", 50, 1)
                    $ Line = "fun"
                else: 
                    $ JeanX.Statup("Inbt", 30, 1)
                    $ Line = "no"
                        
        "No, stay here.":
                if ApprovalCheck(JeanX, 600, "O"):                              
                    #she is obedient
                    if "followed" not in JeanX.RecentActions: 
                        $ JeanX.Statup("Love", 40, -2)                
                        $ JeanX.Statup("Obed", 90, 1)    
                    $ Line = "command"
                    
                elif D20 >= 7 and ApprovalCheck(JeanX, 1400):       
                    #she is generally favorable
                    if "followed" not in JeanX.RecentActions:
                        $ JeanX.Statup("Love", 70, -2)  
                        $ JeanX.Statup("Love", 90, -1)  
                        $ JeanX.Statup("Obed", 50, 2)                                
                        $ JeanX.Statup("Obed", 90, 1)  
                    ch_j ". . . Fine."              
                    $ Line = "yes"
                    
                elif ApprovalCheck(JeanX, 200, "O"):                                         
                    #she is not obedient                   
                    if "followed" not in JeanX.RecentActions:
                        $ JeanX.Statup("Love", 70, -4)  
                        $ JeanX.Statup("Love", 90, -2)   
                    ch_j "You're not the boss of me."  
                    if "followed" not in JeanX.RecentActions:                       
                        $ JeanX.Statup("Inbt", 40, 2)
                        $ JeanX.Statup("Inbt", 60, 1)    
                        $ JeanX.Statup("Obed", 70, -2)
                    ch_j "Ha!"                    
                else:                                                                  
                    #she is obedient, but you failed to meet the checks                  
                    if "followed" not in JeanX.RecentActions:
                        $ JeanX.Statup("Inbt", 30, 1)
                        $ JeanX.Statup("Inbt", 50, 1)                                    
                        $ JeanX.Statup("Love", 50, -1, 1)                               
                        $ JeanX.Statup("Love", 90, -2)
                        $ JeanX.Statup("Obed", 70, -1)  
                    $ Line = "no" 
                #End ordered to stay
                    
    call Taboo_Level(0)
    $ JeanX.RecentActions.append("followed")     
    if not Line:                                                                        
            #You end the dialog neutrally      
            hide Jean_Sprite
            call Gym_Clothes("change", [JeanX])
            return
    
    if Line == "no":                                                                    
            # She's refused, context based dialog
            ch_j "I'd rather not."         
            hide Jean_Sprite
            call Gym_Clothes("change", [JeanX])         
            return
        
    elif Line == "go to":                                                                 
            #You agreed to go to her instead  
            $ Tempmod = 0
            $ Line = 0
            call DrainAll("leaving")
            call DrainAll("arriving")       
            hide Jean_Sprite
            call Gym_Clothes("change", [JeanX])
            if JeanX.Loc == "bg classroom":
                ch_j "Ok."            
                jump Class_Room_Entry
            elif JeanX.Loc == "bg dangerroom": 
                ch_j "I'll get warmed up."
                jump Danger_Room_Entry
            elif JeanX.Loc == "bg jean": 
                ch_j "Ok."
                jump Jean_Room
            elif JeanX.Loc == "bg player": 
                ch_j "Good."
                jump Player_Room                
            elif JeanX.Loc == "bg showerroom": 
                ch_j "Ok, nice."
                jump Shower_Room_Entry
            elif JeanX.Loc == "bg campus": 
                ch_j "Ok."
                jump Campus_Entry
            elif JeanX.Loc == "bg pool": 
                ch_j "Cool."
                jump Pool_Entry
            else:            
                ch_j "I'll just meet you in your room."
                $ JeanX.Loc = "bg player"
                jump Player_Room
            #End "goto" where she's at
            
    #She's agreed to come over    
    elif Line == "lonely":
            ch_j "Well, I guess. . ."
    elif Line == "command": 
            ch_j "Fine, [JeanX.Petname]. . ."
    
    $ Line = 0
    ch_j "I'll stick around."                                
    $ JeanX.Loc = bg_current 
    return

# End Jean Leave / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 

### Jean's Clothes  / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /

label Jean_Clothes:    #rkelj 
    if JeanX.Taboo:
            if "exhibitionist" in JeanX.Traits:
                ch_j "Yeah? . ."  
            elif ApprovalCheck(JeanX, 900, TabM=4) or ApprovalCheck(JeanX, 400, "I", TabM=3): 
                ch_j "Oh, I guess we could. . ."
            else:
                ch_j "I think this is kind of exposed. . ."
                ch_j "Can we talk about this in our rooms?"
                return
    elif ApprovalCheck(JeanX, 900, TabM=4) or ApprovalCheck(JeanX, 600, "L") or ApprovalCheck(JeanX, 300, "O"):
                ch_j "Oh? What about them?"
    else:
                ch_j "Just enjoy, don't advise."
                return
                     
    if Girl != JeanX:
            #This culls returns if sent from another girl
            $ renpy.pop_call()     
    $ Girl = JeanX   
    call Shift_Focus(Girl)
        
label Jean_Wardrobe_Menu: 
    $ JeanX.FaceChange()
    $ Trigger = 1 # to prevent Focus swapping. . .   
    while True:
        menu:
            ch_j "What about my clothes?"      
            "Overshirts":
                        call Jean_Clothes_Over        
            "Legwear":
                        call Jean_Clothes_Legs
            "Underwear":
                        call Jean_Clothes_Under
            "Accessories":
                        call Jean_Clothes_Misc                    
            "Outfit Management":
                        call Jean_Clothes_Outfits                      
            "Let's talk about what you wear around.":
                        call Clothes_Schedule(JeanX)
                
            "Could I get a look at it?" if JeanX.Loc != bg_current:
                    # checks to see if she'll drop the screen
                    call OutfitShame(JeanX,0,2) 
                    if _return:                    
                        show PhoneSex zorder 150
                        ch_j "Nice, right?"
                    hide PhoneSex
            "Could I get a look at it?" if renpy.showing('DressScreen'):
                    # checks to see if she'll drop the screen
                    call OutfitShame(JeanX,0,2) 
                    if _return:
                        hide DressScreen
            "Would you be more comfortable behind a screen? (locked)" if JeanX.Taboo:
                    pass
            "Would you be more comfortable behind a screen?" if JeanX.Loc == bg_current and not JeanX.Taboo and not renpy.showing('DressScreen'):
                    # checks to see if she wants a screen
                    if ApprovalCheck(JeanX, 1500) or (JeanX.SeenChest and JeanX.SeenPussy):
                            ch_j "I don't see why."
                    else:
                            show DressScreen zorder 150
                            ch_j "Yeah, this'll work."
                            
            "Switch to. . .":
                    if renpy.showing('DressScreen'):
                            call OutfitShame(JeanX,0,2) 
                            if _return:
                                hide DressScreen
                            else:
                                $ JeanX.OutfitChange()  
                    $ JeanX.Set_Temp_Outfit() #sets current outfit as temporary
                    $ Trigger = 0
                    call Switch_Chat
                    if Girl != JeanX:
                            ch_p "I wanted to talk about your clothes."
                            call expression Girl.Tag +"_Clothes"
                    $ Girl = JeanX
                    call Shift_Focus(Girl)
                            
            "Never mind, you look good like that.":
                    if "wardrobe" not in JeanX.RecentActions: 
                            #Apply stat boosts only if it's the first time this turn 
                            if JeanX.Chat[1] <= 1:                
                                    $ JeanX.Statup("Love", 70, 15)
                                    $ JeanX.Statup("Obed", 40, 20)
                                    ch_j "Of course?"
                            elif JeanX.Chat[1] <= 10:
                                    $ JeanX.Statup("Love", 70, 5)
                                    $ JeanX.Statup("Obed", 40, 7)
                                    ch_j "Right?" 
                            elif JeanX.Chat[1] <= 50:
                                    $ JeanX.Statup("Love", 70, 1)
                                    $ JeanX.Statup("Obed", 40, 1)  
                                    ch_j "Uh-huh."
                            else:
                                    ch_j "Sure."                    
                            $ JeanX.RecentActions.append("wardrobe") 
                    if renpy.showing('DressScreen'):
                            call OutfitShame(JeanX,0,2) 
                            if _return:
                                hide DressScreen
                            else:
                                $ JeanX.OutfitChange()  
                    $ JeanX.Set_Temp_Outfit() #sets current outfit as temporary  
                    $ JeanX.Chat[1] += 1   
                    $ Trigger = 0             
                    return
               
        #Loops back up 
        #return #jump Jean_Clothes
        #End of Jean Wardrobe Main Menu
        
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Jean_Clothes_Outfits:                                                                               
        # Outfits
        "You should remember that one. [[Set Custom]":
                menu:
                    "Which slot would you like this saved in?"
                    "Custom 1":
                                call OutfitShame(JeanX,3,1)
                    "Custom 2":
                                call OutfitShame(JeanX,5,1)
                    "Custom 3":
                                call OutfitShame(JeanX,6,1)
                    "Gym Clothes":
                                call OutfitShame(JeanX,4,1)
                    "Sleepwear":
                                call OutfitShame(JeanX,7,1)
                    "Swimwear":
                                call OutfitShame(JeanX,10,1)
                    #8 is Emma's teaching clothes, 
                    "Never mind":
                                pass
                                
        "Pink shirt and pants outfit": 
                $ JeanX.OutfitChange("casual1")   
                menu:
                    "You should wear this one out. [[set current outfit]":
                            $ JeanX.Outfit = "casual1"
                            $ JeanX.Shame = 0
                            ch_j "Yeah, I've worn this one a long time."
                    "Let's try something else though.":
                            ch_j "Sure. . ."            
                    
        "Green t-shirt and skirt outfit":  
                $ JeanX.OutfitChange("casual2")
                menu:
                    "You should wear this one out. [[set current outfit]":
                            $ JeanX.Outfit = "casual2"
                            $ JeanX.Shame = 0
                            ch_j "Ok, this one has a real \"classic\" feel. . ."
                    "Let's try something else though.":
                            ch_j "Sure. . ."            
                    
        "Remember that outfit we put together? [[Set a custom outfit] (locked)" if not JeanX.Custom1[0] and not JeanX.Custom2[0] and not JeanX.Custom3[0]:
                        pass       
                        
        "Remember that outfit we put together?" if JeanX.Custom1[0] or JeanX.Custom2[0] or JeanX.Custom3[0]: 
                $ Cnt = 0
                while 1:
                    menu:                
                        "Throw on Custom 1 (locked)" if not JeanX.Custom1[0]:
                                pass
                        "Throw on Custom 1" if JeanX.Custom1[0]:
                                $ JeanX.OutfitChange("custom1")
                                $ Cnt = 3
                        "Throw on Custom 2 (locked)" if not JeanX.Custom2[0]:
                                pass
                        "Throw on Custom 2" if JeanX.Custom2[0]:
                                $ JeanX.OutfitChange("custom2")
                                $ Cnt = 5
                        "Throw on Custom 3 (locked)" if not JeanX.Custom3[0]:
                                pass
                        "Throw on Custom 3" if JeanX.Custom3[0]:
                                $ JeanX.OutfitChange("custom3")
                                $ Cnt = 6
                        
                        "You should wear this one in private. (locked)" if not Cnt:
                                pass
                        "You should wear this one in private." if Cnt:
                                if Cnt == 5:
                                    $ JeanX.Clothing[9] = "custom2"
                                elif Cnt == 6:
                                    $ JeanX.Clothing[9] = "custom3"
                                else:
                                    $ JeanX.Clothing[9] = "custom1"
                                ch_j "Ok, sure."
                        
                        "On second thought, forget about that one outfit. . .":
                                menu:
                                    "Custom 1 [[clear custom 1]" if JeanX.Custom1[0]:
                                        ch_j "Ok."
                                        $ JeanX.Custom1[0] = 0
                                    "Custom 1 [[clear custom 1] (locked)" if not JeanX.Custom1[0]:
                                        pass
                                    "Custom 2 [[clear custom 2]" if JeanX.Custom2[0]:
                                        ch_j "Ok."
                                        $ JeanX.Custom2[0] = 0
                                    "Custom 2 [[clear custom 2] (locked)" if not JeanX.Custom2[0]:
                                        pass
                                    "Custom 3 [[clear custom 3]" if JeanX.Custom3[0]:
                                        ch_j "Ok."
                                        $ JeanX.Custom3[0] = 0
                                    "Custom 3 [[clear custom 3] (locked)" if not JeanX.Custom3[0]:
                                        pass
                                    "Never mind, [[back].":
                                        pass                                               
                                                
                        "You should wear this one out. [[choose outfit first](locked)" if not Cnt:
                                pass
                        "You should wear this one out." if Cnt:
                                call Custom_Out(JeanX,Cnt)
                        "Ok, back to what we were talking about. . .":
                                $ Cnt = 0
                                return #jump Jean_Clothes                  
        
        "Gym Clothes?" if not JeanX.Taboo or bg_current == "bg dangerroom":
                $ JeanX.OutfitChange("gym")
            
        "Sleepwear?" if not JeanX.Taboo:
                if ApprovalCheck(JeanX, 1200):
                        $ JeanX.OutfitChange("sleep")
                else:
                        call Display_DressScreen(JeanX)
                        if _return:
                            $ JeanX.OutfitChange("sleep")
                                        
        "Swimwear? (locked)" if (JeanX.Taboo and bg_current != "bg pool") or not JeanX.Swim[0]:
                $ JeanX.OutfitChange("swimwear")   
        "Swimwear?" if (not JeanX.Taboo or bg_current == "bg pool") and JeanX.Swim[0]:
                $ JeanX.OutfitChange("swimwear")
            
        "Your birthday suit looks really great. . .":                                     
                #Nude
                $ JeanX.FaceChange("sexy", 1)
                $ Line = 0
                if not JeanX.Chest and not JeanX.Panties and not JeanX.Over and not JeanX.Legs and not JeanX.Hose:                
                    ch_j "Duh."  
                elif JeanX.SeenChest and JeanX.SeenPussy and ApprovalCheck(JeanX, 1200, TabM=4):
                    ch_j "You know it. . ."  
                    $ Line = 1
                elif ApprovalCheck(JeanX, 2000, TabM=4):
                    ch_j "Oh, going right for it, huh?"    
                    $ Line = 1
                elif JeanX.SeenChest and JeanX.SeenPussy and ApprovalCheck(JeanX, 1200, TabM=0):
                    ch_j "You know it, but maybe not right here. . ."  
                elif ApprovalCheck(JeanX, 2000, TabM=0):
                    ch_j "Maybe, but not here. . ."  
                elif ApprovalCheck(JeanX, 1000, TabM=0):                
                    $ JeanX.FaceChange("confused", 1,Mouth="smirk")
                    ch_j "Yeah, but I'm not sharing."
                    $ JeanX.FaceChange("bemused", 0)
                else:
                    $ JeanX.FaceChange("angry", 1)
                    ch_j "Of course it is."
                    ch_j "Oh, you wanted to see it?"
                    
                if Line:                                                            
                    #If she got nude. . .                            
                    $ JeanX.OutfitChange("nude")
                    "She throws her clothes off at her feet."
                    call Jean_First_Topless
                    call Jean_First_Bottomless(1)
                    $ JeanX.FaceChange("sexy")
                    menu:
                        "You know, you should wear this one out. [[set current outfit]":
                            if "exhibitionist" in JeanX.Traits:
                                ch_j "mmmm. . ." 
                                $ JeanX.Outfit = "nude"
                                $ JeanX.Statup("Lust", 50, 10) 
                                $ JeanX.Statup("Lust", 70, 5) 
                                $ JeanX.Shame = 50                                
                            elif "nowhammy" not in JeanX.Traits or ApprovalCheck(JeanX, 800, "I") or ApprovalCheck(JeanX, 2800, TabM=0):                    
                                ch_j "Sure, ok. . ."
                                $ JeanX.Outfit = "nude"
                                $ JeanX.Shame = 50
                            else:
                                $ JeanX.FaceChange("sexy", 1)
                                $ JeanX.Eyes = "surprised"
                                ch_j "Yeah, um, I'm not into that right now. . ." 
                                
                        "Let's try something else though.":
                            if "exhibitionist" in JeanX.Traits:
                                ch_j "Oh, ok. . ."                         
                            elif "nowhammy" not in JeanX.Traits or ApprovalCheck(JeanX, 800, "I") or ApprovalCheck(JeanX, 2800, TabM=0):       
                                $ JeanX.FaceChange("bemused", 1)             
                                ch_j "I thought you might want me to go out like this. . ."
                                ch_j ". . ."
                            else:
                                $ JeanX.FaceChange("confused", 1)
                                ch_j "Yeah, I'm not into that right now. . ."   
                $ Line = 0
                                        
        "Never mind":    
            return #jump Jean_Clothes     
            
    return #jump Jean_Clothes
    #End of Jean Outfits
            
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Jean_Clothes_Over:                                                                                            
        # Overshirts
        "Why don't you go with no [JeanX.Over]?" if JeanX.Over:
                $ JeanX.FaceChange("bemused", 1)
                if ApprovalCheck(JeanX, 800, TabM=3) and (JeanX.Chest or JeanX.SeenChest):
                    ch_j "Ok."                    
                elif ApprovalCheck(JeanX, 600, TabM=0):
                    call Jean_NoBra
                    if not _return:
                        if not ApprovalCheck(JeanX, 1200):
                            call Display_DressScreen(JeanX)
                            if not _return:
                                return #jump Jean_Clothes
                        else:
                                return #jump Jean_Clothes
                else:
                    call Display_DressScreen(JeanX)
                    if not _return:
                            ch_j "Not right now."
                            if not JeanX.Chest:
                                ch_j "I'm not wearing a bra right now."
                            return #jump Jean_Clothes                            
                $ Line = JeanX.Over
                $ JeanX.Over = 0
                "She throws her [Line] at her feet."
                if not JeanX.Chest and not renpy.showing('DressScreen'):
                        call Jean_First_Topless
            
        "Try on that pink shirt." if JeanX.Over != "pink shirt":
                $ JeanX.FaceChange("bemused")
                ch_j "Sure." 
                $ JeanX.Over = "pink shirt"   
                
        "Try on that green shirt." if JeanX.Over != "green shirt":
                $ JeanX.FaceChange("bemused")
                ch_j "Sure." 
                $ JeanX.Over = "green shirt"   
                
        "Maybe just throw on a towel?" if JeanX.Over != "towel":
                $ JeanX.FaceChange("bemused", 1)
                if JeanX.Chest or JeanX.SeenChest:
                    ch_j "Um, ok. . ."
                elif ApprovalCheck(JeanX, 1000, TabM=0):
                    $ JeanX.FaceChange("perplexed", 1)
                    ch_j "Huh, ok . ."          
                else:
                    call Display_DressScreen(JeanX)
                    if not _return:                            
                            ch_j "That wouldn't look right."
                            return #jump Jean_Clothes    
                $ JeanX.Over = "towel"    
                            
        "Never mind":
            pass
    return #jump Jean_Clothes
    #End of Jean Top
            
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    label Jean_NoBra:
        menu:
            ch_j "I'm not wearing a bra right now."
            "Then you could slip something on under it. . .":   
                        if ApprovalCheck(JeanX, 1200, TabM=4) or (JeanX.SeenChest and ApprovalCheck(JeanX, 1000, TabM=3)):
                                $ JeanX.Blush = 1
                                ch_j "Well, it's not like I needed one. . ."
                                $ JeanX.Blush = 0          
                        elif ApprovalCheck(JeanX, 900, TabM=2) and "lace bra" in JeanX.Inventory:
                                ch_j "I guess I could find something."
                                $ JeanX.Chest  = "lace bra"    
                                "She pulls out her lace bra and slips it under her [JeanX.Over]."
                        elif ApprovalCheck(JeanX, 700, TabM=2):
                                ch_j "I guess I could find something."
                                $ JeanX.Chest  = "green bra"    
                                "She pulls out her green bra and slips it under her [JeanX.Over]."
                        else:
                                ch_j "Yeah, I don't think so."
                                return 0
                        
            "You could always just wear nothing at all. . .":
                        if ApprovalCheck(JeanX, 1100, "LI", TabM=2) and JeanX.Love > JeanX.Inbt:               
                                ch_j "I guess. . ."
                        elif ApprovalCheck(JeanX, 700, "OI", TabM=2) and JeanX.Obed > JeanX.Inbt:
                                ch_j "Sure. . ."
                        elif ApprovalCheck(JeanX, 600, "I", TabM=2):
                                ch_j "Yeah. . ."
                        elif ApprovalCheck(JeanX, 1300, TabM=2):
                                ch_j "Okay, fine."
                        else: 
                                $ JeanX.FaceChange("surprised")
                                $ JeanX.Brows = "angry"
                                if JeanX.Taboo > 20:
                                    ch_j ". . . not right now. . ."
                                else:
                                    ch_j "Ha! Not for you, [JeanX.Petname]."
                                return 0
            "Never mind.":
                        ch_j "Ok. . ."
                        return 0
        return 1
        #End of Jean bra check
       
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Jean_Clothes_Legs:                                                                                                 
        # Leggings    
        "Maybe go without the [JeanX.Legs]." if JeanX.Legs:
                $ JeanX.FaceChange("sexy", 1)
                if JeanX.SeenPanties and JeanX.Panties and ApprovalCheck(JeanX, 500, TabM=5):
                    ch_j "Ok, sure."
                elif JeanX.SeenPussy and ApprovalCheck(JeanX, 900, TabM=4):
                    ch_j "Yeah, ok."
                elif ApprovalCheck(JeanX, 1300, TabM=2) and JeanX.Panties:
                    ch_j "For you, fine. . ."
                elif ApprovalCheck(JeanX, 700) and not JeanX.Panties:
                    call Jean_NoPantiesOn
                    if not _return and not JeanX.Panties:
                        if not ApprovalCheck(JeanX, 1500):
                            call Display_DressScreen(JeanX)
                            if not _return:
                                return #jump Jean_Clothes
                        else:
                                return #jump Jean_Clothes
                else:
                    call Display_DressScreen(JeanX)
                    if not _return:
                        ch_j "Um, not with you around."
                        if not JeanX.Panties:
                                ch_j "I'm not wearing any panties at the moment."
                        return #jump Jean_Clothes
                        
                if JeanX.Legs == "pants" or JeanX.Legs == "yoga pants":
                        $ JeanX.Legs = 0    
                        "She tugs her pants off and drops them to the ground."
                else:
                        $ JeanX.Legs = 0    
                        "She tugs her skirt off and drops it to the ground."                
                if renpy.showing('DressScreen'):
                    pass
                elif JeanX.Panties:                
                    $ JeanX.SeenPanties = 1
                else:
                    call Jean_First_Bottomless
        
        "You look great in those khaki pants." if JeanX.Legs != "pants":
                ch_j "Yeah, I know."
                $ JeanX.Legs = "pants"
                
        "You look great in those yoga pants." if JeanX.Legs != "yoga pants":
                if ApprovalCheck(JeanX, 800, TabM=4):
                        ch_j "Yeah, I know."
                        $ JeanX.Legs = "yoga pants"
                else:
                    call Display_DressScreen(JeanX)
                    if not _return:
                        ch_j "Those are kind of. . . tight."
                    
        "What about wearing your green skirt?" if JeanX.Legs != "skirt":
                ch_j "Sure, why not."
                $ JeanX.Legs = "skirt"    
            
        "Never mind":
                pass
    return #jump Jean_Clothes
    #End of Jean Pants
    
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 
    
    label Jean_NoPantiesOn:
        menu:
            ch_j "I'm not wearing any panties at the moment."
            "Then you could slip on a pair of panties. . .":   
                        if ApprovalCheck(JeanX, 1500, TabM=4) or (JeanX.SeenPussy and ApprovalCheck(JeanX, 1100, TabM=4)):
                                $ JeanX.Blush = 1
                                ch_j "No, this is fine. . ."
                                $ JeanX.Blush = 0        
                        elif ApprovalCheck(JeanX, 800, TabM=4) and "lace panties" in JeanX.Inventory:
                                ch_j "Oh, sure."
                                $ JeanX.Panties  = "lace panties"  
                                if ApprovalCheck(JeanX, 1200, TabM=4):   
                                    $ Line = JeanX.Legs
                                    $ JeanX.Legs = 0
                                    "She pulls off her [Line] and slips on the lace panties."                                    
                                elif JeanX.Legs == "skirt":
                                    "She pulls out her lace panties and pulls them up under her skirt."
                                    $ JeanX.Legs = 0
                                    "Then she drops the skirt to the floor."
                                else:
                                    $ Line = JeanX.Legs
                                    $ JeanX.Legs = 0
                                    "She steps away a moment and then comes back wearing only the lace panties."                                     
                                return #jump Jean_Clothes
                        elif ApprovalCheck(JeanX, 700, TabM=4):
                                ch_j "Yeah, I guess."
                                $ JeanX.Panties = "green panties"
                                if ApprovalCheck(JeanX, 1200, TabM=4):   
                                    $ Line = JeanX.Legs
                                    $ JeanX.Legs = 0
                                    "She pulls off her [Line] and slips on the green panties."                                    
                                elif JeanX.Legs == "skirt":
                                    "She pulls out her green panties and pulls them up under her skirt."
                                    $ JeanX.Legs = 0
                                    "Then she drops the skirt to the floor."
                                else:
                                    $ Line = JeanX.Legs
                                    $ JeanX.Legs = 0
                                    "She steps away a moment and then comes back wearing only the green panties."                                     
                                return #jump Jean_Clothes
                        else:
                                ch_j "Nope."
                                return 0
                        
            "You could always just wear nothing at all. . .":
                        if ApprovalCheck(JeanX, 1100, "LI", TabM=3) and JeanX.Love > JeanX.Inbt:               
                                ch_j "True. . ."
                        elif ApprovalCheck(JeanX, 700, "OI", TabM=3) and JeanX.Obed > JeanX.Inbt:
                                ch_j "Yes. . ."
                        elif ApprovalCheck(JeanX, 600, "I", TabM=3):
                                ch_j "Hrmm. . ."
                        elif ApprovalCheck(JeanX, 1300, TabM=3):
                                ch_j "Fine."
                        else: 
                                $ JeanX.FaceChange("surprised")
                                $ JeanX.Brows = "angry"
                                if JeanX.Taboo > 20:
                                    ch_j ". . . not right now. . ."
                                else:
                                    ch_j "Ha! Not for you, [JeanX.Petname]."
                                return 0
                                
            "Never mind.":
                ch_j "Ok. . ."
                return 0
        return 1
        #End of Jean Panties check

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 

    menu Jean_Clothes_Under:   
        "Tops":
            menu:
                "How about you lose the [JeanX.Chest]?" if JeanX.Chest:
                        $ JeanX.FaceChange("bemused", 1)
                        if JeanX.SeenChest and ApprovalCheck(JeanX, 900, TabM=2.7):
                            ch_j "Ok."    
                        elif ApprovalCheck(JeanX, 1100, TabM=2):
                            if JeanX.Taboo:
                                ch_j "I don't know, here. . ."
                            else:
                                ch_j "Maybe. . ."
                        elif JeanX.Over and ApprovalCheck(JeanX, 500, TabM=2):
                            ch_j "I guess I could. . ."                          
                        elif not JeanX.Over:                            
                            call Display_DressScreen(JeanX)
                            if not _return:
                                ch_j "Not without some other top."
                                return #jump Jean_Clothes 
                        else:
                            call Display_DressScreen(JeanX)
                            if not _return:
                                ch_j "Nah."
                                return #jump Jean_Clothes 
                        $ Line = JeanX.Chest
                        $ JeanX.Chest = 0
                        if JeanX.Over:
                            "She reaches under her [JeanX.Over] grabs her [Line], and pulls it off, dropping it to the ground."
                        else:
                            "She pulls off her [Line] and drops it to the ground."
                            if not renpy.showing('DressScreen'):
                                call Jean_First_Topless
                    
                    
                "Try on that green bra." if JeanX.Chest != "green bra":
                        ch_j "Ok."
                        $ JeanX.Chest = "green bra" 
                        
                "How about that sports bra." if JeanX.Chest != "sports bra":
                        ch_j "Ok."
                        $ JeanX.Chest = "sports bra"       
                    
                "I like that lace bra." if JeanX.Chest != "lace bra" and "lace bra" in JeanX.Inventory :
                        if JeanX.SeenChest or ApprovalCheck(JeanX, 1300, TabM=2):
                            ch_j "Sure."   
                            $ JeanX.Chest = "lace bra"         
                        else:      
                            call Display_DressScreen(JeanX)
                            if not _return:           
                                ch_j "It's a little transparent. . ."  
                                
                "I like that black corset." if JeanX.Chest != "corset" and "corset" in JeanX.Inventory :
                        if JeanX.SeenChest or ApprovalCheck(JeanX, 1000, TabM=1):
                            ch_j "Sure."   
                            $ JeanX.Chest = "corset"         
                        else:         
                            call Display_DressScreen(JeanX)
                            if not _return:        
                                ch_j "It's a little revealing. . ."  
                        
                "I like that lace corset." if JeanX.Chest != "lace corset" and "lace corset" in JeanX.Inventory :
                        if JeanX.SeenChest or ApprovalCheck(JeanX, 1300, TabM=2):
                            ch_j "Sure."   
                            $ JeanX.Chest = "lace corset"         
                        else:      
                            call Display_DressScreen(JeanX)
                            if not _return:           
                                ch_j "It's a little transparent. . ."  
                                                   
                "I like that bikini top." if JeanX.Chest != "bikini top" and "bikini top" in JeanX.Inventory:
                        if bg_current == "bg pool":
                                ch_j "Sure."   
                                $ JeanX.Chest = "bikini top"         
                        else:                
                                if JeanX.SeenChest or ApprovalCheck(JeanX, 1000, TabM=2):
                                    ch_j "Sure."   
                                    $ JeanX.Chest = "bikini top"         
                                else:      
                                    call Display_DressScreen(JeanX)
                                    if not _return:           
                                            ch_j "This isn't really a \"bikini\" sort of place. . ." 
                "Never mind":
                        pass 
            return #jump Jean_Clothes_Under
              
        "Hose and stockings options":
            menu:          
                "You could lose the hose." if JeanX.Hose:# and JeanX.Hose != 'ripped tights' and JeanX.Hose != 'tights':     
                                $ JeanX.Hose = 0  
                "The thigh-high hose would look good with that." if JeanX.Hose != "stockings":     
                                $ JeanX.Hose = "stockings"  
                "The full length hose would look good with that." if JeanX.Hose != "pantyhose":     
                                $ JeanX.Hose = "pantyhose"  
                "The stockings and garterbelt would look good with that." if JeanX.Hose != "stockings and garterbelt" and "stockings and garterbelt" in JeanX.Inventory:     
                                $ JeanX.Hose = "stockings and garterbelt"  
                "Just the garterbelt would look good with that." if JeanX.Hose != "garterbelt" and "stockings and garterbelt" in JeanX.Inventory:     
                                $ JeanX.Hose = "garterbelt"    
                "Never mind":
                        pass  
            return #jump Jean_Clothes_Under
                        
        #Panties    
        "Panties":
            menu:
                "You could lose those panties. . ." if JeanX.Panties:
                        $ JeanX.FaceChange("bemused", 1)  
                        if ApprovalCheck(JeanX, 900) and (JeanX.Legs or (JeanX.SeenPussy and not JeanX.Taboo)):
                                #If you've got decent approval and either she's wearing pants or you've seen her pussy and it's not in public                        
                                if ApprovalCheck(JeanX, 850, "L"):               
                                        ch_j "True. . ."
                                elif ApprovalCheck(JeanX, 500, "O"):
                                        ch_j "Agreed."
                                elif ApprovalCheck(JeanX, 350, "I"):
                                        ch_j "Heh."
                                else:
                                        ch_j "Sure, I guess."         
                        else:                       #low approval or not wearing pants or in public 
                                if ApprovalCheck(JeanX, 1100, "LI", TabM=3) and JeanX.Love > JeanX.Inbt:               
                                        ch_j "Well look, it's not about you, but. . ."
                                elif ApprovalCheck(JeanX, 700, "OI", TabM=3) and JeanX.Obed > JeanX.Inbt:
                                        ch_j "Well. . ."
                                elif ApprovalCheck(JeanX, 600, "I", TabM=3):
                                        ch_j "Hrmm. . ."
                                elif ApprovalCheck(JeanX, 1300, TabM=3):
                                        ch_j "Okay, okay."
                                else:                                         
                                        call Display_DressScreen(JeanX)
                                        if not _return:
                                            $ JeanX.FaceChange("surprised")
                                            $ JeanX.Brows = "angry" 
                                            if JeanX.Taboo > 20:
                                                ch_j ". . . not right now. . ."
                                            else:
                                                ch_j "Ha! Not for you, [JeanX.Petname]."
                                            return #jump Jean_Clothes                            
                        $ Line = JeanX.Panties
                        $ JeanX.Panties = 0
                        if not JeanX.Legs:
                            "She pulls off her [Line], then drops them to the ground." 
                            if not renpy.showing('DressScreen'):
                                    call Jean_First_Bottomless  
                        elif ApprovalCheck(JeanX, 1200, TabM=4):   
                            $ Trigger = JeanX.Legs
                            $ JeanX.Legs = 0
                            pause 0.5
                            $ JeanX.Legs = Trigger
                            "She pulls off her [JeanX.Legs] and [Line], then pulls the [JeanX.Legs] back on."  
                            $ Trigger = 1
                            call Jean_First_Bottomless(1)                             
                        elif JeanX.Legs == "skirt":
                            "She reaches under her skirt and pulls her [Line] off."
                        else:
                            $ JeanX.Blush = 1
                            "She steps away a moment and then comes back."  
                            $ JeanX.Blush = 0      
                        $ Line = 0
                        
                "Why don't you wear the green panties instead?" if JeanX.Panties and JeanX.Panties != "green panties":
                        if ApprovalCheck(JeanX, 1100, TabM=3):
                                ch_j "Sure."
                                $ JeanX.Panties = "green panties"  
                        else:       
                                call Display_DressScreen(JeanX)
                                if not _return:          
                                        ch_j "That's none of your busines."
                                                    
                "Why don't you wear the lace panties instead?" if "lace panties" in JeanX.Inventory and JeanX.Panties and JeanX.Panties != "lace panties":
                        if ApprovalCheck(JeanX, 1300, TabM=3):
                                ch_j "I guess."
                                $ JeanX.Panties = "lace panties"
                        else:
                                call Display_DressScreen(JeanX)
                                if not _return: 
                                        ch_j "That's none of your busines."
                            
                "I like those bikini bottoms." if "bikini bottoms" in JeanX.Inventory and JeanX.Panties != "bikini bottoms":                            
                        if bg_current == "bg pool":
                                ch_j "Sure."   
                                $ JeanX.Panties = "bikini bottoms"         
                        else:                
                                if ApprovalCheck(JeanX, 1000, TabM=2):
                                    ch_j "Sure."   
                                    $ JeanX.Panties = "bikini bottoms"         
                                else:    
                                    call Display_DressScreen(JeanX)
                                    if not _return:             
                                            ch_j "This is not really a \"bikini\" sort of place. . ." 
                            
                "You know, you could wear some panties with that. . ." if not JeanX.Panties:
                        $ JeanX.FaceChange("bemused", 1)
                        if JeanX.Legs and (JeanX.Love+JeanX.Obed) <= (2 * JeanX.Inbt):
                            $ JeanX.Mouth = "smile"
                            ch_j "I -could,- but I'd rather not. . ."
                            menu:
                                "Fine by me":
                                    return #jump Jean_Clothes
                                "I insist, put some on.":
                                    if (JeanX.Love+JeanX.Obed) <= (1.5 * JeanX.Inbt):
                                        $ JeanX.FaceChange("angry", Eyes="side")
                                        ch_j "Well too bad."
                                        return #jump Jean_Clothes
                                    else:
                                        $ JeanX.FaceChange("sadside")
                                        ch_j "Oh, fine."    
                        else:                
                            ch_j "I guess. . ."
                        menu:
                            extend ""
                            "How about the green ones?":
                                    ch_j "Sure, ok."
                                    $ JeanX.Panties = "green panties"
                            "How about the lace ones?" if "lace panties" in JeanX.Inventory:
                                    ch_j "Fine."                
                                    $ JeanX.Panties  = "lace panties"
                "Never mind":
                    pass
            return #jump Jean_Clothes_Under
        "Never mind":
            pass
    return #jump Jean_Clothes
    #End of Jean Underwear
       
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  
        
    menu Jean_Clothes_Misc:                                                                                                                   
        #Misc
        "Maybe dry out your hair." if JeanX.Hair == "wet":
                if ApprovalCheck(JeanX, 600):
                    ch_j "Ok."
                    $ JeanX.Hair = "short"
                else:
                    ch_j "I don't know, it's fine like this."
                
        "You should go for that wet look with your hair." if JeanX.Hair != "wet":
                if ApprovalCheck(JeanX, 800):
                    ch_j "Hmm?"
                    $ JeanX.Hair = "wet"
                    "She wanders off for a minute and comes back."
                    ch_j "Like this?"
                else:
                    ch_j "Ugh, too much work."
        
        "You know, I like some nice hair down there. Maybe grow it out." if not JeanX.Pubes:
                if "pubes" in JeanX.Todo:
                        $ JeanX.FaceChange("bemused", 1)
                        ch_j "Give it some time. . ."
                else:                
                        $ JeanX.FaceChange("bemused", 1)
                        if ApprovalCheck(JeanX, 1000, TabM=0):               
                            ch_j "Ok, sure. . ."           
                        else: 
                            $ JeanX.FaceChange("surprised")
                            $ JeanX.Brows = "angry"
                            ch_j "None of your business."
                            return #jump Jean_Clothes
                        $ JeanX.Todo.append("pubes")
                        $ JeanX.PubeC = 6        
        "I like it waxed clean down there." if JeanX.Pubes == 1:
                $ JeanX.FaceChange("bemused", 1)            
                if "shave" in JeanX.Todo:
                    ch_j "Yeah, I know, I'll get to it."
                else:
                    if ApprovalCheck(JeanX, 1100, TabM=0):               
                        ch_j "Really? I guess I could give it a shave. . ."        
                    else: 
                        $ JeanX.FaceChange("surprised")
                        $ JeanX.Brows = "angry"
                        ch_j "None of your business."
                        return #jump Jean_Clothes
                    $ JeanX.Todo.append("shave")  
                    
        "Piercings. [[See what she looks like without them first] (locked)" if not JeanX.SeenPussy and not JeanX.SeenChest:
            pass
            
        "You know, you'd look really nice with some ring body piercings." if JeanX.Pierce != "ring" and (JeanX.SeenPussy or JeanX.SeenChest):                     
                if "ring" in JeanX.Todo:
                    ch_j "Yeah, I know, I'll get to it."
                else:                    
                    $ JeanX.FaceChange("bemused", 1)
                    $ Approval = ApprovalCheck(JeanX, 1150, TabM=0)
                    if ApprovalCheck(JeanX, 900, "L", TabM=0) or (Approval and JeanX.Love > 2* JeanX.Obed):   
                        ch_j "You think they'd look good on me?"
                    elif ApprovalCheck(JeanX, 600, "I", TabM=0) or (Approval and JeanX.Inbt > JeanX.Obed):
                        ch_j "I've been thinking about that for a while."
                    elif ApprovalCheck(JeanX, 500, "O", TabM=0) or Approval:
                        ch_j "Sure, [JeanX.Petname]."
                    else: 
                        $ JeanX.FaceChange("surprised")
                        $ JeanX.Brows = "angry"
                        ch_j "Not interested, [JeanX.Petname]."
                        return #jump Jean_Clothes            
                    $ JeanX.Todo.append("ring")
        
        "You know, you'd look really nice with some barbell body piercings." if JeanX.Pierce != "barbell" and (JeanX.SeenPussy or JeanX.SeenChest):                      
                if "barbell" in JeanX.Todo:
                    ch_j "Yeah, I know, I'll get to it."
                else:                    
                    $ JeanX.FaceChange("bemused", 1)
                    $ Approval = ApprovalCheck(JeanX, 1150, TabM=0)
                    if ApprovalCheck(JeanX, 900, "L", TabM=0) or (Approval and JeanX.Love > 2 * JeanX.Obed):  
                        ch_j "You think they'd look good on me?"
                    elif ApprovalCheck(JeanX, 600, "I", TabM=0) or (Approval and JeanX.Inbt > JeanX.Obed):
                        ch_j "I've been thinking about that for a while."
                    elif ApprovalCheck(JeanX, 500, "O", TabM=0) or Approval:
                        ch_j "Sure, [JeanX.Petname]."
                    else: 
                        $ JeanX.FaceChange("surprised")
                        $ JeanX.Brows = "angry"
                        ch_j "Not interested, [JeanX.Petname]."
                        return #jump Jean_Clothes                
                    $ JeanX.Todo.append("barbell")
            
        "You know, you'd look better without those piercings." if JeanX.Pierce:
                $ JeanX.FaceChange("bemused", 1)
                $ Approval = ApprovalCheck(JeanX, 1350, TabM=0)
                if ApprovalCheck(JeanX, 950, "L", TabM=0) or (Approval and JeanX.Love > JeanX.Obed):   
                    ch_j "Make up your mind . ."
                elif ApprovalCheck(JeanX, 700, "I", TabM=0) or (Approval and JeanX.Inbt > JeanX.Obed):
                    ch_j "What?"
                elif ApprovalCheck(JeanX, 600, "O", TabM=0) or Approval:
                    ch_j "Fine."
                else: 
                    $ JeanX.FaceChange("surprised")
                    $ JeanX.Brows = "angry"
                    ch_j "I don't know, I kinda like them now. . ."
                    return #jump Jean_Clothes            
                $ JeanX.Pierce = 0 
                
#        "Why don't you try on that medallion choker." if JeanX.Neck != "leash choker":
#                ch_j "Ok. . ."         
#                $ JeanX.Neck = "leash choker"
#        "Maybe go without a necklace." if JeanX.Neck:
#                ch_j "Ok. . ."         
#                $ JeanX.Neck = 0
            
#        "Why don't you put those wristbands on." if JeanX.Arms != "wrists":
#                ch_j "Ok. . ."         
#                $ JeanX.Arms = "wrists"
#        "Maybe go without the wristbands." if JeanX.Arms:
#                ch_j "Ok. . ."         
#                $ JeanX.Arms = 0
            
        "Never mind":
            pass         
    return #jump Jean_Clothes
    #End of Jean Misc Wardrobe
    
return
#End Jean Wardrobe

# < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < < <

     
    