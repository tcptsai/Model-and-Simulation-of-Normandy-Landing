class SimConst:
	'''
	Constants for the simulation
	'''
	def __init__(self):

		# RNG
		self.RandomSeed = 100

		# Bunkers
		self.Bunker_Default_Shots = 10
		self.Bunker_Health_Decrease_Max = 30
		self.Bunker_Health_Decrease_Min = 10
		self.Bunker_Damaged_Chance = 0.95

		self.Bunker_Default_Health = 1000

		# Soldiers
		self.Soldier_Default_Health = 100
		self.Soldier_Health_Decrease_In_Cone_Max = 30
		self.Soldier_Health_Decrease_In_Cone_Min = 10
		self.Soldier_Health_Decrease_At_Bunker_Max = 30
		self.Soldier_Health_Decrease_At_Bunker_Min = 10
		self.Soldier_Health_Decrease_On_Beach_Max = 30
		self.Soldier_Health_Decrease_On_Beach_Min = 10
		self.Soldier_Damaged_Chance_In_Cone = 0.10
		self.Soldier_Damaged_Chance_At_Bunker = 0.50
		self.Soldier_Damaged_Chance_On_Beach = 0.01


		self.speedBeach = 2
		self.speedLand = 3
		self.speedSlope = 1

		# Ship
		self.Ship_Speed = 5
		self.ShipGenStep = 30
		self.ShipGenNumber = 5

		# Cells
		self.Default_Cone_Value = -1

		# Generators
		self.Soldier_per_Generator = 30

		# Output Image
		self.StepPerImage = 500