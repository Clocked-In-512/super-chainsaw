##Robert Fernandez
##Complete
##This program will read random numbers from a file, display them, and calculate their total, count, and average.

def main():
    try:
        with open('random_numbers.txt', 'r') as file:
            numbers = [int(line.strip()) for line in file.readlines()]
            
            if not numbers:
                print("No numbers found in the file.")
                return
            
            total = sum(numbers)
            count = len(numbers)
            average = total / count

            print(f"Numbers: {numbers}")
            print(f"Total: {total}")
            print(f"Count: {count}")
            print(f"Average: {average:.2f}")

    except FileNotFoundError:
        print("The file random_numbers.txt does not exist.")
    except ValueError:
        print("The file contains non-numeric data.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
