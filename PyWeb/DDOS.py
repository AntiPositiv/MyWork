import requests
#
a = []
for i in range(100):
    req = requests.get('https://sites.google.com/site/donschool8')
    if not (req in a):
        a.append(req)
        print(a)