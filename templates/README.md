![BIG LOCAL NEWS](https://raw.githubusercontent.com/biglocalnews/.github/main/profile/github-840x200.png)

It’s too hard for local journalists to access public records about policing, public health, government and other vital topics.

From its base at Stanford University, Big Local News gathers data, builds tools and collaborates with reporters to produce journalism that makes an impact. Its website at [biglocalnews.org](https://biglocalnews.org) offers a free archiving service for journalists to store and share data.

**Table of contents**

* [Projects](https://github.com/biglocalnews#projects)
* [Staff](https://github.com/biglocalnews#staff)
* [Open-source software](https://github.com/biglocalnews#open-source-software)
* [Bylines](https://github.com/biglocalnews#bylines)

## Projects

What we're working on.

| Topic            | Description                                                                                                   | Products                                                                |
|:-----------------|:--------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------|
| Law enforcement  | Gathering local law enforcment records related to use of force, misconduct and racial profiling | [Community Law Enforcement Accountability Network](https://data.berkeley.edu/news/berkeley-data-science-students-journalism-faculty-building-public-database-police-misconduct), [Stanford Open Policing Project](https://openpolicing.stanford.edu/) |
| Local government | Mining public records from local boards, councils and courts                                    | [Agenda Watch](http://agendawatch.org/), [Court Scraper](https://github.com/biglocalnews/court-scraper)                                             |
| COVID-19         | Tracking the toll the COVID-19 pandemic, as well as its impact on our economy and public institutions         | [COVID-19 Case Mapper](https://covid19.biglocalnews.org/county-maps/index.html#/), [Stanford School Enrollment Project](https://docs.google.com/document/d/1WRm4KZPDGL1USPaf0E1AIa7gbyeKncv04Pg_rM1N7po/edit), [Layoff Watch](https://github.com/biglocalnews/warn-github-flow)  |
| Demographics     | Tools and trainings that help journalists find stories using Census data                             | [The 2020 Census Data Co-op](https://sites.google.com/stanford.edu/census-data-co-op)                                              |                                               |

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
* Ben Welsh ([@palewire](https://github.com/palewire))
* Simon Willison ([@simonw](https://github.com/simonw))

## Open-source software

### 🔢 Data scraping

Repositories that gather public records from the web.

| name             | description                                                                                                                         |
|:-----------------|:------------------------------------------------------------------------------------------------------------------------------------|
| [civic-scraper](https://github.com/biglocalnews/civic-scraper)    | Download agendas, minutes and other documents produced by local governments                                                         |
| [court-scraper](https://github.com/biglocalnews/court-scraper)    | Python library and command-line tool that collects case information from U.S. county courts.        |
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
| [bln-python-client](https://github.com/biglocalnews/bln-python-client) | Python client for the biglocalnews.org API                             |
| [upload-files](https://github.com/biglocalnews/upload-files)           | Upload comma-delimited files to biglocalnews.org in your GitHub Action |

## Bylines

Stories, guides and other articles by the Big Local News team and its partners. Logged in [biglocalnews/bylines](https://github.com/biglocalnews/bylines)

| date | domain | headline |
|:--|:--|:--|{% for obj in byline_list %}
|  {{ obj.pub_date }} | {{ obj.domain }} | [{{ obj.headline }}]({{ obj.url }}) |{% endfor %}

