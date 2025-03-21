# Build stage: Build the static site using MkDocs
FROM squidfunk/mkdocs-material as setup

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt


# Build stage: Build the static site using MkDocs
FROM setup as builder
RUN mkdocs build

# Serve stage: Serve the static site using Nginx
FROM nginx:alpine

COPY --from=builder /app/site /usr/share/nginx/html
COPY docker/nginx/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 CMD wget -q --spider http://localhost/ || exit 1
