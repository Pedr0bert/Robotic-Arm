from time import sleep
from arm import Arm

arm = Arm(15, 14, 13, 12)

while True:
    
    base_angle=180
    angles = [base_angle, 100, 150, 170]
    arms.move_to(angles, 100, 0.01) # , 170 par a garra
    sleep(1)
    arms.home()
    
    sleep(1)
    
    base_angle =   0
    angles = [base_angle, 100, 150, 0]
    arms.move_to(angles, 100, 0.02) # , 170 par a garra
    sleep(1)
    arms.home()