class Foo(object):

	def __init__(self):
		self.x= 'foo'

	def do(self):
		print(self.x)


class Bar(object):

	def __init__(self, foo):
		self.foo = foo

	def do(self):
		self.foo.do()


b = Bar(Foo())
b.do()