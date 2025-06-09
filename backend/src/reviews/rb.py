class RBReview:
    def __init__(self, id: int | None = None,
                name: str | None = None,
                text: str | None = None):
        self.id = id
        self.name = name
        self.text = text
        
    def to_dict(self) -> dict:
        data = {"id": self.id, "name": self.name, "text": self.text}
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data