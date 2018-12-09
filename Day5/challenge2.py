import re
file = open("input.txt","r")
str = file.read()

alphabet = "abcdefghijklmnopqrstuvwxyz"
minLength = 99999999
soughtLetter = ""
for i in range(len(alphabet)):
    currLetter = alphabet[i]
    print("checking letter {0}".format(currLetter))
    newstr = str.replace(currLetter,"").replace(currLetter.upper(),"")
    while True:
        reacted = re.sub("Aa|Bb|Cc|Dd|Ee|Ff|Gg|Hh|Ii|Jj|Kk|Ll|Mm|Nn|Oo|Pp|Qq|Rr|Ss|Tt|Uu|Vv|Ww|Xx|Yy|Zz|aA|bB|cC|dD|eE|fF|gG|hH|iI|jJ|kK|lL|mM|nN|oO|pP|qQ|rR|sS|tT|uU|vV|wW|xX|yY|zZ","",newstr)
        if reacted == newstr:
            break
        else:
            newstr = reacted
    if len(reacted) < minLength:
        minLength = len(newstr)
        soughtLetter = currLetter
print(minLength)
print(soughtLetter)
