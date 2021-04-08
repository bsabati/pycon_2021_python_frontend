class GuestSettings:
    def __init__(self, name: str, side: str, people_invited_count: int, people_arrived_count:int, comments: str):
        self.name = name
        self.side = side
        self.people_invited_count = people_invited_count
        self.people_arrived_count = people_arrived_count
        self.comments = comments
