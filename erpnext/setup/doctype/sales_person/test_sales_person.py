# Copyright (c) 2015, NETMANTHAN. and Contributors
# License: GNU General Public License v3. See license.txt

test_dependencies = ["Employee"]

import frappe

test_records = frappe.get_test_records("Sales Person")

test_ignore = ["Item Group"]
