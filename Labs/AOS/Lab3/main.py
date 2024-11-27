class IEEE754:
    BIAS = 255

    def __init__(self, value) -> None:
        self.value = value
        self.sign = 0 if float(value) >= 0 else 1
        if self.value == 'inf' or self.value == '-inf':
            self.exponent = "1" * 9
            self.mantissa = "0" * 31
        elif not float(self.value):
            self.mantissa = "0" * 31
            self.exponent = 0
        else:
            self.mantissa = self.get_mantissa()
            self.exponent = self.get_exponent()

    def __add__(self, other):
        if isinstance(other, IEEE754):
            return IEEE754(float(self.value) + float(other.value))
        else:
            return IEEE754(float(self.value) + other)

    def __sub__(self, other):
        if isinstance(other, IEEE754):
            return IEEE754(float(self.value) - float(other.value))
        else:
            return IEEE754(float(self.value) - other)

    def __mul__(self, other):
        if other == 0:
            return IEEE754(0)
        if isinstance(other, IEEE754):
            return IEEE754(float(self.value) * float(other.value))
        else:
            return IEEE754(float(self.value) * other)

    def __truediv__(self, other):
        if isinstance(other, IEEE754):
            if other.value == 0:
                return IEEE754('inf')
            return IEEE754(float(self.value) / float(other.value))
        else:
            if other == 0:
                return IEEE754('inf')
            return IEEE754(float(self.value) / other)

    @staticmethod
    def normalize(value):
        while abs(value) >= 2:
            value /= 2
        while abs(value) < 1:
            value *= 2
        return value

    @staticmethod
    def float_bin(number):
        whole = int(number)
        frac = number - whole
        whole_bin = bin(whole).lstrip('0b') if whole != 0 else "0"
        frac_bin = []

        for _ in range(31):
            frac *= 2
            if frac >= 1:
                frac_bin.append("1")
                frac -= 1
            else:
                frac_bin.append("0")

        return f"{whole_bin}.{''.join(frac_bin)}"

    def get_exponent(self):
        value = abs(float(self.value))
        exponent = 0
        while abs(value) >= 2:
            value /= 2
            exponent += 1
        while abs(value) < 1:
            value *= 2
            exponent -= 1
        return exponent

    def get_mantissa(self):
        value = IEEE754.normalize(abs(float(self.value)))
        mantissa = value - 1
        mantissa_bin = IEEE754.float_bin(mantissa)[2:] if mantissa != 0 else "0"

        if len(mantissa_bin) < 31:
            while len(mantissa_bin) != 31:
                mantissa_bin = mantissa_bin + "0"

        return mantissa_bin[:32]

    def get_exp_field(self):
        if self.value == "inf":
            return "1" * 9
        if self.value == 0:
            return "0" * 9
        temp_exp_field = bin(int(self.exponent) + IEEE754.BIAS).lstrip("0b")
        temp_exp_field = temp_exp_field.lstrip("0-0b")
        while len(temp_exp_field) < 9:
            temp_exp_field = "0" + temp_exp_field
        if len(temp_exp_field) > 9:
            temp_exp_field = temp_exp_field[:9]

        return temp_exp_field

    def __str__(self) -> str:
        return f"{self.sign} {self.get_exp_field()} {self.mantissa}"


class Coprocessor:
    def __init__(self):
        self.stack = [IEEE754(0)] * 8  # Список для регістрів (ST0-ST7)

    def load(self, value):
        """Завантаження числа у стек."""
        self.stack.insert(0, value)  # Нове значення стає ST0
        self.stack = self.stack[:8]

    def add(self):
        """Додавання двох верхніх елементів стеку."""
        R0 = self.stack.pop(0)  # ST0
        R1 = self.stack.pop(0)  # ST1
        if R0.value == "inf" or R1.value == "inf":
            self.stack.insert(0, IEEE754("inf"))  # Результат стає ST0
            self.stack.append(IEEE754(0))
        else:
            self.stack.insert(0, R0 + R1)  # Результат стає ST0
            self.stack.append(IEEE754(0))

    def sub(self):
        """Віднімання верхніх елементів стеку."""
        R0 = self.stack.pop(0)  # ST0
        R1 = self.stack.pop(0)  # ST1
        self.stack.insert(0, R0 - R1)  # Результат стає ST0
        self.stack.append(IEEE754(0))

    def mult(self):
        """Множення верхніх елементів стеку."""
        R0 = self.stack.pop(0)  # ST0
        R1 = self.stack.pop(0)  # ST1
        if R0.value == "inf" or R1.value == "inf":
            self.stack.insert(0, IEEE754("inf"))
            self.stack.append(IEEE754(0))
        else:
            self.stack.insert(0, R0 * R1)  # Результат стає ST0
            self.stack.append(IEEE754(0))

    def div(self):
        """Ділення верхніх елементів стеку."""
        R0 = self.stack.pop(0)  # ST0
        R1 = self.stack.pop(0)  # ST1
        if R1 != 0:
            self.stack.insert(0, R0 / R1)  # Результат стає ST0
            self.stack.append(IEEE754(0))
        elif R1.value == float('inf'):
            self.stack.insert(0, IEEE754(0))
            self.stack.append(IEEE754(0))
        elif R1.value == float('-inf'):
            self.stack.insert(0, IEEE754('-0'))
            self.stack.append(IEEE754(0))
        else:
            self.stack.insert(0, IEEE754("inf"))
            self.stack.append(0)

    def swap(self):
        """Заміна місцями двох верхніх елементів стеку."""
        self.stack[0], self.stack[1] = self.stack[1], self.stack[0]

    def dubl(self):
        """Дублювання верхнього елементу стеку."""
        self.stack.insert(0, self.stack[0])
        self.stack = self.stack[:8]

    def show_stack(self):
        """Вивід стану стеку."""
        print("Стан стеку:")
        for i, val in enumerate(self.stack):
            print(f"R{i}: {val}, {val.value}")

    def execute_commands(self, command_file):
        with open(command_file, 'r') as file:
            for line in file:
                cmd = line.strip().split()
                if cmd[0] == "Load":
                    self.load(IEEE754(cmd[1]))
                    print(f"Load")
                    self.show_stack()
                elif cmd[0] == "Add":
                    self.add()
                    print(f"Add")
                    self.show_stack()
                elif cmd[0] == "Sub":
                    self.sub()
                    print(f"Sub")
                    self.show_stack()
                elif cmd[0] == "Mult":
                    self.mult()
                    print(f"Mult")
                    self.show_stack()
                elif cmd[0] == "Div":
                    self.div()
                    print(f"Div")
                    self.show_stack()
                elif cmd[0] == "Swap":
                    self.swap()
                    print(f"Swap")
                    self.show_stack()
                elif cmd[0] == "Dubl":
                    self.dubl()
                    print(f"Dubl")
                    self.show_stack()

if __name__ == "__main__":
    coprocessor = Coprocessor()
    coprocessor.execute_commands("commands.txt")