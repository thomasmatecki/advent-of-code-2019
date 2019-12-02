
def calc_total_fuel(mass):

    module_mass_fuel = mass // 3 - 2
    total_fuel = module_mass_fuel

    additional_fuel_mass = module_mass_fuel

    while True:
        additional_fuel_mass = additional_fuel_mass // 3 - 2

        if additional_fuel_mass <=0:
            break

        total_fuel += additional_fuel_mass

    return total_fuel

with open('day-1-input.txt') as input_file:
    total_module_mass_fuel = sum((int(line.strip()) // 3 - 2 for line in input_file)) # part 1
    input_file.seek(0)

    total_module_mass_fuel = sum(
        (calc_total_fuel(int(line.strip())) for line in input_file)
    ) # part 2

    print(total_module_mass_fuel)
