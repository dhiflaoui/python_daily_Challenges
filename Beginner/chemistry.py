"""
Project Description
Write a program that allows you to search for a chemical element by its symbol and get
its full name and atomic number. The program uses a predefined dictionary of elements. 
"""
elements = {
    "H": {"name": "Hydrogen", "atomic_number": 1},
    "He": {"name": "Helium", "atomic_number": 2},
    "Li": {"name": "Lithium", "atomic_number": 3},
    "Be": {"name": "Beryllium", "atomic_number": 4},
    "B": {"name": "Boron", "atomic_number": 5},
    "C": {"name": "Carbon", "atomic_number": 6},
    "N": {"name": "Nitrogen", "atomic_number": 7},
    "O": {"name": "Oxygen", "atomic_number": 8},
    "F": {"name": "Fluorine", "atomic_number": 9},
    "Ne": {"name": "Neon", "atomic_number": 10},
    "Na": {"name": "Sodium", "atomic_number": 11},
    "Mg": {"name": "Magnesium", "atomic_number": 12},
    "Al": {"name": "Aluminum", "atomic_number": 13},
    "Si": {"name": "Silicon", "atomic_number": 14},
    "P": {"name": "Phosphorus", "atomic_number": 15},
    "S": {"name": "Sulfur", "atomic_number": 16},
    "Cl": {"name": "Chlorine", "atomic_number": 17},
    "Ar": {"name": "Argon", "atomic_number": 18},
    "K": {"name": "Potassium", "atomic_number": 19},
    "Ca": {"name": "Calcium", "atomic_number": 20},
    "Sc": {"name": "Scandium", "atomic_number": 21},
    "Ti": {"name": "Titanium", "atomic_number": 22},
    "V": {"name": "Vanadium", "atomic_number": 23},
    "Cr": {"name": "Chromium", "atomic_number": 24},
    "Mn": {"name": "Manganese", "atomic_number": 25},
    "Fe": {"name": "Iron", "atomic_number": 26},
    "Co": {"name": "Cobalt", "atomic_number": 27},
    "Ni": {"name": "Nickel", "atomic_number": 28},
    "Cu": {"name": "Copper", "atomic_number": 29},
    "Zn": {"name": "Zinc", "atomic_number": 30}
}

chemical_symbol = input("Enter the chemical symbol (e.g., H, He, C): ")


if chemical_symbol:
    chemical_symbol = chemical_symbol.upper() if len(chemical_symbol) == 1 else chemical_symbol[0].upper() + chemical_symbol[1].lower()

    if chemical_symbol in elements:
        element_info = elements[chemical_symbol]
        name = element_info["name"]
        atomic_number = element_info["atomic_number"]
        print(f"The element with symbol {chemical_symbol} is {name} with atomic number {atomic_number}.")
    else:
        print("Element not found in the dictionary.")