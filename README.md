# Data Generation and Export Tool

## Table of Contents
- [Project Description](#project-description)
- [Key Features](#key-features)
- [Benefits](#benefits)
- [Target Audience](#target-audience)
- [Installation](#installation)
  - [Setup](#setup)
  - [Usage](#usage)
- [Database Setup](#database)

## Project Description
The **_"Data Generation and Export Tool"_** is a versatile command-line application built with Django and various Python libraries and modules. Its primary objective is to simplify the process of creating a database model, populating it with synthetic data in bulk, and then exporting this data into CSV and Excel files for streamlined data analysis.

### Key Features
- **Database Model Creation:** Utilizes Django to define a database model, specifying the data structure to be generated and stored.

- **Bulk Data Population:** Provides a straightforward method for efficiently populating the database with large amounts of synthetic data.

- **Data Extraction:** Enables users to effortlessly extract the generated data and save it in CSV and Excel formats, ready for immediate analysis.

This project simplifies data generation and export, making it a convenient tool for data professionals and analysts.

### Benefits
- **Streamlined Data Management:** Simplifies the process of generating and exporting data, enhancing the workflow for data professionals and analysts.

- **Efficient Data Analysis:** Provides immediate access to data in CSV and Excel formats, facilitating swift and efficient data analysis without extensive data preparation.

- **Data Privacy:** Eliminates the risk of exposing sensitive or confidential data by exclusively using synthetic data for testing and analysis.

- **Data Consistency:** Ensures data consistency and integrity by generating synthetic data based on predefined data models, reducing the risk of analysis errors.

- **Scalability:** Effortlessly scales to handle large data volumes, suitable for both small-scale testing and large-scale analysis projects.

- **Customization:** Allows users to customize data templates and extraction tools to match specific project requirements.

- **Time Efficiency:** Reduces the time and effort required to create and manage synthetic datasets.

- **Data Security:** Provides data anonymization features to protect sensitive information.

### Target Audience
- Data Analysts
- Data Professionals
- Researchers
- Quality Assurance Teams
- Business Analysts
- Django Developers
- Anyone in need of efficiently generating and analyzing synthetic data.

## Installation
### Setup
1. Create a virtual environment:
    ```shell
    python3 -m venv virtualenv
    source env/bin/activate
    ```

2. Clone this repository:
    ```shell
    git clone https://github.com/Suboms/data_analysis.git
    ```

### Usage
Open two command prompt or terminal windows.

In the first terminal, navigate to the project directory, Install the required packages and start the Django development server:
```shell
cd data_analysis
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

```
In the second terminal window, run the following command below and follow the instruction
```
python3 -m tools
```

## Database
Configure your PostgresSQL database by following the platform-specific instructions in the official [PostgresSQL documentation](https://www.postgresql.org/docs/).

Update the DATABASES setting in settings.py to point to your PostgresSQL database:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your-database-name',
        'USER': 'your-database-user',
        'PASSWORD': 'your-database-password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```



The **_"Data Generation and Export Tool"_** project, built on the Django framework, offers a comprehensive solution for data professionals seeking to streamline the data generation process, store synthetic data, and effortlessly extract data for analysis. This Django-powered system bridges the gap between data generation and analysis, enhancing the efficiency and effectiveness of data-driven decision-making processes.
