#Code for my Chat bot; Chatty Cathy! She is in her alpha stage at the moment while i work on a Web Scraping function/program! enjoy and simply copy and paste the function you'd like explained to me in discord. @ZixlGaming#4063
import random
from random import randint

def greetingfunc():
    print("Hey, i'm ChattyCathy0.00! What is you name?")
    nameinput = input()
    print("ahhh. Yes. How are you,", nameinput, "?", "Would you like to chat for a little?")
    z = input()
    if z == "y" or z == "Y" or z == "Yes." or z == "yes." or z == "y" or z == "Y" or z == "yes" or z == "Yes" or z == "okay" or z == "Okay" or z == "ok." or z == "Ok." or z == "sure." or z == "Sure." or z == "Next" or z == "next" :
        myreply = "Okay! I'm good at talking about (M)usic!"
    else:
        myreply = "Then Why the *$@# did u run me? Get lost!"
        return quit(myreply)
    return myreply

def musicfunc():
    f = input()
    if f == "M" or f == "m" or f == "Music" or f == "music" or f == "Okay" or f == "ok" or f == "okay" or f == "Ok" or f == "k" or f == "kk" or f == "Sure." or f == "Sure" or f == "sure" :
        x = "Sounds Great! Did you know, *scraped content here*"
    else:
        x = "Then Why the *$@# did u run me? Get lost!"
        return quit(x)
    return x

def musictrivia():
    y = input()
    if y == "Yes." or y == "yes." or y == "y" or y == "Y" or y == "yes" or y == "Yes" or y == "okay" or y == "Okay" or y == "ok." or y == "Ok." or y == "sure." or y == "Sure." or y == "Next" or y == "next" or y == "Cool" or y == "cool" :
        xy = "it worked"
    else:
        xy = "Oops, something went wrong UwU"
    return quit(xy)



print(greetingfunc())
print(musicfunc())
print(musictrivia())