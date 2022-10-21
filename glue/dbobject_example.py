class DbObject():
	def __init__(self, data):
		self.data = data

	def __repr__(self):
		return f"Stunde({self.data})"

	#function to append the object to a panda dataframe
	def apd_pd_dataframe(self,dtframe):
		#convert the current object to a dataframe
		object_pd_repr = pd.DataFrame({
            k: [self.data[k]] for k in self.data
		})
		#append the dataframe with 1 row to the exisiting dataframe
		dtframe.append(object_pd_repr)
		return(dtframe)


my_student_id = DbObject().data.get("student_id")