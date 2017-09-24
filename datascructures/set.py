bri = set(['a', 'b', 'c'])
'a' in  bri
'd' in  bri
bric = bri.copy()
bric.add('d')
bric.issuperset(bri)
bri.remove('b')
bri&bric