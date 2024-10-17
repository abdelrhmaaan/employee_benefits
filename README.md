# Employee Benefits Management Module

## Overview

The **Employee Benefits Management** module is an Odoo application designed to help HR departments manage various employee benefits efficiently. It enables tracking of benefits such as health insurance, transportation, bonuses, and more, assigned to each employee, with automatic computation of total benefits.

## Features

- Manage different types of benefits: health insurance, transportation, bonus, and others.
- Associate benefits with individual employees.
- Track benefit amounts and descriptions.
- Automatically compute the total benefit amount for each employee.

## Installation

1. Download or clone this repository into your Odoo `addons` directory.
2. Restart your Odoo server.
3. Go to **Apps** in the Odoo backend.
4. Click on **Update Apps List**.
5. Search for **Employee Benefits Management** and install it.

## Usage

1. Navigate to the **Employee Benefits** section under the HR module.
2. Create and manage employee benefits.
3. The system will automatically compute the total benefit amount for each employee.

## Fields

- **Benefit Name**: The name of the benefit.
- **Benefit Type**: The type of benefit (Health Insurance, Transportation, Bonus, Other).
- **Description**: A brief description of the benefit.
- **Employee**: The employee associated with the benefit.
- **Benefit Amount**: The monetary value of the benefit.
- **Date Awarded**: The date the benefit was awarded.
- **Total Amount**: Automatically calculated total benefit amount for each employee.

## Dependencies

This module depends on the `hr` module in Odoo.

## License

This module is licensed under the MIT License.
