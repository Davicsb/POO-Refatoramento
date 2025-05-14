# POO-Refatoramento
Este projeto aplica princípios de Programação Orientada a Objetos (POO) e padrões de projeto para organizar, modularizar e facilitar a manutenção de um sistema de fitness. O código foi refatorado para utilizar boas práticas como baixo acoplamento, alta coesão e separação de responsabilidades, promovendo uma arquitetura escalável e flexível para futuras extensões.
## Design Pattern
### Criação
Factory Method (factory.py)\
<img width="524" alt="image" src="https://github.com/user-attachments/assets/cea17a0d-025e-4b32-b728-9e1ca27936ec" />
Por que usar?\
Desacoplamento: a classe principal (FitnessApp) não precisa saber como os objetos são criados, apenas usa os métodos da fábrica;\
Extensibilidade: permite criar variações facilmente;\
Organização: centraliza toda a lógica de criação em um único lugar (factory.py), mantendo o código mais limpo e modular.
### Estrutural
Adapter (adapter.py)\
<img width="316" alt="image" src="https://github.com/user-attachments/assets/38aa73e6-d846-4ebe-beaa-8d412813320e" />
Por que usar?\
Compatibilidade: permite que classes com interfaces diferentes possam ser tratadas de forma uniforme com o mesmo método;\
Reuso: aproveitou funcionalidades existentes do sistema (app, activity_tracker, etc.) sem precisar modificar as classes originais.\
Facade (facade.py)\
<img width="314" alt="image" src="https://github.com/user-attachments/assets/34d93660-171a-4933-9278-eda385ca207d" />
Por que usar?\
Simplicidade: unifica o acesso a vários subsistemas para a criação da fábrica;\
Encapsulamento: esconde a complexidade de configuração dos módulos internos da aplicação, expondo apenas o necessário;\
Organização: evita que a factory fique carregada com várias instâncias diretas, centralizando o controle da lógica do sistema em um ponto único.
### Comportamental
Template Method (adapter.py)\
<img width="163" alt="image" src="https://github.com/user-attachments/assets/f723efb0-f99f-49c1-8ce4-4735f6e656f5" />
Por que usar?\
Padronização: define um fluxo comum de execução (execute()), garantindo que todos os componentes sigam uma estrutura (ex: pre_execute(), run(), post_execute());\
Extensibilidade controlada: permite que subclasses modifiquem apenas partes específicas (run()), mantendo o restante do comportamento comum intacto;\
Reuso de lógica: evita duplicação de código, pois o comportamento genérico está definido na superclasse (FitnessComponent) e os detalhes específicos ficam nas subclasses.
