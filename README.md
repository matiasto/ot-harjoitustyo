# WeatherApp

---

<details>
    <summary>Table of Contents</summary>
    <ol>
        <li>
            <a href="#introduction">Introduction</a>
        </li>
        <li>
            <a href="#getting-started">Getting Started</a>
        </li>
        <li>
            <a href="#testing">Testing</a>
        </li>
        <li>
            <a href="#documentation">Documentation</a>
        </li>
    </ol>
</details>

### Introduction

WeatherApp is an [OpenWeather](https://openweathermap.org/api) API-powered desktop application that allows users to inspect the current weather, forecast, and historical weather data.

### Getting Started

1. Get a free API Key at [OpenWeather](https://home.openweathermap.org/users/sign_in)
2. Download the
    [latest release](https://github.com/matiasto/ot-harjoitustyo/releases/tag/viikko6)
3. Navigate to the project folder and run 
    ```bash
    poetry install
    ````
> Please note that your Download folder may not have the permission to execute.

4. Start the application by executing
    ```bash
    poetry run invoke start
    ````
5. During the first execution, the app will ask for API key accuired from step 1.

For detailed instructions visit [instructions](./documentation/instructions.md)

---
### Testing


> Some of the tests require the API key to work. Go through the [Getting Started](#getting-started) before running tests

- Run tests
    ```bash
    poetry run invoke test
    ````
- Generate coverage report
    ```bash
    poetry run invoke coverage-report
    ````
- Perform pylint quality inspection
    ```bash
    poetry run invoke lint
    ````
- Execute autopep8 format
    ```bash
    poetry run invoke format
    ````

### Documentation

- [Architecture](./documentation/architecture.md)
- [Changelog](./documentation/changelog.md)
- [Instructions](./documentation/instructions.md)
- [Record of Working Hours](./documentation/record_of_working_hours.md)
- [Requirements Specification](./documentation/requirements_specification.md)
- [Testing](./documentation/testing.md)

