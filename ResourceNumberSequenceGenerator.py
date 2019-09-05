# import ProjectNumberSequenceGenerator
# from ProjectNumberSequenceGenerator import ProjectNumber


# class ResourceNumber:
def resource_number(): # SerSel, ResSel, ResQtySel
    # ProjectNum = int(input("enter a project number: "))
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

    ResQtyRg = range(0,100,10)
    for ResQtyGen in range(0,10,1):
        print(f"{ResQtyGen}",end=" ")
    print("\n")
    ResQtySel = int(input("Select a Resource instance: "))
    if ResQtySel == 0:
        for ResQtyCount in range(2):
            ResQtySel = ''
            for NwResQtyCount in range(2):
                ResQtySel += str(0)
        print(f"You have chosen Resource instance: {ResQtySel}")
        NwResQty = int(ResQtyRg[int(ResQtySel)])
    elif ResQtySel or range(1,10,1):
        print(f"You have chosen Resource instance: {ResQtyRg[ResQtySel]}")
        NwResQty = int(ResQtyRg[int(ResQtySel)])
    else:
        print("This is not an acceptable option")

    CombSerResQty = int(NwSer) + int(NwRes) + int(NwResQty) # this combines the resource and the series & quantity
    print(f"The Resource ID# is: {'{:04d}'.format(CombSerResQty)}")


#