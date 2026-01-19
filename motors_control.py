class Motor:
    def __init__(self, name):
        self.name = name
        self.speed = 0

    def set_speed(self, speed):
        self.speed = speed
        print(f"Motor {self.name}: speed set to {self.speed}")


if __name__ == "__main__":
    left_motor = Motor("Left")
    right_motor = Motor("Right")

    left_motor.set_speed(50)
    right_motor.set_speed(50)
