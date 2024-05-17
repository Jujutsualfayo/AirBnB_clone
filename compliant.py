def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest


principal = 1000
rate = 5
time = 2
interest = calculate_simple_interest(principal, rate, time)
print(f"The simple interest is: {interest}")
