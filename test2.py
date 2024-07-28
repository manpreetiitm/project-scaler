import requests
import time
import json

# Constants
TARGET_CPU_UTILIZATION = 0.80
CHECK_INTERVAL = 5  # seconds
API_BASE_URL = "http://localhost:8123/app"  # Default port can be overridden by --port flag
min_replicas = 1 # Replicas shouldnt go below this

def get_current_status():
    """Fetch the current status of the application to get CPU utilization and replica count."""
    response = requests.get(f"{API_BASE_URL}/status", headers={"Accept": "application/json"})
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

def update_replicas(new_replica_count):
    """Update the number of replicas for the application."""
    data = {"replicas": new_replica_count}
    response = requests.put(f"{API_BASE_URL}/replicas", headers={"Content-Type": "application/json"}, data=json.dumps(data))
    response.raise_for_status()  # Raise an error for bad responses
    print(f"Updated replicas to {new_replica_count}")

def main():
    while True:
        try:
            status = get_current_status()
            current_cpu = status['cpu']['highPriority']
            current_replicas = status['replicas']

            print(f"Present CPU Utilization: {current_cpu}, Present Replicas: {current_replicas}")

            # Calculate desired replicas to maintain target CPU utilization
            if current_cpu > TARGET_CPU_UTILIZATION:
                new_replica_count = int(current_replicas * (current_cpu / TARGET_CPU_UTILIZATION))
            elif current_cpu == TARGET_CPU_UTILIZATION:
               print("Scaling is not required")
               exit() 
            else:
                # Decrease replicas to increase CPU utilization
                new_replica_count = max(current_replicas - 1, min_replicas) #Actual Auto-Scaler should reduce the number of replicas as well if CPU < Threshold 0.80

            new_replica_count = max(1, new_replica_count)  # Ensure replica count doesn't go below 1
            
            if new_replica_count != current_replicas:
                update_replicas(new_replica_count)

        except requests.exceptions.RequestException as e:
            print(f"Error while communicating with the application: {e}")
        
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
