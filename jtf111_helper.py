import dcs

m = dcs.Mission()
m.load_file("/Users/robgevers/Downloads/OperationGoodspeed_Mission5_v2.miz")

UHFPresets = {1: 330, 2: 333.3}
VHFPresets = {1: 127, 2: 127.1}

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
    elif(group.name.startswith("Texaco")):
        processTexaco(group)
    elif(group.name.startswith("Shell")):
        processShell(group)
    elif(group.name.startswith("Arco")):
        processArco(group)
    else:
        print("Other Blue Group:", group.name)

print("End JTF-111 Helper")