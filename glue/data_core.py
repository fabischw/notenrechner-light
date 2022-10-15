#notenrechner project data core
"""
This file contains all the code required to handling and managing the data for the notenrechner.
This includes loading from either a local machine database, a cloud service or drag n' drop csv files
"""



"""
Currently supported database source options:

planned / in development:
- local oracle DB (21c XE, notenrechner layout)
- csv drag n' drop
"""




#importing dependencies
import pandas as pd



#interpreting DB tables as objects, EXCLUDING semi-sys tables


#noten table als object:
class noten():
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

		dtframe.append(object_pd_repr)
		return(dtframe)




#schueler table als object:
class schueler():
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


#kurs table as object
class kurs():
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



#stunden table as object
class stunden():
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


#lehrer table as object
class lehrer():
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


#stunden table as object
class stunden():
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



#fach table as object
class fach():
	def __init__(self,fach_id,fname,cre_userid,cre_date,chg_userid,chg_date):
		self.fach_id = fach_id
		self.fname = fname
		self.cre_userid = cre_userid
		self.cre_date = cre_date
		self.chg_userid = chg_userid
		self.chg_date = chg_date

	def __repr__(self):
		return f"Fach({self.fach_id},{self.fname},{self.cre_userid},{self.cre_date},{self.chg_userid},{self.chg_date})"


#schulevents table as object
class schulevents():
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


#arbeiten table as object
class arbeiten():
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




#kalender table as object
class kalender():
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



#kursschuleventsref table as object
class kursschuleventsref():
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




#kursstundenref table as object
class kursstundenref():
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



#kursschuelerref table as object
class kursschuelerref():
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


#lehrerfachref table as object
class lehrerfachref():
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



#notenschuelerref table as object
class notenschuelerref():
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








