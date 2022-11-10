"""
This file is for managing data rows / data frames

the idea is to interpret data rows in the tables as objects until they're inserted into the pandas dataframes

this is mainly for user adding info to the tables and connecting to databases
"""

import pandas as pd



"""
interpreting DB tables as objects, EXCLUDING semi-sys tables proposed in the notenrechner table documentation
adding repr functions for each object in case front-end user wants to query data / see objects
"""


#noten table als object:
class noten_obj():
	def __init__(self,noten_id,score,ntype,kommentar,doclink,ndate,anz_year,kurs_id,cre_userid,cre_date,chg_userid,chg_date):
		self.noten_id = noten_id
		self.score = score
		self.ntype = ntype
		self.kommentar = kommentar
		self.doclink = doclink
		self.ndate = ndate
		self.anz_year = anz_year
		self.kurs_id = kurs_id
		self.cre_userid = cre_userid
		self.cre_date = cre_date
		self.chg_userid = chg_userid
		self.chg_date = chg_date

	def __repr__(self):
		return f"Note({self.noten_id},{self.score},{self.ntype},{self.kommentar},{self.doclink},{self.ndate},{self.anz_year},{self.kurs_id},{self.cre_userid},{self.cre_date},{self.chg_userid},{self.chg_date})"

	#function to append the object to a panda dataframe
	def apd_pd_dataframe(self,dtframe):
		#convert the current object to a dataframe
		object_pd_repr = pd.DataFrame({
			"noten_id": [self.noten_id],
			"score":  [self.score],
			"ntype": [self.ntype],
			"kommentar": [self.kommentar],
			"doclink": [self.doclink],
			"ndate": [self.ndate],
			"anz_year": [self.anz_year],
			"kurs_id": [self.kurs_id],
			"cre_userid": [self.cre_userid],
			"cre_date": [self.cre_date],
			"chg_userid": [self.chg_userid],
			"chg_date": [self.chg_date]
		})
		#append the dataframe with 1 row to the exisiting dataframe
		dtframe.append(object_pd_repr)
		return(dtframe)




#schueler table als object:
class schueler_obj():
	def __init__(self,schueler_id,vorname,nachname,vorname2,email,an_schule_seit,schule,stufe,adresse,salter,gebdatum,cre_userid,cre_date,chg_userid,chg_date):
		self.schueler_id = schueler_id
		self.vorname = vorname
		self.nachname = nachname
		self.vorname2 = vorname2
		self.email = email
		self.an_schule_seit = an_schule_seit
		self.schule = schule
		self.stufe = stufe
		self.adresse = adresse
		self.salter = salter
		self.gebdatum = gebdatum
		self.cre_userid = cre_userid
		self.cre_date = cre_date
		self.chg_userid = chg_userid
		self.chg_date = chg_date
		
	def __repr__(self):
		return f"Schüler({self.schueler_id},{self.vorname},{self.nachname},{self.vorname2},{self.email},{self.an_schule_seit},{self.schule},{self.stufe},{self.adresse},{self.salter},{self.gebdatum},{self.cre_userid},{self.cre_date},{self.chg_userid},{self.chg_date})"

	#function to append the object to a panda dataframe
	def apd_pd_dataframe(self,dtframe):
		#convert the current object to a dataframe
		object_pd_repr = pd.DataFrame({
			"schueler_id": [self.schueler_id],
			"vorname": [self.vorname],
			"nachname": [self.nachname],
			"vorname2": [self.vorname2],
			"email": [self.email],
			"an_schule_seit": [self.an_schule_seit],
			"schule": [self.schule],
			"stufe": [self.stufe],
			"adresse": [self.adresse],
			"salter": [self.salter],
			"gebdatum": [self.gebdatum],
			"cre_userid": [self.cre_userid],
			"cre_date": [self.cre_date],
			"chg_userid": [self.chg_userid],
			"chg_date": [self.chg_date]
		})
		#append the dataframe with 1 row to the exisiting dataframe
		dtframe.append(object_pd_repr)
		return(dtframe)




