DevSecOps Assessment – Flask + EFK Stack
1. Cluster Setup

Kubernetes cluster created using kubeadm (1 master, worker nodes).

Container runtime: containerd.

CNI: Calico.

Metrics-server installed for autoscaling.

RBAC enabled with non-admin service account for deployments.

Helm used for package deployments.

2. CI/CD Pipeline

Implemented with GitHub Actions (.github/workflows/ci-cd.yml).

Steps include:

Security Scanning (SAST + Dependency scanning)

Run unit tests using pytest.

Build Docker image with linting.

Image Security Scan using Trivy.

Push image to Docker Hub.

Deploy to Kubernetes using Helm chart.

Pipeline: GitHub Actions link

3. Security Measures

SAST & Dependency scanning enabled in pipeline.

Trivy used for container image vulnerability scanning.

RBAC enforced (non-admin service account).

EFK stack deployed in namespace apps for centralized logging.

Fluent Bit configured to parse Flask logs into a dedicated Elasticsearch index (flask-logs).

4. Kibana Dashboard

Exposed via NodePort.

Access Dashboard: http://16.52.82.128:31523/

Dashboard includes:

Flask application access logs.

HTTP method/status code distribution.

Request paths & response trends.