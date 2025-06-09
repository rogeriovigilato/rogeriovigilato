## Hi there 👋

<!--
**rogeriovigilato/rogeriovigilato** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->

## Auto Clicker Script

Este repositório contém um script chamado `clicker.py` que identifica imagens na tela e realiza cliques automáticos. Para usar:

1. Instale as dependências (ex.: `pip install pyautogui`).
2. Separe **cinco** imagens de referência na pasta `C:/xls/notas` e nomeie-as de forma ordenada (ex.: `1.png`, `2.png` ... `5.png`).
   Use a opção `--folder` para definir outra pasta se necessário.
3. Execute `python clicker.py --interval 0.5 --loops 1 --timeout 5`.

O script percorre as cinco imagens em ordem, aguardando até `--timeout` segundos por cada uma e clicando assim que aparecem na tela.