#kurs table as object
class kurs_obj():
	def __init__(self,kurs_id,lehrer_id,fach_id,stundenzahl,stufe,cre_userid,cre_date,chg_userid,chg_date):
		self.kurs_id = kurs_id
		self.lehrer_id = lehrer_id
		self.fach_id = fach_id
		self.stundenzahl = stundenzahl
		self.stufe = stufe
		self.cre_userid = cre_userid
		self.cre_date = cre_date
		self.chg_userid = chg_userid
		self.chg_date = chg_date
	
	def __repr__(self):
		return f"Kurs({self.kurs_id},{self.lehrer_id},{self.fach_id},{self.stundenzahl},{self.stufe},{self.cre_userid},{self.cre_date},{self.chg_userid},{self.chg_date})"

	#function to append the object to a panda dataframe
	def apd_pd_dataframe(self,dtframe):
		#convert the current object to a dataframe
		object_pd_repr = pd.DataFrame({
			"kurs_id": [self.kurs_id],
			"lehrer_id": [self.lehrer_id],
			"fach_id": [self.fach_id],
			"stundenzahl": [self.stundenzahl],
			"stufe": [self.stufe],
			"cre_userid": [self.cre_userid],
			"cre_date": [self.cre_date],
			"chg_userid": [self.chg_userid],
			"chg_date": [self.chg_date]
		})
		#append the dataframe with 1 row to the exisiting dataframe
		dtframe.append(object_pd_repr)
		return(dtframe)




#stunden table as object
class stunden_obj():
	def __init__(self,stunden_id,sday,scount,cre_userid,cre_date,chg_userid,chg_date):
		self.stunden_id = stunden_id
		self.sday = sday
		self.scount = scount
		self.cre_userid = cre_userid
		self.cre_date = cre_date
		self.chg_userid = chg_userid
		self.chg_date = chg_date

	def __repr__(self):
		return f"Stunden({self.stunden_id},{self.sday},{self.scount},{self.cre_userid},{self.cre_date},{self.chg_userid},{self.chg_date})"

	#function to append the object to a panda dataframe
	def apd_pd_dataframe(self,dtframe):
		#convert the current object to a dataframe
		object_pd_repr = pd.DataFrame({
			"stunden_id": [self.stunden_id],
			"sday": [self.sday],
			"scount": [self.scount],
			"cre_userid": [self.cre_userid],
			"cre_date": [self.cre_date],
			"chg_userid": [self.chg_userid],
			"chg_date": [self.chg_date]
		})
		#append the dataframe with 1 row to the exisiting dataframe
		dtframe.append(object_pd_repr)
		return(dtframe)





#lehrer table as object
class lehrer_obj():
	def __init__(self,vorname,nachname,vorname2,email,kuerzel,an_schule_seit,schule,origin,adresse,gebdatum,cre_userid,cre_date,chg_userid,chg_date):
		self.vorname = vorname
		self.nachname = nachname
		self.vorname2 = vorname2
		self.email = email
		self.kuerzel = kuerzel
		self.an_schule_seit = an_schule_seit
		self.schule = schule
		self.origin = origin
		self.adresse = adresse
		self.gebdatum = gebdatum
		self.cre_userid = cre_userid
		self.cre_date = cre_date
		self.chg_userid = chg_userid
		self.chg_date = chg_date

	def __repr__(self):
		return f"Lehrer({self.vorname},{self.nachname},{self.vorname2},{self.email},{self.an_schule_seit},{self.schule},{self.origin},{self.adresse},{self.gebdatum},{self.cre_userid},{self.cre_date},{self.chg_userid},{self.chg_date})"

	#function to append the object to a panda dataframe
	def apd_pd_dataframe(self,dtframe):
		#convert the current object to a dataframe
		object_pd_repr = pd.DataFrame({
			"vorname": [self.vorname],
			"nachname": [self.nachname],
			"vorname2": [self.vorname2],
			"email": [self.email],
			"kuerzel": [self.kuerzel],
			"an_schule_seit": [self.an_schule_seit],
			"schule": [self.schule],
			"origin": [self.origin],
			"adresse": [self.adresse],
			"gebdatum": [self.gebdatum],
			"cre_userid": [self.cre_userid],
			"cre_date": [self.cre_date],
			"chg_userid": [self.chg_userid],
			"chg_date": [self.chg_date]
		})
		#append the dataframe with 1 row to the exisiting dataframe
		dtframe.append(object_pd_repr)
		return(dtframe)





