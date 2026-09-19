# A Program to build a computer using composition

class CPU:
    def process(self):
        print("CPU is processing data.")


class RAM:
    def load(self):
        print("RAM is loading data.")


class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.ram = RAM()

    def start(self):
        self.cpu.process()
        self.ram.load()
        print("Computer started.")


computer = Computer()

computer.start()


# Explanation:
# Computer creates both CPU and RAM objects internally.
# These objects become components of the Computer object.
# start() coordinates the behavior of both components.
# This demonstrates how larger objects can be constructed from smaller specialized objects.

# Real-Life Use:
# Composition is widely used in software systems where complex objects are assembled from smaller components.