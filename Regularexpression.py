import re
line = "Learning Data Science"
matchObj = re.match(r'(.*) Data', line) 
print(matchObj)