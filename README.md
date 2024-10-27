# Python NFT Event Listener

This project is a Django-based application designed to listen and respond to NFT transfer events. It includes real-time event fetching capabilities, background processing, and a built-in server to host the application.

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoint](#api-endpoint)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

Follow these instructions to get the application up and running on your local machine for development and testing purposes.

## Prerequisites

Ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/) (for Docker-based deployment)
- [Docker Compose](https://docs.docker.com/compose/install/) (for Docker-based deployment)
- [Python 3.9+](https://www.python.org/downloads/) and [virtualenv](https://virtualenv.pypa.io/) (for local deployment)

## Installation

1. Clone the repository:

    ```bash
    git clone git@github.com:jushwaaang/python-nft-event-listener.git
    cd python-nft-event-listener
    ```
## Running the Application

### Option 1: Using Docker

1. **Build and Start the Docker Container:**

    ```bash
    docker-compose up --build
    ```

2. **Running Background Processes**:

   The application will already execute the fetch on past transfers and listen to live transfer events after docker build:
   
    - `fetch_live_transfer_events` (runs continuously)
    - `fetch_transfer_events` (fetches historical data once)

3. **Access the Application:**

   Once running, the Django server should be accessible at `http://localhost`.

4. **Stopping the Application:**

   To stop the application and all related processes, use:

    ```bash
    docker-compose down
    ```

### Option 2: Running Locally without Docker

1. **Activate the Virtual Environment:**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

2. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run Migrations:**

    ```bash
    python manage.py migrate
    ```

4. **Start the Django Development Server:**

    ```bash
    python manage.py runserver 0.0.0.0:80
    ```

5. **Run Background Processes:**

   Start the event listeners as follows:

    ```bash
    python manage.py fetch_transfer_events
    python manage.py fetch_live_transfer_events
    ```

6. **Access the Application:**

   The application should now be running at `http://localhost`

## API Endpoint

The application exposes an API endpoint to retrieve NFT transfer events:

- **Endpoint**: `http://localhost/api/v1/transfers`
- **Method**: `GET`
- **Parameters**:
  - `token_id` (string): The ID of the token to fetch events for.
  - `page` (integer, optional): The page number for pagination.
  - `page_size` (integer, optional): The number of results per page.

Example request:

```http
GET http://localhost/api/v1/transfers?token_id=<TOKEN_ID>&page=1&page_size=20
