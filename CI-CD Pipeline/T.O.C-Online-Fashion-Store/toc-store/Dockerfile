# Stage 1: Build the React application
FROM node:20-alpine AS build
WORKDIR /app

# Copy package configurations and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the application files and compile
COPY . .
RUN npm run build

# Stage 2: Serve the production build using Nginx
FROM nginx:alpine
# CHANGE THIS LINE: changed /app/build to /app/dist
COPY --from=build /app/dist /usr/share/nginx/html

# Expose port 80 inside the container
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]