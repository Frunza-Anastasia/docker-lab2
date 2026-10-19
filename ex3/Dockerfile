FROM nginx:alpine
LABEL maintainer="Frunza Anastasia" version="1.0" description="Pagina proprie Lab 2"
COPY index.html /usr/share/nginx/html/index.html
EXPOSE 80
HEALTHCHECK --interval=30s --timeout=3s CMD wget -q -O /dev/null http://localhost/ || exit 1