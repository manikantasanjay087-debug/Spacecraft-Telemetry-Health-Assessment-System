def check_rules(data):
    """
    Check telemetry values and return detected issues.
    """

    reasons = []

    if data["BatteryTemp"] > 50:
        reasons.append("Battery temperature is too high")

    if data["BatteryVoltage"] < 26:
        reasons.append("Battery voltage is too low")

    if data["FuelLevel"] < 20:
        reasons.append("Fuel level is critically low")

    if data["CPUUsage"] > 90:
        reasons.append("CPU usage is very high")

    if data["SignalStrength"] < 50:
        reasons.append("Communication signal is weak")

    if len(reasons) == 0:
        status = "Healthy"
    elif len(reasons) <= 2:
        status = "Warning"
    else:
        status = "Critical"

    return status, reasons
