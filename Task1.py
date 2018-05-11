"""
Ralph David N. Gedangoni
Task1
"""
Sessions_Attended = {'sessions' : '1011,2344,3222,44322,555,6332,721,8789,99,1011,1124,1245,137,1499'}

x = Sessions_Attended['sessions'] #using assignment
x = x.split(",")


#using for loop, multiple keys
#y = 0
#for key, value in Sessions_Attended.items(): 
#    x = value.split(",")
#    z = len(x)    
#    y = y + z

#for key, value in Sessions_Attended.items(): "using for loop, only good for 1 key"
#    x = value.split(",")

print("I have attended : ", len(x), "sessions")
