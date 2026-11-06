"""
Programmer: Noah Gaido
Course: ENSC 201, Fall 2026
Programming Assignment #5
Version: 1.2
Date: 10/27/2026

Description: Simulate increasing loads and report component stress.
Sources: PA5 Conditionals and Loops assignment; ENSC 201 Coding Standard.
Notes: OpenAI ChatGPT assisted with generating and revising the code
    and unit tests.
"""


def get_positive_number(prompt):
    """Prompt until the user enters a positive number.

    Args:
        prompt (str): Message displayed when asking for input.

    Returns:
        float: A number greater than zero.

    Notes:
        The user is assumed to enter numeric input.
    """
    number = float(input(prompt))
    while number <= 0:
        print("Please enter a number greater than zero.")
        number = float(input(prompt))
    return number


def calculate_stress(force, area):
    """Calculate the stress on a component.

    Args:
        force (float): Applied force in N.
        area (float): Cross-sectional area in mm^2.

    Returns:
        float: Stress in N/mm^2.

    Notes:
        Preconditions: force >= 0 and area > 0.
    """
    stress = force / area
    return stress


def classify_stress(stress, limit):
    """Check if the stress is safe, a warning, or a failure.

    Args:
        stress (float): Component stress in N/mm^2.
        limit (float): Allowable stress limit in N/mm^2.

    Returns:
        str: SAFE below 80%, WARNING from 80% through 100%, or
            FAILURE above 100% of the limit.

    Notes:
        Preconditions: stress >= 0 and limit > 0.
    """
    warning_limit = 0.8 * limit

    # Stress at the limit is a warning, not a failure.
    if stress < warning_limit:
        return "SAFE"
    elif stress <= limit:
        return "WARNING"
    else:
        return "FAILURE"


def run_load_test(initial_force, increment, cycles, area, limit):
    """Run the loading cycles and stop if the part fails.

    Args:
        initial_force (float): Force applied during the first cycle, in N.
        increment (float): Force added for each subsequent cycle, in N.
        cycles (int): Maximum number of loading cycles.
        area (float): Component cross-sectional area in mm^2.
        limit (float): Allowable stress limit in N/mm^2.

    Returns:
        int: The first failure cycle, or 0 if all cycles finish safely
            or with a warning.

    Notes:
        Preconditions: all arguments > 0, and cycles is an integer.
        Prints the cycle number, stress, and classification each cycle.
    """
    force = initial_force
    for cycle in range(1, cycles + 1):
        stress = calculate_stress(force, area)
        classification = classify_stress(stress, limit)
        print(f"Cycle {cycle}: Stress = {stress} - {classification}")
        # Stop as soon as the part fails.
        if classification == "FAILURE":
            return cycle
        force = force + increment
    return 0


def main():
    """Collect parameters and repeat load tests until the user quits.

    Args:
        None.

    Returns:
        None.

    Notes:
        Reads keyboard input and prints test results to the terminal.
    """
    while True:
        print("\n=== Engineering Load Test Simulator ===\n")
        area = get_positive_number("Enter cross-sectional area (mm^2): ")
        limit = get_positive_number("Enter allowable stress limit (N/mm^2): ")
        initial_force = get_positive_number("Enter initial force (N): ")
        increment = get_positive_number("Enter force increment (N): ")
        cycles = get_positive_number("Enter number of cycles: ")
        # The number of cycles must be a whole number.
        while cycles != int(cycles):
            print("Please enter a whole number of cycles.")
            cycles = get_positive_number("Enter number of cycles: ")
        cycles = int(cycles)

        print("\n--- Load Test Results ---")
        failure_cycle = run_load_test(
            initial_force, increment, cycles, area, limit
        )
        if failure_cycle == 0:
            print("\nOverall Result: PASSED")
            print(f"All {cycles} cycles completed without failure")
        else:
            print("\nOverall Result: FAILED")
            print(f"Component failed during cycle {failure_cycle}")
            if failure_cycle < cycles:
                print("Test terminated early")

        # Ask again if the answer is not y or n.
        again = input("\nRun another test? (y/n): ").strip().lower()
        while again != "y" and again != "n":
            again = input("Please enter y or n: ").strip().lower()
        if again == "n":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
