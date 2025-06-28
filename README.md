# Calculakcal
Perfeito, obrigado pelo esclarecimento! Com isso, aqui está a versão revisada do artigo técnico, refletindo com precisão o público-alvo e a proposta do projeto Calculakcal:

🥗 Calculakcal: Uma Calculadora de Calorias para Bem-Estar e Objetivos Pessoais
📌 Introdução
O Calculakcal é uma aplicação web desenvolvida com o framework Django, que tem como objetivo auxiliar qualquer pessoa — seja individualmente ou em grupo, como famílias — a calcular suas necessidades calóricas diárias com base em dados pessoais e metas de saúde. A proposta é oferecer uma ferramenta acessível, intuitiva e personalizável para quem deseja emagrecer, manter o peso ou ganhar massa corporal.
🎯 Finalidade da Aplicação
A aplicação permite:
- Calcular a taxa metabólica basal (TMB) com base em idade, peso, altura e sexo.
- Ajustar o valor calórico diário conforme o nível de atividade física e o objetivo nutricional.
- Promover o bem-estar e a autonomia alimentar, com foco em metas individuais ou familiares.
👥 Público-Alvo
- Famílias que desejam adotar hábitos saudáveis em conjunto.
- Indivíduos interessados em nutrição, saúde e qualidade de vida.
- Pessoas que buscam uma ferramenta prática, sem necessidade de cadastro ou complexidade técnica.
🛠️ Tecnologias Utilizadas
| Tecnologia | Finalidade | 
| Django | Framework backend em Python para estruturação da aplicação e lógica de negócio. | 
| SQLite | Banco de dados leve e embutido, ideal para projetos de pequeno porte. | 
| HTML5 | Estruturação da interface e formulários. | 
| CSS3 | Estilização da interface. | 
| Bootstrap | Framework CSS para layout responsivo e componentes visuais modernos. | 
| JavaScript | Manipulação dinâmica da interface e lógica de cálculo no frontend. | 


⚙️ Estrutura do Projeto
- models.py: define os modelos de dados (usuários, perfis, metas).
- views.py: contém a lógica de exibição e manipulação dos dados.
- templates/: arquivos HTML com integração Django + Bootstrap.
- db.sqlite3: banco de dados local com persistência das informações.
- static/: arquivos CSS, JS e imagens.
📐 Lógica de Cálculo
A aplicação utiliza a Equação de Harris-Benedict para estimar a TMB. O valor é então ajustado com:
- Um fator de atividade física (sedentário, moderado, intenso).
- Um coeficiente de meta (déficit calórico para emagrecer, superávit para ganho de massa).
📈 Potencial de Expansão
- Integração com APIs de alimentos.
- Dashboard com gráficos de progresso.
- Cadastro de refeições e plano alimentar diário.
- Autenticação de usuários e histórico de cálculos.
📚 Fontes das Tecnologias
- Django: https://www.djangoproject.com
- SQLite: https://www.sqlite.org
- Bootstrap: https://getbootstrap.com
- HTML5: https://developer.mozilla.org/en-US/docs/Web/HTML
- CSS3: https://developer.mozilla.org/en-US/docs/Web/CSS
- JavaScript: https://developer.mozilla.org/en-US/docs/Web/JavaScript
- Equação de Harris-Benedict: https://en.wikipedia.org/wiki/Harris–Benedict_equation
