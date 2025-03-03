# company_service_example.py
from company_service import CompanyService

def main():
    print("Fetching all companies...")
    companies = CompanyService.get_all_companies()
    for company in companies:
        print(company)
    
    print("\nFetching data for a specific company (AAPL)...")
    company = CompanyService.retrieve_by_ticker_or_id("AAPL")
    if company:
        print(f"Company: {company.name} ({company.ticker})")
        print("First 5 time-series records:", company.time_series[:5])
    else:
        print("Company not found.")
    
    print("\nFetching only time-series data for GOOGL...")
    time_series = CompanyService.get_company_time_series("GOOGL")
    if time_series:
        print("First 5 records:", time_series[:5])
    else:
        print("No time-series data found.")
    
    print("\nFetching the latest stock price for TSLA...")
    latest_price = CompanyService.get_latest_stock_price("TSLA")
    if latest_price:
        print(f"Latest TSLA stock price: {latest_price}")
    else:
        print("No stock price available.")

if __name__ == "__main__":
    main()
