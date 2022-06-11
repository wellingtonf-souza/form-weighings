# form-weighings

> Plataforma desenvolvida utilizando a biblioteca [Dash](https://plotly.com/dash/)

Ferramenta desenvolvida como parte do TCC em [Machine Learning in Production](https://iti.ufscar.mba/) da UFSCar. 

O trabalho sendo desenvolvido visa a aplicação de técnicas de machine learning ao cenário de hidroponia. Foi criado um sistema IoT com alguns sensores que captam informações do ambiente e da solução hidroponica e realiza o envio para banco de dados.

Neste cenário é essencial alguma medição das próprias plantas em si, sendo necessária a pesagem de tempos em tempos das mesmas. Para otimizar esse processo foi criada esta ferramenta que valida o acesso do usuário a partir de informação armazenada em um banco mysql e realiza o envio dos dados informados em uma tabela do DynamoDB, nomeada como **weighings**.

Para testes locais é necessário o criar um arquivo `.env` e preencher as variáveis de ambiente definidas no `.env.example`. Também é necessário já possuir a tabela weighings no DynamoDB. A partir destes pontos basta executar:

```bash
docker-compose up -d
```
