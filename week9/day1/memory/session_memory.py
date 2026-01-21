class Memory:
    def __init__(self, window_size=10):
        self.window_size = window_size
        self.messages = []

    def add(self, message):
        self.messages.append(message)
        if len(self.messages) > self.window_size:
            self.messages.pop(0)

    def get_context(self):
        context = ""
        for msg in self.messages:
            context += f"{msg['sender']} → {msg['receiver']}: {msg['content']}\n"
        return context.strip()
