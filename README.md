# Task 15: End-to-End Deep Learning Production Deployment

## Project Overview

This project demonstrates the complete end-to-end deployment of a Deep Learning image classification application using the CIFAR-10 dataset.

The application integrates a trained Convolutional Neural Network (CNN), a Flask REST API, a Streamlit frontend, Docker containerization, Kubernetes orchestration, and cloud deployment using Render.

The system allows users to upload an image and receive a predicted CIFAR-10 class along with the model confidence.

---

## Objectives

* Develop and deploy a Deep Learning image classification model.
* Build a REST API using Flask.
* Develop an interactive frontend using Streamlit.
* Containerize the application using Docker.
* Deploy the application using Kubernetes.
* Configure communication between frontend and backend services.
* Deploy the application to the cloud.
* Verify end-to-end application functionality.

---

## Technologies Used

* Python
* TensorFlow / Keras
* CIFAR-10 Dataset
* Flask
* Streamlit
* Docker
* Docker Compose
* Kubernetes
* Minikube
* kubectl
* Render
* GitHub

---

## Project Architecture

```text
                    User
                     |
                     v
            Streamlit Frontend
                  Port 8501
                     |
                     v
               Flask REST API
                  Port 5000
                     |
                     v
              CIFAR-10 CNN Model
                     |
                     v
               Prediction Result
          Class + Confidence Score
```

---

## CIFAR-10 Classes

The trained model classifies images into the following 10 CIFAR-10 categories:

1. Airplane
2. Automobile
3. Bird
4. Cat
5. Deer
6. Dog
7. Frog
8. Horse
9. Ship
10. Truck

---

## Project Structure

```text
Task15_End_to_End_Deep_Learning/
│
├── model/
│   └── cifar10_cnn.keras
│
├── pages/
│   └── .gitkeep
│
├── kubernetes/
│   ├── flask-deployment.yaml
│   ├── flask-service.yaml
│   ├── streamlit-deployment.yaml
│   └── streamlit-service.yaml
│
├── app.py
├── flask_api.py
├── requirements.txt
├── Dockerfile.flask
├── Dockerfile.streamlit
├── docker-compose.yml
├── frog.png
└── .gitignore
```

---

## Flask API

The Flask application provides a REST API for image prediction.

### Health Check

```text
GET /
```

Example response:

```json
{
  "message": "Task 15 CIFAR-10 Deep Learning API is running",
  "endpoint": "/predict",
  "method": "POST"
}
```

### Prediction Endpoint

```text
POST /predict
```

The API accepts an image using the `image` multipart form field.

Example:

```bash
curl.exe -X POST -F "image=@frog.png" http://localhost:5000/predict
```

Example response:

```json
{
  "predicted_class": "Frog",
  "confidence": 99.01
}
```

---

## Streamlit Frontend

The Streamlit application provides a user-friendly interface for image classification.

The user can:

1. Upload an image.
2. View the uploaded image.
3. Click the prediction button.
4. Send the image to the Flask API.
5. View the predicted CIFAR-10 class.
6. View the prediction confidence.

The Flask API URL is configured using the `FLASK_API_URL` environment variable.

---

## Docker Containerization

Two Docker images are used:

### Flask API

```text
Dockerfile.flask
```

The Flask container runs the REST API on port `5000`.

### Streamlit Frontend

```text
Dockerfile.streamlit
```

The Streamlit container runs the frontend on port `8501`.

---

## Docker Compose

Docker Compose is used to run the Flask API and Streamlit frontend together.

Start the application using:

```bash
docker compose up --build
```

The services are:

```text
Flask API      → http://localhost:5000
Streamlit UI   → http://localhost:8501
```

Stop the application using:

```bash
docker compose down
```

---

## Kubernetes Deployment

The application is deployed to Kubernetes using Minikube.

### Flask Deployment

```text
kubernetes/flask-deployment.yaml
```

The Flask deployment uses two replicas.

### Flask Service

```text
kubernetes/flask-service.yaml
```

The Flask API is exposed internally using a ClusterIP service.

### Streamlit Deployment

```text
kubernetes/streamlit-deployment.yaml
```

The Streamlit frontend uses two replicas.

### Streamlit Service

```text
kubernetes/streamlit-service.yaml
```

The Streamlit frontend is exposed using a NodePort service.

---

## Kubernetes Commands

Start Minikube:

```bash
minikube start --driver=docker
```

Apply Flask deployment:

```bash
kubectl apply -f kubernetes/flask-deployment.yaml
```

