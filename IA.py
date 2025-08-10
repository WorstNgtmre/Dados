import random
import re

def roll_dice_from_string(roll_string):
    """Parses a dice roll string (e.g., '2d6+3', '1d20-1', '3d8') and performs the roll."""
    match = re.match(r'(\d+)d(\d+)([+-]\d+)?', roll_string.lower())
    if not match:
        raise ValueError("Formato de entrada incorrecto. Por favor, usa el formato 'XdY+Z', 'XdY-Z' o 'XdY'.")

    num_dice = int(match.group(1))
    num_sides = int(match.group(2))
    modifier_str = match.group(3)
    modifier = int(modifier_str) if modifier_str else 0

    if num_dice <= 0 or num_sides <= 0:
        raise ValueError("La cantidad de dados y el número de caras deben ser valores positivos.")

    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    total_sum = sum(rolls)
    final_result = total_sum + modifier

    return {
        "rolls": rolls,
        "modifier": modifier,
        "total": total_sum,
        "final_result": final_result,
        "input_string": roll_string
    }

# Main interaction
if __name__ == "__main__":
    while True:
        user_input = input("Introduce la tirada de dados (Ej: 2d4+3, 1d20-1) o 'salir' para terminar: ")
        if user_input.lower() == 'salir':
            break

        try:
            roll_data = roll_dice_from_string(user_input)
            print(f"Resultados de los dados: {roll_data['rolls']}")
            print(f"Suma de los dados: {roll_data['total']}")
            if roll_data['modifier'] != 0:
                print(f"Bonificador: {roll_data['modifier']}")
            print(f"Resultado total: {roll_data['final_result']}")

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")
