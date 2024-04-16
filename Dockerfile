FROM node:18.20.1

WORKDIR /app/customer

COPY package*.json .

RUN npm install

COPY . .

EXPOSE 8001

CMD ["npm", "start"]
