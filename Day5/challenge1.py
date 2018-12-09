import re
file = open("input.txt","r")
str = file.read()

while True:
    print("iteration")
    newstr = re.sub("Aa|Bb|Cc|Dd|Ee|Ff|Gg|Hh|Ii|Jj|Kk|Ll|Mm|Nn|Oo|Pp|Qq|Rr|Ss|Tt|Uu|Vv|Ww|Xx|Yy|Zz|aA|bB|cC|dD|eE|fF|gG|hH|iI|jJ|kK|lL|mM|nN|oO|pP|qQ|rR|sS|tT|uU|vV|wW|xX|yY|zZ","",str)
    if newstr == str:
        break
    else:
        str = newstr
print(newstr)
print(len(newstr))
