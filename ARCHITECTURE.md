
---

# 📄 architecture.md

```markdown
# System Architecture

## Overview

The system follows a modular object-oriented design, separating low-level servo control from high-level arm coordination logic.

The architecture is composed of two main classes:

- `Servo`
- `Arm`

---

## Class: Servo

### Responsibility

Handles low-level PWM control and angle management for a single servo motor.

### Attributes

- `pwm` → PWM object configured at 50Hz
- `min_duty` → Minimum PWM duty cycle
- `max_duty` → Maximum PWM duty cycle
- `angle` → Current servo angle (state tracking)

### Methods

#### `set_angle(angle)`

- Clamps angle between 0° and 180°
- Converts angle to PWM duty cycle
- Updates servo position
- Stores the current angle internally

This internal state tracking allows smooth interpolation.

---

## Class: Arm

### Responsibility

Coordinates multiple servo motors and executes synchronized motion.

### Attributes

- `base`
- `transl`
- `alt`
- `garra`
- `servos` → List containing all servo objects

Using a list enables scalable architecture (easy expansion to more DOF).

---

## Core Method: `_interpolate()`

### Purpose

Performs smooth motion between current and target positions.

### Steps

1. Read current angles from all servos
2. Compute delta for each servo
3. Iterate over a fixed number of steps
4. Update servo angles proportionally
5. Apply delay to control movement speed

### Motion Equation

For each step:

intermediate = current + delta * (step / total_steps)

This produces linear interpolation across time.

---

## Public Methods

### `move_to(angles, steps, delay)`

Moves all servos to the specified angles using interpolation.

### `home()`

Returns all servos to default 90° position.

---

## Design Principles

- Separation of concerns
- State-based servo tracking
- Scalable DOF support
- Hardware abstraction
- Embedded-friendly architecture

---

## Scalability

The system is designed to support:

- Additional servos
- Sequential motion mode
- Advanced motion profiles
- Higher-level kinematic control

Future refactoring may include:

- Motion profile abstraction
- Multi-arm controller class
- Current-aware movement scheduling
