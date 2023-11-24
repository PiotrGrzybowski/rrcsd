
def main() -> None:
    piotr_contract = HourlyContract(pay_rate=50, hours_worked=100)
    piotr = Employee(name="Piotr", contract=piotr_contract)
    print(f"{piotr.name} worked {piotr_contract.hours_worked} hours and earned ${piotr.calculate_salary()}.")

    rachel_contract = PermanentContract(monthly_salary=5000, bonus_percentage=0.1)
    rachel = Employee(name="Rachel", contract=rachel_contract)
    print(f"{rachel.name} earned ${rachel.calculate_salary()}.")


if __name__ == "__main__":
    main()
