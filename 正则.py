import re
s = 'wer|w31'
text = re.search(s,'w3185476erwerwerwerwer')
print(text.groups())