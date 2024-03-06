import os
import glob
import pandas as pd

def process_dat_file(file_path):
    return pd.read_csv(file_path, sep='\t')


def write_to_csv(data, output_file):
    data.to_csv(output_file, index=False)

# Function to add footer to CSV file
def add_footer_to_csv(output_file, second_highest_salary, average_salary):
    with open(output_file, 'a') as csvfile:
        csvfile.write(f'Second Highest Salary,{second_highest_salary}\n')
        csvfile.write(f'Average Salary,{average_salary}\n')

# Function to find second highest salary and calculate average salary
def calculate_statistics(data):
    salaries = data['basic_salary']
    
    # Calculate average salary
    average_salary = salaries.mean()
    
    second_highest_salary = sorted(list(set(salaries)))[-2]
    
    return second_highest_salary, average_salary

def main():
    input_folder = 'C:/Users/RAHUL SINGH/Downloads/'
    output_folder = 'C:/Users/RAHUL SINGH/Documents/'
    
    dat_files = glob.glob(os.path.join(input_folder, '*.dat'))
    data = pd.DataFrame()
    for file_path in dat_files:
        df = process_dat_file(file_path)
        data = data._append(df)
    
    second_highest_salary, average_salary = calculate_statistics(data)
        
    # Write data to CSV file
    output_file = os.path.join(output_folder, os.path.basename('output.csv'))
    write_to_csv(data, output_file)
        
    # Add footer to CSV file
    add_footer_to_csv(output_file, str(second_highest_salary), str(average_salary))

if __name__ == "__main__":
    main()
