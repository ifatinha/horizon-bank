from database.DatabaseOperations import DatabaseOperations

table_address_query = """
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
"""

table_customer_query = """
CREATE TABLE IF NOT EXISTS customer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    telefone VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
"""

table_address_customer_query = """
CREATE TABLE IF NOT EXISTS address_customer(
    id_adress INT NOT NULL,
    code_customer INT NOT NULL,
    PRIMARY KEY(id_adress, code_customer),
    FOREIGN KEY (id_adress) REFERENCES address(id) ON DELETE CASCADE,
    FOREIGN KEY (code_customer) REFERENCES customer(id) ON DELETE CASCADE
);
"""

table_individual_query = """
CREATE TABLE IF NOT EXISTS individual (
    customer_id INT PRIMARY KEY,
    ssn VARCHAR(14) NOT NULL UNIQUE COMMENT 'Social Security Number',
    date_of_birth DATE,
    FOREIGN KEY (customer_id) REFERENCES customer(id) ON DELETE CASCADE
);
"""

table_company_query = """
CREATE TABLE IF NOT EXISTS company (
    customer_id INT PRIMARY KEY,
    ein VARCHAR(18) NOT NULL UNIQUE COMMENT 'Employer Identification Number',
    legal_name VARCHAR(255) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer(id) ON DELETE CASCADE
);
"""

DatabaseOperations.create_table(table_address_query)
DatabaseOperations.create_table(table_customer_query)
DatabaseOperations.create_table(table_address_customer_query)
DatabaseOperations.create_table(table_individual_query)
DatabaseOperations.create_table(table_company_query)
