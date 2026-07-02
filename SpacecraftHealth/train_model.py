import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
df = pd.read_csv("dataset/spacecraft_health.csv")

# Features and target
X = df[["BatteryTemp", "BatteryVoltage", "FuelLevel", "CPUUsage", "SignalStrength"]]
y = df["Health"]

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

print("Model trained successfully!")
print("Saved as model.pkl")
