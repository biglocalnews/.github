![BIG LOCAL NEWS](https://raw.githubusercontent.com/biglocalnews/.github/main/profile/github-840x200.png)

It’s too hard for local journalists to access public records about policing, public health, government and other vital topics.

From its base at Stanford University, Big Local News gathers data, builds tools and collaborates with reporters to produce journalism that makes an impact. Its website at [biglocalnews.org](https://biglocalnews.org) offers a free archiving service for journalists to store and share data.

## Staff

Members of our team on GitHub

* Justin Mayo ([@justinmayo](https://github.com/justinmayo))
* Dilcia Mercedes ([@Dilcia19](https://github.com/dilcia19/))
* Joe Nudell ([@jnu](https://github.com/jnu))
* Cheryl Phillips ([@cephillips](https://github.com/cephillips))
* Lisa Pickoff-White ([@pickoffwhite](https://github.com/pickoffwhite))
* Regina Roberts ([@regirob831](https://github.com/regirob831))
* Eric Sagara ([@esagara](https://github.com/esagara))
* Serdar Tumgoren ([@zstumgoren](https://github.com/zstumgoren))
* Simon Willison ([@simonw](https://github.com/simonw))

## Open-source software

### 🔢 Data scraping

Repositories that gather public records from the web.

| name             | description                                                                                                                         |
|:-----------------|:------------------------------------------------------------------------------------------------------------------------------------|
| [civic-scraper](https://github.com/biglocalnews/civic-scraper)    | Download agendas, minutes and other documents produced by local governments                                                         |
| [court-scraper](https://github.com/biglocalnews/court-scraper)    | Python library and command-line tool that collects case information from U.S. county courts.        |
| [prefect-flow-template](https://github.com/biglocalnews/prefect-flow-template/) | A template repository with all the fundamentals needed to develop and deploy a Python data-processing routine for Prefect pipelines. |
| [local-election-results-etl](https://github.com/biglocalnews/local-election-results-etl) | Extract, transform and load election results posted online by local U.S. election officials |
| [usc-crime-reports-scraper](https://github.com/biglocalnews/usc-crime-reports-scraper) | A GitHub Action workflow for automating the collection of crime and fire logs posted by the University of Southern California's Department of Public Safety. |
| [warn-scraper](https://github.com/biglocalnews/warn-scraper)     | Command-line interface for downloading WARN Act notices of qualified plant closings and mass layoffs |
| [warn-transformer](https://github.com/biglocalnews/warn-transformer) | Consolidate, enrich and republish the data gathered by warn-scraper                                                                 |
| [warn-github-flow](https://github.com/biglocalnews/warn-github-flow) | GitHub Action workflow for automating a WARN Act notice ETL pipeline                                                                |

### 🧮 Data analysis

Code that uses data to conduct an investigation

| name                                                                                 | description                                                                  |
|:-------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------|
| [california-wildfires](https://github.com/biglocalnews/california-wildfires)         | Investigation into the costs of wildfires across the U.S.                    |
| [covid-19-tweets](https://github.com/biglocalnews/covid19-tweets)                    | Tracks information dissemination about COVID-19 by local government agencies |
| [warn-california-analysis](https://github.com/biglocalnews/warn-california-analysis) | An exploration and analysis of the WARN Notices data for California          |

### 🌎 biglocalnews.org

Tools that connect to our platform at [biglocalnews.org](https://biglocalnews.org)

| name                                                                   | description                                                            |
|------------------------------------------------------------------------|------------------------------------------------------------------------|
| [biglocalnews/datasette.biglocalnews.org](https://github.com/biglocalnews/datasette.biglocalnews.org) | A Datasette instance that allows users to explore public and private files hosted by biglocalnews.org  |
| [bln-python-client](https://github.com/biglocalnews/bln-python-client) | Python client for the biglocalnews.org API                             |
| [upload-files](https://github.com/biglocalnews/upload-files)           | Upload comma-delimited files to biglocalnews.org in your GitHub Action |
