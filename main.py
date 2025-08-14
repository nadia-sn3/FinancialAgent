from financial_agent import finance_agent

def main():
    print("\n" + "="*50 + "\n" )
    print("WELCOME TO FINANCIAL ANALYSIS TOOL".center(50) + "\n")
    print("\n" + "="*50)    
    print("\nThis tool provides financial insights about companies." + "\n")
    print("="*50 + "\n")

    while True:
        company_name = input("Enter company name (or 'exit' to quit): ").strip()
        
        if company_name.lower() == 'exit':
            print("\nThank you for using the Financial Analysis Tool. Goodbye!")
            break
        
        if company_name:
            print(f"\nFetching data for {company_name}...\n")
            finance_agent.print_response(
                f"Provide a financial summary including: "
                f"1. Current stock price\n"
                f"2. Analyst recommendations\n"
                f"3. Basic company information\n"
                f"4. Recent news\n"
                f"For {company_name}",
                stream=True
            )
            print("\n" + "="*50 + "\n")
        else:
            print("Please enter a valid company name.")

if __name__ == "__main__":
    main()