#Task 1: Code Correction You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.attendees = input("Enter number of attendees: ")

attendees= int(input("How many attendees do you have?" ))
conference_room=5000
venue = "large hall" if attendees > 100 else conference_room


if attendees <= 100:
    print("venue") 


elif attendees >= 100:
    print("We recommend a conference hall")
    pass
action=input("Enter capital A to include an audio system, capital B to include a projector, capital C for both, or capital D for none.... ")
if action== "A":
    print( " Awesome your guest will now enjoy our audio system!")
elif action == "B" : 
 print ("Done! Your guest will benefit from seeing your vision through our projector!" )
elif action == "C":
    print ( " Wonderful! Your guests will enjoy a dynamic experience with our conveniently installed, high quality audio, and  projector systems!")
else:
    print( "No problem! You can always book additional packages for your event up to 72 hrs in advance!....")
    
    pass
action=input ( "Catering is included! Do your guest require a strictly vegetarian option? Enter YES or NO...")
if action== "YES":
    print("Good! We will recommend Veggie Delight Caterers") 
else:
    print (" No worries! Gourmet Meals Caterers is recommended by our staff because it has healthy and delicious vegetarian and non-vegetarian option so everyone can enjoy!") 