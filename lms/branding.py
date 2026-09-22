import frappe


DEFAULT_BRAND_NAME = "Nova LMS"
LEGACY_BRAND_NAMES = {None, "", "Frappe", "Learning", "Frappe Learning"}


def get_brand_name() -> str:
	"""Return the configured brand while upgrading legacy defaults in-place at read time."""
	brand_name = frappe.db.get_single_value("Website Settings", "app_name")
	return DEFAULT_BRAND_NAME if brand_name in LEGACY_BRAND_NAMES else brand_name
