# Greek Stocks Performance Comparison

A lightweight Django application for analyzing the historical performance of Greek stocks and optionaly, comparing them against the **S&P 500** (using the `SXR8.DE` ETF). The application calculates the benefits of DCA (Dollar Cost Averaging) method on invenstmens.

## Features

- Select a Greek stock.
- Configure:
  - Initial investment amount(optional).
  - Monthly contribution.
  - Investment start date.
  - Investment end date.
- Calculate:
  - Total invested capital.
  - Portfolio value.
  - Investment profit.
  - Annualized return persentage.
- Optionally compare the investment against the **S&P 500** (`SXR8.DE`).
- Visualize results with a performance chart.

## Technologies

- Python
- Django
- Matplotlib
- SQLite (or any database supported by Django ORM)


## Installation

Clone the repository:

```bash
git clone <repository-url>
cd <project>
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

**Linux / macOS**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the database migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

The application will be available at:

```
http://127.0.0.1:8000/
```

## Usage

1. Select a stock.
2. Enter:
   - Initial investment (Optional).
   - Monthly contribution.
   - Start date.
   - End date.
3. (Optional) Enable comparison with the S&P 500.
4. Submit the form to view:
   - Investment summary.
   - Performance statistics.
   - Portfolio value chart.

## Notes

- The S&P 500 comparison is performed using the **SXR8.DE** ETF.
- Calculations are based on historical price data.
- Past performance does not guarantee future results.

## License

This project is licensed under the MIT License.