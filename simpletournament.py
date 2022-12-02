print ("Tournament System")
print ("The teams")

teamlist = []             # declaring a new list, so that it can be filled in with teams using a loop
for a in range(4):       # this will loop from 0-3 (4 times)
    print ("\nTeam", a+1) # a+1 means it will start 1 instead of 0
    tnames = str(input("Enter team name: "))
    teamlist.append(tnames)

print ("\nTeams entered", (teamlist),"\n")
print ("\nThe players")
print ()

playerlist = []         # declaring a new list, so that it can be filled in with players using a loop
for b in range(20):    # this will loop from 0-19 (20 times)
    print ("\nPlayer", b+1) # b+1 means it will start 1 instead of 0
    pnames = str(input("Enter player name: "))
    playerlist.append(pnames)
    
print ("\nPlayers entered", (playerlist))

# declaring the lists
tpointslist =         [ 0, 0, 0, 0 ]    
playerinteamlist =    [ teamlist[0], teamlist[0], teamlist[0], teamlist[0], teamlist[0], teamlist[1], teamlist[1], teamlist[1], teamlist[1], teamlist[1], teamlist[2], teamlist[2], teamlist[2], teamlist[2], teamlist[2], teamlist[3], teamlist[3], teamlist[3], teamlist[3], teamlist[3]]
playerpointslist =    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
eventtypelist = []

def events():
    noofevents= int(input("\nHow many events will there be? select 1 or 5 : "))
    if noofevents == 1 or noofevents == 5:
        for c in range (noofevents):     
            print ("\nSetup Event", c+1)
            print ("\nevent categories available: is, ia, ts, ta ")
            eventcode= (input("\nPlease select event category from above: "))
            if eventcode == "is":
                print ("\nIndividual Sporting event selected")
                eventtypelist.append("An Individual Sporting event")
                enterindividualpoints()             
            elif eventcode == "ia": 
                print ("\nIndividual Academic event selected")
                eventtypelist.append("An Individual Academic event")
                enterindividualpoints()
            elif eventcode == "ts":
                print ("\nTeam Sporting event selected")
                eventtypelist.append("A Team Sporting event")
                enterteampoints()     
            elif eventcode == "ta":
                print ("\nTeam Academic event selected")
                eventtypelist.append("A Team Academic event")
                enterteampoints()
            else:
                print ("\nThat is not a valid code")    
    else:
        print ("\nThat is not a choice")
        events()
         
def enterteampoints():    
    print ()
    print ("\nChoose from the following teams", (teamlist),"\n")
    team1st= (input("\nWhich team was 1st: "))
    
    for d in range (len(teamlist)):
        
        if team1st == teamlist[d]:
            print ("previous total for team", teamlist[d], tpointslist[d])
            
            tpointslist[d] = tpointslist[d]+10
         
            print ("10 points added, new total for team", teamlist[d], tpointslist[d])
            break
    
    print ()
    print ("\nChoose from the following teams", (teamlist),"\n")
    team2nd= (input("\nWhich team was 2nd: "))
    
    for d in range (len(teamlist)):
        
        if team2nd == teamlist[d]:
            print ("previous total for team", teamlist[d], tpointslist[d])
            
            tpointslist[d] = tpointslist[d]+8          
            
            print ("8 points added, new total for team", teamlist[d], tpointslist[d])
            break
    
    print ()   
    print ("\nChoose from the following teams", (teamlist),"\n")
    team3rd= (input("\nWhich team was 3rd: "))
    
    for d in range (len(teamlist)):
        
        if team3rd == teamlist[d]:
            print ("previous total for team", teamlist[d], tpointslist[d])
            
            tpointslist[d] = tpointslist[d]+6           
            
            print ("6 points added, new total for team", teamlist[d], tpointslist[d])
            break
    
    print () 
    print ("\nChoose from the following teams", (teamlist),"\n")   
    team4th= (input("\nWhich team was 4th: "))
    
    for d in range (len(teamlist)):
        
        if team4th == teamlist[d]:
            print ("previous total for team", teamlist[d], tpointslist[d])
            
            tpointslist[d] = tpointslist[d]+4           
            
            print ("4 points added, new total for team", teamlist[d], tpointslist[d])
            break
    
    print ()
    print ("Team points summary")
    print ()
    print ("total for team", teamlist[0], tpointslist[0])
    print ("total for team", teamlist[1], tpointslist[1])
    print ("total for team", teamlist[2], tpointslist[2])
    print ("total for team", teamlist[3], tpointslist[3])


