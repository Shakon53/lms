from unittest.mock import patch

import frappe
from frappe.tests import IntegrationTestCase

from lms.lms.api import set_language


class TestLanguagePreference(IntegrationTestCase):
	def setUp(self):
		self.original_user = frappe.session.user

	def tearDown(self):
		frappe.session.user = self.original_user

	@patch("lms.lms.api.frappe.local.cookie_manager", create=True)
	@patch("lms.lms.api.frappe.db.set_value")
	def test_guest_language_is_stored_in_cookie(self, set_value, cookie_manager):
		frappe.session.user = "Guest"

		self.assertEqual(set_language("ru"), {"language": "ru"})
		cookie_manager.set_cookie.assert_called_once_with(
			"preferred_language",
			"ru",
			max_age=60 * 60 * 24 * 365,
		)
		set_value.assert_not_called()

	@patch("lms.lms.api.frappe.local.cookie_manager", create=True)
	@patch("lms.lms.api.frappe.db.set_value")
	def test_user_language_is_stored_on_user(self, set_value, cookie_manager):
		frappe.session.user = "learner@example.com"

		self.assertEqual(set_language("kk"), {"language": "kk"})
		set_value.assert_called_once_with(
			"User",
			"learner@example.com",
			"language",
			"kk",
		)
		cookie_manager.set_cookie.assert_not_called()

	def test_unsupported_language_is_rejected(self):
		with self.assertRaises(frappe.ValidationError):
			set_language("de")
