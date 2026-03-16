# Imports
from warnings import warn

# Classes
class _DiaryCore:
    class Persistence:
        @staticmethod
        def save(filename: str, entries: list[str], idx: int, entry_sep: str = "::::") -> None:
            with open(file=filename, mode="w") as f:
                for item in [entry_sep.join(entries), idx]:
                    f.write(f"{item}\n")

        @staticmethod
        def load(filename: str, entry_Sep: str = "::::") -> tuple[list[str], int]:
            result = []
            with open(file=filename, mode="r") as f:
                for item in f.readlines():
                    result.append(item.strip())
            return (result[0].split(entry_Sep), int(result[1]))

    class Statistics:
        @staticmethod
        def get_statistics(entries: list[str], idx: int) -> str:
            return f"Count: {idx - 1 if idx != 0 else 0}\nLetters(Avg): {round(len("".join(entries)) / idx - 1 if idx != 0 else 1, 0)}"

class Diary:
    def __init__(self) -> None:
        self.entries = []
        self.idx = 0

    def __repr__(self) -> str:
        return "\n".join(self.entries)

    def add_entry(self, item: str) -> None:
        self.entries.append(f"{self.idx}: {item}")
        self.idx += 1

    def remove_entry(self, idx: int) -> None:
        try:
            self.entries.pop(idx)
        except IndexError:
            warn(message=f"{idx} not found in list size({self.idx - 1 if self.idx != 0 else 0})")

# Runner
if __name__ == "__main__":
    diary = Diary()

    # Add
    diary.add_entry("Täna oli ilus ilm.")
    diary.add_entry("Õppisin programmeerimist.")
    diary.add_entry("SRP on tegelikult väga loogiline.")

    # Print Sisu
    print("---- DIARY SISU ----")
    print(diary)
    print()

    # Statistika Print
    print("---- STATISTIKA ----")
    print(_DiaryCore.Statistics.get_statistics(entries=diary.entries, idx=diary.idx))
    print()

    # Salvestame faili
    filename = "diary.txt"
    _DiaryCore.Persistence.save(filename=filename, entries=diary.entries, idx=diary.idx)
    print(f"Salvestatud faili: {filename}")
    print()

    # Laeme uuesti failist
    diary.entries, diary.idx = _DiaryCore.Persistence.load(filename=filename)
    print("---- FAILIST LAETUD ----")
    print(diary)
    print()

    # Kontrollime, kas loendur töötab edasi
    diary.add_entry("See lisati pärast laadimist.")
    print("---- PÄRAST UUT LISAMIST ----")
    print(diary)

    # Testi remove'imist
    diary.remove_entry(99)
    diary.remove_entry(1)
    print(diary)
