table_admin_query = """
CREATE TABLE IF NOT EXISTS admin(
    user VARCHAR(100) NOT NULL PRIMARY KEY DEFAULT "admin",
    password VARCHAR(100) NOT NULL DEFAULT "12345"
);
"""

table_address_query = """
CREATE TABLE IF NOT EXISTS address(
    id INT AUTO_INCREMENT PRIMARY KEY,
    number VARCHAR(20) NOT NULL DEFAULT 'S/N',
    street VARCHAR(255) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    neighborhood VARCHAR(50) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    address_type ENUM('Residential', 'Business', 'Shipping', 'Billing') DEFAULT 'Residential',
    is_primary BOOLEAN DEFAULT FALSE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
"""

table_customer_query = """
CREATE TABLE IF NOT EXISTS customer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fullname VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);"""

table_address_customer_query = """
CREATE TABLE IF NOT EXISTS address_customer(
    id_address INT NOT NULL,
    id_customer INT NOT NULL,
    PRIMARY KEY(id_address, id_customer),
    FOREIGN KEY (id_address) REFERENCES address(id) ON DELETE CASCADE,
    FOREIGN KEY (id_customer) REFERENCES customer(id) ON DELETE CASCADE
);"""

table_individual_query = """
CREATE TABLE IF NOT EXISTS individual (
    customer_id INT PRIMARY KEY,
    ssn VARCHAR(14) NOT NULL UNIQUE COMMENT 'Social Security Number',
    date_of_birth DATE,
    FOREIGN KEY (customer_id) REFERENCES customer(id) ON DELETE CASCADE
);"""

table_company_query = """
CREATE TABLE IF NOT EXISTS company (
    customer_id INT PRIMARY KEY,
    ein VARCHAR(18) NOT NULL UNIQUE COMMENT 'Employer Identification Number',
    legal_name VARCHAR(255) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer(id) ON DELETE CASCADE
);"""

table_manager_query = """
CREATE TABLE IF NOT EXISTS manager(
    manager_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_number VARCHAR(100) NOT NULL UNIQUE,
    hire_date DATE,
    manager_status BOOLEAN NOT NULL DEFAULT TRUE,
    FOREIGN KEY (manager_id) REFERENCES customer(id) ON DELETE CASCADE
);"""

table_branch_query = """
CREATE TABLE IF NOT EXISTS branch (
    branch_id INT PRIMARY KEY AUTO_INCREMENT,
    branch_number INT NOT NULL UNIQUE,
    branch_name VARCHAR(100) NOT NULL,
    open_date DATE,
    manager_id INT NOT NULL,
    address_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (manager_id) REFERENCES manager(manager_id),
    FOREIGN KEY (address_id) REFERENCES address(id)
);"""

table_account_query = """
CREATE TABLE IF NOT EXISTS account (
    id INT AUTO_INCREMENT PRIMARY KEY,
    number VARCHAR(20) NOT NULL UNIQUE,
    password INT(6) NOT NULL,
    balance DECIMAL(15, 2) DEFAULT 0.00,
    account_type ENUM(
        'Savings',
        'Current',
        'Wage',
        'Digital',
        'University',
        'Business',
        'Joint'
    ) DEFAULT "Current",
    branch_id INT NOT NULL,
    customer_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (branch_id) REFERENCES branch(branch_id) ON DELETE CASCADE,
    FOREIGN KEY (customer_id) REFERENCES customer(id) ON DELETE CASCADE
);"""

table_savigns_account_query = """
CREATE TABLE IF NOT EXISTS savigns_account(
    id INT PRIMARY KEY,
    interest_rate DECIMAL(5, 4) DEFAULT 0.005,
    FOREIGN KEY (id) REFERENCES account(id) ON DELETE CASCADE
);"""

table_current_account_query = """
CREATE TABLE IF NOT EXISTS current_account(
    id INT PRIMARY KEY,
    overdraft_limit DECIMAL(15, 2) DEFAULT 500.00,
    withdrawal_limit DECIMAL(15, 2) DEFAULT 1000.00,
    transaction_limit INT DEFAULT 10,
    FOREIGN KEY (id) REFERENCES account(id) ON DELETE CASCADE
);"""


table_historic_query = """
CREATE TABLE IF NOT EXISTS historic(
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_account INT NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY(id_account) REFERENCES account(id) ON DELETE CASCADE
);"""

table_transactions_query = """
CREATE TABLE IF NOT EXISTS transactions(
    id INT AUTO_INCREMENT PRIMARY KEY,
    amount DECIMAL(15, 2) NOT NULL,
    transaction_type VARCHAR(50) NOT NULL,
    historic_id INT NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (historic_id) REFERENCES historic(id) ON DELETE CASCADE
);"""
