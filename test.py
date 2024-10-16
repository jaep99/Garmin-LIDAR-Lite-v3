from python.lidar_lite import Lidar_Lite
import time

lidar = Lidar_Lite()
connected = lidar.connect(1)


if connected < -1:
  print("Not Connected")
while(1):
  print(f"Distance is {lidar.getDistance()}")
  #print(f"Velocity is {lidar.getVelocity()}")
  time.sleep(1)