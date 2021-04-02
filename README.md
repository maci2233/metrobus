### Metrobus CDMX data pipeline

Once the project is cloned, open a terminal inside the "metrobus" directory (where the docker-compose.yml file is stored)

To run the project docker is needed, so assuming it is installed properly run:

*docker-compose up -d*

---

**Metrobus Consumer**

metrobus_consumer will retrieve metrobus data from a csv file and store it in the DB (3 rows every 30 seconds)

---

**Metrobus Api**

metrobus_api will run a FastAPI project with multiple endpoints to consume the metrobus data stored in the DB

To read the REST API swagger documentation, visit /docs

---

**Postgres**

You can use a Postgres GUI and connect to the DB using the configuration specified inside docker-compose.yml file

NOTE: This project is not supposed to be deployed in its current state.


