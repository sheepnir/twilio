import csv

def read_phone_numbers(file_name):
    phone_numbers = []
    with open(file_name, 'r') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            phone_numbers.append(row[' phone_number'])  # added a space before phone_number

    return phone_numbers
'''
file_name = 'customer_list.csv'
phone_numbers = read_phone_numbers(file_name)

for number in phone_numbers:
    print(number)

first_number = phone_numbers[0]
print(first_number)
'''
# Example usage:


