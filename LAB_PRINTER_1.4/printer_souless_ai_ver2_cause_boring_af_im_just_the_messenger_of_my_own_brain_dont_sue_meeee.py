from abc import ABC, abstractmethod

# =====================
# Interfaces
# =====================

class Printer(ABC):
    @abstractmethod
    def print_(self, *args) -> None:
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self, *args) -> None:
        pass


class Fax(ABC):
    @abstractmethod
    def fax(self, *args) -> None:
        pass


# =====================
# Devices
# =====================

# Only prints
class OldPrinter(Printer):
    def print_(self, *args) -> None:
        print(*args)


# Prints + scans
class Photocopier(Printer, Scanner):
    def print_(self, *args) -> None:
        print(*args)

    def scan(self, *args) -> None:
        print(f"Scanned: {args}")


# Full feature device
class MultiPrinter(Printer, Scanner, Fax):
    def print_(self, *args) -> None:
        print(*args)

    def scan(self, *args) -> None:
        print(f"Scanned: {args}")

    def fax(self, *args) -> None:
        print(f"Faxed: {args}")


# =====================
# MultiFunctionMachine (composition)
# =====================

class MultiFunctionMachine(Printer, Scanner):
    def __init__(self, printer: Printer, scanner: Scanner):
        self._printer = printer
        self._scanner = scanner

    def print_(self, *args) -> None:
        self._printer.print_(*args)

    def scan(self, *args) -> None:
        self._scanner.scan(*args)


# =====================
# Test
# =====================

if __name__ == "__main__":
    # Old printer (only print)
    old = OldPrinter()
    old.print_("Oh wow", "damn", 678)

    print("-----")

    # Photocopier (print + scan)
    photo = Photocopier()
    photo.print_("Copy this")
    photo.scan("Document1")

    print("-----")

    # Multi-function machine using composition
    mfm = MultiFunctionMachine(old, photo)
    mfm.print_("Delegated print")
    mfm.scan("Delegated scan")