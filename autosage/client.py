from autosage.api import Client

class Poe(Client):
    def __init__(self, name_session: str = 'my_account', email: str = None):
        super().__init__(name_session, email)
    
    def connect(self):
        return super().connect()
    
    def send_verification_code(self, verification_code: str):
        return super().send_verification_code(verification_code)
    
    def sage(self, prompt: str):
        return super().sage(prompt)