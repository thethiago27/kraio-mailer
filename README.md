## Visão Geral
Este projeto consiste em um servidor de envio de email escalável construído sobre a AWS Lambda, utilizando o Simple Email Service (SES) para o envio de emails. O servidor é projetado para lidar com solicitações de envio de emails acionadas por uma fonte de eventos, como uma fila do Amazon Simple Queue Service (SQS).

## Arquitetura
Escalabilidade: Utiliza a AWS Lambda para uma arquitetura serverless, permitindo escalabilidade contínua com base na demanda.

Integração com SES: Envia emails por meio do AWS SES, um serviço de email confiável e escalável.

Análise de Modelos: Oferece suporte a modelos de emails HTML com conteúdo dinâmico usando um analisador de modelos.

Tratamento de Erros: Implementa tratamento de erros para gerenciar exceções durante o envio de emails.