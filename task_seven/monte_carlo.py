import random
from rich.console import Console
from rich.table import Table

def roll_n_dices(dices_qty):
    total = 0
    for _ in range(dices_qty):
        total += random.randint(1, 6)
    return total

def dice_roll_simulation(simulation_number):
    dice_role_results = {i: 0 for i in range(2, 13)}

    for _ in range(simulation_number):
        total = roll_n_dices(2)
        dice_role_results[total] += 1
    
    return dice_role_results

def calculate_sum_probabilities(dice_role_results, simulation_number):
    probabilities = []

    for sum, count in dice_role_results.items():
        probability = f"{count / simulation_number * 100:.2f}% ({count}/{simulation_number})"
        probabilities.append([str(sum), probability])

    return probabilities

def print_table(rows):
    table = Table(title="Probabilities")
    columns = ["Sum", "Probability"]

    for column in columns:
        table.add_column(column)

    for row in rows:
        table.add_row(*row, style='bright_green')

    console = Console()
    console.print(table)

simulation_number = 1000000
dice_role_results = dice_roll_simulation(simulation_number)
probabilities = calculate_sum_probabilities(dice_role_results, simulation_number)
print_table(probabilities)
