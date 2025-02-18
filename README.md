# Crypto Data Integration with Elasticsearch

## Overview

This project integrates real-time cryptocurrency data from an external API and stores it in **Elasticsearch** for efficient searching, retrieval, and analytics. With this setup, we can query historical and live crypto data with ease, enabling powerful insights for future dashboards and analytics.

## Features

- **Real-Time Data Integration**: Continuously pulls cryptocurrency data from a public API.
- **Elasticsearch Integration**: Stores the data in Elasticsearch with customized mappings for efficient querying and analysis.
- **Dockerized Setup**: The entire application, including the Elasticsearch cluster, is containerized using Docker for easy deployment and scalability.
- **Future Enhancements**: Currently, working on enhancing the API integration to leverage the stored data in Elasticsearch for building interactive dashboards and advanced analytics.

## Getting Started

### Prerequisites

- Docker & Docker Compose installed
- Python 3.x (with `elasticsearch` package)
  
### Quick Setup with Docker

1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd <repo_directory>
