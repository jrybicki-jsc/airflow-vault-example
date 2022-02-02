from airflow.decorators import dag, task
from airflow.utils.dates import days_ago
from airflow.providers.hashicorp.hooks.vault import VaultHook
    
default_args = {
    'owner': 'airflow',
}


@dag(default_args=default_args, schedule_interval=None, start_date=days_ago(2), tags=['example'])
def test_secrets():
    @task()
    def load():
        print("Testing vault secrets")
        connection_id = 'my_vault'
        vault_hook = VaultHook(vault_conn_id=connection_id)
        print('hook:',vault_hook.get_secret(secret_path='connections/mycon'))

    
    load()


dag = test_secrets()
