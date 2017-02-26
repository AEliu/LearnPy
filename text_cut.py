# coding: utf-8
import nltk

with open(r'D:\Calibre Library\Angela Duckworth\Grit (295)\Grit - Angela Duckworth.txt', 'r', encoding='utf-8') \
    as f:
    f.readline()
    doc = []
    for line in f:
        if line:
            doc.append(line.strip())
f.close()
sentence = []
for line in doc:
    st = nltk.sent_tokenize(line)
    sentence = sentence + st

st = '\n'.join(sentence)

with open('end.txt', 'w',encoding='utf-8' ) as f:
    f.write(st)
f.close()