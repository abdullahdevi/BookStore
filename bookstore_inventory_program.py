
import csv

def main():
    num_books = input_number_of_books()

    # setting the sizes of the parallel lists
    titles = [' '] * num_books
    authors = [' '] * num_books
    quantities = [0] * num_books

    for i in range(num_books):
        titles[i] = input_book_title()
        authors[i] = input_book_author()
        quantities[i] = input_quantity_on_hand()

    display_inventory(titles, authors, quantities)
    write_inventory_to_file(titles, authors, quantities)

# Function to input number of books with exception handling
def input_number_of_books():
    while True:
        try:
            num_books = int(input("Enter the number of books: "))
            if num_books <= 0:
                raise ValueError("The number of books must be greater than 0.")
            return num_books
        except ValueError as e:
            print(e)

# Function to input the book title
def input_book_title():
    return input("Enter the book title: ")

# Function to input the book author
def input_book_author():
    return input("Enter the book author: ")

# Function to input quantity on hand with exception handling
def input_quantity_on_hand():
    while True:
        try:
            quantity = int(input("Enter the quantity on hand: "))
            if quantity < 0:
                raise ValueError("Quantity on hand must be >= 0.")
            return quantity
        except ValueError as e:
            print(e)

# Function to display the inventory
def display_inventory(titles, authors, quantities):
    print(f'{"Title":20s} {"Author":20s} {"Quantity":10s}')
    for i in range(len(titles)):
        print(f'{titles[i]:20s} {authors[i]:20s} {quantities[i]:10d}')

# Function to write the inventory to a CSV file
def write_inventory_to_file(titles, authors, quantities):
    try:
        with open('book_inventory.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Title', 'Author', 'Quantity'])
            for i in range(len(titles)):
                writer.writerow([titles[i], authors[i], quantities[i]])
        print("Inventory successfully written to book_inventory.csv")
    except IOError as e:
        print(f"Error writing to file: {e}")

# Call the main function
if __name__ == "__main__":
    main()
