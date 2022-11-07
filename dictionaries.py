# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }
#extracting population of spain
print(europe['spain']['population'])
#addimg infor to the dict can be done 
data = {'capital':'rome', 'population':'67.1'}
europe['italy'] = data
print(europe)
