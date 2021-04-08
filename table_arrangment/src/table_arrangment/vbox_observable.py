import ipywidgets
from typing import List, Callable


class VBoxObservable(ipywidgets.VBox):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.observers: List[Callable] = list()
        self.make_observe_vbox_observable_and_trigger_value_change()

    def add_observer(self, observer: Callable):
        self.observers.append(observer)

    def add_observe_to_internal_box_children(self, box: ipywidgets.Box):
        for item in box.children:
            if len(getattr(item, 'children', [])) > 0:
                self.add_observe_to_internal_box_children(item)
            else:
                item.observe(self.on_value_change, names='value')

    def make_observe_vbox_observable_and_trigger_value_change(self):
        self.add_observe_to_internal_box_children(self)
        self.on_value_change()

    def on_value_change(self, *args, **kwargs):
        for observer in self.observers:
            observer(*args, **kwargs)
