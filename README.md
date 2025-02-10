# grafana_rabbitmq  

Certainly! Here's a comprehensive README file with step-by-step instructions to set up the Grafana-RabbitMQ monitoring project:

---

# Grafana-RabbitMQ Monitoring Setup

This project provides a Docker Compose configuration to monitor RabbitMQ instances using Prometheus and Grafana. Follow the steps below to set up and run the monitoring stack.

## Prerequisites

- **Docker**: Ensure Docker is installed on your system. You can download it from [Docker's official website](https://www.docker.com/get-started).

- **Docker Compose**: Verify that Docker Compose is installed. It's typically included with Docker Desktop installations. To check, run:

  ```bash
  docker-compose --version
  ```

  If it's not installed, follow the instructions on the [Docker Compose installation page](https://docs.docker.com/compose/install/).

## Setup Instructions

1. **Clone the Repository**

   Begin by cloning this repository to your local machine:

   ```bash
   git clone https://github.com/SaiKrishnaVoruganti86/grafana_rabbitmq.git
   cd grafana_rabbitmq
   ```

2. **Enable Prometheus Plugin in RabbitMQ**

   The RabbitMQ instances need to have the `rabbitmq_prometheus` plugin enabled to expose metrics. If you're using RabbitMQ version 3.8.0 or later, you can enable the plugin by running:

   ```bash
   rabbitmq-plugins enable rabbitmq_prometheus
   ```

   This command activates the Prometheus plugin, allowing RabbitMQ to expose metrics at the `/metrics` endpoint. For more details, refer to the [RabbitMQ Prometheus Plugin documentation](https://github.com/rabbitmq/rabbitmq-server/blob/master/deps/rabbitmq_prometheus/README.md).

3. **Configure Prometheus**

   The `prometheus.yml` file in this repository is pre-configured to scrape metrics from RabbitMQ instances. Ensure that the `targets` under the `scrape_configs` section point to the correct RabbitMQ endpoints. By default, it looks like this:

   ```yaml
   scrape_configs:
     - job_name: 'rabbitmq'
       static_configs:
         - targets: ['rabbitmq:15692']
   ```

   If your RabbitMQ instances are running on different hosts or ports, update the `targets` list accordingly.

4. **Start the Docker Containers**

   Use Docker Compose to build and start the containers defined in the `docker-compose.yml` file:

   ```bash
   docker-compose up -d
   ```

   This command will download the necessary Docker images (if not already available) and start the Prometheus and Grafana containers in detached mode.

5. **Access Grafana**

   Once the containers are up and running, access the Grafana dashboard by navigating to `http://localhost:3000` in your web browser.

   - **Default Credentials**:
     - **Username**: `admin`
     - **Password**: `admin`

     Upon first login, you'll be prompted to change the default password for security reasons.

6. **Import RabbitMQ Dashboard into Grafana**

   To visualize RabbitMQ metrics, import a pre-configured dashboard into Grafana:

   - **Download the Dashboard JSON**:

     You can use the RabbitMQ dashboard JSON provided in this repository or download one from the Grafana community dashboards. For instance, the [RabbitMQ Overview Dashboard](https://grafana.com/grafana/dashboards/10991) is compatible with the metrics exposed by the `rabbitmq_prometheus` plugin.

   - **Import the Dashboard**:

     In Grafana:

     - Click on the **"+"** icon on the left sidebar.
     - Select **"Import"**.
     - Upload the downloaded JSON file or enter the dashboard ID (`10991` for the RabbitMQ Overview Dashboard) and click **"Load"**.
     - Select the Prometheus data source configured earlier and click **"Import"**.

     The dashboard will now be available, displaying real-time metrics from your RabbitMQ instances.

7. **Monitor Your RabbitMQ Instances**

   With the dashboard imported, you can now monitor various metrics of your RabbitMQ instances, such as message rates, queue lengths, and resource usage, all in real-time.

## Additional Notes

- **Customizing the Setup**:

  - **Adding More RabbitMQ Instances**:

    If you have multiple RabbitMQ instances to monitor, update the `prometheus.yml` file's `static_configs` to include all instances:

    ```yaml
    scrape_configs:
      - job_name: 'rabbitmq'
        static_configs:
          - targets: ['rabbitmq1:15692', 'rabbitmq2:15692']
    ```

    Ensure that each RabbitMQ instance has the Prometheus plugin enabled and is accessible from the Prometheus container.

  - **Security Considerations**:

    For production deployments, consider securing your Prometheus and Grafana instances by enabling authentication and HTTPS. Additionally, ensure that your RabbitMQ metrics endpoints are not publicly accessible to prevent unauthorized access.

- **Stopping the Containers**:

  To stop the monitoring stack, run:

  ```bash
  docker-compose down
  ```

  This command will stop and remove the containers defined in the `docker-compose.yml` file.

- **Updating the Stack**:

  Periodically, check for updates to the Docker images used in this setup. To update, pull the latest images and recreate the containers:

  ```bash
  docker-compose pull
  docker-compose up -d --force-recreate
  ```

By following these steps, you will have a robust monitoring setup for your RabbitMQ instances using Prometheus and Grafana.

--- 
