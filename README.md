# OSM Stats Generator

Whenever there are some recent map edits, we are curious to know who mapped what and how many of them. While there are already numerous tools to get similar type of statistics, the need of this one is due to the following use-cases

- Counting how many schools or hospitals (or anything) someone mapped within particular timeperiod

# Installation

Start with cloning the repository. Then create a Virtual Environment to install the required dependencies.

```
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

# Data Preparation

Before using the OSM stats generator script, you need the prepare the data first. Please follow the steps for that.

- Download the latest data (internal data with usernames) from Geofabrik for the region. For that, you need to Login with OpenStreetMap account.
- Place the downloaded file inside the 'data' directory as 'internal-latest.osm.pbf'. Create 'data' directory if it doesn't exist.
- Then create necessary period/changes files with the command simiar to the following. Change the dates as required.

```
osmium time-filter  data/internal-latest.osm.pbf 2022-03-27T00:00:00Z -o data/start.osm.pbf
osmium time-filter  data/internal-latest.osm.pbf 2022-04-01T00:00:00Z -o data/end.osm.pbf
osmium derive-changes data/start.osm.pbf data/end.osm.pbf -o data/changes.osc
```

# Usage

You can run the script with following command

```
Usage: python OSMStatsGenerator.py '<osmusername>'
Example: python OSMStatsGenerator.py 'User Name'
```

# Limitations

- Considers only creation and modification changes for now.
