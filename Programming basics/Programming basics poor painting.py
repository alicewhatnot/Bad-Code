lengthOfWalls = float(input("Enter the length of the walls: "))
heightOfWalls = float(input("Enter the height of the walls: "))
AreasNotNeedingPaint = True
totalArea = 0
while AreasNotNeedingPaint == True:
    lengthOfNotPainting = float(input("Enter the length of something you are not painting: "))
    heightOfNotPainting = float(input("Enter the height of something you are not painting: "))
    continuing = str(input("Continue adding things not to paint? (y/n)"))
    area = (lengthOfNotPainting*heightOfNotPainting)
    totalArea = totalArea + area
    if continuing == "n":
        AreasNotNeedingPaint = False
coats = int(input("Enter the number of coats needed: "))
amountOfPaint = (((lengthOfWalls*heightOfWalls)-totalArea)*coats)/11
print ("You will need:",amountOfPaint,"litres of paint")
    
    