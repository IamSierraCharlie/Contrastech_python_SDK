import cv2
import linux_cams_sdk

sensor_width = 1280
sensor_height = 1024
# Ideally, you should select PAL or NTSC supported resolutions
# others work, but its a bit hit and miss
img_width = 640
img_height = 640
channels = 3
# this is here to show that you probably should set the framerate of the camera and the framerate
# of the cv2 window the same.  I had problems here and this appeared to resolve them

# ToDo:  make changes here so you can set more settings
target_framerate = 23
framerate_cv2_window = int(1000/target_framerate)
camera = linux_cams_sdk.Camera(sensor_width, sensor_height, img_width, img_height, channels)
camera.change_setting(setting="TriggerSource", option='Software')
camera.change_setting(setting="TriggerSelector", option='FrameStart')
camera.change_setting(setting='AcquisitionMode', option='Continuous')
# activates the camera - light should start flashing on the back
camera.change_setting(setting="TriggerMode", option='On')
camera.activate()
camera.change_setting(setting="ExposureAuto", option='Off')
camera.change_setting(setting="ExposureTime", option=15000)  # will fail if ExposureAuto is not set to Off First

while True:
    image = camera.grab_image()
    corrected_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cv2.imshow('Contrastech Mars USB3 Vision Camera Test', corrected_image)
    k = cv2.waitKey(framerate_cv2_window)
    #print(k)
    if k == 1048603:  # Esc key to stop
        # camera.change_setting(setting=b"TriggerMode", option=b'Off')
        camera.deactivate()
        break

# deactivates the camera - light should stop flashing on the back

# camera.activate()

# camera.change_setting(setting=b"ExposureAuto", option=b'Continuous')
# acquisitrion framerate
# camera.change_setting(setting=b"AcquisitionFrameRateEnable", option=False)
# camera.change_setting(setting=b"AcquisitionFrameRate", option=target_framerate)
# camera.change_setting(setting=b"AcquisitionFrameRateEnable", option=True)
# Notes - this setting will impact the exposure time and may fail
# due to the selected framerate being too high for the requested exposure time






