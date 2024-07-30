from classes.Deposit import Deposit
from classes.Withdraw import Withdraw
from classes.Transfer import Transfer
from datetime import datetime


class TransactionCreator:

    @staticmethod
    def deposit_creator(historic_id, value):
        deposit = Deposit(value)
        return deposit.to_tuple(historic_id)

    @staticmethod
    def withdraw_creator(historic_id, value):
        withdraw = Withdraw(value)
        return withdraw.to_tuple(historic_id)

    @staticmethod
    def transfer_creator(historic_id, value):
        transfer = Transfer(value)
        return transfer.to_tuple(historic_id)

    @staticmethod
    def from_db_record(record) -> str:
        """
        Formata um registro de banco de dados em uma string legível.

        :param record: Tupla contendo informações da transação.
        :return: String formatada com detalhes da transação.
        """
        try:
            amount, transaction_type, created_at = record

            # Se created_at for uma string, converta para datetime
            if isinstance(created_at, str):
                created_at = datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S")

            formatted_amount = f"R$ {amount:.2f}"
            formatted_date = created_at.strftime("%d/%m/%Y %H:%M:%S")

            return (
                f"Valor: {formatted_amount}\n"
                f"Transação: {transaction_type}\n"
                f"Data: {formatted_date}"
            )
        except (IndexError, TypeError, ValueError) as e:
            return f"Erro ao formatar o registro: {e}"
