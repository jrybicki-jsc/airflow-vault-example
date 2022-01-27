from airflow.decorators import dag, task
from airflow.providers.ssh.hooks.ssh import SSHHook
from airflow.utils.dates import days_ago

    
default_args = {
    'owner': 'airflow',
}


@dag(default_args=default_args, schedule_interval=None, start_date=days_ago(2), tags=['example'])
def test_vault():
    @task()
    def load():
        print("Testing vault connection")
        connection_id = 'mycon'
        ssh_hook = SSHHook(ssh_conn_id=connection_id)
        with ssh_hook.get_conn() as ssh_client:
            sftp_client = ssh_client.open_sftp()
            print("Connected!")
        return connection_id

    
    load()


dag = test_vault()
