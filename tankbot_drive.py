"""Drive until we get too close
https://github.com/4tronix/PiconZero
"""
from piconzero import piconzero as pz
from gpiozero import DistanceSensor
import time


def main():
    dist = DistanceSensor(echo=38, trigger=38)

    pz.init()
    pz.forward(60)
    dist.wait_for_out_of_range()
    pz.stop()

    pz.cleanup()


if __name__ == '__main__':
    main()
