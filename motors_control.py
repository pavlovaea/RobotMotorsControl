import time


class Motor:
    def __init__(self, name):
        self.name = name
        self.speed = 0

    def set_speed(self, speed):
        self.speed = speed
        print(f"Motor {self.name}: speed set to {self.speed}")

    def smooth_speed_change(self, target_speed, step=5, delay=0.1):
        while self.speed != target_speed:
            if self.speed < target_speed:
                self.speed += step
            else:
                self.speed -= step

            if abs(self.speed - target_speed) < step:
                self.speed = target_speed

            print(f"Motor {self.name}: speed {self.speed}")
            time.sleep(delay)


if __name__ == "__main__":
    left_motor = Motor("Left")
    right_motor = Motor("Right")

    speed = int(input("Enter target speed: "))

    left_motor.smooth_speed_change(speed)
    right_motor.smooth_speed_change(speed)
