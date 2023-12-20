FROM node:18.19

WORKDIR /app/customer

COPY package*.json .

RUN npm install

COPY . .

EXPOSE 8001

CMD ["npm", "start"]
