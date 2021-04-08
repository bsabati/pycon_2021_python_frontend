import ipywidgets
from table_arrangment.src.table_arrangment.guest_settings import GuestSettings


class GuestSettingsVm(ipywidgets.HBox):
    def __init__(self):
        self.guest_name = ipywidgets.Text(
            placeholder='Add Guest...',
            description='Guest Name:'
        )
        self.guest_side = ipywidgets.Dropdown(
            options=['Bride', 'Groom'],
            description='Guest Side:'
        )
        self.people_invited_count = ipywidgets.BoundedIntText(value=1, min=0, max=8, step=1, description='People Invited:')
        self.people_arrived_count = ipywidgets.BoundedIntText(value=0, min=0, max=1, step=1,
                                                              description='People Arrived:')
        self.people_invited_count.observe(self.update_people_arrived_count_max, 'value')
        self.comments = ipywidgets.Textarea(
            placeholder='Comments...',
            description='Comments:',
            disabled=False
        )
        super().__init__(
            [self.guest_name, self.guest_side, self.people_invited_count, self.people_arrived_count, self.comments])

    def update_people_arrived_count_max(self, *args, **kwargs):
        self.people_arrived_count.max = self.people_invited_count.value

    @property
    def guest_settings(self) -> GuestSettings:
        return GuestSettings(name=self.guest_name.value, side=self.guest_side.value,
                             people_invited_count=self.people_invited_count.value,
                             people_arrived_count=self.people_arrived_count.value,
                             comments=self.comments.value)
