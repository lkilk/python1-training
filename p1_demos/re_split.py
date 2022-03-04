import re

Line = "This:line:is:separated:by:colons"

Line2 = "This:line;is:separated:by:a;mixture:of;colons:and:semi-colons"

print("\nLine before splitting based on : separator\n")
print(Line,"\n")
List1 = Line.split(":") # Returns a list 
print(List1,"\n")

print("Line2 before splitting based on : separator\n")
print(Line2,"\n")
List2 = Line2.split(":")
print(List2,"\n")

print("Line2 split into list using ; separator\n")
List3 = Line2.split(";")
print(List3,"\n")

print("Line2 split into list using ; and : separator\n")
List4 = re.split("[:;]",Line2)
print(List4,'\n')
