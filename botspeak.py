import pyfiglet
"botspeak"
def say(txt):
    L = []
    counter1 = 0
    while counter1+45 < len(txt):
        L.append(txt[counter1:counter1+45])
        counter1 += 45
    else:
        L.append(txt[counter1:])
    LEN = 0
    for i in L:
        if len(i) > LEN:
            LEN = len(i)
            
    BOT = [" "*(LEN+8)+"       \     /",
           " "*(LEN+8)+"       _\___/_",
           " "*(LEN+8)+"      |       |",
           " "*(LEN+8)+"     [| 0   0 |]",
           " "*(LEN+8)+"      |  ___  |",
           " "*(LEN+8)+"      |_______|",
           " "*(LEN+8)+" _______|___|_______" ,              
           " "*(LEN+8)+"[_\     _____     /_]"	,
           " "*(LEN+8)+"[__\   |     |   /__]",
           " "*(LEN+8)+"[__]\  |__/__|  /[__]",
           " "*(LEN+8)+"[__] |         | [__]",
           " "*(LEN+8)+"[__] | oooo    | [__]",
           " "*(LEN+8)+"[__] | ||||  []|[__]",
           " "*(LEN+8)+"[__].|_________|.[__]",
           " "*(LEN+8)+"|||| [___] [___] ||||",
           " "*(LEN+8)+"     [___] [___]",
           " "*(LEN+8)+"     [___] [___]",
           " "*(LEN+8)+"     [___] [___]",
           " "*(LEN+8)+"     [___] [___]",
           " "*(LEN+8)+"     [___] [___]",
           " "*(LEN+8)+"     [___] [___]",
           " "*(LEN+8)+"    |_____|_____|"]

    print("   "+ "_" * (LEN+8))
    print(" .'"+ " " * (LEN+8)+"'.")
    for i in L:
        print("|"+"{0:{align}}".format(i,align = ("^"+str(LEN+12)))+"|")
    print(" '." + "_" * (LEN+4)+"    .'")
    print(" "*(LEN+7)+"\   |")
    print(" "*(LEN+8)+"\  |")
    print(" "*(LEN+9)+"\ |")
    print(" "*(LEN+10)+"\|")
    for i in BOT:
        print(i)
                   
def fancy_say(text,font = 'standard',width = 65):
    import pyfiglet
        
    TXT = pyfiglet.figlet_format(text,font = font,width = width)
    LIST = TXT.split("\n")
    LEN = 0
    for i in LIST:
        if LEN<len(i):
            LEN = len(i)
    if (LEN > 8):
        botLEN = LEN-15
    else:
        botLEN = LEN
    BOT = [" "*(botLEN+8)+"       \     /",
           " "*(botLEN+8)+"       _\___/_",
           " "*(botLEN+8)+"      |       |",
           " "*(botLEN+8)+"     [| 0   0 |]",
           " "*(botLEN+8)+"      |  ___  |",
           " "*(botLEN+8)+"      |_______|",
           " "*(botLEN+8)+" _______|___|_______" ,              
           " "*(botLEN+8)+"[_\     _____     /_]"	,
           " "*(botLEN+8)+"[__\   |     |   /__]",
           " "*(botLEN+8)+"[__]\  |__/__|  /[__]",
           " "*(botLEN+8)+"[__] |         | [__]",
           " "*(botLEN+8)+"[__] | oooo    | [__]",
           " "*(botLEN+8)+"[__] | ||||  []| [__]",
           " "*(botLEN+8)+"[__].|_________|.[__]",
           " "*(botLEN+8)+"|||| [___] [___] ||||",
           " "*(botLEN+8)+"     [___] [___]",
           " "*(botLEN+8)+"     [___] [___]",
           " "*(botLEN+8)+"     [___] [___]",
           " "*(botLEN+8)+"     [___] [___]",
           " "*(botLEN+8)+"     [___] [___]",
           " "*(botLEN+8)+"     [___] [___]",
           " "*(botLEN+8)+"    |_____|_____|"]

    print("   "+ "_" * (LEN+8))
    print(" .'"+ " " * (LEN+8)+"'.")
    for i in LIST:
        print("|"+"{0:{align}}".format(i,align = ("^"+str(LEN+12)))+"|")
    print(" '." + "_" * (botLEN+4)+"     "+"_"*(LEN-botLEN-1)+".'")
    print(" "*(botLEN+7)+"\   |")
    print(" "*(botLEN+8)+"\  |")
    print(" "*(botLEN+9)+"\ |")
    print(" "*(botLEN+10)+"\|")
    for i in BOT:
        print(i)


