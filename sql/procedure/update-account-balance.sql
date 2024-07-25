DELIMITER //
	CREATE PROCEDURE AtualizarSaldoComJuros()
	BEGIN
		DECLARE interest_rate DECIMAL(5,4);
        
        -- consultar a taxa de juros na tabela poupança
        SELECT interest_rate INTO interest_rate FROM savigns_account LIMIT 1;
        
        -- verifica se o dia atual é o primeiro do mês
        IF DAY(CURDATE()) = 1 THEN
			UPDATE account
            SET balance = balance * (1 + interest_rate / 100)
            WHERE account_type = 'Savings'; 
		END IF;
    END
DELIMITER //