import pprint
from typing import List

from nmdc_schema.get_nmdc_view import ViewGetter


class ClassSlotsGetter:
    def get_class_slots(self, class_name) -> List[str]:
        # assumes induced
        view_getter = ViewGetter()
        nmdc_view = view_getter.get_view()
        nmdc_class = nmdc_view.induced_class(class_name)
        class_slots = nmdc_class.attributes

        class_slot_names = [v.name for k, v in class_slots.items()]
        class_slot_names.sort()
        return class_slot_names
