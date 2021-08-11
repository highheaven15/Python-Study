x = [(('subject', 'to'), 18), (('subject', 'and'), 5), (('subject', 'of'), 4), (('subject', 'the'), 3), (('subject', 'that'), 2), (('subject', 'owing'), 2), (('subject', 'making'), 2)]

x=list(map(lambda el:el[0][1], x))

print(x)

#['to', 'and', 'of', 'the', 'that', 'owing', 'making']
