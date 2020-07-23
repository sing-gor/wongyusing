FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf

# COPY ./nginx/default.conf /etc/nginx/conf.d/
COPY ./back_end/wongyusing/static_file/* /static_file/
COPY ./nginx/default.conf /etc/nginx/conf.d/