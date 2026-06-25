"""
Portfolio management utilities
"""

import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class Portfolio:
    """Manage user portfolio"""
    
    def __init__(self, user_id, initial_balance=10000):
        self.user_id = user_id
        self.balance = initial_balance
        self.holdings = {}  # {symbol: {quantity, avg_cost}}
        self.transactions = []
    
    def buy_stock(self, symbol, quantity, price):
        """Buy stocks"""
        cost = quantity * price
        
        if self.balance < cost:
            logger.warning(f"Insufficient balance for buying {quantity} shares of {symbol}")
            return False
        
        self.balance -= cost
        
        if symbol not in self.holdings:
            self.holdings[symbol] = {'quantity': 0, 'avg_cost': 0}
        
        # Calculate average cost
        old_quantity = self.holdings[symbol]['quantity']
        old_avg = self.holdings[symbol]['avg_cost']
        
        total_cost = (old_quantity * old_avg) + cost
        new_quantity = old_quantity + quantity
        new_avg = total_cost / new_quantity
        
        self.holdings[symbol]['quantity'] = new_quantity
        self.holdings[symbol]['avg_cost'] = new_avg
        
        self._record_transaction('BUY', symbol, quantity, price)
        logger.info(f"Bought {quantity} shares of {symbol} at ${price}")
        
        return True
    
    def sell_stock(self, symbol, quantity, price):
        """Sell stocks"""
        if symbol not in self.holdings or self.holdings[symbol]['quantity'] < quantity:
            logger.warning(f"Insufficient holdings of {symbol}")
            return False
        
        revenue = quantity * price
        self.balance += revenue
        
        self.holdings[symbol]['quantity'] -= quantity
        
        if self.holdings[symbol]['quantity'] == 0:
            del self.holdings[symbol]
        
        self._record_transaction('SELL', symbol, quantity, price)
        logger.info(f"Sold {quantity} shares of {symbol} at ${price}")
        
        return True
    
    def _record_transaction(self, transaction_type, symbol, quantity, price):
        """Record transaction in history"""
        transaction = {
            'date': datetime.now(),
            'type': transaction_type,
            'symbol': symbol,
            'quantity': quantity,
            'price': price,
            'total': quantity * price
        }
        self.transactions.append(transaction)
    
    def get_portfolio_value(self, current_prices):
        """Calculate current portfolio value"""
        value = self.balance
        for symbol, holding in self.holdings.items():
            if symbol in current_prices:
                value += holding['quantity'] * current_prices[symbol]
        return value
    
    def get_gain_loss(self, current_prices):
        """Calculate total gain/loss"""
        current_value = self.get_portfolio_value(current_prices)
        initial_investment = 10000  # Initial balance
        return current_value - initial_investment
