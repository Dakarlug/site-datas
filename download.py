import urllib , os
for url in set(open('links.md').readlines()):
    data  = urllib.urlopen(url).read()
    name  = 'datas/%s' % url.split('/')[-1]
    name  = name.replace("\n", "")
    if os.path.exists(name):
        continue
    print name 
    with open(name, 'wb+') as f:
        f.write(data)
