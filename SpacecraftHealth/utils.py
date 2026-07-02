def analyze_operator_note(note):
    """
    Analyze operator note and detect important keywords.
    """

    findings = []

    note = note.lower()

    if "temperature" in note:
        findings.append("Operator reported temperature issue.")

    if "battery" in note:
        findings.append("Operator reported battery issue.")

    if "communication" in note:
        findings.append("Operator reported communication issue.")

    if "signal" in note:
        findings.append("Operator reported signal issue.")

    if "fuel" in note:
        findings.append("Operator reported fuel issue.")

    if "cpu" in note:
        findings.append("Operator reported CPU issue.")

    if len(findings) == 0:
        findings.append("No issues found in operator note.")

    return findings
