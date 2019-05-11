programowanie = ['Python', 'C#', 'JS', 'PHP', 'Java']

print (programowanie)
print(type(programowanie))

first = programowanie[0]
print(f'Pierwszy jezyk programowania: {first}')

last = programowanie[-1]
print(f'Ostatni jezyk programowania: {last}')

threeElements = programowanie[0:3]
print(f'Trzy jezyki programowania: {threeElements}')

programowanie.append('R')
print(programowanie)

ile = programowanie.count('Python')
print(ile)
programowanie.append('Python')
ile = programowanie.count('Python')'
print(ile)

iloscElem = len(programowanie)
print(iloscElem)

inneJezyki = ['C', 'C++']
programowanie.extend(inneJezyki)
print(programowanie)
print(inneJezyki)

print(id(programowanie))
print(id(inneJezyki))

nowa = programowanie
nowa.append('GO')
print(nowa)
print(programowanie)

nowa.clear();
print(nowa)
print(programowanie)
print(id(nowa))
print(id(programowanie))
