"""
Stock API utilities for fetching real-time stock data
"""

import requests
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class StockAPI:
    """Handle stock data API calls"""
    
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.base_url = "https://api.example.com"  # Replace with actual API
    
    def get_stock_price(self, symbol):
        """Fetch current stock price"""
        try:
            # API call implementation
            response = requests.get(
                f"{self.base_url}/quote/{symbol}",
                params={'apikey': self.api_key}
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Error fetching stock price for {symbol}: {e}")
            return None
    
    def get_historical_data(self, symbol, start_date, end_date):
        """Fetch historical stock data"""
        try:
            response = requests.get(
                f"{self.base_url}/historical/{symbol}",
                params={
                    'from': start_date,
                    'to': end_date,
                    'apikey': self.api_key
                }
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Error fetching historical data for {symbol}: {e}")
            return None
    
    def search_stocks(self, query):
        """Search for stocks by symbol or name"""
        try:
            response = requests.get(
                f"{self.base_url}/search",
                params={'q': query, 'apikey': self.api_key}
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"Error searching stocks: {e}")
            return None
