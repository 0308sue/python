from bitarray import test


text = "<title>지금은 문자열 연습입니다.</title>"

print(text[0:7])
print(text.find('문')) #있으면 위치값
print(text.find('파')) #없으면 -1
print(text.index('문')) #있으면 위치값
# print(text.index('파')) 없으연 오류

text1 = "        <title>지금은 문자열 연습입니다.</title>    "
text2 = ";"
print(text1.strip()+text2)
print(text1.lstrip()+text2)
print(text1.rstrip()+text2)
print(text.replace('<title>','<div>'))
print(text.replace('<title>',''))

import re
text3 = ('111<head>안녕하세요</head>22')
body = re.search('<head.*/head>',text3)
print(body)
body = body.group()
print(body)

#[0-9],[a-z]
#ab*c : abc,abbc,abbbc,abbbbbc
#*(1이상),+(0이상),?(0이상 1이하)

text4 = "<head>안녕하세요...<title>지금은 문자열 연습입니다.</title></head>"
body = re.search('<title.*/title>',text4)
body = body.group()
print(body)
body = re.sub('<.+?>','',body)
print(body)