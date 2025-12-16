#!/bin/bash

echo "Building Docker images..."
docker compose -f docker-compose.prod.yml build

echo "Stopping old containers..."
docker compose -f docker-compose.prod.yml down

echo "Starting containers..."
docker compose -f docker-compose.prod.yml up -d

echo "Deployment complete!"
