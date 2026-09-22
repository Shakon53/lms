import json
from unittest.mock import patch

import frappe
from frappe.tests import IntegrationTestCase

from lms.lms.api import get_audit_log


class TestAuditLog(IntegrationTestCase):
	def test_requires_system_manager(self):
		frappe.set_user("Guest")
		with self.assertRaises(frappe.PermissionError):
			get_audit_log()

	@patch("lms.lms.api.frappe.get_all")
	def test_summarizes_version_without_returning_raw_data(self, get_all):
		frappe.set_user("Administrator")
		get_all.return_value = [
			frappe._dict(
				name="VER-1",
				ref_doctype="LMS Course",
				docname="course-1",
				owner="Administrator",
				creation="2026-09-22 12:00:00",
				data=json.dumps(
					{
						"changed": [["title", "Old", "New"]],
						"added": [["instructors", {"instructor": "teacher@example.com"}]],
					}
				),
			)
		]

		result = get_audit_log()

		self.assertEqual(result[0].changed_fields, ["title"])
		self.assertEqual(result[0].added_rows, 1)
		self.assertNotIn("data", result[0])

	def test_rejects_unscoped_doctype(self):
		frappe.set_user("Administrator")
		with self.assertRaises(frappe.ValidationError):
			get_audit_log(doctype="User")