#stunden table as object
class stunden_obj():
	def __init__(self,stunden_id,sday,scount,cre_userid,cre_date,chg_userid,chg_date):
		self.stunden_id = stunden_id
		self.sday = sday
		self.scount = scount
		self.cre_userid = cre_userid
		self.cre_date = cre_date
		self.chg_userid = chg_userid
		self.chg_date = chg_date

	def __repr__(self):
		return f"Stunde({self.stunden_id},{self.sday},{self.scount},{self.cre_userid},{self.cre_date},{self.chg_userid},{self.chg_date})"

	#function to append the object to a panda dataframe
	def apd_pd_dataframe(self,dtframe):
		#convert the current object to a dataframe
		object_pd_repr = pd.DataFrame({
			"stunen_id": [self.stunden_id],
			"sday": [self.sday],
			"scount": [self.scount],
			"cre_userid": [self.cre_userid],
			"cre_date": [self.cre_date],
			"chg_userid": [self.chg_userid],
			"chg_date": [self.chg_date]
		})
		#append the dataframe with 1 row to the exisiting dataframe
		dtframe.append(object_pd_repr)
		return(dtframe)




#fach table as object
class fach_obj():
	def __init__(self,fach_id,fname,cre_userid,cre_date,chg_userid,chg_date):
		self.fach_id = fach_id
		self.fname = fname
		self.cre_userid = cre_userid
		self.cre_date = cre_date
		self.chg_userid = chg_userid
		self.chg_date = chg_date

	def __repr__(self):
		return f"Fach({self.fach_id},{self.fname},{self.cre_userid},{self.cre_date},{self.chg_userid},{self.chg_date})"

	#function to append the object to a panda dataframe
	def apd_pd_dataframe(self,dtframe):
		#convert the current object to a dataframe
		object_pd_repr = pd.DataFrame({
			"fach_id": [self.fach_id],
			"fname": [self.fname],
			"cre_userid": [self.cre_userid],
			"cre_date": [self.cre_date],
			"chg_userid": [self.chg_userid],
			"chg_date": [self.chg_date]
		})
		#append the dataframe with 1 row to the exisiting dataframe
		dtframe.append(object_pd_repr)
		return(dtframe)



#schule table as object
class schule_obj():
	def __init__(self,schule_id,name,stype,adresse,cre_userid,cre_date,chg_userid,chg_date):
		self.schule_id = schule_id
		self.name = name
		self.stype = stype
		self.adresse = adresse
		self.cre_userid = cre_userid
		self.cre_date = cre_date
		self.chg_userid = chg_userid
		self.chg_date = chg_date

	def __repr__(self):
		return f"Fach({self.schule_id},{self.name},{self.stype},{self.adresse},{self.cre_userid},{self.cre_date},{self.chg_userid},{self.chg_date})"

	#function to append the object to a panda dataframe
	def apd_pd_dataframe(self,dtframe):
		#convert the current object to a dataframe
		object_pd_repr = pd.DataFrame({
			"schule_id": [self.schule_id],
			"name": [self.name],
			"stype": [self.stype],
			"adresse": [self.adresse],
			"cre_userid": [self.cre_userid],
			"cre_date": [self.cre_date],
			"chg_userid": [self.chg_userid],
			"chg_date": [self.chg_date]
		})
		#append the dataframe with 1 row to the exisiting dataframe
		dtframe.append(object_pd_repr)
		return(dtframe)








