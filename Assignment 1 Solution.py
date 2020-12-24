#!/usr/bin/env python
# coding: utf-8

# In[14]:


import PyPDF2
import itertools


def extractTextList(self):
    text_list = []
    content = self["/Contents"].getObject()
    if not isinstance(content, ContentStream):
        content = ContentStream(content, self.pdf)

    for operands, operator in content.operations:
        if operator == b_("Tj"):
            _text = operands[0]
            if isinstance(_text, TextStringObject) and len(_text.strip()):
                text_list.append(_text.strip())
        elif operator == b_("T*"):
            pass
        elif operator == b_("'"):
            pass
            _text = operands[0]
            if isinstance(_text, TextStringObject) and len(operands[0]):
                text_list.append(operands[0])
        elif operator == b_('"'):
            _text = operands[2]
            if isinstance(_text, TextStringObject) and len(_text):
                text_list.append(_text)
        elif operator == b_("TJ"):
            for i in operands[0]:
                if isinstance(i, TextStringObject) and len(i):
                    text_list.append(i)
    return text_list

from PyPDF2.pdf import PageObject, u_, ContentStream, b_, TextStringObject
PageObject.extractTextList = extractTextList


def between(text_elements, drop_while, take_while):    
    return list(itertools.takewhile(take_while, itertools.dropwhile(drop_while, text_elements)))[1:]    

pdfFileObj = open('C:/Users/Lenovo/Downloads/Assignment-1.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
page0 = pdfReader.getPage(0)
text_elements = page0.extractTextList()
print("name")
lines = between(text_elements, lambda x: x != 'First name', lambda x: 'Planning Portal Reference' not in x)
lines.remove('Surname')
lines.remove('Address line 2')
lines.remove('Address line 3')
lines.remove('Town/city')
lines.remove('Country')
print('\n'.join(lines))

print("\t")
page1 = pdfReader.getPage(1)
text_elements = page1.extractTextList()
lines1 = between(text_elements, lambda x: x != 'Miss', lambda x: 'Primary number' not in x)
lines1.remove('Address line 2')
lines1.remove('Address line 3')
lines1.remove('This is the Space')
lines1.remove('Town/city')
lines1.remove('Country')
print('\n'.join(lines1))

print("\t")
page2 = pdfReader.getPage(2)
text_elements = page2.extractTextList()
print("materials : ")
lines2 = between(text_elements, lambda x: x != 'Description of proposed materials and finishes:', lambda x: 'Are you supplying additional information on submitted plans, drawings or a design and access statement?' not in x)
lines2.remove('Roof')
lines2.remove('Description of existing materials and finishes (optional):')
lines2.remove('None')
lines2.remove('Description of proposed materials and finishes:')
lines2.remove('Windows')
lines2.remove('Doors')
lines2.remove('Description of existing materials and finishes (optional):')
lines2.remove('None')
lines2.remove('Description of proposed materials and finishes:')
lines2.remove('Description of existing materials and finishes (optional):')
lines2.remove('None')
lines2.remove('Description of proposed materials and finishes:')
print('\n'.join(lines2))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




