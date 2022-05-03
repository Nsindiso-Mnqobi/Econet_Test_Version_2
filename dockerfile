FROM mnqobi94/ecocontainer
ADD . /usr/src/myapp
WORKDIR /usr/src/myapp
EXPOSE 5000
ENV FLASK_APP=rest_api.py
CMD ["flask","run","--host=0.0.0.0"]
