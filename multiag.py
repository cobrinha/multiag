from visual import *
from Tkinter import *
import time
from random import random, randrange
import math
import os

class ex_multiagente:
    bola       = []
    bolax      = []
    bolay      = []
    bolah      = []
    posx       = []
    posy       = []         
    somax      = []         
    somay      = []         
    agente     = []
    angulo     = []

    def mover(self,z,t):
        if(t == 1):
            #controlando x
            if(self.posx[z] > 60):
                self.somax[z] = false
            elif(self.posx[z] < -60):
                self.somax[z] = true
            if(self.somax[z]==true):
                self.newx = self.posx[z] + self.velocx
            else:
                self.newx = self.posx[z] - self.velocx
            #controlando y
            if(self.posy[z] > 58):
                self.somay[z] = false
            elif(self.posy[z] < -58):
                self.somay[z] = true
            if(self.somay[z]==true):
                self.newy = self.posy[z] + self.velocy
            else:
                self.newy = self.posy[z] - self.velocy
            self.posx[z] = self.newx            
            self.posy[z] = self.newy
            newpos = (self.newx,self.newy, 20)
            self.agente[z].pos = newpos
        elif(t == 2):
            #controlando x
            if(self.posx[z] > 58):
                self.somax[z] = false
            elif(self.posx[z] < -58):
                self.somax[z] = true
            if(self.somax[z]==true):
                self.newx = self.posx[z] + 1
            else:
                self.newx = self.posx[z] - 1
            #controlando y
            if(self.posy[z] > 58):
                self.somay[z] = false
            elif(self.posy[z] < -58):
                self.somay[z] = true
            if(self.somay[z]==true):
                self.newy = self.posy[z] + 1
            else:
                self.newy = self.posy[z] - 1
            self.posx[z] = self.newx            
            self.posy[z] = self.newy
            newpos = (self.newx,self.newy, 20)
            self.agente[z].pos = newpos
        elif(t == 3):
            #angulo = randrange(0, 6.28 * int(100000) / int(100000) - 3.14)
            angulo = randrange(0, 1000000)
            angulo = (angulo * 6.28) - 3.14
            radiano = angulo
            veloc   = self.velocx
                
            if(self.somax[z]==1):
                self.newx = self.posx[z] + math.cos(self.angulo[z] + radiano) * int(veloc)
            else:
                self.newx = self.posx[z] - math.cos(self.angulo[z] + radiano) * int(veloc)
        
            if(self.somay[z]==1):
                self.newy =  self.posy[z] + math.sin(self.angulo[z] + radiano) * int(veloc)
            else:
                self.newy =  self.posy[z] - math.sin(self.angulo[z] + radiano) * int(veloc)

            if (self.newx > 58):
                self.newx = 58
            elif (self.newx < -58):
                self.newx = -58
            
            if (self.newy > 58):
                self.newy = 58
            elif (self.newy < -58):
                self.newy = -58

        self.posx[z] = self.newx            
        self.posy[z] = self.newy
        newpos = (self.newx,self.newy, 20)
        self.agente[z].pos = newpos

    def pegar(self):
        z = 0
        for z in range(self.total_ag):
            self.mover(z,self.tipo)
            i = 0
            while i < self.total_bo:
                if(self.bolah[i] == 1):                
                    if((self.bolax[i] <= (self.newx + 2)) and (self.bolax[i] >= (self.newx - 2))):
                        if((self.bolay[i] <= (self.newy + 2)) and (self.bolay[i] >= (self.newy - 2))):                        
                            self.agente[z].color = color.green
                            '''self.bola[i].color   = color.yellow'''
                            self.bola[i].visible   = 0                        
                            self.bolax[i] = ''
                            self.bolay[i] = ''
                            self.total_el = self.total_el + 1
                i = i + 1
                if (int(self.tempo) != int(time.time())):
                    self.tempo = int(time.time())
                    label(pos=(-70,-60,10), text='Eliminados: '+str(self.total_el)+'\nTempo: '
                                + str(int(time.time()) - int(self.start)) , height=10, border=6)
            
    def __init__(self, total_ag, total_bo, velocx, velocy, tipo):
        scene.title = 'Exemplo de MultiAgentes'
        self.total_ag      = int(total_ag)
        self.total_bo      = int(total_bo)
        self.velocx        = int(velocx)
        self.velocy        = int(velocy)
        self.tipo          = int(tipo)                  
        self.y             = -70        
        self.x             = 70
        self.newx          = 0        
        self.newy          = 0
        self.total_el      = 0          
        self.tempo         = 0
        self.start         = int(time.time()) - int(0)
        self.pos_mundo     = [(self.y,self.y),(self.y,self.x),(self.x,self.x),(self.x,self.y),(self.y,self.y)]
        self.mundo         = curve(pos=self.pos_mundo, color=color.white)
        i                  = 0
        while i < self.total_bo:
            xx = randrange (-60,60)
            yy = randrange (-60,60)
            hh = randrange (1,4)
            if(hh == 1):
                cor = color.white
            elif(hh ==2):
                cor = color.red
            elif(hh ==3):
                cor = color.blue
            self.bola.append(sphere(pos=vector(xx, yy, 10), color=cor, radius=hh))
            self.bolax.append(xx)
            self.bolay.append(yy)
            self.bolah.append(hh)            
            i = i + 1
        for z in range(self.total_ag):
            self.posx.append(randrange(-60,60))
            self.posy.append(randrange(-60,60))
            self.agente.append(box(pos=(self.posx[z],self.posy[z],10), length=2, height=2, width=2))
            self.somax.append(z)            
            self.somay.append(z)
            self.angulo.append(randrange(0,360))


