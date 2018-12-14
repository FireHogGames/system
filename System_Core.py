from Window import WinAPI


def Say(sentence):
    print(str(sentence))

#use this to keep the communication running
isRunning = True
isInit = False;

#create a loop that keeps running until the user ends the session or system crashes
while isRunning == True:

    system_status = "Inactive"
    
    user_input = input("system->command: ")

    if(user_input == "End session"):
        isRunning = False
        exit()

    if(user_input == "System are you there"):
        if(isInit == False):
            isInit = True
            Say("How can I help you?")
            system_status = "Active"
        else:
            Say("How can I help you sir?")

    if(user_input == "System wake up"):
        if(isInit == False):
            isInit = True
            Say("How can I help you?")
            system_status = "Active"
        else:
            Say("I'm already active!")
    
    if(isInit == True):

        if(user_input == "Test communication"):
            Say("Hello world!")

        if(user_input == "Hello system"):
            Say("Hello sir, how can I help you?")

        if(user_input == "Initiate suit"):
            Say("Suit module not found")

        if(user_input == "Standby mode"):
            if(isInit == True):
                isInit = False
                Say("Standby mode on!")

        if(user_input == "Make a window for me"):
            WinAPI.InitWindow()

        if(user_input == "Make a calculation for me"):
           Say("Whats value a?")
           a = input("A: ")
           Say("What is value b?")
           b = input("B: ")
           c = 0

           c=int(a)+int(b)

           Say("The answer is " + str(c) + "!")
            
        

    else:
        Say("I'm currently on standby!")



