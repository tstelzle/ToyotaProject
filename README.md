# Toyota Project Vote

This little webscraper automatically votes for "Jessica Steiger" at the Toyota Project.

https://www.toyota-crowd.de/projekt-des-jahres/abstimmung

## Running

Running it with docker can be easily done by using the Makefile.

```bash
make build-image
make run
```

You can furthermore scpecify how often the script should vote. 
By default this is two times.
This can be done by setting the parameter "REPEATS" in the make command

```bash
make run REPEATS=5
```

