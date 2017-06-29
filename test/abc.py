class Student(object):
	def __init__(self,name,score):
		self.name=name
		self.score=score

	def get_grade(self):
		if self.score>90:
			print('A')
		elif self.score>=60:
			print("B")
		else:
			print("C")
			return
bart=Student("caowei",33)
print(bart.name)
bart.get_grade()
