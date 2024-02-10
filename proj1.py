# Your name:
# Your student id:
# Your email:
# Who or what you worked with on this homework (including generative AI like ChatGPT):
# If you worked with generative AI also add a statement for how you used it.  
# e.g.: 
# Asked Chatgpt hints for debugging and suggesting the general sturcture of the code

import csv
import unittest



def csv_loader(filename):

    """

    Load employee data from a CSV file.



    Args:

        filename (str): The name of the CSV file containing employee data.



    Returns:

        dict: A dictionary where each key is an employee ID and each value is another dictionary

        containing demographic categories ('gender', 'race', and 'hire_year') as keys and their corresponding data as values.

        The 'hire_year' is converted into an integer.


    Reminder: use encoding='utf-8-sig' when opening the file.
    """

    pass

    



def layoff_risk_level_group(employees, dict_risk_framework):

    """

    Split employee data into five different layoff-risk groups based on their hire years.



    Args:

        employees (dict): A dictionary where each key is an employee ID and each value is a dictionary

        containing employee data, including 'hire_year'.

        dict_risk_framework (dict): A dictionary where each key is a layoff risk level and each value is a
        
        tuple containing the earliest hiring year associated with that fire risk level and the latest hiring year associated with that layoff risk level.


    Returns:

        dict: A dictionary where each key is a layoff risk level and each value is another dictionary containing employee data associated with that layoff risk level.


    """

    pass

    



def race_or_gender_counter(employees):

    """

    Count the number of employees belonging to each race and gender category.



    Args:

        employees (dict): A dictionary where each key is an employee ID and each value is a dictionary

        containing employee data, including 'race' and 'gender'.



    Returns:

        dict: A dictionary containing two keys: 'race' and 'gender'. Each key maps to a sub-dictionary

        with race or gender categories as keys and their corresponding counts as values.



    """

    pass





def race_and_gender_counter(employees):

    """

    Count the number of employees within each combination of race and gender.



    Args:

        employees (dict): A dictionary where each key is an employee ID and each value is a dictionary

        containing employee data, including 'race' and 'gender'.



    Returns:

        dict: A dictionary where keys represent combinations of race and gender in the format "Race_Gender",

        and values represent the count of employees within each combination.



    """

    pass





def csv_writer(data, filename):

    """

    Write data to a CSV file.



    Args:

        data (dict): A dictionary containing data to be written to the CSV file.

        filename (str): The name of the CSV file to be created.


    Reminder: use encoding='utf-8-sig' when writing the file.
    """

    pass


#EXTRA CREDIT
def count_employees_by_years_worked(employees):

    """

    Count the number of employees of different years they worked based on each gender and each race.

    

    Args:

        employees (dict): A dictionary where each key is an employee ID and each value is a dictionary

        containing employee data, including 'race' and 'gender'.

    Returns:

        dict: A collection of nested dictionaries where the sequential keys are a working year (1976-hiring year), a race, and a gender in that order

        and the innermost values represent the count of employees whose information matches the hiring year, race, and gender keys.



    """

    pass




class TestEmployeeDataAnalysis(unittest.TestCase):

    def setUp(self):
        
        #Set up any variables you will need for your test cases
        
        #Feel free to use smaller_dataset.csv for your test cases so that you can verify the correct output

        pass


    def test_csv_loader(self):

        # Your test code for csv_loader goes here

        # Write a test case that checks for the length of the outer dictionary.

        
        # Write a test case that checks for the length of the inner dictionary value of the first (key, value) pair.

        pass



    def test_layoff_risk_level_group(self):
        # Set up the dictionary for the layoff risk level
        layoff_risk_dict = {'Very High': (1970, 1976), 'High': (1964, 1969), 'Medium': (1958, 1963), 'Low': (1954, 1957), 'Very Low': (1950, 1953)}

        # Your test code for layoff_risk_level_group goes here

        #Test that the function correctly puts employees into different layoff risk level groups based on their hiring year.

        pass



    def test_race_or_gender_counter(self):

        # Your test code for race_or_gender_counter goes here

        #Test that there are only two keys in the returned dictionary
        
        
        #Test that the function accurately counts the number of employees belonging to each race and gender category.

        pass



    def test_race_and_gender_counter(self):

        # Your test code for race_and_gender_counter goes here

        #Test that there are the correct number of keys in the dictionary representing each combination of race and gender in this dataset.
         
        
        # Test that the function correctly counts the number of employees within each combination of race and gender.
        
        pass






