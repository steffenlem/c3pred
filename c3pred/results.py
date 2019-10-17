class Results:
    def __init__(self, error, error_type, description, sequence, activity=None):
        self.error = error
        self.error_type = error_type
        self.description = description
        self.sequence = sequence
        self.activity = activity
