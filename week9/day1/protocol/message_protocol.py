import time


class MessageProtocol:

    def create(sender, receiver, role, content):
        return {
            "sender": sender,
            "receiver": receiver,
            "role": role,
            "content": content,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }