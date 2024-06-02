#Task 1: Code Correction You are provided with a Python script that is supposed to guide a user through an adventure game, but it has some errors. Identify and fix them.


place = input(" Choose a place: forest or cave? ")

if place == "forest": 
     action =input ("climb a tree or cross a river? "  )
if place =="cave": 
    action =input ("light a torch or proceed in the dark? ") 
elif place!= "forest" or "cave":
        pass
action =input (" You discovered a hidden forest! Grow a rose or plant a seed"  )
if action== "light a torch":
        print( "You found a golden egg nest! You earned 10 points!")
elif action == "proceed in the dark":
        print( " You found a magical gem! You earned 10 points! ")
       
if action== "climb a tree":
    print( "You found a bird's nest!")
elif action == "cross a river":
    print( " You found a hidden treasure!")
elif action!= "climb a tree" or "cross a river": 
    pass 


 
 # Task 3: Default Path
 # If the user makes an invalid choice at any point, use the pass statement for now. Later, you can enhance this to provide feedback or a different branch of the story.

 
action!= ("light a torch" ) or action!= ("proceed in the dark" )

pass

action =input ("There are more treasures in this enchanted garden! Are you ready to enter? yes or no? "  )

#Options


if action== "Yes" or "yes":
    pass
    
action =input (" No worries your the ruler of this meadow! Pick a flower or plant a seed? "  )

if action=="Pick"or "pick" or "flower" or"Pick a flower" or "rose" or "Grow a rose" or "pick a flower":
    print ( " You have a golden touch! oh, how the roses are blooming! You won the game!")
elif action=="Plant" or "seed" or "Seed" or "plant"or " plant a seed":
    print ( " You have a golden hand! Wow! The roses are blooming..... YOU won the game!") 

 








    
   





   





    
    

