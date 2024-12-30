# simple_interest.py
def calculate_simple_interest(principal, rate, time):
    """
    Calculate Simple Interest.

    :param principal: Principal amount
    :param rate: Annual interest rate (in percentage)
    :param time: Time period in years
    :return: Simple interest
    """
    return (principal * rate * time) / 100

if __name__ == "__main__":
    principal = float(input("Enter Principal Amount: "))
    rate = float(input("Enter Annual Interest Rate (in %): "))
    time = float(input("Enter Time Period (in years): "))
    interest = calculate_simple_interest(principal, rate, time)
    print(f"Simple Interest: {interest}")
