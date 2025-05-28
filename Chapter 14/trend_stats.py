import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from datetime import datetime
from pmdarima import auto_arima

# ----------------- PREPARE DEMO DATA -----------------
# Function to create a date range
def create_date_range(start_date, end_date, freq='H'):
    return pd.date_range(start=start_date, end=end_date, freq=freq)

# Generate a date range for one year of hourly data
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31, 23)
dates = create_date_range(start_date, end_date)

# Number of data points
n = len(dates)

# Hardcoded performance data with a constant deterioration in response time
data = {
    'Timestamp': dates,
    'Response Time (ms)': [200 + (i * 0.1) for i in range(n)],  # Linear deterioration in response time
    'Error Rate (%)': [0.5 + (0.01 * (i % 10)) for i in range(n)],  # Example pattern for error rate
    'CPU Usage (%)': [50 + (i % 20) for i in range(n)],  # Example pattern for CPU usage
    'Memory Usage (MB)': [1024 + (i % 1024) for i in range(n)],  # Example pattern for memory usage
    'User Load': [1000 + (i % 1000) for i in range(n)]  # Example pattern for user load
}

# Create DataFrame
performance_data = pd.DataFrame(data)
performance_data.set_index('Timestamp', inplace=True)

# ----------------- TIME SERIES DECOMPOSITION -----------------

# Perform time series decomposition on 'Response Time (ms)'
response_time_series = performance_data['Response Time (ms)']
decomposition = sm.tsa.seasonal_decompose(response_time_series, model='multiplicative', period=24)

# Plot the decomposition results
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(15, 10), sharex=True)

decomposition.observed.plot(ax=ax1)
ax1.set_ylabel('Observed')

decomposition.trend.plot(ax=ax2)
ax2.set_ylabel('Trend')

decomposition.seasonal.plot(ax=ax3)
ax3.set_ylabel('Seasonal')

decomposition.resid.plot(ax=ax4)
ax4.set_ylabel('Residual')

# ----------------- PLOT AND GRAPH -----------------

plt.suptitle('Time Series Decomposition of Response Time (ms)')
plt.savefig('time_series_decomposition.png')
plt.show()

# ----------------- CLEAR THE PLOT -----------------
plt.cla()

# ----------------- MOVING AVERAGES TREND ANALYSIS -----------------
performance_data['Response Time - 24H MA'] = performance_data['Response Time (ms)'].rolling(window=24).mean()
performance_data['Response Time - 7D MA'] = performance_data['Response Time (ms)'].rolling(window=24*7).mean()

# Plot original data and moving averages
plt.figure(figsize=(15, 8))

plt.plot(performance_data.index, performance_data['Response Time (ms)'], label='Original Response Time', color='blue')
plt.plot(performance_data.index, performance_data['Response Time - 24H MA'], label='24-Hour Moving Average', color='orange')
plt.plot(performance_data.index, performance_data['Response Time - 7D MA'], label='7-Day Moving Average', color='green')

plt.xlabel('Timestamp')
plt.ylabel('Response Time (ms)')
plt.title('Response Time with Moving Averages')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('response_time_moving_averages.png')
plt.show()

# ----------------- CLEAR THE PLOT -----------------
plt.cla()

# ----------------- ARIMA MODEL FORECAST -----------------
# Fit ARIMA model and make a forecast
response_time_series = performance_data['Response Time (ms)']
arima_model = auto_arima(response_time_series, seasonal=False, trace=True, error_action='ignore', suppress_warnings=True)
n_periods = 24 * 7  # Forecast for the next 7 days
forecast, conf_int = arima_model.predict(n_periods=n_periods, return_conf_int=True)

# Create a DataFrame for the forecasted values
forecast_index = pd.date_range(start=performance_data.index[-1], periods=n_periods + 1, freq='H')[1:]
forecast_df = pd.DataFrame(forecast, index=forecast_index, columns=['Forecast'])

# Plot original data, moving averages, and forecast
plt.figure(figsize=(15, 8))

plt.plot(forecast_df.index, forecast_df['Forecast'], label='ARIMA Forecast', color='red')

# Plot forecast confidence intervals
plt.fill_between(forecast_index, conf_int[:, 0], conf_int[:, 1], color='pink', alpha=0.3)

plt.xlabel('Timestamp')
plt.ylabel('Response Time (ms)')
plt.title('Response Time ARIMA Forecast')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('response_time_forecast.png')
plt.show()