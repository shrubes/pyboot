unlucky_numbers = [4, 13]

# for number in range(1, 21):
#     if number in unlucky_numbers:
#         print(f"{number} is unlucky")
#     elif number % 2 == 0:
#         print(f"{number} is even")
#     elif number % 2 != 0:
#         print(f"{number} is odd")

for number in range(1, 21):
    if number in unlucky_numbers:
        state = "unlucky"
    elif number % 2 == 0:
        state = "even"
    elif number % 2 != 0:
        state = "odd"
    print(f"{number} is {state}")
