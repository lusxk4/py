# 🎮 Aviator Bot - Controle por Voz

Bot de automação para o jogo Aviator controlado 100% por comandos de voz em português brasileiro.

## 🚀 Funcionalidades

- ✅ **Apostas manuais** com valor customizado ou padrão
- ✅ **Apostas automáticas** com auto cashout configurável
- ✅ **Saque manual** de apostas ativas
- ✅ **Controle de auto cashout** (ativar/desativar)
- ✅ **Abertura de histórico**
- ✅ **Reconhecimento de voz rápido** e natural em PT-BR

## 📋 Requisitos

- Python 3.8+
- Microfone funcional
- Windows (testado no Windows 11)

## 📦 Instalação

1. Clone o repositório:
```bash
git clone <seu-repositorio>
cd aviator-bot
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as coordenadas:
   - Abra o jogo Aviator
   - Edite `coordinates.py` com as posições dos botões na sua tela
   - Use uma ferramenta como AutoHotkey para capturar as coordenadas

## 🎯 Uso

Execute o bot:
```bash
python main.py
```

### Comandos de Voz

#### Apostas Manuais
- `"aposta 1"` - Aposta na posição 1 com valor padrão (R$ 5)
- `"aposta 2"` - Aposta na posição 2 com valor padrão (R$ 10)
- `"5 reais aposta 1"` - Aposta R$ 5 na posição 1
- `"15 reais aposta 2"` - Aposta R$ 15 na posição 2
- `"r$ 10 aposta 1"` - Aposta R$ 10 na posição 1

#### Apostas Automáticas
- `"15 reais aposta 1 auto 5"` - Aposta R$ 15 na posição 1 com cashout automático em 5x
- `"10 aposta 2 auto 3"` - Aposta R$ 10 na posição 2 com cashout em 3x
- `"20 aposta 1 auto"` - Aposta R$ 20 com cashout padrão (2x)

#### Saque
- `"sac 1"` ou `"sacar 1"` - Saca a aposta 1
- `"sac 2"` ou `"sacar 2"` - Saca a aposta 2

#### Controle de Auto Cashout
- `"tirar auto 1"` - Desativa auto cashout da aposta 1
- `"desligar auto 2"` - Desativa auto cashout da aposta 2

#### Histórico
- `"abrir histórico"` - Abre o histórico de partidas

## 🔧 Configuração

### Valores Padrão
Edite em `main.py`:
```python
DEFAULT_BET_VALUES = {1: 5.0, 2: 10.0}
```

### Coordenadas
Configure em `coordinates.py` as posições dos elementos na tela:
```python
# Exemplo
BET1_VALUE_INPUT = (x, y)
BET1_BET_BUTTON = (x, y)
# ...
```

## 📁 Estrutura do Projeto

```
aviator-bot/
├── main.py           # Script principal com parsing de comandos
├── voice.py          # Reconhecimento de voz
├── aviator.py        # Automação do jogo (cliques e digitação)
├── coordinates.py    # Coordenadas dos elementos da tela
├── requirements.txt  # Dependências Python
├── README.md         # Este arquivo
└── .gitignore       # Arquivos ignorados pelo git
```

## 🛠️ Tecnologias

- **speech_recognition** - Reconhecimento de voz via Google Speech API
- **pyautogui** - Automação de mouse e teclado
- **threading** - Execução paralela para não travar o reconhecimento

## ⚙️ Como Funciona

1. O bot **escuta continuamente** comandos de voz
2. Transcreve o áudio usando Google Speech Recognition
3. Faz **parsing inteligente** do comando em português
4. Executa ações usando **pyautogui** (cliques e digitação)
5. Usa **threads** para não bloquear o reconhecimento durante execução

## 🐛 Troubleshooting

### Bot não reconhece minha voz
- Verifique se o microfone está funcionando
- Fale de forma clara e próxima ao microfone
- Ajuste `recognizer.energy_threshold` em `voice.py`

### Cliques acontecem no lugar errado
- Reconfigure as coordenadas em `coordinates.py`
- Certifique-se que a resolução da tela não mudou
- Use ferramentas como MousePosition para obter coordenadas precisas

### Bot está lento
- Os delays já estão otimizados ao mínimo
- Verifique sua conexão de internet (Google Speech API)
- Considere usar um microfone de melhor qualidade

## ⚠️ Avisos

- Este bot é apenas para fins educacionais
- Use por sua conta e risco
- Não me responsabilizo por perdas financeiras
- Respeite os termos de serviço da plataforma

## 📝 Licença

MIT License - Sinta-se livre para usar e modificar

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas funcionalidades
- Melhorar a documentação
- Enviar pull requests

---

**Desenvolvido com ❤️ para a comunidade**