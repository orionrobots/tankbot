"""Simple demo.
>>> import tankbot as tb
>>> tb.move_and_turn()
"""
import time
from piconzero import piconzero as pz
pz.init()

turret = 0

pz.setOutputConfig(turret, 2)

def move_and_turn():
    try:
        pz.forward(60)
        time.sleep(1)
        pz.setOutput(turret, 70)
        time.sleep(1)
        pz.setOutput(turret, 100)
        time.sleep(1)
        pz.setOutput(turret, 90)
        time.sleep(1)
    finally:
        pz.stop()
