from cv2 import *
from picamera import PiCamera
from picamera.array import PiRGBArray
from networktables import *
import grip

NetworkTables.initialize(server='roborio-167-frc.local')
table = NetworkTables.getTable('myContoursReport')

# class PiVideoStream:
#    def __init__(self):
#        self.camera = PiCamera()
#        self.camera.resolution = VisionMap.resolution
#        self.camera.framerate = VisionMap.framerate
#        self.camera.shutter_speed = VisionMap.exposure
#        self.camera.brightness = VisionMap.brightness
#        self.camera.sharpness = VisionMap.sharpness
#        self.camera.saturation = VisionMap.saturation
#        self.camera.rotation = VisionMap.rotation
#        self.rawCapture = PiRGBArray(self.camera, size=VisionMap.resolution)
#        self.stream = self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True)
camera = PiCamera()
camera.resolution = (410, 308)
camera.framerate = 24
rawCapture = PiRGBArray(camera, size=(410, 308))
for frame in camera.capture_continuous(rawCapture, format='bgr', use_video_port=True):
    image = frame.array
    processor = grip.NetworkTableTest()
    result = processor.process(image)
    data = cv2.boundingRect(result)
    for contour in frame:
        table.putNumber('x', data[0])
        table.putNumber('y', data[1])
        table.putNumber('width', data[2])
        table.putNumber('height', data[3])

# Ignore This code for now

# M = cv2.moments(result)
#  cX = int(M["m10"] / M["m00"])
# cy = int(M["m01"] / M['m00'])
