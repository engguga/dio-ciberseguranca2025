Aviso de segurança (LEIA ANTES DE RODAR)

Finalidade educacional: conteúdo criado para aprendizado em ambiente controlado.

Isolamento obrigatório: execute somente em uma VM ou ambiente sandbox isolado (ex.: VirtualBox/VMware, com rede desativada ou NAT restrito).

Snapshots: crie snapshot da VM antes de qualquer teste para poder reverter mudanças.

Dados sensíveis: NÃO use dados reais (senhas, documentos pessoais, chaves privadas).

Rede: desligue conexões desnecessárias; se testar envio por e‑mail, configure uma conta de teste em ambiente controlado.

Repositório público: o código é público apenas como exemplo; remova/anonimize quaisquer dados privados nos arquivos logs/ antes de commitar.

Ransomware (simulado)
O que faz

Exemplifica um fluxo simplificado: geração de chave (Fernet), encriptação de arquivos de teste e criação de uma mensagem de "resgate".

Inclui script de decriptação que utiliza a chave correta (para fins de demonstração).

Dependências

Python 3.10+

biblioteca cryptography (Fernet)

Observação

Os scripts não implementam técnicas avançadas de persistência ou espalhamento — são intencionalmente limitados para estudo.

Keylogger (simulado)
O que faz

Captura eventos de teclado (padrão com pynput) e grava em arquivo .txt local.

Versão de demonstração inclui opção de armazenar logs localmente e uma rotina que simula envio automático por e‑mail (apenas em ambiente de teste).

Dependências

Python 3.10+

biblioteca pynput

módulo smtplib (biblioteca padrão) para simulação de envio de e‑mail

Observação

O keylogger implementado é uma simulação educativa. Em ambientes reais, captura de teclas é ilegal sem consentimento explícito.

Como rodar (passo a passo recomendado)

Crie VM isolada e tire snapshot.

Clone este repositório na VM (ou copie apenas as pastas relevantes).

Crie um ambiente virtual e instale dependências:

python3 -m venv venv
source venv/bin/activate
pip install -r ransomware/requirements.txt
pip install -r keylogger/requirements.txt

Teste o Ransomware simulado apenas com arquivos de teste em ransomware/test_files/.

Teste o Keylogger simulando digitação em um terminal da VM; revise os logs em keylogger/logs/.

Nunca execute os scripts fora da máquina isolada.

Boas práticas e medidas de defesa

Use antivírus e EDR com assinaturas/heurísticas atualizadas.

Mantenha sistema e software atualizados (patch management).

Restrinja privilégios: principo de menor privilégio (PoLP).

Backup offline e testado regularmente (3‑2‑1 rule: 3 cópias, 2 mídias, 1 offsite).

Segmentação de rede e aplicação de firewall.

Detecção e resposta: logs centralizados, monitoramento de integridade de arquivos, alertas para comportamento anômalo.

Educação e phishing awareness para usuários.

Como contribuir

Abra uma issue descrevendo a proposta.

Faça um fork, implemente alterações em branch separado e envie pull request.

Use commits atômicos e mensagens claras.

Observação: evite enviar código que amplie a capacidade ofensiva além do escopo didático.

Licença

Este repositório está licenciado como MIT (consulta o arquivo LICENSE se incluído). Uso com responsabilidade.

Contato

Se precisar de ajuda para adaptar os scripts ao seu ambiente de laboratório, gerar comandos para organizar as pastas no repositório ou criar o repositório remoto no GitHub, me diga — eu preparo os comandos prontos para colar no terminal.
