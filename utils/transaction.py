"""
Transaction processing and validation
"""

import logging
from datetime import datetime
from enum import Enum

logger = logging.getLogger(__name__)


class TransactionType(Enum):
    BUY = "BUY"
    SELL = "SELL"


class TransactionStatus(Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"


class Transaction:
    """Represent a single transaction"""
    
    def __init__(self, user_id, transaction_type, symbol, quantity, price):
        self.user_id = user_id
        self.transaction_type = transaction_type
        self.symbol = symbol
        self.quantity = quantity
        self.price = price
        self.total = quantity * price
        self.timestamp = datetime.now()
        self.status = TransactionStatus.PENDING
    
    def execute(self, portfolio):
        """Execute the transaction"""
        try:
            if self.transaction_type == TransactionType.BUY:
                success = portfolio.buy_stock(self.symbol, self.quantity, self.price)
            elif self.transaction_type == TransactionType.SELL:
                success = portfolio.sell_stock(self.symbol, self.quantity, self.price)
            else:
                success = False
            
            if success:
                self.status = TransactionStatus.COMPLETED
                logger.info(f"Transaction {self.transaction_type.value} completed for {self.symbol}")
                return True
            else:
                self.status = TransactionStatus.FAILED
                logger.warning(f"Transaction {self.transaction_type.value} failed for {self.symbol}")
                return False
        
        except Exception as e:
            self.status = TransactionStatus.FAILED
            logger.error(f"Error executing transaction: {e}")
            return False
    
    def cancel(self):
        """Cancel the transaction"""
        self.status = TransactionStatus.CANCELLED
        logger.info(f"Transaction cancelled: {self.transaction_type.value} {self.symbol}")
    
    def to_dict(self):
        """Convert transaction to dictionary"""
        return {
            'user_id': self.user_id,
            'type': self.transaction_type.value,
            'symbol': self.symbol,
            'quantity': self.quantity,
            'price': self.price,
            'total': self.total,
            'timestamp': self.timestamp.isoformat(),
            'status': self.status.value
        }
