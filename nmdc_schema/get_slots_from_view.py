import pprint
from typing import List

from nmdc_schema.get_nmdc_view import ViewGetter


class SchemaSlotsGetter:
    def get_schema_slots(self) -> List[str]:
        view_getter = ViewGetter()
        nmdc_view = view_getter.get_view()

        schema_slots = nmdc_view.all_slots()
        schema_slot_names = [v.name for k, v in schema_slots.items()]
        schema_slot_names.sort()
        return schema_slot_names

