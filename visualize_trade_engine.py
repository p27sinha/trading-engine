import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# FIX: Read CSV using comma separator
df = pd.read_csv('trades.csv', sep=',', engine='python')
print(df.head())
print(df.shape)

# Normalize and check column names
df.columns = df.columns.str.strip().str.capitalize()
print(df.columns)

# Continue if Price column exists
if 'Price' in df.columns:
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
    df = df.dropna(subset=['Price'])

    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df['Price'], label='Trade Price', color='blue')
    plt.xlabel('Trade Number')
    plt.ylabel('Price')
    plt.title('Trade Price Over Time')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('trade_prices.png')
    print("✅ Chart saved as trade_prices.png")
else:
    print("❌ 'Price' column not found. Please check your CSV formatting.")