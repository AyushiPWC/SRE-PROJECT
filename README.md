# Hotel Booking Platform 🚀

![Python](https://img.shields.io/badge/Python-3.12+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Kind-326CE5)
![Prometheus](https://img.shields.io/badge/Monitoring-Prometheus-orange)
![Grafana](https://img.shields.io/badge/Dashboard-Grafana-F46800)
![GitHub
Actions](https://img.shields.io/badge/CI/CD-GitHub%20Actions-2088FF)

## Overview

A production-style **Hotel Booking Platform** built with **FastAPI**,
**React**, and **PostgreSQL**. The application is containerized with
**Docker**, deployed on **Kubernetes (Kind)**, monitored using
**Prometheus & Grafana**, and automated using **GitHub Actions CI/CD**
with a **self-hosted runner**.

## Features

-   User Authentication
-   Hotel CRUD APIs
-   Booking APIs
-   Swagger UI (`/docs`)
-   PostgreSQL persistence
-   Prometheus metrics (`/metrics`)
-   Grafana dashboards
-   Kubernetes Ingress
-   Public access through Cloudflare Tunnel
-   Automated CI/CD

------------------------------------------------------------------------

# Architecture

``` text
                Git Push
                   │
          GitHub Actions CI
                   │
        Build Docker Images
                   │
          Push to Docker Hub
                   │
          GitHub Actions CD
                   │
        Self-hosted GitHub Runner
                   │
              Kind Cluster
                   │
      ┌────────────┴─────────────┐
      │                          │
 React Frontend            FastAPI Backend
      │                          │
      └────────────┬─────────────┘
                   │
             PostgreSQL
                   │
            Prometheus
                   │
               Grafana
```

------------------------------------------------------------------------

# Technology Stack

| Component | Technology |
|------------|------------|
| **Frontend** | React |
| **Backend** | FastAPI |
| **Database** | PostgreSQL |
| **ORM** | SQLAlchemy |
| **API Documentation** | Swagger UI |
| **Containers** | Docker |
| **Container Orchestration** | Kubernetes (Kind) |
| **Ingress Controller** | NGINX Ingress |
| **Monitoring** | Prometheus + Grafana |
| **CI/CD Pipeline** | GitHub Actions |
| **Build Runner** | Self-hosted Windows Runner |
| **Public Access** | Cloudflare Tunnel |

------------------------------------------------------------------------

# Project Structure

``` text
hotel-booking/
├── backend/
├── frontend/
├── k8s/
├── docker-compose.yml
├── .github/
│   └── workflows/
└── README.md
```

------------------------------------------------------------------------

# API Endpoints

## Authentication

-   POST `/api/v1/login`
-   POST `/api/v1/register`

## Hotels

-   GET `/api/v1/hotels`
-   POST `/api/v1/hotels`
-   PUT `/api/v1/hotels/{id}`
-   DELETE `/api/v1/hotels/{id}`

## Bookings

-   POST `/api/v1/bookings`
-   GET `/api/v1/bookings`
-   DELETE `/api/v1/bookings/{id}`
-   PUT  `/api/v1/bookings/{booking_id}/status`

## Documentation

-   Swagger: `/docs`
-   OpenAPI: `/openapi.json`

------------------------------------------------------------------------

# Monitoring

The backend exposes Prometheus metrics via:

``` text
/metrics
```

Grafana dashboards display: - HTTP request count - HTTP request
duration - Average response time - Backend health

------------------------------------------------------------------------

# Kubernetes Components

-   Deployment (Frontend)
-   Deployment (Backend)
-   StatefulSet (PostgreSQL)
-   Services
-   NGINX Ingress
-   ConfigMaps / Secrets 

------------------------------------------------------------------------

# CI/CD Pipeline

1.  Developer pushes code.
2.  GitHub Actions starts CI.
3.  Docker images are built.
4.  Images are pushed to Docker Hub.
5.  CD workflow runs on self-hosted runner.
6.  Kubernetes deployment is updated.
7.  Grafana reflects live metrics.

------------------------------------------------------------------------

# Local Development

## Backend
``` bash
cd backend
python -m venv venv
pip install -r requirements.txt
uvicorn app.main:app --reload
```
## Frontend

``` bash
cd frontend
npm install
npm run dev
```
## Docker

``` bash
docker compose up -d
```
## Kubernetes

``` bash
kubectl apply -f k8s/
```
------------------------------------------------------------------------
**# CLOUDFLARED link to access the file:**
https://rice-deer-metres-array.trycloudflare.com/grafana/ -- grafana

https://rice-deer-metres-array.trycloudflare.com/docs -- Swagger UI

https://rice-deer-metres-array.trycloudflare.com/ -- Hotelp-booking-page

**Used Kind and hosted on the CloudFlared Tunnel, else we can use Cloud service provider as well** 

# Future Enhancements
-   Helm Charts
-   Argo CD
-   Terraform
-   Horizontal Pod Autoscaler
-   Alertmanager
-   Distributed Tracing (OpenTelemetry)
------------------------------------------------------------------------
# Author
**Ayushi Mukherjee**
------------------------------------------------------------------------

