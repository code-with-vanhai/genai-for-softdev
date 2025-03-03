# company_service.py
from database_connection import DatabaseConnection

class CompanyData:
    def __init__(self, company_id, ticker, name, time_series):
        self.company_id = company_id
        self.ticker = ticker
        self.name = name
        self.time_series = time_series
        self.high_bollinger = []
        self.low_bollinger = []
        self.moving_average = []
        self.grade = ""

class CompanyDataFactory:
    @staticmethod
    def create(company_id, ticker, name, time_series):
        return CompanyData(company_id, ticker, name, time_series)

class CompanyService:
    @staticmethod
    def retrieve_by_ticker_or_id(identifier):
        """
        Retrieve a company and its time-series data by ticker or ID.
        """
        db = DatabaseConnection()
        cursor = db.cursor

        if isinstance(identifier, int):
            cursor.execute("SELECT id, ticker, name FROM Company WHERE id = ?", (identifier,))
        else:
            cursor.execute("SELECT id, ticker, name FROM Company WHERE ticker = ?", (identifier,))

        company = cursor.fetchone()
        if not company:
            return None

        company_id, ticker, name = company

        cursor.execute("SELECT date, value FROM TimeSeries WHERE company_id = ? ORDER BY date", (company_id,))
        time_series = cursor.fetchall()

        return CompanyDataFactory.create(company_id, ticker, name, time_series)

    @staticmethod
    def get_all_companies():
        """
        Retrieve a list of all companies in the database.
        """
        db = DatabaseConnection()
        cursor = db.cursor

        cursor.execute("SELECT id, ticker, name FROM Company ORDER BY ticker")
        companies = cursor.fetchall()

        return [{"id": c[0], "ticker": c[1], "name": c[2]} for c in companies]

    @staticmethod
    def get_company_time_series(identifier):
        """
        Retrieve only the time-series data for a given company by ID or ticker.
        """
        company = CompanyService.retrieve_by_ticker_or_id(identifier)
        if company:
            return company.time_series
        return None

    @staticmethod
    def get_latest_stock_price(identifier):
        """
        Retrieve the most recent stock price for a given company by ID or ticker.
        """
        db = DatabaseConnection()
        cursor = db.cursor

        if isinstance(identifier, int):
            cursor.execute("""
                SELECT value FROM TimeSeries 
                WHERE company_id = ? 
                ORDER BY date DESC LIMIT 1
            """, (identifier,))
        else:
            cursor.execute("""
                SELECT value FROM TimeSeries 
                WHERE company_id = (SELECT id FROM Company WHERE ticker = ?) 
                ORDER BY date DESC LIMIT 1
            """, (identifier,))

        result = cursor.fetchone()
        return result[0] if result else None
