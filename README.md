# Tigat QA Automation Portfolio

A professional-grade UI test automation and CI/CD pipeline repository demonstrating end-to-end software quality assurance capabilities.

## 🚀 Project Overview
This repository contains automated user interface tests, infrastructure configuration, and defect tracking documentation designed to validate web application workflows.

## 🛠️ Tech Stack
* **Language:** Python 3.11
* **Test Framework:** Pytest
* **Browser Automation:** Selenium WebDriver
* **CI/CD Pipeline:** GitHub Actions (Automated cloud test execution)

## 🔄 CI/CD Pipeline Integration
* Automated execution triggers on every push to the main branch.
* Configured to spin up an isolated Linux virtual environment (`ubuntu-latest`), install dependencies, and run UI test assertions headlessly.
* Features a verified passing workflow status badge.

## 📂 Repository Structure
* `test_tigat_web.py` — Core Selenium UI automation test scripts.
* `.github/workflows/test.yml` — GitHub Actions continuous integration pipeline configuration.
* `docs/defect_report_sample.md` — Professional defect tracking and lifecycle documentation.
