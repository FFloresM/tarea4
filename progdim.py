

def leer(file):
	""" Lee un un archivo de texto con una lista de objetos """
	g = {}
	letra = valor = None
	with open(file, 'r') as file:
		content = file.read().splitlines()
	for i in content:
		for x in i:
			if x.isalpha():
				letra = x
			elif x.isdigit():
				valor = int(x)
		g[letra] = valor
		
	return g

g = leer('objetos.txt')
print(g)



