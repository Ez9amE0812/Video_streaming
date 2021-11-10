import cv2

class VideoStream:
	def __init__(self, filename):
		self.filename = filename
		try:
			self.file = open(filename, 'rb')
		except:
			raise IOError
		self.frameNum = 0
		self.video = cv2.VideoCapture(self.filename)
		
	def nextFrame(self):
		"""Get next frame."""
		
		data = self.file.read(5) # Get the framelength from the first 5 bits
		if data: 
			framelength = int(data)
							
			# Read the current frame
			data = self.file.read(framelength)
			self.frameNum += 1
		return data
		

		
	def frameNbr(self):
		"""Get frame number."""
		return self.frameNum

	def totaltime(self):
		video = cv2.VideoCapture(self.filename)
		self.fps = video.get(cv2.CAP_PROP_FPS)
		self.frames = self.countframe(video)
		self.duration = self.frames / self.fps
		return self.duration


	def countframe(self, video):
		frames = 0
		while True:
			(grabbed, frame) = video.read()
			
			if not grabbed:
				break
			frames += 1
		return frames
