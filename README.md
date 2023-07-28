# SMTP_Checker &middot; [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![GitHub stars](https://badgen.net/github/stars/DeadpoolMDE/SMTP_Checker)](https://GitHub.com/DeadpoolMDE/SMTP_Checker) [![GitHub forks](https://badgen.net/github/forks/DeadpoolMDE/SMTP_Checker/)](https://GitHub.com/DeadpoolMDE/SMTP_Checker)


<p align="center">
  <img src="https://media.discordapp.net/attachments/1134316798620217364/1134320197940027523/SnaJuqE.png" width="600" height="450" />
</p> 

**SMTP_Checker** is a tool designed to check the validity of SMTP servers. It allows you to test multiple SMTP servers simultaneously and categorize them into valid and invalid based on their response.

Feel free to use, modify, and contribute to this project. If you encounter any issues or have suggestions for improvement, please open an issue or create a pull request. Happy SMTP checking! 📧🔍

- [Installation](#installation)
- [Tool Configuration](#tool-configuration)
- [Explanation of configuration options](#explanation-of-configuration-options)

## Installation
>Follow these steps to run the SMTP_Checker tool:
+ 1- Run setup.bat or install requirements.txt file.
```bash
pip install -r requirements.txt
```
+ 2- Run start.bat or Execute `smtp_checker.py`.
```bash
python smtp_checker.py
```

## Tool Configuration

> Configuration file is `config.yaml`.
```yaml
files:
  smtp_file: "./output/smtp.txt"
  valid_file: "./output/valid.txt"
  invalid_file: "./output/invalid.txt"

config:
  threading: 50
  email_to_send_result: "deadpoolsmtp@gmail.com"
```

## Explanation of configuration options

+ `smtp_file:` Path to the file containing a list of SMTP servers to check. 
+ `valid_file:` Path to the file where the valid SMTP servers will be saved. 
+ `invalid_file:` Path to the file where the invalid SMTP servers will be saved. 
+ `threading:` Number of threads used for concurrent checking of SMTP servers. 
+ `email_to_send_result:` Email address where the result of the SMTP server check will be sent. 

## Donate ❤️
> **Dontate to make me more passionate to make more scripts :)**

<a href="https://www.buymeacoffee.com/deadpoolmde" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>


