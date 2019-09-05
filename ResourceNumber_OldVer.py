# promfi resource id generator test on 190423 @ 6:30pm
ProjectNum = int(input("enter a project number: "))
SerRg = range(0,10000,1000) # this is the range of values allowed in the series
for Series in range(0,10,1):# options that can be used, assigns range values to series variable
    print(f"{Series}",end=" ")# prints list of values horizontally
print("\n") # prints new line before running next command
SerSel = int(input("Select a series value: ")) # here user selects a series
if SerSel == 0: # when selected series is 0 we need nested logic
    for SerCount in range(4): # here we want to generate a string with 4 zeroes
        SerSel = '' # we assume the string is empty
        for NwSerCount in range(4): # now we concatenate all zeroes by repeating this line until end of range
            SerSel += str(0) # this variable stores the generated string
    print(f"You have chosen series: {SerSel}") # this line confirms the generated string
    NwSer = int(SerRg[int(SerSel)])
elif SerSel or range(1,10,1):
    print(f"You have chosen series: {SerRg[SerSel]}")
    NwSer = int(SerRg[int(SerSel)])
else:
    print("This is not an acceptable option")

# leave this line + 1 above and 1 below empty

ResRg = range(0,1000,100) # this is the range of values allowed in the resource
for ResGen in range(0,10,1):# options that can be used, assigns range values to resource
    print(f"{ResGen}",end=" ")# prints list of values horizontally
print("\n") # prints new line before running next command
ResSel = int(input("Select a Resource range: ")) # here user selects a resource
if ResSel == 0: # when selected series is 0 we need nested logic
    for ResCount in range(3): # here we want to generate a string with 3 zeroes
        ResSel = '' # we assume the string is empty
        for NwResCount in range(3): # now we concatenate all zeroes by repeating this line until end of range
            ResSel += str(0) # this variable stores the generated string
    print(f"You have chosen Resource range: {ResSel}") # this line confirms the generated string
    NwRes = int(ResRg[int(ResSel)])
elif ResSel or range(1,10,1):
    print(f"You have chosen Resource range: {ResRg[ResSel]}") # returns the selected resource matching the range
    NwRes = int(ResRg[int(ResSel)])
else:
    print("This is not an acceptable option")

# leave this line + 1 above and 1 below empty

ResQtyRg = range(0,100,10)
for ResQtyGen in range(0,10,1):
    print(f"{ResQtyGen}",end=" ")
print("\n")
ResQtySel = int(input("Select a Resource range: "))
if ResQtySel == 0:
    for ResQtyCount in range(2):
        ResQtySel = ''
        for NwResQtyCount in range(2):
            ResQtySel += str(0)
    print(f"You have chosen Resource range: {ResQtySel}")
    NwResQty = int(ResQtyRg[int(ResQtySel)])
elif ResQtySel or range(1,10,1):
    print(f"You have chosen Resource range: {ResQtyRg[ResQtySel]}")
    NwResQty = int(ResQtyRg[int(ResQtySel)])
else:
    print("This is not an acceptable option")

# print(type(int(SerRg[int(SerSel)])))
# print(type(int(ResRg[int(ResSel)])))
# print(type(int(ResQtyRg[int(ResQtySel)])))

CombSerResQty = int(NwSer) + int(NwRes) + int(NwResQty) # this combines the resource and the series & quantity

relationshipCode = input("enter a relationship code: (hint: rrf.A.a.a)")
taskCode = input("enter a Task code: (hint: DT-IT)")
print(f"The Project# is: {'{:05d}'.format(ProjectNum)}")
print(f"The Resource ID# is: {'{:04d}'.format(CombSerResQty)}")
print(f"The Task Code is: {taskCode}")
print(f"The Relationship Code is: {relationshipCode}")
print(f"The Sequence ID# is: {'{:05d}'.format(ProjectNum)}-{'{:04d}'.format(CombSerResQty)}_{taskCode} {relationshipCode}")
# note: @ 9:54pm I was finally able to generate a sequence ID for promfi using python
# total python programming time today was 3 hours 30 minutes; note today I did not watch the tutorial
# first time I attempted this with python was some time in the summer of 2018


# python console output results below from 190423 @ 10pm
# enter a project number: 0
# 0 1 2 3 4 5 6 7 8 9
#
# Select a series value: 0
# You have chosen series: 0000
# 0 1 2 3 4 5 6 7 8 9
#
# Select a Resource range: 0
# You have chosen Resource range: 000
# 0 1 2 3 4 5 6 7 8 9
#
# Select a Resource range: 0
# You have chosen Resource range: 00
# enter a relationship code: rrf.A.a.a
# enter a Task code: DT-IT
# The Project# is: 00000
# The Resource ID# is: 0000
# The Task Code is: DT-IT
# The Relationship Code is: rrf.A.a.a
# The Sequence ID# is: 00000-0000_DT-IT rrf.A.a.a