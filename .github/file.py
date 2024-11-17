
def command_arg(command_line):
    try:
        with open(command_line, 'r') as file:
            for line in file:
                if not line.strip():
                    print("Error, line is empty")
                    continue
                try:
                    print(float(line))
                except ValueError:
                    print("Line cannot be turned into float value")
                    continue
    except FileNotFoundError:
        print("Error, file cannot be opened, try retyping it more carefully")
        exit()

command_arg("commanding.txt")