# Specify the base image
FROM node:latest

# Create and set the working directory
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port that the application will listen on
EXPOSE 3000

# Set the command to start the application
CMD ["npm", "start"]