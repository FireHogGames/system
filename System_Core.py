import pyttsx
import time

mute = False

def Say(sentence):
    print(str(sentence))
    
    if(mute == False):
        engine = pyttsx.init()
        engine.say(str(sentence))
        engine.runAndWait()

#use this to keep the communication running
isRunning = True

#used for standby and start up
isInit = False;

#create a loop that keeps running until the user ends the session or system crashes
while isRunning == True:
    
    user_input = input("system->command: ")

    if(user_input == "mute"):
        mute = True

    if(user_input == "unmute"):
        mute = False
    
    if(user_input == "end session"):
        isRunning = False
        exit()

    if(user_input == "system are you there"):
        if(isInit == False):
            isInit = True
            Say("How can I help you?")
            system_status = "Active"
        else:
            Say("How can I help you sir?")

    if(str(user_input) == "system wake up"):
        if(isInit == False):
            isInit = True
            Say("How can I help you?")
            system_status = "Active"
        else:
            Say("I'm already active!")
    
    if(isInit == True):

        if(user_input == "test communication"):
            Say("Hello world!")

        if(user_input == "Hello system"):
            Say("Hello sir, how can I help you?")

        if(user_input == "Initiate suit"):
            Say("Suit module not found")

        if(user_input == "Standby mode"):
            if(isInit == True):
                isInit = False
                Say("Standby mode on!")

        if(user_input == "make a calculation for me"):
           Say("Whats value a?")
           a = input("A: ")
           Say("What is value b?")
           b = input("B: ")
           c = 0

           c=int(a)+int(b)

           Say("The answer is " + str(c) + "!")

        if(user_input == "open the database"):
            #Load the database file
            f = open("./database.txt", "r")
            
            #create an array of users
            lines = f.readlines()

            #reset the line numbers
            linenumber = 0
            #show how many contacts are abailible
            Say("You have " + str(len(lines)) + " contacts in your database.")

            Say("Wich user would you like to see, sir?")
            
            #ask for a certain id
            linenumber = input("ID-> ")

            #show the asked data
            Say("Here is the data for id " + str(linenumber) + "!")

            #correct the array pointer
            linenumber = int(linenumber) - 1

            #give the outputdata
            Say(lines[int(linenumber)])

        if(user_input == "set a timer"):
            Say("How long do you want the timer to be?")
            length = input("Time length in seconds: ")
            Say("Timer set for " + str(length) + ".")
            
            time.sleep(int(length))

            #repeat the alarm 5 times
            for x in range(0, 5):
                Say("Time is over.")

        if(user_input == "hide window"):
            Say("Niek, it doesn't work like that!!")

    else:
        Say("I'm currently on standby!")


