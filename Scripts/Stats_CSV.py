import pandas as pd

df = pd.read_csv("TFU-E2-MkI-35pct-runtime.csv")
runtime_hours = (df["time"].max() - df["time"].min()) / 3600
initial_lux = df["lux"].iloc[0]
final_lux = df["lux"].iloc[-1]
drop_pct = (1 - final_lux/initial_lux) * 100

print(f"Runtime: {runtime_hours:.2f} h")
print(f"Lumen drop: {drop_pct:.1f}% over run")
