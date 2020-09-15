class Vetor:
	def __init__(self, lista):
		if isinstance(list, list):
			self.content = lista
		else:
			self.content = list(lista)

		self.size = len(self.content)

	def __repr__(self):
		return(str(self.content))

	def __add__(self, other):
		if isinstance(other, Vetor):
			if self.size != other.size:
				raise errorVectors()
			return Vetor([si + oi for si,oi in zip(self.content, other.content)])
		elif isinstance(other, (int, float)):
			return Vetor(si + other for si in self.content)
		else:
			print('operation not defined')

	def __sub__(self, other):
		if isinstance(other, Vetor):
			if self.size != other.size:
				raise errorVectors()
			return Vetor([si - oi for si,oi in zip(self.content, other.content)])
		elif isinstance(other, (int, float)):
			return Vetor(si - other for si in self.content)
		else:
			print('operation not defined')

	def dot_product(self, other):
		if isinstance(other, Vetor):
			if self.size != other.size:
				raise errorVectors()
			return sum([si * oi for si,oi in zip(self.content, other.content)])

	def __pow__(self, scalar):
		if isinstance(scalar, (int, float)):
			return Vetor(si**scalar for si in self.content)

	def distance(self, other):
		if isinstance(other, Vetor):
			if self.size != other.size:
				raise errorVectors()
			return (sum(Vetor(self - other)**2))**(1/2)


	def __len__(self):
		return len(self.content)

	def __getitem__(self, index):
		return(self.content[index])

	def __reversed__(self):
		return(self.content[::-1])

	def __eq__(self, other):
		if isinstance(other, Vetor):
			if self.size != other.size:
				raise errorVectors()
			return all([si == oi for si, oi in zip(self.content, other.content)])


def zeros(num):
	return Vetor([0 for i in range(num)])

def ones(num):
	return Vetor([1 for i in range(num)])


class errorVectors(Exception):
	def __init__(self, message = "can't perform this operation on vectors of different sizes"):
		self.message = message
		super().__init__(message)