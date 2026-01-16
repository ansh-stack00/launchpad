FROM node:18-alpine

# set working directory inside constainer  
WORKDIR /src

# copying all the all the files starting with package 
COPY package*.json ./

# installing dependencies 
RUN npm install

# copying src code 
COPY src ./src 

EXPOSE 8080 
# Run  script 
CMD ["npm" , "run","start"]