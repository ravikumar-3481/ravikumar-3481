def emi_calculator(principal, annual_intrest_rate, tenure_years):
    monthly_intrest_rate = annual_intrest_rate / (12 * 100)
    tenure_months = tenure_years * 12
    
    emi = principal * monthly_intrest_rate * ( 1 + monthly_intrest_rate)**tenure_months /\
    (( 1 + monthly_intrest_rate) ** tenure_months - 1 )
    
    total_payment = emi * tenure_months
    total_intrest = total_payment - principal
    
    return round(emi,2), round(total_payment,2), round(total_intrest,2)


print("Welcome To Emi Calculator, Here You can calculate \nyour Emi ,Intrest by Enter Your Principal Amount (₹), Annual Interest Rate (%), And Tenure (in years)\n \n")
p = float(input("    Enter Your Loan Amount (₹) "))
r = float(input("\n    Enter Annual Intrest Rate (%) "))
n = int(input("\n    Enter tenure Years "))
    
emi,total,intrest = emi_calculator(p,r,n)


print(f"\n📌 Your Monthly Emi : {emi} ")
print(f"💰 Your Total Payment : {total} ")
print(f"📈 Your Total Interest : {intrest}")

print(f" \n \n Here is Your Result {emi_calculator(p, r, n)}")    

    
