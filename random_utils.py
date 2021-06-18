import random


class stable_random_generator():
	def __init__(self, seed):
		self.seed = random.seed(seed)
		self.generation_keys = [random.randint(0, 10**8) for _ in range(500)]

	def get_next_key(self):
		key = self.generation_keys[0]
		del self.generation_keys[0]
		return key

	def set_seed(self):
		key = self.get_next_key()
		random.seed(key)

	def choice(self,ls):
		self.set_seed()
		return random.choice(ls)

	def randint(self,low, high):
		self.set_seed()
		return random.randint(low, high)

	def shuffle(self,ls):
		self.set_seed()
		random.shuffle(ls)
