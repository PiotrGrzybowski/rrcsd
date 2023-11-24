This code defines a simple system to calculate salaries for employees based on different types of contracts using Python. 


1. Implement Abstract Base Class Contract with single abstract method payment.

2. Implement PermanentContract and HourlyContract classes that inherit from Contract. Implement following fields for PermanentContract:
  - monthly_salary
  - bonus_percentage
  - Implement payment method for PermanentContract that calculates total payment based on monthly_salary and bonus_percentage.

3. Implement HourlyContract that has following fields:
  - hours_worked
  - hourly_rate
  - Implement payment method for HourlyContract that calculates total payment based on hours_worked and hourly_rate.

4. Implement Employee class that has following fields:
  - name
  - contract
  - Implement calculate_salary method that calculates salary based on contract type.

5. Main is already implemented 
