# Homework Submissions

## Answer 1 - Understanding Docker Images
Run this inside the terminal:
```
docker run -it --rm --entrypoint=bash python:3.13
```
Then run this inside the container's interactive shell:
```
pip -V
```
**Answer**: 25.3

Full Terminal workings:
```
@ruthyishere ➜ /workspaces/data-engineering-zoomcamp-hw-submissions (main) $ docker run -it --entrypoint=bash python:3.13
root@8fefff89a671:/# pip --help

Usage:   
  pip <command> [options]

Commands:
  install                     Install packages.
  lock                        Generate a lock file.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  inspect                     Inspect the python environment.
  list                        List installed packages.
  show                        Show information about installed packages.
  check                       Verify installed packages have compatible dependencies.
  config                      Manage local and global configuration.
  search                      Search PyPI for packages.
  cache                       Inspect and manage pip's wheel cache.
  index                       Inspect information available from package indexes.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion.
  debug                       Show information useful for debugging.
  help                        Show help for commands.

General Options:
  -h, --help                  Show help.
  --debug                     Let unhandled exceptions propagate outside the main subroutine, instead of logging them to stderr.
  --isolated                  Run pip in an isolated mode, ignoring environment variables and user configuration.
  --require-virtualenv        Allow pip to only run in a virtual environment; exit with an error otherwise.
  --python <python>           Run pip with the specified Python interpreter.
  -v, --verbose               Give more output. Option is additive, and can be used up to 3 times.
  -V, --version               Show version and exit.
  -q, --quiet                 Give less output. Option is additive, and can be used up to 3 times (corresponding to WARNING, ERROR, and
                              CRITICAL logging levels).
  --log <path>                Path to a verbose appending log.
  --no-input                  Disable prompting for input.
  --keyring-provider <keyring_provider>
                              Enable the credential lookup via the keyring library if user input is allowed. Specify which mechanism to
                              use [auto, disabled, import, subprocess]. (default: auto)
  --proxy <proxy>             Specify a proxy in the form scheme://[user:passwd@]proxy.server:port.
  --retries <retries>         Maximum attempts to establish a new HTTP connection. (default: 5)
  --timeout <sec>             Set the socket timeout (default 15 seconds).
  --exists-action <action>    Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, (a)bort.
  --trusted-host <hostname>   Mark this host or host:port pair as trusted, even though it does not have valid or any HTTPS.
  --cert <path>               Path to PEM-encoded CA certificate bundle. If provided, overrides the default. See 'SSL Certificate
                              Verification' in pip documentation for more information.
  --client-cert <path>        Path to SSL client certificate, a single file containing the private key and the certificate in PEM format.
  --cache-dir <dir>           Store the cache data in <dir>.
  --no-cache-dir              Disable the cache.
  --disable-pip-version-check
                              Don't periodically check PyPI to determine whether a new version of pip is available for download. Implied
                              with --no-index.
  --no-color                  Suppress colored output.
  --use-feature <feature>     Enable new functionality, that may be backward incompatible.
  --use-deprecated <feature>  Enable deprecated functionality, that will be removed in the future.
  --resume-retries <resume_retries>
                              Maximum attempts to resume or restart an incomplete download. (default: 5)
root@8fefff89a671:/# pip -V
pip 25.3 from /usr/local/lib/python3.13/site-packages/pip (python 3.13)
```

## Answer 2 - Understanding Docker networking and docker-compose

```
services:
  **db: <-- Service Name** 
    **container_name: postgres**
    image: postgres:17-alpine
    environment:
      POSTGRES_USER: 'postgres'
      POSTGRES_PASSWORD: 'postgres'
      POSTGRES_DB: 'ny_taxi'
    ports:
      - **'5433:5432' (host port:container port)**
    volumes:
      - vol-pgdata:/var/lib/postgresql/data

...
```

pgadmin should connect to port 5432 as it's Postgres container port number
pgadmin can connect to the following hostnames: postgres (name of PostgreSQL container); db (name of service that configures PostgreSQL container)

**Answers**: postgres:5432 or db:5432

Not localhost because pgadmin container will just refer to itself.
Not 5433 because that refers to port on host machine, not the container port in this network.

## Answer 3 - Counting short trips

1. Create docker-compose yaml file from prev question

2. Get python ingestion script from lessons and tweak it

2. Download the data in terminal
```
wget -P data/ https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet

wget -P data/ https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv
```

3. Compose docker containers using yaml file
```
docker compose up -d
```

4. Run ingestion script for each data source
```
uv run python ingest_data.py \
  --path="./data/green_tripdata_2025-11.parquet" \
  --pg-user=postgres \
  --pg-pass=postgres \
  --pg-host=localhost \
  --pg-port=5433 \
  --pg-db=ny_taxi \
  --tablename=green_taxi_trips

uv run python ingest_data.py \
  --path="./data/taxi_zone_lookup.csv" \
  --pg-user=postgres \
  --pg-pass=postgres \
  --pg-host=localhost \
  --pg-port=5433 \
  --pg-db=ny_taxi \
  --tablename=taxi_zones
```

5. Open pgAdmin, login, connect to server and open query tool for tables.

6. Run following SQL query
```
SELECT
	COUNT(*)
FROM green_taxi_trips
WHERE extract(month FROM "lpep_pickup_datetime") = 11 AND "trip_distance" <= 1;
```

**Answer**: 8007

## Answer 4 - Longest trip for each day

```
SELECT 
	"lpep_pickup_datetime",
	MAX("trip_distance")
FROM green_taxi_trips
WHERE "trip_distance" < 100
GROUP BY "lpep_pickup_datetime"
ORDER BY MAX("trip_distance") DESC;
```

Select the date of the first row

## Answer 5 - Biggest pickup zone

```
SELECT
	tz."Zone", Count(*) AS count
FROM taxi_zones tz 
LEFT JOIN green_taxi_trips gtt ON tz."LocationID" = gtt."PULocationID"
WHERE extract(year FROM "lpep_pickup_datetime") = 2025 AND 
	extract(month FROM "lpep_pickup_datetime") = 11 AND 
	extract(day FROM "lpep_pickup_datetime") = 18
GROUP BY tz."Zone"
ORDER BY count DESC;
```

Select the Zone of the first row.

## Answer 6 - Drop off Zone with largest tip

Get location ID for East Harlem North from taxi zones table

```
SELECT
	"LocationID"
FROM taxi_zones WHERE "Zone" = 'East Harlem North';
```

LocationID is 74.

Then, run following to get DO zone that had the biggest tip

```
SELECT
	dotz."Zone", gtt."tip_amount" AS tip
FROM green_taxi_trips gtt
JOIN taxi_zones dotz ON gtt."DOLocationID" = dotz."LocationID"
JOIN taxi_zones putz ON gtt."PULocationID" = putz."LocationID"
WHERE putz."Zone" = 'East Harlem North' AND
	extract(year FROM gtt."lpep_pickup_datetime") = 2025 AND 
	extract(month FROM gtt."lpep_pickup_datetime") = 11
ORDER BY tip DESC;
```

Select Zone in first row.

**Answer**: Yorkville West

## Answer 7 - Terraform

**Answer**: ```terraform init, terraform apply -auto-approve, terraform destroy```