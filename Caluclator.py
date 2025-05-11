import math

def calculate_required_mark_for_first():
    marks = []
    print("\nEnter the marks for Level 5 across your four modules:")
    for i in range(4):
        mark = float(input(f"Enter mark {i + 1}: "))
        marks.append(mark)

    top_3_marks = sorted(marks, reverse=True)[:3]
    average = sum(top_3_marks) / len(top_3_marks)
    result = (70 - (average * 0.30)) / 0.7
    rounded_result = math.ceil(result)

    print(f"\nWhat you'll need to get on your Level 6 modules this year to secure a 1st honours: {rounded_result}%\n")

def calculate_classification():
    print("\nEnter your marks:")

    l5 = float(input("Level 5 average (%): ") or 0)

    print("\n-- ATICS (30 credits, two 50% assessments) --")
    atics1 = float(input("ATICS Assessment 1 (%): ") or 0)
    atics2 = float(input("ATICS Assessment 2 (%): ") or 0)
    atics = (atics1 + atics2) / 2

    print("\n-- OSIB (30 credits, two 50% assessments) --")
    osib1 = float(input("OSIB Assessment 1 (%): ") or 0)
    osib2 = float(input("OSIB Assessment 2 (%): ") or 0)
    osib = (osib1 + osib2) / 2

    print("\n-- ITIS (30 credits, single assessment) --")
    itis = float(input("ITIS Assessment (%): ") or 0)

    print("\n-- FYP (60 credits) --")
    fyp_prop = float(input("FYP Proposal (20%): ") or 0)
    fyp_report = float(input("FYP Report (60%): ") or 0)
    fyp_viva = float(input("FYP Viva (20%): ") or 0)
    fyp = 0.2 * fyp_prop + 0.6 * fyp_report + 0.2 * fyp_viva

    modules30 = [atics, osib, itis]
    lowest30 = min(modules30)
    total30 = sum(modules30) - lowest30

    points = total30 * 30 + fyp * 60
    l6_avg = points / 120
    overall = 0.7 * l6_avg + 0.3 * l5

    if overall >= 70:
        classification = "First (1st)"
    elif overall >= 60:
        classification = "Upper-Second (2:1)"
    elif overall >= 50:
        classification = "Lower-Second (2:2)"
    elif overall >= 40:
        classification = "Third"
    else:
        classification = "Fail"

    print(f"""
-- Summary --
ATICS: {atics:.2f}%
OSIB: {osib:.2f}%
ITIS: {itis:.2f}%
Lowest 30-credit module dropped: {lowest30:.2f}%
FYP: {fyp:.2f}% (60 credits)
Level 6 average (after drop): {l6_avg:.2f}%
Overall weighted average: {overall:.2f}%
Projected classification: {classification}
""")

def main():
    while True:
        print("Staffordshire Degree Classification Menu")
        print("1. Calculate required Level 6 average for 1st class honours")
        print("2. Calculate degree classification from Level 5 & 6 marks")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            calculate_required_mark_for_first()
        elif choice == "2":
            calculate_classification()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()