#INTERFACE/TKINTER
def butOkClick():
    cMAgente = ex_multiagente(txtAg.get(1.0, END),txtBo.get(1.0, END),
                              txtVelx.get(1.0, END),txtVely.get(1.0, END), lstTipo.get(ACTIVE))
    tkr.destroy()    
    while 1:
        rate(50)
        cMAgente.pegar()
            
tkr = Tk()
tkr.title('Config')
frm = Frame(tkr,width=600, height=600)
frm.pack(expand='no', padx=10, pady=10)
lblAg = Label(frm, text='Total de Agentes:')
lblAg.pack(side = "top", expand = 1, pady=5)
txtAg = Text(frm, height=1, width=30)
txtAg.insert(END, "5")
txtAg.pack(side = "top", expand = 1, pady=5)
lblBo = Label(frm, text='Total de Residuos:')
lblBo.pack(side = "top", expand = 1, pady=5)
txtBo = Text(frm, height=1, width=30)
txtBo.insert(END, "200")
txtBo.pack(side = "top", expand = 1, pady=5)
lblVelx = Label(frm, text='Velocidade x:')
lblVelx.pack(side = "top", expand = 1, pady=5)
txtVelx = Text(frm, height=1, width=30)
txtVelx.insert(END, "2")
txtVelx.pack(side = "top", expand = 1, pady=5)
lblVely = Label(frm, text='Velocidade y:')
lblVely.pack(side = "top", expand = 1, pady=5)
txtVely = Text(frm, height=1, width=30)
txtVely.insert(END, "3")
txtVely.pack(side = "top", expand = 1, pady=5)

#listbox
lblTipo = Label(frm, text='Selecione o tipo:')
lblTipo.pack(side = "top", expand = 1, pady=5)
lstTipo = Listbox(frm, width=30,height=4)
for item in ["1", "2", "3"]:
    lstTipo.insert(END, item)
lstTipo.pack()

butOk = Button(frm, command=butOkClick, text= "Iniciar", width="30", height="2")
butOk.pack(side = "top", expand = 1, pady=5)
tkr.mainloop() # Tk event loop
