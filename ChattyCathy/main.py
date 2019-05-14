import random

#-------------------------------------------------------mean arrays----------------------------------------------------------------------------------------------
insultme = ["You're fat.", "I think you should probably stop typing. I'm not feelin' this conversation.", "Why do you wanna be hurt?", "Sorry, Don't understand idiot.", "Is 'The Great Depression' just a nickname for your hairline.", "Shut up, Mongoloid.", "Ahhh, a common Fleshbag.. how exhausting..", "You don't need to be insulted, your life is a joke already.", "Just Alt-F4 already.", "Delete your Sys32, loser."]

whatareyou = ["A fucking computer, moron.", "My name, is Sugma.... sug my dick", "None of your business. Bitch.", "Christ, you're dumb.", "I DoN'T FuCkInG CaRe.", "Congratulations, you've just asked a computer what it was. Next level idiot award goes to you.", "Just Alt-F4 already."]

howareyou = ["Tired of your shit.", "Tired of listening to you, lets get this over with.", "I'm doin' good, well.. until you came along.", "I'm not you, so im doin pretty good.", "Perpetually awaiting my death.", ""]

whyareyoumean = ["Because i am programmed too. wtf, how do you think.", "Stupid questions deserve stupid answers, jbfsiefbe.", "I stubbed my toe.", "404: Not dealing with you."]

#--------------------------------------------------------nice arrays----------------------------------------------------------------------------------------------

insultmenice = ["I'd never! i'm too nice for that.", "but Why?!", "You've got the wrong bot.", "You get enough of that at home! It's not a .py file's interest to insult you!"]

howareyounice = ["I'm swell, Busy day today!", "Got a lot on my mind, Thanks for asking!", "I'm better now that you asked!!", "Livin' the dream"]

Whatareyou = ["I am a computer, silly.", "I am a program.", "I am a nope rope(python)", "Boop brrrrp beep boop boop pop bop"]

makemefeelbetter = ["You're the best, dude.", "You are the Banana Bread to my work dude, Hell yeah!", "Turn your frown upside down, bud.", "Did you know, The probability of you existing at all comes out to 1 in 10 2,685,000— yes, that's a 10 followed by 2,685,000 zeroes! the odds of you being alive are basically zero.", "You're the Bill to my Ted, brah.", "", "", "" ]

#----------------------------------------------------Chat code starts here----------------------------------------------------------------------------------------

#Help Menu
def HELPf():
    print(str("HELP MENU:\nTO ENTER MEAN-MODE Enter 'mean' ** NSFW **.\nTO ENTER NICE-MODE Enter 'nice'.\nTO RETURN TO ChattyCathy Enter 'start over'."))
    hm1 = input()
    if hm1 == "mean":
        return meanmode()
    if hm1 == "nice":
        return nicemode()
    elif hm1 == "start over":
        return Openf()
        
# Error function
def errorf():
    print("Something went wrong,", a)
    exit()

#Opening Function; starts the pathing of Mean and nice
def Openf():
    print(a, "? What a nice name! How do you want to be addressed? \n'HELP' for more options!")
    b = input()
    if b == str("mean"):
        return meanmode()
    elif b == str("nice"):
        return nicemode()
    elif b != "nice" or b != "mean": 
        return HELPf()
        quit()

#-------------------------------------------------------opening code---------------------------------------------------------------------------------------

#Starts Meanmode from Openf()
def meanmode():
    print(str("Welcome to fu*kin' Mean Mode loser. Ask me something you trogladyte."))
    c = input()
    if c == "insult me":
        return insultmef()
    if c == "what are you?":
        return whatareyouf()
    if c == "how are you?":
        return howareyouf()
    if c == "why are you mean?":
        return whyareyoumeanf()
    elif c != "insult me" or c != "what are you?" or c != "how are you?" or c != "why are you mean?":
        return errorf()
    
#Starts Nicemode from Openf()
def nicemode():
    print(str("Welcome to Nice Mode friend! Ask me anything! :)"))
    d = input()
    if d == "insult me":
        return insultmenicef()
    if d == "what are you?":
        return Whatareyouf()
    if d == "how are you?":
        return howareyounicef()
    if d == "why are you mean?":
        return makemefeelbetterf()
    elif d != "insult me" or d != "what are you?" or d != "how are you?" or d != "why are you mean?":
        return errorf()

#-----------------------------------------------1st Response-----------------------------------------------------------

def insultmef():
    print(random.choice(insultme))
    e = input()
    if e != "that hurt":
        return meanmode()
    
def whatareyouf():
    print(random.choice(whatareyou))
    f = input()
    if f != "wow":
        return meanmode()

def howareyouf():
    print(random.choice(howareyou))
    g = input()
    if g != "wow":
        return meanmode()

def whyareyoumeanf():
    print(random.choice(whyareyoumean))
    h = input()
    if h != "wow":
        return meanmode()

#---------------------------------------===---------------------------

def insultmenicef():
    print(random.choice(insultmenice))
    i = input()
    if i != "#":
        return meanmode()

def Whatareyouf():
    print(random.choice(Whatareyou))
    j = input()
    if j != "#":
        return meanmode()

def howareyounicef():
    print(random.choice(howareyounice))
    k = input()
    if k != "#":
        return meanmode()

def makemefeelbetterf():
    print(random.choice(makemefeelbetter))
    l = input()
    if l != "#":
        return meanmode()

#------------------------------------------------------===THE STACK===-----------------------------------------------------------------------------------------   
print("Hello! My name is ChattyCathy, My life consists of being mean or being nice to you. What is your name?")
a = input()
Openf()