memory_store = []

def save_to_memory(entry):
    memory_store.append(entry)

def get_memory():
    return memory_store[-5:]  # last 5 items
