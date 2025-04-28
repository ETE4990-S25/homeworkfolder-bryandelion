# Paste your python file here 
# don't forget to upload it with your submission
import logging
import random

# Define different components and their sample messages    generated using chat
components = {
    "frontend": [
        "User navigated to homepage",
        "Loaded dashboard components",
        "User attempted invalid input on form",
        "Failed to load user profile data",
        "Frontend script crashed unexpectedly"
    ],
    "backend": [
        "Received API request for user data",
        "Slow response detected on API endpoint",
        "Failed to process payment request",
        "Backend server crash: out of memory",
        "Authentication token verified"
    ],
    "sqldb": [
        "Database connection established",
        "Query execution time exceeds threshold",
        "Failed to insert new user record",
        "Database corruption detected in users table",
        "Backup completed successfully"
    ],
    "authserver": [
        "User login request received",
        "Multiple failed login attempts detected",
        "Session creation failed",
        "Authentication service unavailable",
        "Password reset token generated"
    ],
    "system": [
        "System maintenance scheduled",
        "CPU usage exceeds 85%",
        "Disk write failure in logging system",
        "Kernel panic detected",
        "System heartbeat OK"
    ]
}

# Log levels random gen
levels = [logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]

#  function to configure and write logs
def setup_logger(component_name):
    logger = logging.getLogger(component_name)
    logger.setLevel(logging.DEBUG)
    #handler saving the output next to the script file, you should see an output in the same folder the script is in, <<<<
    handler = logging.FileHandler(f"{component_name}.log")
    formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    return logger

#  loggers for each component
for component, messages in components.items():
    logger = setup_logger(component)
    
    for _ in range(5):  # log entries fromatting liek the examples showed with time and all 
        message = random.choice(messages)
        level = random.choice(levels)
        
        if level == logging.INFO:
            logger.info(message)
        elif level == logging.WARNING:
            logger.warning(message)
        elif level == logging.ERROR:
            logger.error(message)
        elif level == logging.CRITICAL:
            logger.critical(message)

print("Log files created ")
