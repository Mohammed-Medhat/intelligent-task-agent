def save_notes(subtask, content, filename="notes.txt"):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"\n### {subtask}\n{content}\n")
