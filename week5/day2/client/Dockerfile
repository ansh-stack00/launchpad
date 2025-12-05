# optimised base image for node 
FROM node:18-alpine

# setting work directory inside container 
WORKDIR /app

# copying all the file starting with package 
COPY package*.json ./

# installind dependencies
RUN npm install

# copying all the source code  and public folde 
COPY src ./src  
COPY public ./public

# expose frontend port 
EXPOSE 3000

# run script 
CMD ["npm" , "start"]