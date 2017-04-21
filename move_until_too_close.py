from piconzero import piconzero as pz
from piconzero import hcsr04
import time

def get_dist_in_cm():
  dist = hcsr04.getDistance()
  if dist > 1600:
    dist = 0
  print "Distance in Cm", dist
  return dist


try:
  pz.init()
  hcsr04.init()
  pz.forward(40)
  while get_dist_in_cm() > 7.0:
    time.sleep(0.02)
  print "Thats close enough!"
finally:
  pz.stop()
  pz.cleanup()
  hcsr04.cleanup()
