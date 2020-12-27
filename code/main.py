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
		self.value = collections.namedtuple('value',['val','ttl']) 



	def add(key,value,timeout=0):
		try:
			if key in self.data:
				raise Exception("The Given key is created already..")
		
		
			if helperfunctions.check_dict_constraints(self.data) and helperfunctions.check_key_constraints(key) and helperfunctions.check_val_constraints(value) :
				if timeout==0:
					self.data[key]=self.value(value,timeout)
				else:
					self.data[key]=self.value(value,time.time()+timeout)



		except Exception as e:
			print("The error is {}".format(e))
		




	def read(key):
		try:
			if key not in self.data:
				raise Exception("The Given key is not found Enter another Key..")
			else:
				key_data=self.data[key]
				if 	key_data.ttl<time.time():

					print("The Value is{}".format(key_data.val))
				else:

					raise Exception("The Given key Time to live has been expired.")
			
		except Exception as e:
			print("The error is {}".format(e))




	def  delete(key):
		try:
			if key not in self.data:
				raise Exception("The Given key is not found Enter another Key..")
			else:
				key_data = self.data[key]
				if 	key_data.ttl<time.time():
					del self.data[key]
					print("The key is deleted now")
				else:

					raise Exception("The Given key Time to live has been expired.")
			
		except Exception as e:
			print("The error is {}".format(e))