#schulevents table as object
class schulevents_obj():
	def __init__(self,schulevents_id,descript,datum,cre_userid,cre_date,chg_userid,chg_date):
		self.schulevents_id = schulevents_id
		self.descript = descript
		self.datum = datum
		self.cre_userid = cre_userid
		self.cre_date = cre_date
		self.chg_userid = chg_userid
		self.chg_date = chg_date

	def __repr__(self):
		return f"Schulevent({self.schulevents_id},{self.descript},{self.datum},{self.cre_userid},{self.cre_date},{self.chg_userid},{self.chg_date})"

	#function to append the object to a panda dataframe
	def apd_pd_dataframe(self,dtframe):
		#convert the current object to a dataframe
		object_pd_repr = pd.DataFrame({
			"schulevents_id": [self.schulevents_id],
			"descript": [self.descript],
			"datum": [self.datum],
			"cre_userid": [self.cre_userid],
			"cre_date": [self.cre_date],
			"chg_userid": [self.chg_userid],
			"chg_date": [self.chg_date]
		})
		#append the dataframe with 1 row to the exisiting dataframe
		dtframe.append(object_pd_repr)
		return(dtframe)



#arbeiten table as object
class arbeiten_obj():
	def __init__(self,arbeiten_id,atype,kurs_id,datum,acount,cre_userid,cre_date,chg_userid,chg_date):
		self.arbeiten_id = arbeiten_id
		self.atype = atype
		self.kurs_id = kurs_id
		self.datum = datum
		self.acount = acount
		self.cre_userid = cre_userid
		self.cre_date = cre_date
		self.chg_userid = chg_userid
		self.chg_date = chg_date

	def __repr__(self):
		return f"Arbeit({self.arbeiten_id},{self.atype},{self.kurs_id},{self.datum},{self.acount},{self.cre_userid},{self.cre_date},{self.chg_userid},{self.chg_date})"

	#function to append the object to a panda dataframe
	def apd_pd_dataframe(self,dtframe):
		#convert the current object to a dataframe
		object_pd_repr = pd.DataFrame({
			"arbeiten_id": [self.arbeiten_id],
			"atype": [self.atype],
			"kurs_id": [self.kurs_id],
			"datum": [self.datum],
			"acount": [self.acount],
			"cre_userid": [self.cre_userid],
			"cre_date": [self.cre_date],
			"chg_userid": [self.chg_userid],
			"chg_date": [self.chg_date]
		})
		#append the dataframe with 1 row to the exisiting dataframe
		dtframe.append(object_pd_repr)
		return(dtframe)




#kalender table as object
class kalender_obj():
	def __init__(self,kalender_id,events_descript,events_date,cre_userid,cre_date,chg_userid,chg_date):
		self.kalender_id = kalender_id
		self.events_descript = events_descript
		self.events_date = events_date
		self.cre_userid = cre_userid
		self.cre_date = cre_date
		self.chg_userid = chg_userid
		self.chg_date = chg_date

	def __repr__(self):
		return f"Kalender({self.kalender_id},{self.events_descript},{self.events_date},{self.cre_userid},{self.cre_date},{self.chg_userid},{self.chg_date})"

	#function to append the object to a panda dataframe
	def apd_pd_dataframe(self,dtframe):
		#convert the current object to a dataframe
		object_pd_repr = pd.DataFrame({
			"kalender_id": [self.kalender_id],
			"events_descript": [self.events_descript],
			"events_date": [self.events_date],
			"cre_userid": [self.cre_userid],
			"cre_date": [self.cre_date],
			"chg_userid": [self.chg_userid],
			"chg_date": [self.chg_date]
		})
		#append the dataframe with 1 row to the exisiting dataframe
		dtframe.append(object_pd_repr)
		return(dtframe)





