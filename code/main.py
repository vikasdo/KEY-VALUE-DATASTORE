import sys,time
class helperfunctions:
	def check_dict_constraints(d):
		if str(d.__sizeof__())>(1000*1024*1024):
			print("The size of Dictionary is exceeded the limit 1GB")

			return False

	def check_key_constraints(key):
		if len(key)>32 and key.isalpha() :
			print("The size of key you entered is exceeded the limit OF 32 chars")
			return False
		


	def check_val_constraints(val):
		if sys.getsizeof(val)>(16*1024):
			print("The size of val you entered is exceeded the limit OF 16 KB")

			return false

		

class dbstore:

	def __init__(self):
		self.data={}



	def add(key,value,timeout=0):
		if key in self.data:
			raise Exception("The Given key is created already..")
		
		try:
			if helperfunctions.check_dict_constraints(self.data) and helperfunctions.check_key_constraints(key) and helperfunctions.check_val_constraints(value) :
				if timeout==0:
					self.data[key]=(value,timeout)
				else:
					self.data[key]=(value,time.time()+timeout)



		except Exception as e:
			print("The error is {}".format(e))
		




	def read(key):
		if key  in self.data():
			print()



		except:




	def  delete(key):
		pass


