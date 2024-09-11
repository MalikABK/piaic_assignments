# Today we are building a number exploration game for our friends

### Steps to make this exploration game
  * first will ask the user to enter his name
  * After that we will ask the user to enter his three favorite numbers
  * we will store the user's favorite numbers in a list
  * we will loop through the list to tell the user number is odd or even
  * And we will also print the each number and it's square
  * finally we will calculate total sum of the number and check if it's a prime number
# CODE 
  ```python
  def is_prime(n):
    
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    name: str = input("Enter your name: ")
    num_list: list[int] = []
    first_favorite_number: int = int(input("Enter your first favorite number: "))
    num_list.append(first_favorite_number)
    second_favorite_number: int = int(input("Enter your second favorite number: "))
    num_list.append(second_favorite_number)
    third_favorite_number: int = int(input("Enter your third favorite number: "))
    num_list.append(third_favorite_number)

    print(f"Hello, {name}! Lets explore your favorite number: ")

    list_tuples: list[tuple[int, int]] = []

    for num in num_list:
        if num % 2 == 0:
            print(f"The number {num} is an even.")
            list_tuples.append((num, num**2))
        else:
            print(f"The number {num} is an odd.")
            list_tuples.append((num, num**2))
        
    for num, square_num in list_tuples:
            print(f"Number {num} and it's square {square_num}.")

    total: int = sum(num_list)

    print(f"The sum of your favorite numbers is {total}.")
    
    if is_prime(total):
        print(f"Amazing! The {total} is a prime number!")
    else:
        print(f"the {total} is not a prime number, but it's still special!")

if __name__ == "__main__":
    main()

```
