class Evidence:
    # credentials
    token = "64cfb043fdcad132819bd09b"
    base_url = "https://dummyapi.io/data/v1/"

    def fetch_evidence(self):
        raise NotImplementedError("Subclass must implement this method")
