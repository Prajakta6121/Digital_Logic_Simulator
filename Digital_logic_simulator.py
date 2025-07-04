def AND(a, b): return a & b
def OR(a, b): return a | b
def NOT(a): return int(not a)
def NAND(a, b): return int(not (a & b))
def NOR(a, b): return int(not (a | b))
def XOR(a, b): return a ^ b
def XNOR(a, b): return int(not (a ^ b))

# ----- Combinational Circuits -----

def half_adder(a, b):
    sum_bit = XOR(a, b)
    carry = AND(a, b)
    return sum_bit, carry

def full_adder(a, b, c_in):
    sum1, carry1 = half_adder(a, b)
    final_sum, carry2 = half_adder(sum1, c_in)
    final_carry = OR(carry1, carry2)
    return final_sum, final_carry

def half_subtractor(a, b):
    diff = XOR(a, b)
    borrow = AND(NOT(a), b)
    return diff, borrow

def full_subtractor(a, b, b_in):
    diff1, borrow1 = half_subtractor(a, b)
    final_diff, borrow2 = half_subtractor(diff1, b_in)
    final_borrow = OR(borrow1, borrow2)
    return final_diff, final_borrow

# ----- Truth Table Generator -----

def generate_truth_table(gate_name):
    print(f"\n=== Truth Table for {gate_name.upper()} ===")
    
    if gate_name == "NOT":
        print(" A | OUT ")
        print("---------")
        for a in [0, 1]:
            result = NOT(a)
            print(f" {a} |  {result}")
    else:
        print(" A | B | OUT ")
        print("-------------")
        for a in [0, 1]:
            for b in [0, 1]:
                if gate_name == "AND":
                    result = AND(a, b)
                elif gate_name == "OR":
                    result = OR(a, b)
                elif gate_name == "NAND":
                    result = NAND(a, b)
                elif gate_name == "NOR":
                    result = NOR(a, b)
                elif gate_name == "XOR":
                    result = XOR(a, b)
                elif gate_name == "XNOR":
                    result = XNOR(a, b)
                print(f" {a} | {b} |  {result}")
    
    input("\n(Press ENTER to return to menu...)")

# ----- User Input Helper -----

def get_input(prompt="Enter 0 or 1: "):
    while True:
        try:
            val = int(input(prompt))
            if val in [0, 1]:
                return val
            else:
                print("❌ Enter only 0 or 1.")
        except:
            print("❌ Invalid input. Try again.")

# ----- Simulation Functions -----

def simulate_half_adder():
    print("\n--- HALF ADDER ---")
    a = get_input("A: ")
    b = get_input("B: ")
    s, c = half_adder(a, b)
    print(f"Sum: {s}, Carry: {c}")

def simulate_full_adder():
    print("\n--- FULL ADDER ---")
    a = get_input("A: ")
    b = get_input("B: ")
    c_in = get_input("Carry-In: ")
    s, c_out = full_adder(a, b, c_in)
    print(f"Sum: {s}, Carry-Out: {c_out}")

def simulate_half_subtractor():
    print("\n--- HALF SUBTRACTOR ---")
    a = get_input("A: ")
    b = get_input("B: ")
    d, b_out = half_subtractor(a, b)
    print(f"Difference: {d}, Borrow: {b_out}")

def simulate_full_subtractor():
    print("\n--- FULL SUBTRACTOR ---")
    a = get_input("A: ")
    b = get_input("B: ")
    b_in = get_input("Borrow-In: ")
    d, b_out = full_subtractor(a, b, b_in)
    print(f"Difference: {d}, Borrow-Out: {b_out}")

# ----- Main Menu -----

def main():
    gates = {
        "AND": lambda: print("Output:", AND(get_input("A: "), get_input("B: "))),
        "OR": lambda: print("Output:", OR(get_input("A: "), get_input("B: "))),
        "NOT": lambda: print("Output:", NOT(get_input("A: "))),
        "NAND": lambda: print("Output:", NAND(get_input("A: "), get_input("B: "))),
        "NOR": lambda: print("Output:", NOR(get_input("A: "), get_input("B: "))),
        "XOR": lambda: print("Output:", XOR(get_input("A: "), get_input("B: "))),
        "XNOR": lambda: print("Output:", XNOR(get_input("A: "), get_input("B: "))),
        "HALF ADDER": simulate_half_adder,
        "FULL ADDER": simulate_full_adder,
        "HALF SUBTRACTOR": simulate_half_subtractor,
        "FULL SUBTRACTOR": simulate_full_subtractor
    }

    while True:
        print("\n=== DIGITAL LOGIC SIMULATOR ===")
        print("Available operations:")
        for gate in gates:
            print(f"• {gate}")
        print("• TRUTH TABLE")
        print("• EXIT")
        
        choice = input("Select an operation: ").strip().upper()

        if choice == "EXIT":
            print("👋 Exiting...")
            break
        elif choice in gates:
            gates[choice]()
        elif choice == "TRUTH TABLE":
            gate_tt = input("Enter gate name for truth table: ").strip().upper()
            if gate_tt in ["AND", "OR", "NOT", "NAND", "NOR", "XOR", "XNOR"]:
                generate_truth_table(gate_tt)
            else:
                print("❌ Unsupported gate for truth table.")
        else:
            print("❌ Invalid choice. Try again.")

# Run the simulator
main()
