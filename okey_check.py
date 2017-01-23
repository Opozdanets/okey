import requests
import re


prodcut_urls = ['https://www.okeydostavka.ru/spb1/kofe-molotyi-lavatstsa-krem-gusto-250g-pach-619107-parent-20', \
          'https://www.okeydostavka.ru/spb1/bumaga-tual-zewa-plius-romashka-2sl-4sht--451580-parent-20']

product_info = []
for r in prodcut_urls:
    print(r)
    response = requests.get(r,verify=False)
    response_text = response.text
    pi = re.findall(r'var product = {.*url', response_text)
    product_info.append(pi)

for items in product_info:
    #print(type(items))
    if len(items) == 2:
        s = items[1].replace("var product = {", '')
        s = s.replace(', url', "")
        # print(s)
        s = s.split(',')
        print(s[0], s[1], s[7])
    else:
        s = items[0].replace("var product = {", '')
        s = s.replace(', url', "")
        # print(s)
        s = s.split(',')
        print(s[0], s[1], s[7])

        #r = requests.get('https://www.okeydostavka.ru/spb1/kofe-molotyi-lavatstsa-krem-gusto-250g-pach-619107-parent-20',
#                 verify=False)
#r1 = requests.get('https://www.okeydostavka.ru/spb1/bumaga-tual-zewa-plius-romashka-2sl-4sht--451580-parent-20',verify=False)
# print(r.text)

#product_info = re.findall(r'var product = {.*url', r.text)
#product_info1 = re.search(r'var product = {.*url', r1.text)

#content = r.text

#filtered = "".join([s for s in content.strip().splitlines(True) if s.strip()])


#pi1 = product_info1.group()

#pi = pi.replace('var product = ', '')
#pi1 = pi1.replace('var product = ', '')

#print(filtered)
#print(pi)
#print(pi1)

#test = pi.split(',')

#print(test)

#print(filtered)