def enterindividualpoints():    
    print ()
    print ("Choose from the following players", (playerlist))
    print ("Player points so far",(playerpointslist),"\n")
    individual1st = (input("\nWhich player was in 1st position: "))
    
    for e in range (len(playerlist)):
        
        if individual1st == playerlist[e]:
                      
            playerpointslist[e] = playerpointslist[e]+5
            
            print ("\n5 points added, new total for", playerlist[e], playerpointslist[e])
            
            teamname = playerinteamlist[e]
            
            for f in range (len(teamlist)):
                
                if teamname == teamlist[f]:
                                       
                    tpointslist[f] = tpointslist[f]+5               
                    print ("\nnew total for team", teamlist[f], tpointslist[f])

    print ()
    print ("Choose from the following players", (playerlist))
    print ("Player points so far",(playerpointslist),"\n")
    individual2nd = (input("\nWhich player was in 2nd position: "))
        
    for e in range (len(playerlist)):
        
        if individual2nd == playerlist[e]:
            
            playerpointslist[e] = playerpointslist[e]+4
            
            print ("\n4 points added, new total for", playerlist[e], playerpointslist[e])
            
            teamname = playerinteamlist[e]
            
            for f in range (len(teamlist)):
                
                if teamname == teamlist[f]:
                    
                    tpointslist[f] = tpointslist[f]+4               
                    print ("\nnew total for team", teamlist[f], tpointslist[f])
            
    print ()
    print ("Choose from the following players", (playerlist))
    print ("Player points so far",(playerpointslist),"\n")
    individual3rd = (input("\nWhich player was in 3rd position: "))
        
    for e in range (len(playerlist)):
        
        if individual3rd == playerlist[e]:
            
            playerpointslist[e] = playerpointslist[e]+3
            print ("\n3 points added, new total for", playerlist[e], playerpointslist[e])
            
            teamname = playerinteamlist[e]
            
            for f in range (len(teamlist)):
                
                if teamname == teamlist[f]:
                 
                    tpointslist[f] = tpointslist[f]+3               
                    print ("\nnew total for team", teamlist[f], tpointslist[f])
               
    print ()
    print ("Choose from the following players", (playerlist))
    print ("Player points so far",(playerpointslist),"\n")
    individual4th = (input("\nWhich player was in 4th position: "))
        
    for e in range (len(playerlist)):
        
        if individual4th == playerlist[e]:
            
            playerpointslist[e] = playerpointslist[e]+2
            
            print ("\n2 points added, new total for", playerlist[e], playerpointslist[e])
            
            teamname = playerinteamlist[e]
            
            for f in range (len(teamlist)):
                
                if teamname == teamlist[f]:
                    
                    tpointslist[f] = tpointslist[f]+2               
                    print ("\nnew total for team", teamlist[f], tpointslist[f])

    print ()
    print ("Choose from the following players", (playerlist))
    print ("Player points so far",(playerpointslist),"\n")
    individual5th = (input("\nWhich player was in 5th position: "))
        
    for e in range (len(playerlist)):
        
        if individual5th == playerlist[e]:
            
            playerpointslist[e] = playerpointslist[e]+1
            
            print ("\n1 points added, new total for", playerlist[e], playerpointslist[e])
            
            teamname = playerinteamlist[e]
            
            for f in range (len(teamlist)):
                
                if teamname == teamlist[f]:
                    
                    tpointslist[f] = tpointslist[f]+1               
                    print ("\nnew total for team", teamlist[f], tpointslist[f])
                    
    print ()
    print ("Team points summary")
    print ()
    print ("total for team", teamlist[0], tpointslist[0])
    print ("total for team", teamlist[1], tpointslist[1])
    print ("total for team", teamlist[2], tpointslist[2])
    print ("total for team", teamlist[3], tpointslist[3])

# main program

events()

print ("\nEvents information", (eventtypelist),"\n")
print("\nThank you")


