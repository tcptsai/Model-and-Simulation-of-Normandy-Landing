from PIL import Image


class ImportImage:

	def __init__(self, beach, width, height, nBunker):
		self.beach = beach
		self.width = width
		self.height = height
		self.nBunker = nBunker
		self.matrix = [[-1 for x in range(self.height)] for x in range(self.width)]
		self.cone = [[] for x in range(nBunker)]

	def set(self):
		im = Image.open("image/" + self.beach + ".bmp").getdata()
		i = 0
		for y in range(self.height):
			for x in range(self.width):
				if im[i] == (0, 128, 255):
					self.matrix[x][y] = 0
				elif im[i] == (255, 255, 0):
					self.matrix[x][y] = 1
				elif im[i] == (255, 128, 0):
					self.matrix[x][y] = 2
				elif im[i] == (128, 128, 0):
					self.matrix[x][y] = 3
				else:
					for t in range(self.nBunker):
						if im[i] == (255, 0, t):
							self.matrix[x][y] = 4 + t
				i += 1
		im = Image.open("image/" + self.beach + "_cone.bmp").getdata()
		i = 0
		for y in range(self.height):
			for x in range(self.width):
				if im[i][1] > 0 and im[i][1] <= self.nBunker:
					self.cone[im[i][1] - 1].append((x,y))
				if im[i][2] > 0 and im[i][2] <= self.nBunker:
					self.cone[im[i][2] - 1].append((x,y))
				i += 1

	def writeFile(self):
		text_file = open("image/" + self.beach + ".txt", "w")
		for y in range(self.height):
			for x in range(self.width):
				text_file.write(str(self.matrix[x][y]) + " ")
			text_file.write("\n")
		text_file = open("image/" + self.beach + "_cone.txt", "w")
		for t in range(self.nBunker):
			for co in self.cone[t]:
				text_file.write(str(co) + ";")
			text_file.write("\n")

omaha = ImportImage("omaha", 6600, 1600, 13)
omaha.set()
omaha.writeFile()
print("omaha done")

utah = ImportImage("utah", 5600, 2100, 7)
utah.set()
utah.writeFile()
print("utah done")

gold = ImportImage("gold", 3700, 2100, 6)
gold.set()
gold.writeFile()
print("gold done")

juno = ImportImage("juno", 1800, 2400, 3)
juno.set()
juno.writeFile()
print("juno done")

sword = ImportImage("sword", 2500, 2500, 3)
sword.set()
sword.writeFile()
print("sword done")