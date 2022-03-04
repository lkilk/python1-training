import re

namesRegex = r'Agent \w+' #\w+ matches 1 or more 'word' characters 
sensitiveInfo = "\nAgent Alice sent the restricted emails to Agent Bond" 

print( sensitiveInfo , '\n')

redacted1 = re.sub( namesRegex, 'CENSORED', sensitiveInfo )

print ( redacted1 ,'\n')

agentNamesRegex = r'Agent (\w)\w*' # 1 subgroup '(\w)' defined

# \1 is a 'placeholder' for the (1st) subgroup in 'agentNamesRegex'
#r needed so \1 is not 'translated' as escape character

replaceRegex = r'\1***' 

sensitiveInfo = "Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent" ;

redacted2 = re.sub( agentNamesRegex, replaceRegex , sensitiveInfo )

print (redacted2, '\n')