#You do not need to change anything in the main() function

def main():

    # Load employee data from the CSV file

    employee_data = csv_loader('GM_employee_data.csv')


    # Task 1: Put employees into different layoff risk level groups based on their hiring year
    layoff_risk_level = {'Very High': (1970, 1976), 'High': (1964, 1969), 'Medium': (1958, 1963), 'Low': (1954, 1957), 'Very Low': (1950, 1953)}
    dict_layoff_risk_level = layoff_risk_level_group(employee_data, layoff_risk_level)



    # Task 2: Count employees by race or gender for all employees and for employees whose layoff risk level is "Medium", "Low" or "Very Low"
    employees_not_high_risk = {**dict_layoff_risk_level["Medium"], **dict_layoff_risk_level["Low"], **dict_layoff_risk_level["Very Low"]} 
    race_gender_counts_total = race_or_gender_counter(employee_data)

    
    race_gender_counts_after_layoffs = race_or_gender_counter(employees_not_high_risk)



    # Task 3: Count employees by race and gender combinations before and after layoffs

    gendered_race_counts_total = race_and_gender_counter(employee_data)

    gendered_race_counts_after_layoffs = race_and_gender_counter(employees_not_high_risk)



    # Print and interpret the results

    print("Analysis Results:")

    print("--------------------------------------------------------")



    # Task 1: Putting employees into different layoff risk level groups based on their hiring year

    print("Task 1: Split Employees by Hire Year")

    print(f"Number of employees hired total: {len(employee_data)}")

    print(f"Number of employees with medium, low or very low risk: {len(employees_not_high_risk)}")

    print("--------------------------------------------------------")



    # Task 2: Comparing race or gender of all employees and employees with medium, low or very low risk

    print("Task 2: Comparing Race and Gender of All Employees and Employees with Medium, Low or Very Low Risk")

    print("Category: All Employees ---> Employees with Medium, Low or Very Low Risk")

    print("Race:")

    for category, count_all in race_gender_counts_total['race'].items():

        count_not_high_risk = race_gender_counts_after_layoffs['race'].get(category, 0)

        print(f"\t{category}: {count_all} ---> {count_not_high_risk}")



    print("Gender:")

    for category, count_all in race_gender_counts_total['gender'].items():

        count_not_high_risk = race_gender_counts_after_layoffs['gender'].get(category, 0)

        print(f"\t{category}: {count_all} ---> {count_not_high_risk}")



    print("--------------------------------------------------------")



    # Task 3: Comparing race and gender combinations for all employees and employees with medium, low or very low risk

    print("Task 3: Comparing Gendered Race Combinations Before and After Layoffs")

    print("Category: All Employees ---> Employees with Medium, Low or Very Low Risk")

    print("Gendered races:")

    for category, count_all in gendered_race_counts_total.items():

        count_not_high_risk = gendered_race_counts_after_layoffs.get(category, 0)

        print(f"\t{category}: {count_all} ---> {count_not_high_risk}")



    print("--------------------------------------------------------")



    csv_writer(gendered_race_counts_total, "GM_employee_data_all_before_layoffs.csv")

    csv_writer(gendered_race_counts_after_layoffs, "GM_employee_data_not_high_risk.csv")






if __name__ == "__main__":

    unittest.main(verbosity=2)

    main()



