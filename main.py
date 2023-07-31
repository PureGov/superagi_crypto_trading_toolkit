from api_client import APIClient
from data_processor import DataProcessor
from trading_strategy import TradingStrategy
from portfolio_manager import PortfolioManager

def main():
    # Initialize APIClient
    api_client = APIClient()

    # Fetch market data
    market_data = api_client.fetch_market_data()

    # Initialize DataProcessor
    data_processor = DataProcessor()

    # Process and analyze market data
    analyzed_data = data_processor.process_data(market_data)

    # Initialize TradingStrategy
    trading_strategy = TradingStrategy()

    # Execute trading strategy
    trading_strategy.execute_strategy(analyzed_data)

    # Initialize PortfolioManager
    portfolio_manager = PortfolioManager()

    # Manage user's portfolio
    portfolio_manager.manage_portfolio()

if __name__ == "__main__":
    main()
