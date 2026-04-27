FROM node:24-alpine AS build

WORKDIR /usr/local/app

COPY package.json package-lock.json ./

RUN npm ci

COPY . .

RUN npm run build

FROM nginx:trixie AS prod

COPY nginx.conf /etc/nginx/nginx.conf

COPY --chown=nginx:nginx --from=build /usr/local/app/dist/ng-migrate/browser /usr/share/nginx/html

USER nginx

EXPOSE 80

CMD ["nginx", "-c", "/etc/nginx/nginx.conf", "-g", "daemon off;"]