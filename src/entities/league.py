class League:
    name: str
    cc: str
    id: str

    def __init__(self, id: str, name: str, cc: str):
        self.id = id
        self.name = name
        self.cc = cc

    def __str__(self):
        return f"League(name: {self.name}, cc: {self.cc}, id: {self.id})"

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_cc(self):
        return self.cc
