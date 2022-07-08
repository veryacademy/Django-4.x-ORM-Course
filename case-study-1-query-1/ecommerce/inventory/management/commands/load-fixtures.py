from django.core.management import call_command
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        call_command("makemigrations")
        call_command("migrate")
        call_command("loaddata", "db_admin_fixture_50.json")
        call_command("loaddata", "db_category_fixture_50.json")
        call_command("loaddata", "db_product_fixture_50.json")
        call_command("loaddata", "db_product_category_fixture_50.json")
        call_command("loaddata", "db_attribute_fixture_50.json")
        call_command("loaddata", "db_attribute_value_fixture_50.json")
        call_command("loaddata", "db_inventory_fixture_50.json")
        call_command("loaddata", "db_attribute_values_fixture_50.json")
        call_command("loaddata", "db_image_fixture_50.json")
        call_command("loaddata", "db_stock_control_fixture_50.json")