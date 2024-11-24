import socket
import threading
import json
import random
from datetime import datetime
from geopy.geocoders import Nominatim
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Honeypot:
    def __init__(self, host="0.0.0.0", ports=(22, 80, 21)):
        self.host = host
        self.ports = ports
        self.logs = []
        self.geolocator = Nominatim(user_agent="honeypot")
        self.attack_patterns = []
        self.model = None

    def start(self):
        print("Starting honeypot...")
        for port in self.ports:
            thread = threading.Thread(target=self.run_service, args=(port,))
            thread.start()

    def run_service(self, port):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, port))
        server_socket.listen(5)
        print(f"Listening on port {port}...")

        while True:
            client_socket, client_address = server_socket.accept()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = self.log_connection(client_address, port, timestamp)

            if port == 22:  # SSH
                self.emulate_ssh(client_socket, log_entry)
            elif port == 80:  # HTTP
                self.emulate_http(client_socket, log_entry)
            elif port == 21:  # FTP
                self.emulate_ftp(client_socket, log_entry)

            client_socket.close()

    def log_connection(self, client_address, port, timestamp):
        location = self.get_location(client_address[0])
        log_entry = {
            "timestamp": timestamp,
            "source_ip": client_address[0],
            "source_port": client_address[1],
            "service": self.get_service_name(port),
            "geo_location": location,
        }
        self.logs.append(log_entry)
        print(f"Logged connection: {log_entry}")
        return log_entry

    def get_location(self, ip):
        # Simulate IP location retrieval
        try:
            location = self.geolocator.geocode(ip)
            if location:
                return {"latitude": location.latitude, "longitude": location.longitude}
            else:
                return {"latitude": random.uniform(-90, 90), "longitude": random.uniform(-180, 180)}
        except:
            return {"latitude": random.uniform(-90, 90), "longitude": random.uniform(-180, 180)}

    def get_service_name(self, port):
        return {22: "SSH", 80: "HTTP", 21: "FTP"}.get(port, "Unknown")

    def emulate_ssh(self, client_socket, log_entry):
        client_socket.send(b"SSH-2.0-OpenSSH_8.0\r\n")
        log_entry["action"] = "Simulated SSH response sent"

    def emulate_http(self, client_socket, log_entry):
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>Welcome to the Honeypot</h1>"
        client_socket.send(response.encode())
        log_entry["action"] = "Simulated HTTP response sent"

    def emulate_ftp(self, client_socket, log_entry):
        client_socket.send(b"220 Welcome to the Honeypot FTP server\r\n")
        log_entry["action"] = "Simulated FTP response sent"

    def save_logs(self, filename="honeypot_logs.json"):
        with open(filename, "w") as log_file:
            json.dump(self.logs, log_file, indent=4)
        print(f"Logs saved to {filename}")

    def analyze_logs(self):
        print("Analyzing logs...")
        df = pd.DataFrame(self.logs)
        df["latitude"] = df["geo_location"].apply(lambda x: x["latitude"])
        df["longitude"] = df["geo_location"].apply(lambda x: x["longitude"])
        self.attack_patterns = df[["latitude", "longitude"]]
        self.run_clustering(df)

    def run_clustering(self, df):
        kmeans = KMeans(n_clusters=3)
        coords = df[["latitude", "longitude"]].values
        self.model = kmeans.fit(coords)
        df["cluster"] = kmeans.labels_
        self.plot_clusters(df)

    def plot_clusters(self, df):
        plt.figure(figsize=(10, 6))
        for cluster in df["cluster"].unique():
            subset = df[df["cluster"] == cluster]
            plt.scatter(subset["longitude"], subset["latitude"], label=f"Cluster {cluster}")
        plt.title("Attack Patterns by Geolocation")
        plt.xlabel("Longitude")
        plt.ylabel("Latitude")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    honeypot = Honeypot()
    try:
        honeypot.start()
    except KeyboardInterrupt:
        print("Stopping honeypot...")
        honeypot.save_logs()
        honeypot.analyze_logs()

