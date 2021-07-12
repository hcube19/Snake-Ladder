from random import randint

#Function to roll Dice
def dice():
  num=randint(1,6)
  return num

#Function to move forward
def move(pos,num):
  pos=pos+num
  return pos

#Dictionary to go up ladder
up={19:66,36:53,61:98}

#Dictionary when eaten by a snake
down={99:1,46:12}

pos=0
num=0
count=1
position=[]

while pos <100:
  print("CHANCE: ",count)
  num=dice()
  print("DICE: ",num)
  pos=move(pos,num)
  print("INITIAL POSITION: ",pos)

#IF position is in up or down
#Check if player can go up ladder or has to come down due to snake
  if pos in up.keys():
    pos=up[pos]
  elif pos in down.keys():
    pos=down[pos]
  print("POSITION AFTER UP & DOWN: ",pos)

  if pos <= 100:
   position.append(pos)

#For keep rooling dice to get PERFECT 100,
#Eg. if on 99 U NEED 1 to get 100, Will not work if u get any other number
  if pos >100:
    pos=position[-1]
  print("FINALPOSITION: ",pos)
  count=count+1
  print()
print(position)