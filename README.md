# WeatherApp
---

<!-- TABLE OF CONTENTS -->
<details>
    <summary>Table of Contents</summary>
    <ol>
        <li>
            <a href="#introduction">Introduction</a>
        </li>
        <li>
            <a href="#installation-instructions">Installation Instructions</a>
        </li>
        <li>
            <a href="#usage">Usage</a>
        </li>
        <li>
            <a href="#documentation">Documentation</a>
        </li>
    </ol>
</details>

### Introduction

WeatherApp is an [OpenWeather](https://openweathermap.org/api) API-powered desktop application that allows users to inspect the current weather, forecast, and historical weather data.

### Getting started

1. Get a free API Key at [OpenWeather](https://home.openweathermap.org/users/sign_in)
2. Clone the repo
    ```bash
    git clone https://github.com/matiasto/ot-harjoitustyo.git
    ```
3. In the root folder, export the accuired API key. Note that the variable name needs to be exactly the same!
    ```bash
    export OPENWEATHER_API_KEY=<your API key without quotes>
    ```
4. Check
    ```bash
    echo $OPENWEATHER_API_KEY
    ```
    If succesful, it should log your API key to the console.

5. Install dependecies
    ```bash
    poetry install
    ````
6. Run
    ```bash
    poetry run invoke start
    ````
---
### Testing

- Run tests
    ```bash
    poetry run invoke test
    ````
- Generate coverage report
    ```bash
    poetry run invoke coverage-report
    ````

### Documentation

- [Requirements Specification](./documentation/requirements_specification.md)
- [Record of Working Hours](./documentation/record_of_working_hours.md)

