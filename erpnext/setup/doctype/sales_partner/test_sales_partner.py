# Copyright (c) 2015, ShoperPrime Solutions and Contributors
# License: GNU General Public License v3. See license.txt

import frappe

test_records = frappe.get_test_records("Sales Partner")

test_ignore = ["Item Group"]
