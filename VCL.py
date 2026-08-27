import time

class VCL:
    def apl_open(self):
        print("Application opened")
        time.sleep(2)
    
    def video_start(self):
        print("Video started")
        time.sleep(2)
    
    def audio_start(self):
        print("Audio started")
        time.sleep(2)
        
    def volume(self):
        print("Volume increased")
        time.sleep(2)
    
    def prog_bar(self):
        print("Progress bar activated")
        time.sleep(2)
    
v1 = VCL()
v1.apl_open()
v1.video_start()
v1.audio_start()
v1.volume()
v1.prog_bar()

print("Application closed")