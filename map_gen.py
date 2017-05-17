from sys import maxint
from sets import Set
from ast import literal_eval

class Cell:
	def __init__(self, ctype):
		self.cell_type = ctype
		self.fields = [9999.0]*3
		self.cones = []
		self.neighbors = []
		self.xy = ()

mapfile = open("image/sword.txt", "r+")
data = []
for line in mapfile:
	data.append(line.split(" ")[:-1])

bunkers = {}
cells = []

for i in range(len(data)):
	row = []
	for j in range(len(data[0])):
		c = int(data[i][j])
		# if c == 0 :
		# 	continue
		cell = Cell(c)
		row.append(cell)
		if c > 3:
			if c in bunkers.keys():
				bunkers[c].append((i,j)) # row, col
			else:
				bunkers[c] = [(i,j)]
	cells.append(row)

print len(cells)
print len(cells[0])

print "done loading map"

confile = open("image/sword_cone.txt")
bunkerID = 4
for line in confile:
	coords = line.split(";")[:-1]
	for c in coords:
		xy = literal_eval(c)
		cells[xy[0]][xy[1]].cones.append(bunkerID)
	bunkerID += 1

print "done doing cones"

#find center of each target
#the first cell of each target is the top left most cell
#bunkers are "concave up" on top
#find top left most and right most, then middle of top most line, then all the way down and take the middle which is roughly the center

for tgroup in bunkers.keys():
	leftmost = bunkers[tgroup][0]
	rightmost = leftmost
	for t in bunkers[tgroup]:
		if t[1] > rightmost[1]:
			break
		else:
			rightmost = t
	topmid = (leftmost[0], (leftmost[1]+rightmost[1])/2)
	botmid = topmid
	while(botmid in bunkers[tgroup]):
		botmid = (botmid[0]+1, botmid[1])
	bunkers[tgroup] = []
	bunkers[tgroup].append(((topmid[0]+botmid[0])/2, botmid[1]))
	print bunkers[tgroup]
	print botmid

