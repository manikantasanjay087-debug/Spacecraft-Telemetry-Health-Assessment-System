from flask import Flask, render_template, request
import pandas as pd
import joblib

from rules import check_rules
from utils import analyze_operator_note

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    # Read uploaded CSV
    file = request.files["telemetry"]
    telemetry = pd.read_csv(file)

    # Read latest telemetry row
    latest = telemetry.iloc[-1]

    # Rule-based analysis
    rule_status, reasons = check_rules(latest)

    # Prepare ML input
    X = pd.DataFrame([{
        "BatteryTemp": latest["BatteryTemp"],
        "BatteryVoltage": latest["BatteryVoltage"],
        "FuelLevel": latest["FuelLevel"],
        "CPUUsage": latest["CPUUsage"],
        "SignalStrength": latest["SignalStrength"]
    }])

    # ML prediction
    prediction = model.predict(X)[0]

    confidence = round(max(model.predict_proba(X)[0]) * 100, 2)

    # Operator note
    note = request.form["note"]

    findings = analyze_operator_note(note)

    # Recommended action
    if prediction == "Healthy":
        action = "Continue normal spacecraft monitoring."

    elif prediction == "Warning":
        action = "Monitor spacecraft closely and schedule diagnostics."

    else:
        action = "Immediate intervention required. Notify Mission Control."

    return render_template(
        "result.html",
        prediction=prediction,
        confidence=confidence,
        rule_status=rule_status,
        reasons=reasons,
        note=note,
        findings=findings,
        action=action
    )


if __name__ == "__main__":
    app.run(debug=True)