#kursschuleventsref table as object
class kursschuleventsref_obj():
	def __init__(self,kursschuleventsref_id,kurs_id,schulevents_id,cre_userid,cre_date,chg_userid,chg_date):
		self.kursschuleventsref_id = kursschuleventsref_id
		self.kurs_id = kurs_id
		self.schulevents_id = schulevents_id
		self.cre_userid = cre_userid
		self.cre_date = cre_date
		self.chg_userid = chg_userid
		self.chg_date = chg_date

	def __repr__(self):
		return f"Kursschuleventsref({self.kursschuleventsref_id},{self.kurs_id},{self.schulevents_id},{self.cre_userid},{self.cre_date},{self.chg_userid},{self.chg_date})"

	#function to append the object to a panda dataframe
	def apd_pd_dataframe(self,dtframe):
		#convert the current object to a dataframe
		object_pd_repr = pd.DataFrame({
			"kursschuleventsref_id": [self.kursschuleventsref_id],
			"kurs_id": [self.kurs_id],
			"schulevents_id": [self.schulevents_id],
			"cre_userid": [self.cre_userid],
			"cre_date": [self.cre_date],
			"chg_userid": [self.chg_userid],
			"chg_date": [self.chg_date]
		})
		#append the dataframe with 1 row to the exisiting dataframe
		dtframe.append(object_pd_repr)
		return(dtframe)




#kursstundenref table as object
class kursstundenref_obj():
	def __init__(self,kursstundenref_id,kurs_id,stunden_id,cre_userid,cre_date,chg_userid,chg_date):
		self.kursstundenref_id = kursstundenref_id
		self.kurs_id = kurs_id
		self.stunden_id = stunden_id
		self.cre_userid = cre_userid
		self.cre_date = cre_date
		self.chg_userid = chg_userid
		self.chg_date = chg_date

	def __repr__(self):
		return f"Kursstundenref({self.kursstundenref_id},{self.kurs_id},{self.stunden_id},{self.cre_userid},{self.cre_date},{self.chg_userid},{self.chg_date})"

	#function to append the object to a panda dataframe
	def apd_pd_dataframe(self,dtframe):
		#convert the current object to a dataframe
		object_pd_repr = pd.DataFrame({
			"kursstundenref_id": [self.kursstundenref_id],
			"kurs_id": [self.kurs_id],
			"stunden_id": [self.stunden_id],
			"cre_userid": [self.cre_userid],
			"cre_date": [self.cre_date],
			"chg_userid": [self.chg_userid],
			"chg_date": [self.chg_date]
		})
		#append the dataframe with 1 row to the exisiting dataframe
		dtframe.append(object_pd_repr)
		return(dtframe)




#kursschuelerref table as object
class kursschuelerref_obj():
	def __init__(self,kursschuelerref_id,kurs_id,schueler_id,cre_userid,cre_date,chg_userid,chg_date):
		self.kursschuelerref_id = kursschuelerref_id
		self.kurs_id = kurs_id
		self.schueler_id = schueler_id
		self.cre_userid = cre_userid
		self.cre_date = cre_date
		self.chg_userid = chg_userid
		self.chg_date = chg_date

	def __repr__(self):
		return f"Kursschuelerref({self.kursschuelerref_id},{self.kurs_id},{self.schueler_id},{self.cre_userid},{self.cre_date},{self.chg_userid},{self.chg_date})"

	#function to append the object to a panda dataframe
	def apd_pd_dataframe(self,dtframe):
		#convert the current object to a dataframe
		object_pd_repr = pd.DataFrame({
			"kursschuelerref_id": [self.kursschuelerref_id],
			"kurs_id": [self.kurs_id],
			"schueler_id": [self.schueler_id],
			"cre_userid": [self.cre_userid],
			"cre_date": [self.cre_date],
			"chg_userid": [self.chg_userid],
			"chg_date": [self.chg_date]
		})
		#append the dataframe with 1 row to the exisiting dataframe
		dtframe.append(object_pd_repr)
		return(dtframe)





