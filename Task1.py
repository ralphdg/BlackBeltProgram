"""
Ralph David N. Gedangoni
Task1
"""

Sessions_Attended = {'sessions' : '1011,2344,3222,44322,555,6332,721,8789,99,1011,1124,1245,137,1499'}

for key, value in Sessions_Attended.items():
    x = value.split(",")

print("I have attended : ", len(x), "sessions")
    