for tgroup in bunkers.keys(): #group of bunkers
	for t in bunkers[tgroup]: #each target in group
		print t
		visited = [[False for x in range(len(cells[0]))] for y in range(len(cells))]
		queue = []
		cur = None
		queue.append(t)
		visited[t[0]][t[1]] = True
		cells[t[0]][t[1]].fields[tgroup-4] = 0

		count= 0;

		while len(queue) > 0:
			cur = queue[0]
			queue = queue[1:]
			cells[cur[0]][cur[1]].xy = (cur[0], cur[1])
			count+=1
			if count % 1000000 == 0:
				print count

			if cur[0] > 0:
				newNeighbor = (cur[0]-1, cur[1])
				if newNeighbor not in cells[cur[0]][cur[1]].neighbors and cells[newNeighbor[0]][newNeighbor[1]].cell_type > 0:
					cells[cur[0]][cur[1]].neighbors.append(newNeighbor)
				if not visited[cur[0]-1][cur[1]] and cells[cur[0]-1][cur[1]].cell_type > 0:
					queue.append((cur[0]-1,cur[1]))
					visited[cur[0]-1][cur[1]] = True
					cells[cur[0]-1][cur[1]].fields[tgroup-4] = min(cells[cur[0]-1][cur[1]].fields[tgroup-4], cells[cur[0]][cur[1]].fields[tgroup-4]+1)
				#print 't', cur

			if cur[0] < len(cells)-1:
				newNeighbor = (cur[0]+1, cur[1])
				if newNeighbor not in cells[cur[0]][cur[1]].neighbors and cells[newNeighbor[0]][newNeighbor[1]].cell_type > 0:
					cells[cur[0]][cur[1]].neighbors.append(newNeighbor)
				if not visited[cur[0]+1][cur[1]] and cells[cur[0]+1][cur[1]].cell_type > 0:
					queue.append((cur[0]+1,cur[1]))
					visited[cur[0]+1][cur[1]] = True
					cells[cur[0]+1][cur[1]].fields[tgroup-4] = min(cells[cur[0]+1][cur[1]].fields[tgroup-4], cells[cur[0]][cur[1]].fields[tgroup-4]+1)
				#print 'b', cur

			if cur[1] > 0:
				newNeighbor = (cur[0], cur[1]-1)
				if newNeighbor not in cells[cur[0]][cur[1]].neighbors and cells[newNeighbor[0]][newNeighbor[1]].cell_type > 0:
					cells[cur[0]][cur[1]].neighbors.append(newNeighbor)
				if not visited[cur[0]][cur[1]-1] and cells[cur[0]][cur[1]-1].cell_type > 0:
					queue.append((cur[0],cur[1]-1))
					visited[cur[0]][cur[1]-1] = True
					cells[cur[0]][cur[1]-1].fields[tgroup-4] = min(cells[cur[0]][cur[1]-1].fields[tgroup-4], cells[cur[0]][cur[1]].fields[tgroup-4]+1)
				#print 'l', cur

			if cur[1] < len(cells[0])-1:
				newNeighbor = (cur[0], cur[1]+1)
				if newNeighbor not in cells[cur[0]][cur[1]].neighbors and cells[newNeighbor[0]][newNeighbor[1]].cell_type > 0:
					cells[cur[0]][cur[1]].neighbors.append(newNeighbor)
				if not visited[cur[0]][cur[1]+1] and cells[cur[0]][cur[1]+1].cell_type > 0:
					queue.append((cur[0],cur[1]+1))
					visited[cur[0]][cur[1]+1] = True
					cells[cur[0]][cur[1]+1].fields[tgroup-4] = min(cells[cur[0]][cur[1]+1].fields[tgroup-4], cells[cur[0]][cur[1]].fields[tgroup-4]+1)
				#print 'r', cur

			if cur[0] > 0 and cur[1] > 0:
				newNeighbor = (cur[0]-1, cur[1]-1)
				if newNeighbor not in cells[cur[0]][cur[1]].neighbors and cells[newNeighbor[0]][newNeighbor[1]].cell_type > 0:
					cells[cur[0]][cur[1]].neighbors.append(newNeighbor)
				if not visited[cur[0]-1][cur[1]-1] and cells[cur[0]-1][cur[1]-1].cell_type > 0:
					queue.append((cur[0]-1,cur[1]-1))
					visited[cur[0]-1][cur[1]-1] = True
					cells[cur[0]-1][cur[1]-1].fields[tgroup-4] = min(cells[cur[0]-1][cur[1]-1].fields[tgroup-4], cells[cur[0]][cur[1]].fields[tgroup-4]+1.5)
				#print 'tl', cur

			if cur[0] > 0 and cur[1] < len(cells[0])-1:
				newNeighbor = (cur[0]-1, cur[1]+1)
				if newNeighbor not in cells[cur[0]][cur[1]].neighbors and cells[newNeighbor[0]][newNeighbor[1]].cell_type > 0:
					cells[cur[0]][cur[1]].neighbors.append(newNeighbor)
				if not visited[cur[0]-1][cur[1]+1] and cells[cur[0]-1][cur[1]+1].cell_type > 0:
					queue.append((cur[0]-1,cur[1]+1))
					visited[cur[0]-1][cur[1]+1] = True
					cells[cur[0]-1][cur[1]+1].fields[tgroup-4] = min(cells[cur[0]-1][cur[1]+1].fields[tgroup-4], cells[cur[0]][cur[1]].fields[tgroup-4]+1.5)
				#print 'tr', cur

			if cur[0] < len(cells)-1 and cur[1] > 0:
				newNeighbor = (cur[0]+1, cur[1]-1)
				if newNeighbor not in cells[cur[0]][cur[1]].neighbors and cells[newNeighbor[0]][newNeighbor[1]].cell_type > 0:
					cells[cur[0]][cur[1]].neighbors.append(newNeighbor)
				if not visited[cur[0]+1][cur[1]-1] and cells[cur[0]+1][cur[1]-1].cell_type > 0:
					queue.append((cur[0]+1,cur[1]-1))
					visited[cur[0]+1][cur[1]-1] = True
					cells[cur[0]+1][cur[1]-1].fields[tgroup-4] = min(cells[cur[0]+1][cur[1]-1].fields[tgroup-4], cells[cur[0]][cur[1]].fields[tgroup-4]+1.5)
				#print 'bl', cur

			if cur[0] < len(cells)-1 and cur[1] < len(cells[0])-1:
				newNeighbor = (cur[0]+1, cur[1]+1)
				if newNeighbor not in cells[cur[0]][cur[1]].neighbors and cells[newNeighbor[0]][newNeighbor[1]].cell_type > 0:
					cells[cur[0]][cur[1]].neighbors.append(newNeighbor)
				if not visited[cur[0]+1][cur[1]+1] and cells[cur[0]+1][cur[1]+1].cell_type > 0:
					queue.append((cur[0]+1,cur[1]+1))
					visited[cur[0]+1][cur[1]+1] = True
					cells[cur[0]+1][cur[1]+1].fields[tgroup-4] = min(cells[cur[0]+1][cur[1]+1].fields[tgroup-4], cells[cur[0]][cur[1]].fields[tgroup-4]+1.5)



print "done generating FF"

f1 = open("sword.csv", "w+")

# coord;cid;type;len of neighbors;neighbors;ff fields;len of cones; cones
cid = 0
for r in cells:
	for c in r:
		if c.cell_type > 0:
			cid += 1
			curstr = ""+str(c.xy)+";"
			curstr += str(cid) + ";"
			curstr += str(c.cell_type) + ";"
			curstr += str(len(c.neighbors)) + ";"
			for n in c.neighbors:
				curstr += str(n)+";"
			for f in c.fields:
				curstr += str(f)+";"
			curstr += str(len(c.cones)) + ";"
			for cone in c.cones:
				curstr += str(cone) + ";"
			f1.write(curstr)
			f1.write('\n')

print 'done'
