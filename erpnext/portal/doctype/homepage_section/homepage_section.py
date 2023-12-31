# Copyright (c) 2019, ShoperPrime Solutions and contributors
# For license information, please see license.txt


from frappe.model.document import Document
from frappe.utils import cint


class HomepageSection(Document):
	@property
	def column_value(self):
		return cint(12 / cint(self.no_of_columns or 3))
