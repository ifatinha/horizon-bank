CREATE TABLE IF NOT EXISTS address(
    id INT AUTO_INCREMENT PRIMARY KEY,
    number VARCHAR(20) NOT NULL DEFAULT 'S/N',
    street VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    postal_code VARCHAR(20) NOT NULL,
    country VARCHAR(100) NOT NULL,
    latitude DECIMAL(9, 6),
    longitude DECIMAL(9, 6),
    address_type ENUM('Residential', 'Business', 'Shipping', 'Billing') DEFAULT 'Residential',
    is_primary BOOLEAN DEFAULT FALSE,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS customer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fullname VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS address_customer(
    id_adress INT NOT NULL,
    code_customer INT NOT NULL,
    PRIMARY KEY(id_adress, code_customer),
    FOREIGN KEY (id_adress) REFERENCES address(id) ON DELETE CASCADE,
    FOREIGN KEY (code_customer) REFERENCES customer(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS individual (
    customer_id INT PRIMARY KEY,
    ssn VARCHAR(14) NOT NULL UNIQUE COMMENT 'Social Security Number',
    date_of_birth DATE,
    FOREIGN KEY (customer_id) REFERENCES customer(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS company (
    customer_id INT PRIMARY KEY,
    ein VARCHAR(18) NOT NULL UNIQUE COMMENT 'Employer Identification Number',
    legal_name VARCHAR(255) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS manager(
    manager_id INT PRIMARY KEY AUTO_INCREMENT,
    hire_date DATE,
    manager_status BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (manager_id) REFERENCES customer(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS branch (
    branch_id INT PRIMARY KEY AUTO_INCREMENT,
    branch_name VARCHAR(100) NOT NULL,
    address_id INT NOT NULL,
    manager_id INT NOT NULL,
    open_date DATE,
    FOREIGN KEY (address_id) REFERENCES branch_address(id),
    FOREIGN KEY (manager_id) REFERENCES manager(manager_id)
);

CREATE TABLE IF NOT EXISTS branch_address(
    address_id INT PRIMARY KEY,
    branch_id INT PRIMARY KEY,
    PRIMARY KEY(address_id, branch_id),
    FOREIGN KEY(address_id) REFERENCES address(id) ON DELETE CASCADE,
    FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS account (
    id INT AUTO_INCREMENT PRIMARY KEY,
    branch VARCHAR(10) NOT NULL,
    account_number VARCHAR(20) NOT NULL UNIQUE,
    balance DECIMAL(15, 2) DEFAULT 0.00,
    customer_id INT NOT NULL,
    account_type ENUM(
        'Savings',
        'Current',
        'Wage',
        'Digital',
        'University',
        'Business',
        'Joint'
    ) DEFAULT "Current",
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customer(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS savigns_account(
    id INT PRIMARY KEY,
    interest_rate DECIMAL(5, 4) DEFAULT 0.005,
    FOREIGN KEY (id) REFERENCES account(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS current_account(
    id INT PRIMARY KEY,
    overdraft_limit DECIMAL(15, 2) DEFAULT 500.00,
    withdrawal_limit DECIMAL(15, 2) DEFAULT 1000.00,
    transaction_limit INT DEFAULT 10,
    FOREIGN KEY (id) REFERENCES account(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS historic(
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_account INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (id_account) REFERENCES account(id)
);

CREATE TABLE IF NOT EXISTS transactions(
    id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_type VARCHAR(50) NOT NULL,
    amount DECIMAL(15, 2) NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_historic INT NOT NULL,
    FOREIGN KEY(id_historic) REFERENCES historic(id)
)