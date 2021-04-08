import ipyaggrid
import ipywidgets
import pandas as pd

from table_arrangment.src.table_arrangment.table_settings_vm import GuestSettingsVm
from table_arrangment.src.table_arrangment.vbox_observable import VBoxObservable


class RSVP(ipywidgets.VBox):
    def __init__(self):
        self.guests_setting_vms = VBoxObservable([])
        self.guests_setting_vms.add_observer(self.on_guests_settings_vm_change)
        self.add_guests_button = ipywidgets.interactive(self.add_guest, {'manual': True, 'manual_name': 'Add Guest'})
        column_defs = [{'headerName': 'Name', 'field': 'name'},
                       {'headerName': 'Side', 'field': 'side'},
                       {'headerName': 'People Invited', 'field': 'people_invited_count'},
                       {'headerName': 'People Arrived', 'field': 'people_arrived_count'},
                       {'headerName': 'Comments', 'field': 'comments'},
                       ]
        grid_options = {
            'columnDefs': column_defs,
            'enableSorting': True,
            'enableFilter': True,
            'enableEditing': True,
        }
        self.guests_grid = ipyaggrid.Grid(grid_data=self.guests, grid_options=grid_options, )
        super().__init__([self.add_guests_button, self.guests_setting_vms, self.guests_grid])

    def on_guests_settings_vm_change(self, *args, **kwargs):
        self.guests_grid.update_grid_data(self.guests)

    def add_guest(self, *args, **kwargs):
        guest_setting_list = list(self.guests_setting_vms.children)
        guest_setting_list.append(GuestSettingsVm())
        self.guests_setting_vms.children = tuple(guest_setting_list)
        self.guests_setting_vms.make_observe_vbox_observable_and_trigger_value_change()

    @property
    def guests(self):
        return pd.DataFrame([o.guest_settings.__dict__ for o in self.guests_setting_vms.children])