#lehrerfachref table as object
class lehrerfachref_obj():
	def __init__(self,lehrerfachref_id,lehrer_id,fach_id,cre_userid,cre_date,chg_userid,chg_date):
		self.lehrerfachref_id = lehrerfachref_id
		self.lehrer_id = lehrer_id
		self.fach_id = fach_id
		self.cre_userid = cre_userid
		self.cre_date = cre_date
		self.chg_userid = chg_userid
		self.chg_date = chg_date

	def __repr__(self):
		return f"Lehrerfachref({self.lehrerfachref_id},{self.lehrer_id},{self.fach_id},{self.cre_userid},{self.cre_date},{self.chg_userid},{self.chg_date})"

	#function to append the object to a panda dataframe
	def apd_pd_dataframe(self,dtframe):
		#convert the current object to a dataframe
		object_pd_repr = pd.DataFrame({
			"lehrerfachref_id": [self.lehrerfachref_id],
			"lehrer_id": [self.lehrer_id],
			"fach_id": [self.fach_id],
			"cre_userid": [self.cre_userid],
			"cre_date": [self.cre_date],
			"chg_userid": [self.chg_userid],
			"chg_date": [self.chg_date]
		})
		#append the dataframe with 1 row to the exisiting dataframe
		dtframe.append(object_pd_repr)
		return(dtframe)





#notenschuelerref table as object
class notenschuelerref_obj():
	def __init__(self,notenschuelerref_id,noten_id,schueler_id,cre_userid,cre_date,chg_userid,chg_date):
		self.notenschuelerref_id = notenschuelerref_id
		self.noten_id = noten_id
		self.schueler_id = schueler_id
		self.cre_userid = cre_userid
		self.cre_date = cre_date
		self.chg_userid = chg_userid
		self.chg_date = chg_date

	def __repr__(self):
		return f"Notenschuelerref({self.notenschuelerref_id},{self.noten_id},{self.schueler_id},{self.cre_userid},{self.cre_date},{self.chg_userid},{self.chg_date})"

	#function to append the object to a panda dataframe
	def apd_pd_dataframe(self,dtframe):
		#convert the current object to a dataframe
		object_pd_repr = pd.DataFrame({
			"notenschuelerref_id": [self.notenschuelerref_id],
			"noten_id": [self.noten_id],
			"schueler_id": [self.schueler_id],
			"cre_userid": [self.cre_userid],
			"cre_date": [self.cre_date],
			"chg_userid": [self.chg_userid],
			"chg_date": [self.chg_date]
		})
		#append the dataframe with 1 row to the exisiting dataframe
		dtframe.append(object_pd_repr)
		return(dtframe)



#noten_simplified 'table' as object
class noten_simplified_obj():
	def __init__(self,score,fach,type,count,cre_userid,cre_date,chg_userid,chg_date):
		self.score = score
		self.fach = fach
		self.type = type
		self.count = count
		self.cre_userid = cre_userid
		self.cre_date = cre_date
		self.chg_userid = chg_userid
		self.chg_date = chg_date

	def __repr__(self):
		return f"noten_simplified({self.score},{self.fach},{self.type},,{self.count},{self.cre_userid},{self.cre_date},{self.chg_userid},{self.chg_date})"

	#function to append the object to a panda dataframe
	def apd_pd_dataframe(self,dtframe):
		#convert the current object to a dataframe
		object_pd_repr = pd.DataFrame({
			"score": [self.score],
			"fach": [self.fach],
			"type": [self.type],
			"count": [self.count],
			"cre_userid": [self.cre_userid],
			"cre_date": [self.cre_date],
			"chg_userid": [self.chg_userid],
			"chg_date": [self.chg_date]
		})
		#append the dataframe with 1 row to the exisiting dataframe
		dtframe.append(object_pd_repr)
		return(dtframe)




#custom error message when running the program with wrong entry file
class FileExecutionError(Exception):
	def __init__(self,message="This file is not supposed to run as the main file."):
		self.message = message
		super().__init__(self.message)
if __name__ == "__main__":
	raise  FileExecutionError