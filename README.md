# 🚀 AWS EC2 Instance Starter with Boto3

Este projeto contém um script em Python que utiliza a biblioteca Boto3 para iniciar uma instância EC2 na AWS. 

## 📋 Descrição

O script permite iniciar uma instância EC2 na AWS usando a biblioteca Boto3. Ele é configurado para iniciar uma instância de teste `t2.micro` com uma imagem Ubuntu, mas pode ser facilmente personalizado para atender às suas necessidades.

## 🛠️ Pré-requisitos

- Python 3.x
- Biblioteca Boto3 instalada (`pip install boto3`)
- Credenciais AWS configuradas

## 🚀 Como Usar

1. Clone este repositório:

    ```bash
    git clone https://github.com/seu_usuario/aws-ec2-starter.git
    cd aws-ec2-starter
    ```

2. Configure suas credenciais AWS no script:

    ```python
    aws_access_key_id = 'SUA_ACCESS_KEY'
    aws_secret_access_key = 'SEU_SECRET_ACCESS_KEY'
    aws_session_token = 'SEU_SESSION_TOKEN'
    aws_region = 'SUA_REGIAO'
    ```

3. Configure o tipo de instância, chave SSH, grupo de segurança e ID da imagem:

    ```python
    instance_type = 't2.micro' # Tipo de instância
    key_name = 'SUA_KEY' # Nome da chave SSH
    security_group_ids = ['SEU_SECURITY_GROUP'] # IDs do grupo de segurança
    image_id = 'ami-0fc5d935ebf8bc3bc' # ID da imagem do Ubuntu
    ```

4. Execute o script:

    ```bash
    python start_ec2_instance.py
    ```

5. O script retornará o ID da nova instância EC2 iniciada:

    ```
    Nova instância iniciada com ID: i-xxxxxxxxxxxxxxxxx
    ```

## 🧑‍💻 Autor
- Brian Guimarães Gomes
