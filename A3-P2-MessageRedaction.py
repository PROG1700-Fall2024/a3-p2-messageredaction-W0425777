#Program 2 – Message Redaction
#Description:   Design and write a program that counts and removes all desired letters from 
#               any user-entered sentence or phrase.

#Student #: W0425777    
#Student Name: Katherine Tucker

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #While loop with quite as end
    Redact = []
    InPhrase= ""
    Letters= ""

    def GetInPhrase(): 
        In=input("\nType a phrase (or quit to exit program): ").lower()
        return In
    
    def GetLetters():
        Let=input("\nType a comma-separated list of letters to redact: ").lower()
        return Let

    while True: 
        InPhrase= GetInPhrase()
        if (InPhrase == "quit"):
            break
        #chose 2 if statmetns instead of elif so I could call the returns from both fuctions induvidally so the output looks better
        Letters = GetLetters()
        if (Letters == "quit"):
            break

        Redact.extend(Letters.split(","))

        for letters in Redact:
            InPhrase=InPhrase.replace(letters,"_")
            HowMany=InPhrase.count("_")

        #List needs to be cleared
        Redact.clear()

        
        print("Number of letters redacted: {0}".format(HowMany))
        print("Redacted phrase: {0}".format(InPhrase))    
        #Phrase=
        #for i in Redact:
       #     InPrhase=InPhrase.replace(Redact[i],"_")
        
    
    #print("Number of letter redacted: {0}".format())
    #print(Redact)
    #input for phrase in function

    #input for letters

    #create list for how many letters are replaced 


    # YOUR CODE ENDS HERE

main()