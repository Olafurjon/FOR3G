## Variacion del algoritmo de busqueda A*: con coste de movimiento fijo.
## Importante: no utiliza movimientos diagonales.
##
## Por: Francisco Rivera.

        
class Nodo:

    def __init__(self, x, y, tipo):
        self.x = x
        self.y = y
        self.tipo = tipo
        self.g = 0
        self.f = 0
        self.padre = None
        
    def __str__(self):
        return "Tipo: " + str(self.tipo) + " x: " + str(self.x) + " y: " + str(self.y)
        
    def set_padre(self, nodo):
        self.padre = nodo
        
    def set_f(self, h):
        self.f = self.g + h
        
    def set_g(self, g):
        self.g = g


class AStar:

    def __init__(self, nodos, x_com, y_com, x_fin, y_fin):
        self.nodos = nodos
        self.abiertos = set()
        self.cerrados = set()        
        self.set_comienzo(x_com, y_com)
        self.set_fin(x_fin, y_fin)
        self.encontro = True
        self.main()
        
    def main(self):
        cuadro_actual = self.inicio
        while cuadro_actual != self.final:
            # cierro el actual
            self.cerrados.add(cuadro_actual)
            self.abiertos.remove(cuadro_actual)
            # agrego los alrededores
            self.alrededor(cuadro_actual)
            # me posiciono en el mas barato
            t = self.getMasBarato()
            if t is None:
                self.encontro = False
                break
            else:
                cuadro_actual = t
        # recuperamos el camino
        n = cuadro_actual
        self.resultado = []
        while n.padre != None:
            self.resultado.append((n.x, n.y))#, n.f, n.g))
            n = n.padre
            
    def get(self):
        return self.resultado
        
    def set_comienzo(self, x, y):
        self.inicio = self.nodos[x, y]
        self.abiertos.add(self.inicio)
    
    def set_fin(self, x, y):
        self.final = self.nodos[x, y]
        
    def heuristica(self, nodo):
        h = (abs(nodo.x - self.final.x) + abs(nodo.y - self.final.y))
        #print nodo, "h:", h
        return h
        
    def getMasBarato(self):
        # devuelve el nodo con el menor F de toda la lista abierta
        min = 100000
        min_n = None
        for n in self.abiertos:
            if n == self.final:
                return n
            if n.f < min:
                min_n = n
                min = n.f
        return min_n
        
    def alrededor(self, nodo):
        # devuelve todos los nodos "caminables" y no cerrados alrededor de un nodo
        x = nodo.x
        y = nodo.y
        cuadrante = [[0, -1], [-1,  0], [1,  0], [0,  1]]
        for pos in cuadrante:
            n = self.nodos[x + pos[0], y + pos[1]]
            if n.tipo == 1 or n in self.cerrados:
                pass
            else:                
                if n not in self.abiertos:
                    n.set_padre(nodo)
                    n.set_g(nodo.g + 10)
                    n.set_f(self.heuristica(n))
                    self.abiertos.add(n)
                else:
                    if n.g < nodo.g:
                        n.set_padre(nodo)
                        n.set_g(nodo.g + 10)
                        n.set_f(self.heuristica(n))
                        self.abiertos.add(n)
                    else:
                        pass

        
# testing
if __name__ == '__main__':

    mapa = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
            [1, 0, 1, 3, 1, 0, 0, 2, 0, 1],
            [1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
            
    nodos = {}
    for y in range(len(mapa)):
        for x in range(len(mapa[y])):
            nodos[x, y] = Nodo(x, y, mapa[y][x])
            if mapa[y][x] == 3:
                x_f, y_f = x, y
            elif mapa[y][x] == 2:
                x_i, y_i = x, y
                
    AStar(nodos, x_i, y_i, x_f, y_f)