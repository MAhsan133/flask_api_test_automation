import os


class EnvironementSetup:

    @staticmethod
    def get_base_url():
        base_url = "localhost:5000"
        try:
            base_url = os.environ['BASE_URL']
        except KeyError:
            pass
        return base_url
