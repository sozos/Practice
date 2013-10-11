#!/usr/bin/python
import random

# Notes while learning about Python classes:
# fnA means fnA is public and is what should be called
# _fnA means fnA is still publicly accessible but should not be used. i.e. its implementation is not guaranteed to always stay the same
# __fnA means fnA is private and can only be used within the class
#
# functions have self as first parameter so it can access its own attributes. i.e. (self, paramA, ...)
# calling the functions will just be obj.fnA(paramA, ...). The "obj." does the referencing with "self"


# We represent nodes as lists, then mutate them as opposed to storing nodes directly
# There are 2 reasons:
# 1) Due to Python's strange value passing, we can't modify the value as intended.
# 2) Storing as a list will allow easy augmentation of data. e.g. size of subtree, color of node, etc.
class Node:
	"""Tree Node"""
	def __init__(self, data):
		self.__data = data
		self.__parent = [None]
		self.__leftChild = [None]
		self.__rightChild = [None]

	def getData(self):
		return self.__data;

	def getParent(self):
		return self.__parent

	def getLeftChild(self):
		return self.__leftChild

	def getRightChild(self):
		return self.__rightChild

	def setParent(self, parent):
		self.__parent = [parent]

	def setLeftChild(self, leftChild):
		self.__leftChild = [leftChild]

	def setRightChild(self, rightChild):
		self.__rightChild = [rightChild]

