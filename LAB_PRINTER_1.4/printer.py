# Parent Class
class Machine():
    def print_(self, *args) -> None:
        print(*args)

    def scan(self, *args) -> None:
        print(f"Scanned: '{args}'")

    def fax(self, *args) -> None:
        print(f"Scanned: {args}")

# Classes
class MultiPrinter(Machine): pass
class OldPrinter(Machine):
    def fax(self, *args):
        raise NotImplementedError("Operation not supported")

    def scan(self, *args):
        raise NotImplementedError("Operation not supported")

# Test
printer = OldPrinter()
printer.print_("Oh wow", "damn", 678)
printer.fax(89)