import os
import threading
import pygame2
import pygame2.sdl
import pygame2.sdl.wm
import pygame2.sdl.time
import pygame2.sdl.mouse
import pygame2.sdl.event
import pygame2.sdl.video
import pygame2.sdl.keyboard
import pygame2.sdl.constants
import pygame2.sdlext
import pygame2.sdlext.draw
import pygame2.sdlgfx
from pathfinder import AStar, Nodo


class Bloque():
    
    def __init__(self, x, y, color):        
        self._update(x, y)
        if color == "rojo":
            self.color = pygame2.Color(255, 0, 0)
        else:
            self.color = pygame2.Color(0, 0, 255)       
        
    def _update(self, x, y):
        self.x = x
        self.y = y
        
    def update(self, x, y):
        self._update(x, y)
        
    def get(self):
        return self.x, self.y

        
class Enemigo(threading.Thread, Bloque):

    DELAY_MOV = 500
    
    def __init__(self, x, y, color, azul, mapa):
        threading.Thread.__init__(self)
        Bloque.__init__(self, x, y, color)
        self.azul = azul
        self.mapa = mapa
        self.andar = True
        self.bloqueado = False
        self.start()
        
    def run(self):
        while self.andar:
            self.update()
            pygame2.sdl.time.delay(self.DELAY_MOV)
                                
    def update(self):
        if not self.bloqueado:
            nodos = {}
            for y in range(len(self.mapa)):
                for x in range(len(self.mapa[y])):
                    if self.mapa[y][x] > 0:
                        id = 1
                    else:
                        id = 0
                    nodos[x, y] = Nodo(x, y, id)
            x_f, y_f = self.azul.x, self.azul.y
            x_i, y_i = self.x, self.y
            camino = AStar(nodos, x_i, y_i, x_f, y_f).get()
            if camino:
                self._update(camino[-1][0], camino[-1][1])
    
    
class Pantalla:

    def __init__(self):
        pygame2.sdl.video.init()
        self.pantalla = pygame2.sdl.video.set_mode((400, 400))
        pygame2.sdl.wm.set_caption("Pathfinder grafico")
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        self.fps_man = pygame2.sdlgfx.FPSmanager(30)
        
        self.azul = Bloque(8, 8, "azul")
        self.mapa = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
                     [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                     [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
                     [2, 0, 1, 0, 0, 0, 0, 0, 0, 2],
                     [2, 0, 1, 1, 0, 0, 1, 1, 0, 2],
                     [2, 0, 0, 1, 0, 0, 1, 0, 0, 2],
                     [2, 0, 0, 1, 1, 1, 1, 0, 0, 2],
                     [2, 0, 0, 0, 0, 0, 1, 0, 0, 2],
                     [2, 0, 0, 0, 0, 0, 1, 0, 0, 2],
                     [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]                            
        self.rojo = Enemigo(2, 2, "rojo", self.azul, self.mapa)
        
        self.main()
        
    def main(self):
        while True:
            # dibujamos mapa
            for y in range(len(self.mapa)):
                for x in range(len(self.mapa[y])):
                    if self.mapa[y][x]:
                        color = pygame2.Color(0, 0, 0)
                    else:
                        color = pygame2.Color(255, 255, 255)
                    rx = x * 40
                    ry = y * 40
                    pygame2.sdlext.draw.rect(self.pantalla, color, pygame2.Rect(rx, ry, 40, 40))
            # dibujamos bloques
            rx = self.rojo.x * 40
            ry = self.rojo.y * 40
            pygame2.sdlext.draw.rect(self.pantalla, self.rojo.color, pygame2.Rect(rx, ry, 40, 40))
            rx = self.azul.x * 40
            ry = self.azul.y * 40
            pygame2.sdlext.draw.rect(self.pantalla, self.azul.color, pygame2.Rect(rx, ry, 40, 40))
            # refrescamos
            pygame2.sdl.event.pump()
            self.pantalla.flip()
            # handler de teclado y mouse
            if not self.update():
                break
            self.fps_man.delay()
        self.rojo.andar = False
        pygame2.sdl.video.quit()
    
    def update(self):
        # handler teclado
        teclas = pygame2.sdl.keyboard.get_state()                
        if teclas[pygame2.sdl.constants.K_ESCAPE]:
            return False
        elif teclas[pygame2.sdl.constants.K_LEFT]:
            x, y = self.azul.get()
            if not self.mapa[y][x - 1]:
                self.azul.update(x - 1, y)
        elif teclas[pygame2.sdl.constants.K_RIGHT]:
            x, y = self.azul.get()
            if not self.mapa[y][x + 1]:
                self.azul.update(x + 1, y)
        elif teclas[pygame2.sdl.constants.K_UP]:
            x, y = self.azul.get()
            if not self.mapa[y - 1][x]:
                self.azul.update(x, y - 1)
        elif teclas[pygame2.sdl.constants.K_DOWN]:
            x, y = self.azul.get()
            if not self.mapa[y + 1][x]:
                self.azul.update(x, y + 1)       
        # handler ventana
        for evento in pygame2.sdl.event.get():
            if evento.type == pygame2.sdl.constants.QUIT:
                return False
        # handler mouse
        mouse = pygame2.sdl.mouse.get_state()
        if mouse[0] == 1:
            # ponemos pared
            x, y = mouse[1], mouse[2]
            x = x // 40
            y = y // 40
            if self.mapa[y][x] == 0:
                self.mapa[y][x] = 1
        elif mouse[0] == 4:
            # borramos pared
            x, y = mouse[1], mouse[2]
            x = x // 40
            y = y // 40
            if self.mapa[y][x] == 1:
                self.mapa[y][x] = 0
        return True
    
    
Pantalla()