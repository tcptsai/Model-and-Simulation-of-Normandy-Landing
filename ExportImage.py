from PIL import Image
import numpy as np


def exportImage(t, mp, bks):
	mapfile = open("image/" + mp + ".txt", "r+")
	data = []
	for line in mapfile:
		data.append(line.split(" ")[:-1])
	mapfile.close()

	# print(data)

	pedfile = open("images2/test" + str(t) + ".csv", "r+")
	for line in pedfile:
		temp = line.split(",")
		data[int(temp[1])][int(temp[0])] = -1
		data[int(temp[1]) - 1][int(temp[0]) - 1] = -1
		data[int(temp[1])][int(temp[0]) - 1] = -1
		data[int(temp[1]) + 1][int(temp[0]) - 1] = -1
		data[int(temp[1]) - 1][int(temp[0])] = -1
		data[int(temp[1]) + 1][int(temp[0])] = -1
		data[int(temp[1]) - 1][int(temp[0]) + 1] = -1
		data[int(temp[1])][int(temp[0]) + 1] = -1
		data[int(temp[1]) + 1][int(temp[0]) + 1] = -1
	pedfile.close()

	pedfile2 = open("images2/ship" + str(t) + ".csv", "r+")
	for line in pedfile2:
		temp = line.split(",")
		for i in range(10):
			for j in range(-2, 3):
				data[int(temp[1]) + i][int(temp[0]) + j] = -2
	pedfile2.close()

	w, h = len(data[0]), len(data)
	matrix = np.zeros((h, w, 3), dtype=np.uint8)



	for i in range(h):
		for j in range(w):
			if int(data[i][j]) == 0:
				matrix[i, j] = [0, 128, 255]
			elif int(data[i][j]) == 1:
				matrix[i, j] = [255, 255, 0]
			elif int(data[i][j]) == 2:
				matrix[i, j] = [255, 128, 0]
			elif int(data[i][j]) == 3:
				matrix[i, j] = [128, 128, 0]
			elif int(data[i][j]) == -1:
				matrix[i, j] = [0, 0, 0]
			elif int(data[i][j]) == -2:
				matrix[i, j] = [255, 0, 0]
			else:
				matrix[i, j] = [255, 0, 0]

	for b in bks:
		if b.dead:
			for i in range(-10, 11):
				for j in range(-10, 11):
					matrix[b.center[1] + i, b.center[0]+ j] = [0, 255, 0]

	img = Image.fromarray(matrix, 'RGB')
	img.save("images2/sol" + str(t) + ".png")
