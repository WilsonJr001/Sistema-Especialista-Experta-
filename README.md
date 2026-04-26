# Configurador de PC Gamer - Sistema Especialista

Este projeto foi desenvolvido como parte da **Atividade 02** da disciplina de **Inteligência Artificial (ECOI22)** na **Universidade Federal de Itajubá (UNIFEI)**. O objetivo é auxiliar usuários na seleção de componentes compatíveis para a montagem de um computador, evitando gargalos técnicos e garantindo a melhor performance dentro de um orçamento definido.

## 🚀 Sobre o Projeto

O sistema atua como um consultor de hardware, processando variáveis como orçamento, preferência de fabricante (Intel/AMD) e finalidade de uso (Jogos, Trabalho ou Servidor). 

O projeto conta com duas implementações distintas para estudo de motores de inferência:
1.  **Expert Sinta:** Implementação utilizando encadeamento para trás (*Backward Chaining*).
2.  **Experta (Python):** Implementação utilizando encadeamento para frente (*Forward Chaining*).

## 🛠️ Tecnologias Utilizadas

* [Expert Sinta](http://www.lia.ufc.br/~sinta/) (Shell para Sistemas Especialistas)
* [Python 3.10+](https://www.python.org/)
* [Experta](https://experta.readthedocs.io/en/latest/) (Biblioteca Python para Sistemas Especialistas baseada no algoritmo Rete)

## 📂 Estrutura de Arquivos

* `PC-Ideal.bcm`: Base de conhecimento estruturada para o software Expert Sinta.
* `configurador.py`: Código fonte da implementação em Python.
* `Relatorio_Atividade_02.pdf`: Relatório técnico detalhado seguindo o modelo IEEE (LaTeX).

## 💻 Como Executar (Versão Python)

### Pré-requisitos
Certifique-se de ter o Python instalado. É recomendado o uso de um ambiente virtual.

### Instalação
1. Clone ou baixe este repositório.
2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
