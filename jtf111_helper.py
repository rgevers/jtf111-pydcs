import dcs

m = dcs.Mission()
m.load_file("/Users/robgevers/Downloads/OperationGoodspeed_Mission5_v2.miz")

UHFPresets = {1: 330, 2: 333.3, 4: 258.1, 8: 265.1, 16: 285, 17: 285.1, 9: 265.2, 18: 285.2, 5: 258.2, 10: 280, 20: 300, 11: 280.1, 3: 258, 6: 258.3, 12: 280.3, 13: 280.4, 7: 265, 14: 280.5, 15: 280.6, 19: 285.3}
VHFPresets = {1: 127, 2: 127.1, 4: 151, 8: 149.1, 16: 137.2, 17: 139.1, 9: 149.2, 18: 139.2, 5: 151.1, 10: 40, 20: 155.975, 11: 40.1, 3: 127.2, 6: 151.2, 12: 40.2, 13: 145.1, 7: 149, 14: 145.2, 15: 137.1, 19: 155.975}

GunPreset1 = {7: 149, 1: 127, 2: 127.1, 4: 151, 8: 149.1, 9: 149.2, 5: 151.1, 10: 135.1, 3: 127.2, 6: 151.2}
GunPreset2 = {7: 265, 1: 330, 2: 333.3, 4: 258.1, 8: 265.1, 9: 265.2, 5: 258.2, 10: 285, 3: 258, 6: 258.3}
GunPreset3 = {7: 40.2, 1: 30, 2: 30.1, 4: 30.3, 8: 40.3, 9: 50, 5: 40, 10: 50.1, 3: 30.2, 6: 40.1}
GunPreset4 = {7: 40.2, 1: 30, 2: 30.1, 4: 30.3, 8: 40.3, 9: 50, 5: 40, 10: 50.1, 3: 30.2, 6: 40.1}

def processTomcat(group):
    for plane in group.units:
        plane.addpropaircraft['INSAlignmentStored'] = True
        for i in range(1,len(UHFPresets)):
            plane.radio[1]['channels'][i] = UHFPresets[i]
        
        for i in range(1,len(VHFPresets)):
            plane.radio[2]['channels'][i] = VHFPresets[i]

def processGun(group):
    for helo in group.units:
        for i in range(1,len(GunPreset1)):
            helo.radio[1]['channels'][i] = GunPreset1[i]
        
        for i in range(1,len(GunPreset2)):
            helo.radio[2]['channels'][i] = GunPreset2[i]

        for i in range(1,len(GunPreset3)):
            helo.radio[2]['channels'][i] = GunPreset3[i]

        for i in range(1,len(GunPreset4)):
            helo.radio[2]['channels'][i] = GunPreset4[i]

def processFixedWing(group, groupNum, abbrev, STN, makeName):
    print("Processing",group.name)
    #Can we assume they are always in order?
    planeNum = 1
    for plane in group.units:
        planeSuffix = str(groupNum) + str(planeNum)
        plane.addpropaircraft['STN_L16'] = STN + planeSuffix
        plane.addpropaircraft['VoiceCallsignLabel'] = abbrev
        plane.addpropaircraft['VoiceCallsignNumber'] = planeSuffix

        plane.callsign_dict['name'] = makeName + planeSuffix
        plane.callsign_dict[4] = makeName + planeSuffix
        
        for i in range(1,len(UHFPresets)):
            plane.radio[1]['channels'][i] = UHFPresets[i]
        
        for i in range(1,len(VHFPresets)):
            plane.radio[2]['channels'][i] = VHFPresets[i]

        #TODO - Laser Codes?
        planeNum = planeNum + 1

def processTexaco(group):
    print("Processing", group.name)
    
    group.frequency = 280
    for point in group.points:
        if len(point.tasks) > 0 and point.tasks[0].id == "Orbit":
            #Set speed and altitutde
            point.tasks[0].params['altitude'] = 6705
            point.tasks[0].params['speed'] = 221
    
    plane = group.units[0]
    plane.addpropaircraft['VoiceCallsignLabel'] = "TO"
    plane.addpropaircraft['VoiceCallsignNumber'] = "11"
    plane.callsign_dict['name'] = "Texaco11"

def processShell(group):
    print("Processing", group.name)
    
    group.frequency = 280.3
    for point in group.points:
        if len(point.tasks) > 0 and point.tasks[0].id == "Orbit":
            #Set speed and altitutde
            point.tasks[0].params['altitude'] = 7620
            point.tasks[0].params['speed'] = 257
    
    plane = group.units[0]
    plane.addpropaircraft['VoiceCallsignLabel'] = "SL"
    plane.addpropaircraft['VoiceCallsignNumber'] = "11"
    plane.callsign_dict['name'] = "Shell11"

def processArco(group):
    print("Processing", group.name)
    
    group.frequency = 280.5
    for point in group.points:
        if len(point.tasks) > 0 and point.tasks[0].id == "Orbit":
            #Set speed and altitutde
            point.tasks[0].params['altitude'] = 6401
            point.tasks[0].params['speed'] = 190
    
    plane = group.units[0]
    if(plane.addpropaircraft is not None): #TODO - Why?
        plane.addpropaircraft['VoiceCallsignLabel'] = "AO"
        plane.addpropaircraft['VoiceCallsignNumber'] = "11"
    plane.callsign_dict['name'] = "Arco11"

for group in m.coalition['blue'].countries['USA'].plane_group:
    if(group.name.startswith("Hellcat-1")):
        processFixedWing(group, 1, "HT", "031", "Hornet")
    elif(group.name.startswith("Hellcat-2")):
        processFixedWing(group, 2, "HT", "031", "Hornet")
    elif(group.name.startswith("Hellcat")):
        processFixedWing(group, 3, "HT", "031", "Hornet")
    elif(group.name.startswith("Nickel-1")):
        processFixedWing(group, 1, "NL", "041", "Viper")
    elif(group.name.startswith("Nickel-2")):
        processFixedWing(group, 2, "NL", "041", "Viper")
    elif(group.name.startswith("Nickel")):
        processFixedWing(group, 3, "NL", "041", "Viper")
    elif(group.name.startswith("Gypsy")):
        processTomcat(group)
    elif(group.name.startswith("Texaco")):
        processTexaco(group)
    elif(group.name.startswith("Shell")):
        processShell(group)
    elif(group.name.startswith("Arco")):
        processArco(group)
    else:
        print("Other Blue Group:", group.name)

for group in m.coalition['blue'].countries['USA'].helicopter_group:
    if(group.name.startswith("Gun")):
        processGun(group)

print("End JTF-111 Helper")