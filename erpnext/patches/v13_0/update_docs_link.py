# Copyright (c) 2023, ShoperPrime Solutions and Contributors
# License: MIT. See LICENSE


import frappe


def execute():
	navbar_settings = frappe.get_single("Navbar Settings")
	for item in navbar_settings.help_dropdown:
		if item.is_standard and item.route == "https://shopersolutions.com/docs/user/manual":
			item.route = "https://docs.shopersolutions.com/docs/v14/user/manual/en/introduction"

	navbar_settings.save()
