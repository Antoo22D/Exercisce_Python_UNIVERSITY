stringa = ""
tappo = 0
while tappo != 2:
    x = str(input())
    if tappo == 0:
        if x == "o":
            tappo += 1
        else:
            tappo = 0
            stringa += x
    else:
        if x == "k":
            tappo += 1
        else:
            tappo = 0
            stringa += "o"
            stringa += x
print(len(stringa), end="")