Apply Flask service:

```bash
kubectl apply -f kubernetes/flask-service.yaml
```

Apply Streamlit deployment:

```bash
kubectl apply -f kubernetes/streamlit-deployment.yaml
```

Apply Streamlit service:

```bash
kubectl apply -f kubernetes/streamlit-service.yaml
```

Check deployments:

```bash
kubectl get deployments
```

Check pods:

```bash
kubectl get pods
```

Check services:

```bash
kubectl get services
```

Access the Streamlit application:

```bash
minikube service streamlit-service --url
```

---

## Kubernetes Architecture

```text
                 Kubernetes Cluster
                         |
          +--------------+--------------+
          |                             |
          v                             v
   Streamlit Deployment          Flask Deployment
      2 Replicas                    2 Replicas
          |                             |
          v                             v
 Streamlit Service              Flask Service
    NodePort                      ClusterIP
          |                             |
          +-------------+---------------+
                        |
                        v
                 CIFAR-10 Model
```

---

## Cloud Deployment

The application is also deployed to the cloud using Render.

### Flask API

Public Flask API:

```text
https://task15-flask-api.onrender.com/
```

### Streamlit Application

The Streamlit frontend is deployed as a separate Render web service.

The Streamlit application communicates with the Flask API using the environment variable:

```text
FLASK_API_URL
```

The production value is:

```text
https://task15-flask-api.onrender.com
```

---

## End-to-End Workflow

```text
User uploads image
        |
        v
Streamlit Frontend
        |
        v
Flask REST API
        |
        v
Image preprocessing
        |
        v
CIFAR-10 CNN model
        |
        v
Prediction
        |
        v
Predicted class + confidence
        |
        v
Streamlit displays result
```

---

## Testing and Verification

The application was tested at multiple deployment levels:

### Local Flask API

* Health endpoint tested.
* Image prediction endpoint tested.
* CIFAR-10 prediction successfully generated.

### Streamlit Application

* Image upload tested.
* Prediction button tested.
* Prediction result and confidence displayed.

### Docker

* Flask and Streamlit Docker images built successfully.
* Containers executed successfully.
* Docker Compose integration verified.

### Kubernetes

* Flask and Streamlit deployments created.
* Multiple replicas verified.
* Kubernetes services created.
* Streamlit application accessed through Minikube.
* Frontend-to-backend communication verified.

### Cloud

* Flask API deployed publicly.
* Streamlit frontend deployed publicly.
* Cloud frontend successfully communicated with the Flask API.
* Image prediction successfully tested through the public application.

---

## Model Prediction Example

For the test image `frog.png`, the deployed system successfully predicted:

```text
Predicted Class: Frog
Confidence: Approximately 99%
```

The exact confidence value may vary depending on the deployment environment and model execution.

---

## Deployment Components

| Component                | Technology       | Purpose                      |
| ------------------------ | ---------------- | ---------------------------- |
| Deep Learning Model      | TensorFlow/Keras | Image classification         |
| Backend                  | Flask            | REST API                     |
| Frontend                 | Streamlit        | User interface               |
| Containerization         | Docker           | Application packaging        |
| Local Orchestration      | Docker Compose   | Multi-container execution    |
| Production Orchestration | Kubernetes       | Deployment and scaling       |
| Kubernetes Platform      | Minikube         | Local Kubernetes environment |
| Cloud Platform           | Render           | Public deployment            |
| Source Control           | GitHub           | Source code management       |

---

## Key Features

* CIFAR-10 image classification
* RESTful prediction API
* Interactive Streamlit interface
* Docker containerization
* Docker Compose integration
* Kubernetes deployment
* Multiple Kubernetes replicas
* Internal service communication
* Public cloud deployment
* End-to-end prediction workflow

---

## Practical Applicability

The architecture demonstrated in this project can be extended to other Deep Learning applications such as:

* Object detection
* Image recognition
* Medical image classification
* Industrial defect detection
* Automated visual inspection
* Smart surveillance systems

The separation between frontend, API, and model service also makes the application suitable for further MLOps development.

---

## Conclusion

This project demonstrates an end-to-end Deep Learning production deployment workflow.

The trained CIFAR-10 model was integrated with a Flask REST API and a Streamlit frontend. The application was containerized using Docker, orchestrated using Kubernetes and Minikube, and deployed publicly using Render.

The complete workflow was tested from image upload to final prediction, demonstrating the integration of Deep Learning, API development, containerization, orchestration, and cloud deployment.
