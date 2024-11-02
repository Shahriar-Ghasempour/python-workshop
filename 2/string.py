question = input()
    
# enroll | sarbazi => amoozesh
# remove => modir
# hejab => herasat
# room => khabgah
# pool => sport
# launch | dinner | breakfast => selfservice

if "enroll" in question or "sarbazi" in question:
    print("amoozesh")
    
if "remove" in question:
    print("modir")
    
if "hejab" in question:
    print("herasat")
    
if "room" in question:
    print("khabgah")
    
if "pool" in question:
    print("sport")
    
if "launch" in question or "dinner" in question or "breakfast" in question:
    print("self service")