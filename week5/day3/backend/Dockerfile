FROM node:18-alpine

# Creating app directory inside container 
WORKDIR /app

# Install dependencies
COPY package*.json  ./
RUN npm install

# Copy application files
COPY . .

# Expose backend port
EXPOSE 3000

# Run the app
CMD ["npm", "start"]
