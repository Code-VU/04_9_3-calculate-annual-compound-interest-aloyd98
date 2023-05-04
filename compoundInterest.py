def calculateCompoundInterest():
    
    def print_calcs(principal, time, rate):
        
        total_amount = principal*(1 + (rate/100))**time
        compound_interest = total_amount - principal

        print ('Compound Interest: ' + str(round(total_amount - principal,2)))
    
    def collect_client_input():
    
        client_principal = float(input("Principle (amount): "))
        client_time = float(input("Time: "))
        client_rate = float(input("Rate: "))

        return client_principal, client_time, client_rate
    
    def calculate_input():
        
        line_break = "---"

        client_principal_1, client_time_1, client_rate_1 = collect_client_input()
        print_calcs(client_principal_1, client_time_1, client_rate_1)
        print(line_break)

        client_principal_2, client_time_2, client_rate_2 = collect_client_input()
        print_calcs(client_principal_2,client_time_2,client_rate_2)
        print(line_break)

        client_principal_3, client_time_3, client_rate_3 = collect_client_input()
        print_calcs(client_principal_3,client_time_3,client_rate_3)

    calculate_input()


 #print("Compound Interest: "+str(interest))

    # end assignment

## If you want to test locally run > python compoundInterest.py

if __name__ == "__main__":
    calculateCompoundInterest()
