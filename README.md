# form-weighings

> Plataforma desenvolvida utilizando a biblioteca [Dash](https://plotly.com/dash/)

Ferramenta desenvolvida como parte do TCC em [Machine Learning in Production](https://iti.ufscar.mba/) da UFSCar. 

O trabalho sendo desenvolvido visa a aplicação de técnicas de machine learning ao cenário de hidroponia. Foi criado um sistema IoT com alguns sensores que captam informações do ambiente e da solução hidroponica e realiza o envio para banco de dados.

Neste cenário é essencial alguma medição das próprias plantas em si, sendo necessária a pesagem de tempos em tempos das mesmas. Para otimizar esse processo foi criada esta ferramenta que valida o acesso do usuário a partir de informação armazenada em um banco mysql e realiza o envio dos dados informados em uma tabela do DynamoDB, nomeada como **weighings**.

Para testes locais é necessário o criar um arquivo `.env` e preencher as variáveis de ambiente definidas no `.env.example`. Também é necessário já possuir a tabela weighings no DynamoDB. A partir destes pontos basta executar:

```bash
docker-compose up -d
```

Para realizar o deploy no Heroku é necessário ter um banco MySQL em cloud e executar os seguintes passos:

1. Acessar a pasta especifica da plataforma:
```bash
cd dash
```
2. Realizar o login no Heroku:
```bash
heroku login
```

3. Realizar o login no Container Registry:
```bash 
heroku container:login
```

4. Criar o aplicativo:
```bash
heroku create
```

5. Com o comando acima foi criado um aplicativo no Heroku e seu nome foi apresentado em tela. Este nome também pode ser visualizado executando `heroku apps`. Neste momento é necessário acessar o Heroku via navegador, ir nas configurações do aplicativo recém-criado e adicionar as variáveis de ambiente necessárias para a aplicação, definidas no arquivo `.env`.

6. Crie a imagem e envie para o Container Registry. app_name é referente ao nome do seu aplicativo, obtido anteriormente ao executar `heroku apps`.
```bash
heroku container:push web -a app_name
```
7. Libere a imagem para seu aplicativo:
```bash
heroku container:release web -a app_name
```

8. Agora já é possível abir o aplicativo pelo seu navegador:
```bash
heroku open -a app_name
```