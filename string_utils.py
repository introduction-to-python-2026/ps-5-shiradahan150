
def split_before_each_uppercases(formula):
  if not formula:
    return []

  index = 0
  split_string = []

  for i, char in enumerate(formula):

    if char.isupper() and index < i:
      split_string.append(formula[index:i])
      index = i

  split_string.append(formula[index:])
  
  return split_string

def split_at_digit(formula):
  s = ""

  for index, char in enumerate(formula):
    if char.isdigit() == True:
      return (s, int(formula[index:]))
    else:
      s += char
    
  return (s, 1)

def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.
    Example: 'H2O' → {'H': 2, 'O': 1}"""

    # Step 1: Initialize an empty dictionary to store atom counts
    atom_counts = {}

    for atom in split_before_each_uppercases(molecular_formula):
      atom_name, atom_count = split_at_digit(atom)
      atom_counts[atom_name] = atom_count

      # Step 2: Update the dictionary with the atom name and count

    # Step 3: Return the completed dictionary
    return atom_counts



def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
