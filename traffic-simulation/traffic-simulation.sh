#!/bin/bash

# For Docker Desktop, use localhost as the NODE_IP
NODE_IP=localhost

# Set the NodePort for the service (replace with actual NodePort if different)
NODE_PORT=30001

# Print the resolved URL for debugging
echo "Simulating traffic to http://$NODE_IP:$NODE_PORT/node"

# Simulate traffic with Apache Benchmark
ab -n 1000 -c 50 http://$NODE_IP:$NODE_PORT/node
