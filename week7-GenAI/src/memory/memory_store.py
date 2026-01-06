from collections import deque

_memory_buffer = None

def init_memory(max_turns=5):
    global _memory_buffer
    _memory_buffer = deque(maxlen=max_turns * 2)

def add_user_message(message):
    _memory_buffer.append({"role": "user", "content": message})

def add_assistant_message(message):
    _memory_buffer.append({"role": "assistant", "content": message})

def get_memory():
    return list(_memory_buffer)

def clear_memory():
    _memory_buffer.clear()
