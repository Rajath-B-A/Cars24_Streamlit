import streamlit as st
import yfinance as yf

dic = {"Apple":"AAPL","Microsoft":"MSFT","Google":"GOOG"}

st.title('Stock Market App')

symbol = st.text_input("Please enter the ticker","AAPL")

tickerdata = yf.Ticker(symbol)

col1,col2 = st.columns(2)
with col1:
    start_date = st.date_input("Select the Start date")
with col2:
    end_date = st.date_input("Select the End date")

ticker_df=tickerdata.history(period='1d',start=start_date,end=end_date)

st.write("Here is the day wise stock price.")
st.dataframe(ticker_df)

st.write("Price movement over time.")
st.line_chart(ticker_df['Close'])