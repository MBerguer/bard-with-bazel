from bardapi import Bard


class BardModule:
    def __init__(self):
        """Initialize the Bard API"""
        self.session = Bard()  # from: https://github.com/dsdanielpark/Bard-API

    def ask(self, question: str = "") -> str:
        """Ask a question to the Bard API and return the answer"""
        if not question:
            raise Exception("Question is empty")
        return self.session.get_answer(question)["content"]
