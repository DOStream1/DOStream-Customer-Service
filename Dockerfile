FROM node:18.20.4

WORKDIR /app/customer

COPY package*.json .

RUN npm install

COPY . .

EXPOSE 8001

CMD ["npm", "start"]
