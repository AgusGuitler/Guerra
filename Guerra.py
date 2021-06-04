import random

valores = {"Dos": 2, "Tres": 3, "Cuatro": 4, "Cinco": 5, "Seis": 6, "Siete": 7, "Ocho": 8, "Nueve": 9, "Diez": 10, "Sota": 11, "Reina": 12, "Rey": 13, "As": 14}
palos = ("corazones", "pica", "diamantes", "trébol")
rangos = ("Dos", "Tres", "Cuatro", "Cinco", "Seis", "Siete", "Ocho", "Nueve", "Diez", "Sota", "Reina", "Rey", "As")


class Carta():
    
    def __init__ (self, palo, rango):
        self.palo = palo
        self.rango = rango
        self.valor = valores[rango]
    
    def __str__ (self):
        return self.rango + " de " + self.palo
        

class Mazo():
    
    def __init__ (self):
    #NO toma ninguna entrada del usuario porque cada mazo debería ser igual independientemente del usuario
        self.all_cards = []
        
        for palo in palos:
            for rango in rangos:
                carta_creada = Carta(palo,rango)
                
                self.all_cards.append(carta_creada)
                
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
        
    def eliminar_una(self):
        return self.all_cards.pop()


class Jugador():
    
    def __init__ (self, name):
        
        self.name = name
        self.all_cards = []
        
    
    def quitar_una(self):
        return self.all_cards.pop(0)
    
    
    def agregar_cartas(self, nuevas_cartas):
        
        if type(nuevas_cartas) == type([]):
            self.all_cards.extend(nuevas_cartas)
        
        else:
            self.all_cards.append(nuevas_cartas)  


jugador1 = Jugador("Uno")
jugador2 = Jugador("Dos")

nuevo_mazo = Mazo()
nuevo_mazo.shuffle()

for x in range(26):
    jugador1.agregar_cartas(nuevo_mazo.eliminar_una())
    jugador2.agregar_cartas(nuevo_mazo.eliminar_una())


juego = True

ronda = 0

while juego:
    
    ronda += 1
    print (f"Ronda {ronda}")
    
    if len(jugador1.all_cards) == 0:
        print("Jugador 1 se quedó sin cartas! Gana el jugador 2!")
        juego = False
        break
        
    if len(jugador2.all_cards) == 0:
        print("Jugador 2 se quedó sin cartas! Gana el jugador 1!")
        juego = False
        break
    
    jugador1_cartas_jugadas = []
    jugador1_cartas_jugadas.append(jugador1.quitar_una())
    
    jugador2_cartas_jugadas = []
    jugador2_cartas_jugadas.append(jugador2.quitar_una())
    
    
    guerra = True
    
    while guerra:
        
        if jugador1_cartas_jugadas[-1].valor > jugador2_cartas_jugadas[-1].valor:
            
            jugador1.agregar_cartas(jugador1_cartas_jugadas)
            jugador1.agregar_cartas(jugador2_cartas_jugadas)
            print("Jugador 1 gana la ronda")
            print(f"El jugador 1 tiene {len(jugador1.all_cards)} y el jugador 2 tiene {len(jugador2.all_cards)}")
            
            guerra = False
            
        
        elif jugador1_cartas_jugadas[-1].valor < jugador2_cartas_jugadas[-1].valor:
            
            jugador2.agregar_cartas(jugador1_cartas_jugadas)
            jugador2.agregar_cartas(jugador2_cartas_jugadas)
            print("Jugador 2 gana la ronda")
            print(f"El jugador 2 tiene {len(jugador2.all_cards)} y el jugador 1 tiene {len(jugador1.all_cards)}")
            guerra = False
            
        else:
            print("Habemus Guerra!")
            
            if len(jugador1.all_cards) < 5:
                print("El jugador 1 no tiene suficientes cartas para la guerra")
                print("Ganador: Jugador 2!")
                juego = False
                break
            
            if len(jugador2.all_cards) < 5:
                print("El jugador 2 no tiene suficientes cartas para la guerra")
                print("Ganador: Jugador 1!")
                juego = False
                break
                
            else:
                for num in range(5):
                    jugador1_cartas_jugadas.append(jugador1.quitar_una())
                    jugador2_cartas_jugadas.append(jugador2.quitar_una())