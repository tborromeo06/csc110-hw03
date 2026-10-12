"""
Name: (Thalia Borromeo)
Peers: (add any collaborators)
References: (anything you checked to solve this)
"""

# imported modules
import statistics # let's us use mean, median, mode

# This is a global variable (seen by all local scopes)
grades = [0,0,0,0,0] # initialized with five zeros

# Task 1:
#  Complete the function "read_five_ints" below:
def read_five_ints():
    """ updates content of grades depending on the user's input

    Updates the values inside the global variable grades (list)
    with each of the user's 5 input ints.
    If the user inputs are not digits, it prints
    "Error in read_five_ints: input string is not for an integer",
    and if the input converted to int is outside of [0,10], prints
    "Error in read_five_ints: input integer outside of range".
    """
    for idx in range ( len(grades) ):
        # for each idx in 0, 1,... 4 do:
        # check if the input is not a digit print error
        # convert to int
        # check if the int is not in the interval [0 to 10] print error
        # add the int to grades at index idx

        in_str = input("Give me the next grade in [0 to 10]:")

        # Step 1: Check if input consists only of digits
        if not in_str.isdigit():
            print(
                "Error in read_five_ints: input string is not for an integer"
            )
            exit()

        num = int(in_str)

        # Step 2: Check if integer is within [0, 10]
        if num < 0 or num > 10:
            print("Error in read_five_ints: input integer outside of range")
            exit()

        # Step 3: Assign valid integer to global grades list
        grades[idx] = num

    #Anything with this indentation is NO LONGER inside the loop


# Task 2:
#  Complete the function "pick_averaging_method" below:
def pick_averaging_method():
    """ returns an average depending on the user's selection

    Obtains an average using either mean, median or mode,
    depending on user input.
    User should pick 'a' for mean, 'b' for median, 'c' for mode.
    Any other input prints
    'Error in pick_averaging_method: incorrect option picked'.
    """
    """Prompts user to select an averaging method (mean, median, or mode),

    prints selection, calculates, and returns the result.
    """
    opt = input("Pick 'a' for mean, 'b' for median, 'c' for mode: ")

    if opt == "a":
        print("picked: Mean")
        avg = statistics.mean(grades)
        return avg
    elif opt == "b":
        print("picked: Median")
        avg = statistics.median(grades)
        return avg
    elif opt == "c":
        print("picked: Mode")
        avg = statistics.mode(grades)
        return avg
    else:
        print("Error in pick_averaging_method: incorrect option picked")
        exit()

# Task 3:
#  Complete the function "pick_visualization" below:
def pick_visualization(average):
    """ prints the result in a format that depends on the user's selection

    Prints the numeric average or prints in a special way
    depending on user input.
    User should pick '1' for print average, or '2' for plot average.
    Any other input prints
    'Error in pick_visualization: incorrect option picked'.
    """
    """Prompts user for visualization preference (1 for standard print,

    2 for plot) and invokes the corresponding function.
    """
    opt = input("Pick '1' for print average, or '2' for plot average: ")

    if opt == "1":
        print_list_and_average(average)
    elif opt == "2":
        plot_grades(average)
    else:
        print("Error in pick_visualization: incorrect option picked")
        exit()


# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

# Do not modify this function
def print_list_and_average(average):
    print(f"The average of {grades} is {average}")

def plot_grades(average):
    print ("Annotated grades: ")
    prev = -1
    for g in grades:
        if prev < average < g:
            print("^", end="")
        if average > g:
            print(" ", end="")
        if average == g:
            print(f"({g})", end="")
        else:
            print(f"{g} ", end="")
        prev = g
    print()

# Do not modify this function
def main ():
    # calls the function and updates the grades
    read_five_ints()
    # this reorders the values in grades in increasing order
    grades.sort()
    print(f"Sorted grades: {grades}")
    # gets avg depending on selection
    avg = pick_averaging_method()
    # prints or 'plots' result
    pick_visualization(avg)
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
