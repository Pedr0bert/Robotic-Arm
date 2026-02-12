from machine import Pin, PWM
from time import sleep
from servo import Servo

class Arm():
    def __init__(self, pin_base, pin_transl, pin_alt , pin_garra):# , pin_garra
        self.base = Servo(pin_base)
        self.transl = Servo(pin_transl)
        self.alt = Servo(pin_alt)
        self.garra = Servo(pin_garra)
        self.servos = [self.base, self.transl, self.alt, self.garra]
    
        # Update TODO: Fazer no futuro uma segunda classe(subclasse) para que seja possivel
        # criar um braco e herdar de outra(no caso dessa classe) para ser possivel criar uma lista de bracos
        # para poderem agir juntas caso o braco tenha configuracoes diferentes e quantidades
        # diferentes de motores
        
        
    def _interpolate(self, angles: List, steps, delay): # Adicionar , simultaneous=True
        current_angles = [servo.angle for servo in self.servos]
        target_angles = angles
        
        
        # subtrair os angulos e calcular distancia
        delta = [target_angles[i] - current_angles[i] for i in range(len(current_angles))]
        #if simultaneous:
        for step in range(1, steps+1):
            for idx in range(len(servos)):
                intermediate_angle = current_angles[idx] + delta[idx]*(step/steps)
                servos[idx].set_angle(intermediate_angle)
            sleep(delay)
    
            
    def move_to(self,angle, steps=100, delay=0.01):
        self._interpolate(angle, steps, delay)
        
    def home(self):
        angle = [90 for i in range(len(self.servos))]
        self._interpolate(angle, 50,0.02  )