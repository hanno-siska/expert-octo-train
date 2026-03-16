class Diary:
    def __init__(self) -> None:
        self.diary = []
        self.idx = 0

    def __str__(self):
        return "\n".join(self.diary)

    def load(self, filename: str) -> None:
        with open(filename, "r") as f:
            self.diary = f.readline().strip().split("::::")
            self.idx = int(f.readline().strip())

    def save(self, filename: str) -> None:
        diary = "::::".join(self.diary)
        with open(filename, "w") as f:
            for i in [diary, self.idx]:
                f.write(f"{i}\n")

    def remove_entry(self, index: int) -> None:
        try:
            self.diary.pop(index)
        except Exception as e:
            raise Warning(f"Index: {index}, not found")

    def add_entry(self, text: str) -> None:
        self.diary.append(f"{self.idx}: {text}")
        self.idx += 1

    def print_statistics(self) -> None:
        print(f"Count: {self.idx-1}\nLetters(Avg): {round(len("".join(self.diary)) / len(self.diary), 0)}")

d = Diary()
d.load("omg.txt")
d.add_entry("Tufeufiuges")
d.add_entry("84383848363")
d.save("omg.txt")
d.print_statistics()
print(d)