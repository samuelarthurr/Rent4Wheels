class Vehicle:
    def __init__(self, vehicle_id, model):
        self.vehicle_id = vehicle_id
        self.model = model

    def __str__(self):
        return f"{self.model} (ID: {self.vehicle_id})"
