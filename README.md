# **Legal Disclaimer**

This honeypot is intended for **defensive and educational purposes only**. Use of this tool comes with legal and ethical responsibilities.

Please read the full [Legal Disclaimer](LegalDisclaimer.md) before deploying or using this honeypot to ensure compliance with relevant laws and regulations.

# Cybersecurity Honeypot

A Python-based honeypot designed to emulate vulnerable services, log malicious activity, and analyze attack patterns using machine learning. This tool is intended for research and defensive purposes to understand attacker behavior and improve security.

---

## **Features**

### **Service Emulation**

- Emulates the following services to attract attackers:
  - **SSH (port 22)**
  - **HTTP (port 80)**
  - **FTP (port 21)**
- Simulates responses to make services appear legitimate.

### **Connection Logging**

- Captures critical details for each connection:
  - Source IP address.
  - Source port.
  - Timestamp.
  - Service accessed.
  - Geolocation (latitude and longitude).
- Logs are stored in JSON format (`honeypot_logs.json`).

### **Machine Learning Analysis**

- Uses **K-Means clustering** to analyze attack patterns based on geolocation.
- Generates scatter plots for visualizing clusters of attacker activity.

### **Real-Time Geolocation Mapping**

- Maps IP addresses to approximate geolocations using `geopy`.

### **Customization**

- Easily modify ports or add additional services to emulate.

---

## **Getting Started**

### **Prerequisites**

- Python 3.7 or higher.
- Install the required dependencies:

```bash
pip install geopy scikit-learn pandas numpy matplotlib


```

# **Troubleshooting**

| **Issue**              | **Cause**                     | **Solution**                             |
|------------------------|-------------------------------|------------------------------------------|
| Dependency not found   | Missing library               | Run `pip install -r requirements.txt`    |
| Permission denied      | Lack of admin privileges      | Run the script with elevated permissions |
| Geolocation errors     | Geopy cannot resolve IP       | Check your internet connection           |


# **Future Improvements**

- Integration with threat intelligence APIs.
- Adding more services (e.g., DNS, SMTP).
- Real-time dashboards for attack monitoring.

## Legal and Ethical Examples

### Example Use Cases:

1. **Research and Education:**

   - Understand attacker behavior patterns.
   - Train cybersecurity students on real-world attack scenarios.

2. **Defensive Preparation:**
   - Simulate attacks to test detection and response systems.
   - Use log data to improve firewall rules or intrusion detection configurations.

### **What Not to Do**

- Deploy the honeypot on a public network without informing relevant parties.
- Use it to collect unauthorized data or interfere with legitimate operations.

Always consult with legal and compliance teams before deploying the honeypot in any environment.

## FAQ

### **1. Will this honeypot affect my network performance?**

No, the honeypot is designed to operate independently and should not interfere with regular network traffic. However, ensure it is deployed on an isolated network or VM for safety.

### **2. Can I test the honeypot without exposing it to attackers?**

Yes, you can test the honeypot by connecting locally (e.g., `telnet localhost 22`). Logs will record your activity for analysis.

### **3. What if attackers compromise the honeypot?**

The honeypot is not designed to be fully secure but to log attacker behavior. Always deploy it in a sandboxed environment to prevent further compromise.

### **4. What data does the honeypot collect?**

It logs:

- Source IP address and port.
- Timestamp of connection.
- Geolocation (latitude/longitude) of IP.
- Service accessed (SSH, HTTP, FTP).

Sensitive data like IP addresses can be anonymized or encrypted if required.

### **5. How do I add new services?**

Edit the `run_service` method in `honeypot.py` and define the behavior for the new service. Update the `get_service_name` method to map the new port to a service name.
