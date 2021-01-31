# London Walking Tours API

A very simple Flask-RESTful API for [London walks](https://www.walks.com/). 
Hosted on Heroku [here](https://walking-tours-ldn.herokuapp.com/). 

## API Documentation

### Base URL

```
https://walking-tours-ldn.herokuapp.com/
```

### Endpoints

### Guides

Use this endpoint to return a list of guides and guide descriptions on the site. 

```
/guides
```

<b>Parameters</b>

No parameters for this request required.

<b> Sample Request </b>

```
GET https://walking-tours-ldn.herokuapp.com/guides
```

### Tour info

Use this endpoint to return a list of all tours between two different dates. 

```
/tours?start=YYYY-MM-DD&end=YYYY-MM-DD
```
the start date and end date are required parameters. 

<b> Sample Request </b>

```
GET https://walking-tours-ldn.herokuapp.com/tours?start=2021-01-01&end=2021-01-03
```
