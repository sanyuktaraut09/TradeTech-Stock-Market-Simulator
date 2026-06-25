# TradeTech Stock Market Simulator

A web-based stock market simulator application that allows users to practice trading stocks in a risk-free environment.

## Features

- **User Authentication**: Secure login and registration system
- **Real-time Stock Data**: Live stock prices and market updates
- **Portfolio Management**: Track your investments and portfolio performance
- **Trading Interface**: Buy and sell stocks with a simple interface
- **Transaction History**: View all your buy and sell transactions
- **Performance Analytics**: Monitor your gain/loss and portfolio metrics

## Tech Stack

- **Backend**: Python Flask
- **Database**: SQLite (SQLAlchemy ORM)
- **Frontend**: HTML5, CSS3, JavaScript
- **Authentication**: Flask-Login
- **API Integration**: Requests library

## Project Structure

```
TradeTech-Stock-Market-Simulator/
├── app.py                 # Main Flask application
├── config.py              # Configuration settings
├── models.py              # Database models
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── .gitignore             # Git ignore rules
│
├── static/
│   ├── css/
│   │   └── style.css      # Main stylesheet
│   ├── js/
│   │   └── script.js      # Main JavaScript
│   └── images/            # Image assets
│
├── templates/
│   ├── base.html          # Base template
│   ├── index.html         # Home page
│   ├── dashboard.html     # User dashboard
│   ├── portfolio.html     # Portfolio page
│   ├── history.html       # Transaction history
│   ├── login.html         # Login page
│   └── register.html      # Registration page
│
├── utils/
│   ├── stock_api.py       # Stock API utilities
│   ├── portfolio.py       # Portfolio management
│   └── transaction.py     # Transaction processing
│
├── screenshots/           # Application screenshots
└── docs/                  # Documentation
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sanyuktaraut09/TradeTech-Stock-Market-Simulator.git
   cd TradeTech-Stock-Market-Simulator
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

## Configuration

Create a `.env` file in the root directory for environment variables:

```env
SECRET_KEY=your_secret_key_here
STOCK_API_KEY=your_api_key_here
DATABASE_URL=sqlite:///database.db
FLASK_ENV=development
```

## Usage

1. **Register**: Create a new account with username, email, and password
2. **Login**: Sign in with your credentials
3. **Dashboard**: View market overview and quick trade options
4. **Buy/Sell**: Execute buy and sell transactions
5. **Portfolio**: Monitor your holdings and performance
6. **History**: Review all your transactions

## API Integration

The application uses external stock market APIs to fetch real-time data. Configure your API key in the `.env` file.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, email support@tradetech.com or open an issue on GitHub.

## Author

Sanyukta Raut

## Acknowledgments

- Flask documentation
- SQLAlchemy community
- Stock market API providers
