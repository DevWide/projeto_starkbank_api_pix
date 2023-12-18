import starkbank
import datetime
import time
import logging
from random import randint

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Autenticação
project = starkbank.Project(
    environment="sandbox",
    id="6247741164355584", # ID do projeto no SandBox
    private_key="""-----BEGIN EC PRIVATE KEY-----
    MHQCAQEEIAmBUDvkSrEW2nsyOoM586WevzwG69o7EPYM4NXrnjeYoAcGBSuBBAAK
    oUQDQgAECyX8n5BBz/H3x5RFg+WThjPztHp7IwTp/n46kIeXer2DT+RwflScqYnN
    I2zU0gx9D85ilrSxQKHt0/LJ4W9WTQ==
    -----END EC PRIVATE KEY-----
    """
)

# Inicialize o SDK do StarkBank
starkbank.user = project

def create_pix_transfers():
    transfers = []
    for _ in range(10):
        transfers.append(starkbank.Transfer(
            amount=randint(1000, 10000),
            bank_code="20018183",
            branch_code="0001",
            account_number="6341320293482496",
            tax_id="012.345.678-90",
            name="Random Person {}".format(randint(1, 100)),
            account_type="checking"  # Ajuste para um valor válido
        ))

    try:
        created_transfers = starkbank.transfer.create(transfers)
    except starkbank.error.StarkBankError as e:
        # Log a mensagem de erro específica
        logging.error(f"StarkBank Error: {e}")
        return None
    except Exception as e:
        # Log a mensagem de erro genérica
        logging.error(f"Unexpected Error: {e}")
        return None
    return created_transfers

def main():
    start_time = datetime.datetime.now()
    transfer_logs = []

    while (datetime.datetime.now() - start_time).total_seconds() < 86400:  # 24 horas
        transfers = create_pix_transfers()
        if transfers:
            for transfer in transfers:
                transfer_logs.append({
                    'transfer_id': transfer.id,
                    'time_created': transfer.created,
                    'status': transfer.status
                })

        time.sleep(10800)  # Espera por 3 horas

    # O código abaixo irá gerar o relatório...
    successful_transfers = [t for t in transfer_logs if t['status'] == 'CREATED']
    failed_transfers = [t for t in transfer_logs if t['status'] != 'CREATED']

    success_rate = len(successful_transfers) / len(transfer_logs) * 100 if transfer_logs else 0
    error_counts = {t['status']: failed_transfers.count(t) for t in failed_transfers}

    total_processing_time = sum((t['time_created'] - start_time).total_seconds() for t in transfer_logs)
    average_processing_time = total_processing_time / len(transfer_logs) if transfer_logs else 0

    print("Total Transfers:", len(transfer_logs))
    print("Successful Transfers:", len(successful_transfers))
    print("Failed Transfers:", len(failed_transfers))
    print("Success Rate:", success_rate)
    print("Error Counts:", error_counts)
    print("Average Processing Time (seconds):", average_processing_time)

if __name__ == "__main__":
    main()
