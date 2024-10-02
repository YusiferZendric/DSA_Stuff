import random

coordinate_plane = [[i,j] for i in range(100) for j in range(100)]
food_at_places = random.sample(coordinate_plane,2)
print(food_at_places)
instance=-1
blob_food = 0
blob_location = random.choice(coordinate_plane)

def navigation(where):
    if where == "up" and blob_location[1]!=99:
        blob_location[1]+=1
    if where == "down" and blob_location[1]!=0:
        blob_location[1]-=1
    if where == "right" and blob_location[0]!=99:
        blob_location[0]+=1
    if where == "left" and blob_location[0]!=0:
        blob_location[0]-=1

def pairs():
    navs = []
    choices = ['up', 'down', 'right', 'left']
    for _ in range(random.randint(3,5)):
        navs.append(random.choice(choices))
    return navs
while True:
    instance+=1
    l = pairs()
    exit_loop = False
    for j in l:
        navigation(j)
        if blob_location in food_at_places:
            blob_food+=1
            print("Blob found food: ",blob_food, " at instance ", instance)
            if blob_food==2:
                exit_loop = True
                break
    if exit_loop:
        break  