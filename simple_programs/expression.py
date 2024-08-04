import re
text = "Hi, my name is vignesh . I am an python programmer. I am from 3rd year cse of CBIT"
info = {'year':'-','branch':'-','knowledge on python ':'no'}
if re.findall('^hi|Hi',text) :
    print("hi")
# finding which year do the text person is from
year = re.findall('[0-9]+.*year',text)
year = year[0]
info['year']= year
# finding which branch the text person is from
br = ['cse','CSE','ece','ECE','eee','EEE']
for i in br :
    if re.findall(i, text) :
        info['branch'] = i
# lets see do the user has the knowledge on python or not
if re.findall('python|Python',text):
    info['knowledge on python '] = 'yes'
print(info)