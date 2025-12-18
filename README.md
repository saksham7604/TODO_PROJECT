# 3-Tier App (No Istio)

## Structure
- frontend/: Nginx + static HTML
- backend/: Flask API connecting to MongoDB
- k8s/: Kubernetes manifests (single namespace `myapp`)

## Build & Publish images (example)
### Frontend
cd frontend
docker build -t your-dockerhub/frontend:v1 .
docker push your-dockerhub/frontend:v1

### Backend
cd backend
docker build -t your-dockerhub/backend:v1 .
docker push your-dockerhub/backend:v1

## Deploy to Kubernetes
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/ -n myapp

## Notes
- Replace `your-dockerhub/*` image names with your registry.
- Frontend Service is `LoadBalancer` type to expose externally; change to `NodePort` if needed.
