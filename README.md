# Robotic Arm Controller (MicroPython)

## Overview

This project implements a 4-DOF robotic arm controller using MicroPython on an Raspberry Pi Pico W.  
The system performs smooth multi-servo motion using linear interpolation between current and target angles.

The goal of this project is to explore embedded systems control, modular software architecture, and motion interpolation for robotic applications.

---

## Features

- 4 DOF servo control (Base, Translation, Elevation, Gripper)
- Smooth linear interpolation movement
- Configurable step resolution
- Adjustable movement speed
- Home positioning
- Modular and scalable architecture

---

## Hardware

- Raspberry Pi Pico W (MicroPython firmware)
- 4x Servo Motors (50Hz PWM)
- External 5V Power Supply (Recommended: ≥ 3A)
- Common ground between Raspberry Pi Pico W and servo power

⚠️ Servos should NOT be powered directly from the Raspberry Pi Pico W 3.3 pin.

---

## Software

- MicroPython
- Tested using Thonny IDE
- PWM frequency: 50Hz

---

## How It Works

Each servo maintains its current angle internally.  
When a new target position is requested:

1. The system reads current servo angles.
2. It computes the difference (delta) between current and target angles.
3. It gradually updates each servo position over a defined number of steps.
4. A small delay between steps controls movement speed.

This produces smooth, synchronized motion.

---

## Example Usage

```python
from arm import Arm

arm = Arm(15, 14, 13, 12)

angles = [180, 100, 150, 170]
arm.move_to(angles, steps=100, delay=0.01)

arm.home()
