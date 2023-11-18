# BookBridge-Exchange-Hub

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Setup Instructions

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd BookBridge-Exchange-Hub
    ```

3. **Create a `.env` file in the project root and set the following environment variables:**

    ```env
    POSTGRES_USER=postgres_username
    POSTGRES_PASSWORD=postgres_password
    POSTGRES_DB=postgres
    PGADMIN_DEFAULT_EMAIL=pgadmin_email
    PGADMIN_DEFAULT_PASSWORD=pgadmin_password
    ```

4. **Run the following command to start the Docker containers:**

    ```bash
    docker-compose up -d
    ```

    This will create and start containers for PostgreSQL and pgAdmin.

5. **Access pgAdmin in your browser by navigating to [http://localhost:5050](http://localhost:5050). Log in using the credentials specified in the `.env` file.**

6. **In pgAdmin, add a new server with the following details:**

    - Host name/address: `db`
    - Port: `5432`
    - Maintenance database: `postgres`
    - Username: `admin`
    - Password: `admin`

7. **Save the server configuration, and you should now have a connection to the PostgreSQL database.**

## Accessing PostgreSQL Database

You can connect to the PostgreSQL database using your preferred database client with the following details:

- Host: `localhost`
- Port: `5432`
- Database: `postgres`
- Username: `postgres_username`
- Password: `postgres_password`

## Cleanup

To stop and remove the Docker containers, run:

```bash
docker-compose down
