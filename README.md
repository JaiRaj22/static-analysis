# Static Code Analysis App

## Introduction
This repository contains a Static Code Analysis App that analyzes code metrics, identifies reserved keywords, extracts identifiers, and visualizes the Abstract Syntax Tree (AST) of the input code.

## Packages and Tools Used
- Streamlit: for creating the web application interface
- Radon: for code analysis metrics
- Altair and Plotly Express: for data visualization
- Pandas: for data manipulation
- Parse: for generating the AST

## Algorithm Used
The app uses Radon's metrics to calculate code complexity and maintainability index. It also utilizes parsing techniques to extract reserved keywords and identifiers from the input code. The Abstract Syntax Tree (AST) is generated using the Parse library to represent the code's structure.

## Docker and GitHub Workflows
- Docker: The project includes a Dockerfile for containerizing the application, making it easy to deploy in different environments without worrying about dependencies.
- GitHub Workflows: Automated workflows are set up using GitHub Actions to streamline the testing and deployment process. This ensures that changes are tested and deployed smoothly, especially when deploying the app on Streamlit.

## Use Cases
- Developers can use this app to analyze the complexity and maintainability of their code.
- It can help in identifying common reserved keywords and understanding the structure of the code through the AST visualization.
