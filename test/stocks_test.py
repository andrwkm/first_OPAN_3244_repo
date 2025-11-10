from pandas import DataFrame

from app.stocks import fetch_stocks_csv

def test_fetch_stocks_csv():

    stocks_df = fetch_stocks_csv("UNH")

    assert isinstance(stocks_df, DataFrame)

    assert "timestamp" in stocks_df.columns

    assert "adjusted_close" in stocks_df.columns

    assert len(stocks_df) >= 100