# Copyright (c) 2023, Sowaan and contributors
# For license information, please see license.txt

import frappe
import json
from frappe.model.document import Document

class NamingSeriesUpdate(Document):
	def validate(self):
		values = {'name': self.series}
		data = frappe.db.sql("""
			select * from `tabSeries` where name=%(name)s
		""", values=values, as_dict=0)
		if len(data)>0:
			self.current_value = data[0][1]

	def on_submit(self):
		values = {'name': self.get("series")}
		data = frappe.db.sql("""
			select * from `tabSeries` where name=%(name)s
		""", values=values, as_dict=0)

		values = {'name': self.series, 'new_value': self.new_value}
		if len(data)==0:
			frappe.db.sql("""
				INSERT INTO `tabSeries` (`name`, `current`) VALUES (%(name)s,%(new_value)s)
			""", values=values, as_dict=0)
		else:
			frappe.db.sql("""
				UPDATE `tabSeries` SET current=%(new_value)s where name=%(name)s
			""", values=values, as_dict=0)

@frappe.whitelist()
def execute_query(doc):
	doc = json.loads(doc)
	values = {'name': doc.get("series")}
	data = frappe.db.sql("""
		select * from `tabSeries` where name=%(name)s
	""", values=values, as_dict=0)
	if len(data)>0:
		return data[0][1]