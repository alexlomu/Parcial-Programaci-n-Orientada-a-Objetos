class Libro:
    def __init__(self, nombre, autor, genero, ISBN, paginas):
        self.nombre = nombre
        self.autor = autor
        self.genero = genero
        self.ISBN = ISBN
        self.paginas = paginas
    
    def get_nombre(self):
        return self.nombre
    def get_autor(self):
        return self.autor
    def get_genero(self):
        return self.genero
    def get_ISBN(self):
        return self.ISBN
    def get_paginas(self):
        return self.paginas
    
    def printLibro(self):
        print("\nNombre: "+str(self.get_nombre())+"\nAutor: "+str(self.get_autor())+"\nGenero: "+str(self.get_genero())+"\nISBN: "+str(self.get_ISBN())+"\nNumero de paginas: "+str(self.get_paginas()))

nombre = input("Introduzca el nombre del libro: ")
autor = input("Introduzca el autor del libro :" )
genero = input("Introduzca el género del libro: " )
ISBN = int(input("Introduzca el ISBN del libro: " ))
paginas = int(input("Introduzca el número de páginas del libro: "))

book = Libro(nombre, autor, genero, ISBN, paginas)
book.printLibro()