# node optimised base image
FROM node:18-alpine

# set woring directory inside container 
WORKDIR /app

# copying all the files starting with the package
COPY package*.json ./

# installing dependecies
RUN npm install 

# copying all the src code 
COPY src ./src

# exposing backend port 
EXPOSE 5000

# start script 
CMD ["npm" , "start"]