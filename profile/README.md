Big Local News is a program at Stanford University creating tools and data that empower journalists to better cover their community. 

Our team authors open-source software that gathers and refines hard-to-obtain public records about policing, politics, public health, employment and other topics. We work with reporters to analyze the records, find stories and produce journalism with impact.

Our website at [biglocalnews.org](https://biglocalnews.org/) allows journalists to pool data and work together.

## Open-source software

### Data scraping

Repositories that gather public records from the web.

| name             | description                                                                                                                         |
|:-----------------|:------------------------------------------------------------------------------------------------------------------------------------|
| [civic-scraper](https://github.com/biglocalnews/civic-scraper)    | Download agendas, minutes and other documents produced by local governments                                                         |
| [court-scraper](https://github.com/biglocalnews/court-scraper)    | Python library and command-line tool that help search and download case information from county courts in the United States.        |
| [warn-scraper](https://github.com/biglocalnews/warn-scraper)     | Command-line interface for downloading WARN Act notices of qualified plant closings and mass layoffs from state government websites |
| [warn-transformer](https://github.com/biglocalnews/warn-transformer) | Consolidate, enrich and republish the data gathered by warn-scraper                                                                 |
| [warn-github-flow](https://github.com/biglocalnews/warn-github-flow) | GitHub Action workflow for automating a WARN Act notice ETL pipeline                                                                |

### biglocalnews.org

| name                                                                   | description                                                            |
|------------------------------------------------------------------------|------------------------------------------------------------------------|
| [bln-python-client](https://github.com/biglocalnews/bln-python-client) | Python client for the biglocalnews.org API                             |
| [upload-files](https://github.com/biglocalnews/upload-files)           | Upload comma-delimited files to biglocalnews.org in your GitHub Action |