class BinaryTree:
	"""Vanilla binary tree. Assumes unique node data"""
	# comparatorFn(a,b): a > b, return 1; a = b, return 0; a < b, return -1
	comparatorFn = None
	root = [None]

	def __init__(self, comparator):
		self.comparatorFn = comparator

	def printTree(self):
		self.__printNode(self.root, 1)

	def __printNode(self, node, level):
		indentation = ""
		for i in range(1, level):
			indentation += "-"
		indentation += ">"
		
		if (node == [None]):
			print indentation, 'None'
		else:
			print indentation, node[0].getData()
			self.__printNode(node[0].getLeftChild(), level+1)
			self.__printNode(node[0].getRightChild(), level+1)

	def insert(self, node):
		self.__insertAt(node, self.root, [None])

	def __insertAt(self, node, current, parent):
		if (current == [None]):
			current[0] = node
			current[0].setParent(parent[0])

			if (parent[0] != None):
				if (self.comparatorFn(parent[0], current[0]) == 1):
					# parent > newNode
					parent[0].setLeftChild(current[0])
				else:
					# parent < newNode
					parent[0].setRightChild(current[0])
		elif (self.comparatorFn(current[0], node) == 1):
			# current > node. Look at left subtree
			self.__insertAt(node, current[0].getLeftChild(), current)
		else:
			# current < node. Look at right subtree
			self.__insertAt(node, current[0].getRightChild(), current)

	def inorderWalk(self):
		treewalk = self.__inorderWalkAt(self.root[0])
		flattened = self.__flattenNestedList(treewalk)
		output = []
		for i in range(0, len(flattened)):
			output.append(flattened[i].getData())
		return output

	def __inorderWalkAt(self, node):
		if (node == None):
			return []

		leftsubtree = self.__inorderWalkAt(node.getLeftChild()[0])
		data = [node]
		rightsubtree = self.__inorderWalkAt(node.getRightChild()[0])

		# A 3-tuple. [[left subtree][self][right subtree]]
		return [leftsubtree, data, rightsubtree]
	
	def __flattenNestedList(self, lst):
		if (not isinstance(lst, list)):
			return [lst]
		elif (len(lst) == 0):
			return []
		else:
			output = []
			for i in range(0, len(lst)):
				output.extend(self.__flattenNestedList(lst[i]))
			return output

	def search(self, data):
		treewalk = self.__inorderWalkAt(self.root[0])
		flattened = self.__flattenNestedList(treewalk)
		for i in range(0, len(flattened)):
			if (flattened[i].getData() == data):
				return flattened[i]
		return None

	def successor(self, node):
		rightsubtree = self.__inorderWalkAt(node)[2]
		flattened = self.__flattenNestedList(rightsubtree)

		if (len(rightsubtree) != 0):
			# Return smallest item in it's right subtree
			return flattened[0]
		else:
			# No right subtree
			if (node.getParent()[0] == None):
				return None # node is root
			elif (node == node.getParent()[0].getLeftChild()[0]):
				return node.getParent()[0] # node is a left child
			else:
				# Keep going upwards (along ancestors of right children) until we " become a left child"
				temp = node
				while (temp.getParent()[0] != None):
					if (temp == temp.getParent()[0].getLeftChild()[0]):
						return temp.getParent()[0]
					else:
						temp = temp.getParent()[0]
				return None

	def remove(self, data):
		node = self.search(data)
		if (node == None):
			print "No such node in tree"
			return

		leftChild = node.getLeftChild()[0]
		rightChild = node.getRightChild()[0]

		if (leftChild == None and rightChild == None):
			# 0 child
			if (self.root[0] == node):
				self.root = [None]
			else:
				parent = node.getParent()[0]
				if (node == parent.getLeftChild()[0]):
					parent.setLeftChild(None)
				else:
					parent.setRightChild(None)
		elif (leftChild != None and rightChild != None):
			# 2 children, i.e. successor exists
			succ = self.successor(node)

			# Remove links from succ
			# succ is not root and it has at most 1 child
			if (succ.getLeftChild()[0] == None):
				onlyChild = succ.getRightChild()[0]
			else:
				onlyChild = succ.getLeftChild()[0]
			# onlyChild could be None

			succParent = succ.getParent()[0] 
			if (succ == succParent.getLeftChild()[0]):
				succParent.setLeftChild(onlyChild)
			else:
				succParent.setRightChild(onlyChild)

			# Grab new left/right child of node.
			# They may be updated due to removal of links from succ
			leftChild = node.getLeftChild()[0]
			rightChild = node.getRightChild()[0]
			succ.setLeftChild(leftChild)
			succ.setRightChild(rightChild)

			if (self.root[0] == node):
				self.root = [succ]
				succ.setParent(None)
			else:
				parent = node.getParent()[0]
				succ.setParent(parent)
				if (node == parent.getLeftChild()[0]):
					parent.setLeftChild(succ)
				else:
			 		parent.setRightChild(succ)
		else:
			# 1 left child only
			if (leftChild == None):
				onlyChild = rightChild
			else:
				onlyChild = leftChild

			if (self.root[0] == node):
				self.root = [onlyChild]
			else:
				parent = node.getParent()[0]
				onlyChild.setParent(parent)
				if (node == parent.getLeftChild()[0]):
					parent.setLeftChild(onlyChild)
				else:
					parent.setRightChild(onlyChild)

#======#
# MAIN #
#======#
def comparatorFn(a,b):
	dataA = a.getData()
	dataB = b.getData()
	if (dataA == dataB):
		return 0
	elif (dataA > dataB):
		return 1
	elif (dataA < dataB):
		return -1
	else:
		print "ERROR"
		return None

BT = BinaryTree(comparatorFn)
minVal = input()
maxVal = input()
A = range(minVal, maxVal)

random.shuffle(A)
print "Input order:\n", A

for val in A:
	node = Node(val)
	BT.insert(node)

print "\nOutput binary tree: "
BT.printTree()
print BT.inorderWalk()

for i in range(minVal,maxVal-1):
	data = (BT.successor(BT.search(i))).getData()
	if (data != i+1):
		print "Failed at finding successor for", i, data
	else:
		print "Successor of", i, ":", data
print "Successor of", maxVal-1, ":", BT.successor(BT.search(maxVal-1))

for i in range(minVal, maxVal):
	print "\nRemoving", i
	BT.remove(i)
	BT.printTree()
	print BT.inorderWalk()