def createTriangle(thickness):
    flag = 1
    width = thickness - 1
    totalW = width + thickness
    array = []
    for i in range(0, thickness):
        array.append(('H'*flag).center(totalW))
        flag+=2
        
    return array

def triangle(thickness):
    array = createTriangle(thickness)
    for i in range(len(array)):
        print(array[i])
    

def reversedTriangle(thickness):
    array = createTriangle(thickness)
    for i in range(len(array)):
        print((array[::-1][i]).rjust(thickness*6-1))

        
def logo(thickness):
    
    #Up side of the H
    for i in range(thickness+1):
     print(('H'*thickness).center(thickness*2)+('H'*thickness).center(thickness*6))  
    
    #Center of the H
    for i in range(int((thickness+1)/2)):
        print(('H'*thickness*5).center(thickness*6))
     
    #Down side of the H
    for i in range(thickness+1):
     print(('H'*thickness).center(thickness*2)+('H'*thickness).center(thickness*6)) 
   
  
def printAll(thickness):
    triangle(thickness)
    logo(thickness)
    reversedTriangle(thickness)
  
thickness = int(input())
printAll(thickness)
