# project-scaler
scaler-project

ScaleIt
ScaleIt is an auto-scaler application designed to manage the number of replicas of a separate application based on its CPU utilization metrics. The goal is to adjust the number of replicas dynamically to keep the average CPU utilization around 80% (0.80).

Purpose
The application interfaces with a provided API to monitor and adjust the number of replicas. The provided application mimics real-world behavior with fluctuating CPU usage and occasionally returns errors. Your task is to maintain an optimal number of replicas to ensure the average CPU usage stays around the desired threshold.

Requirements
Language: Python, Go, Ruby, Java, TypeScript/JavaScript, or C/C++
Code should be clean, readable, testable, performant, and well-documented.
Demonstrate knowledge of best practices in the chosen programming language.
Correct and bug-free code.

API Overview
Current Status
Endpoint: /app/status
Method: GET
Headers: Accept: application/json
Response:
json
Copy code
{
    "cpu": {
        "highPriority": 0.68
    },
    "replicas": 10
}
cpu.highPriority: CPU utilization as a float between 0 and 1.
replicas: Current number of replicas (integer greater than or equal to 1).
Updating the Replica Count
Endpoint: /app/replicas
Method: PUT
Headers: Content-Type: application/json
Request Body:
json
Copy code
{
    "replicas": 11
}
replicas: New number of replicas (integer greater than one).
