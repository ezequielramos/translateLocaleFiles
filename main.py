from googletrans import Translator
import json

translator = Translator()

with open('locale_pt.json','r') as file:
    pt = json.loads(file.read())

with open('locale_en.json','r') as file:
    en = json.loads(file.read())

with open('locale_es.json','r') as file:
    es = json.loads(file.read())

all = {}

for key in pt.keys():
    all[key] = {"pt":pt[key], "en": None, "es": None}

for key in en.keys():
    if key not in all:
        all[key] = {"pt":None, "en": en[key], "es": None}
    else:
        all[key]["en"] =  en[key]

for key in es.keys():
    if key not in all:
        all[key] = {"pt":None, "en": None, "es": es[key]}
    else:
        all[key]["es"] =  es[key]

for key in all:
    if all[key]['en'] == None:
        if all[key]['pt'] != None:
            all[key]['en'] = translator.translate(all[key]['pt'],dest='en').text
        else:
            all[key]['en'] = translator.translate(all[key]['es'],dest='en').text
    
    if all[key]['es'] == None:
        if all[key]['pt'] != None:
            all[key]['es'] = translator.translate(all[key]['pt'],dest='es').text
        else:
            all[key]['es'] = translator.translate(all[key]['en'],dest='es').text
    
    if all[key]['pt'] == None:
        if all[key]['en'] != None:
            all[key]['pt'] = translator.translate(all[key]['en'],dest='pt').text
        else:
            all[key]['pt'] = translator.translate(all[key]['es'],dest='pt').text

print(all)