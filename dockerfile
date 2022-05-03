FROM mnqobi94/ecocontainer
WORKDIR /usr/src/myapp
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000
RUN python database.py
CMD ["flask", "run"]