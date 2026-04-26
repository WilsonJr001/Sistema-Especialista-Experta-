import collections
import collections.abc
collections.Mapping = collections.abc.Mapping

from experta import *

class PC_Ideal(KnowledgeEngine):

    @DefFacts()
    def dados_iniciais(self):
       print("==================================================")
       print("   SISTEMA ESPECIALISTA - CONFIGURADOR DE PC      ")
       print("==================================================\n") 

       orc_input = input("Qual o orçamento do projeto? (Baixo/Medio/Alto)").strip().capitalize()
       marcaCPU_input = input("Qual sua marca de preferencia? (Intel/AMD)").strip().upper()
       objetivo_input = input("Qual seu objetivo? (JogosLeves/JogosAAA/Servidor)").strip().capitalize()

       print("\nProcessando a base de conhecimento...\n")

       yield Fact(orcamento=orc_input)
       yield Fact(marcaCPU=marcaCPU_input)
       yield Fact(objetivo=objetivo_input)

    # --- CAMADA A: Categoria ---
    @Rule(Fact(orcamento='Baixo'))
    def orcamento_baixo(self):
        self.declare(Fact(categoria='Entrada'))

    @Rule(Fact(orcamento='Medio'))
    def orcamento_medio(self):
        self.declare(Fact(categoria='Intermediaria'))

    @Rule(Fact(orcamento='Alto'))
    def orcamento_alto(self):
        self.declare(Fact(categoria='Avancado'))

    # --- CAMADA B: CPU e Socket ---
    @Rule(Fact(categoria='Entrada'), Fact(marcaCPU='INTEL'))
    def cpu_intel_entrada(self):
        self.declare(Fact(cpu='Core i3-12100F'))
        self.declare(Fact(socket='LGA1700'))

    @Rule(Fact(categoria='Intermediaria'), Fact(marcaCPU='INTEL'))
    def cpu_intel_intermediaria(self):
        self.declare(Fact(cpu='Core i5-13400'))
        self.declare(Fact(socket='LGA1700'))

    @Rule(Fact(categoria='Avancado'), Fact(marcaCPU='INTEL'))
    def cpu_intel_avancado(self):
        self.declare(Fact(cpu='Core i7-14700K'))
        self.declare(Fact(socket='LGA1700'))

    @Rule(Fact(categoria='Entrada'), Fact(marcaCPU='AMD'))
    def cpu_amd_entrada(self):
        self.declare(Fact(cpu='Ryzen 5 5600'))
        self.declare(Fact(socket='AM4'))

    @Rule(Fact(categoria='Intermediaria'), Fact(marcaCPU='AMD'))
    def cpu_amd_intermediaria(self):
        self.declare(Fact(cpu='Ryzen 5 7600'))
        self.declare(Fact(socket='AM5'))

    @Rule(Fact(categoria='Avancado'), Fact(marcaCPU='AMD'))
    def cpu_amd_avancado(self):
        self.declare(Fact(cpu='Ryzen 7 7800X3D'))
        self.declare(Fact(socket='AM5'))

    # --- CAMADA C: Placa-Mãe e Tipo de RAM ---
    @Rule(Fact(socket='LGA1700'), Fact(categoria='Entrada'))
    def mobo_intel_entrada(self):
        self.declare(Fact(placa_mae='H610'))
        self.declare(Fact(ram_tipo='DDR4'))

    @Rule(Fact(socket='LGA1700'), Fact(categoria='Intermediaria'))
    def mobo_intel_intermediaria(self):
        self.declare(Fact(placa_mae='B760'))
        self.declare(Fact(ram_tipo='DDR5'))

    @Rule(Fact(socket='LGA1700'), Fact(categoria='Avancado'))
    def mobo_intel_avancado(self):
        self.declare(Fact(placa_mae='Z790'))
        self.declare(Fact(ram_tipo='DDR5'))

    @Rule(Fact(socket='AM4'))
    def mobo_amd_am4(self):
        self.declare(Fact(placa_mae='B550'))
        self.declare(Fact(ram_tipo='DDR4'))

    @Rule(Fact(socket='AM5'), Fact(categoria='Intermediaria'))
    def mobo_amd_am5_intermediaria(self):
        self.declare(Fact(placa_mae='B650'))
        self.declare(Fact(ram_tipo='DDR5'))

    @Rule(Fact(socket='AM5'), Fact(categoria='Avancado'))
    def mobo_amd_am5_avancado(self):
        self.declare(Fact(placa_mae='X670'))
        self.declare(Fact(ram_tipo='DDR5'))

    # --- CAMADA D: GPU e Fonte ---
    @Rule(Fact(categoria='Entrada'))
    def gpu_fonte_entrada(self):
        self.declare(Fact(gpu='RX 6600'))
        self.declare(Fact(fonte='500W'))

    @Rule(Fact(categoria='Intermediaria'))
    def gpu_fonte_intermediaria(self):
        self.declare(Fact(gpu='RTX 4060'))
        self.declare(Fact(fonte='650W'))

    @Rule(Fact(categoria='Avancado'))
    def gpu_fonte_avancado(self):
        self.declare(Fact(gpu='RTX 4080'))
        self.declare(Fact(fonte='850W'))

    # --- CAMADA E: Capacidade RAM, Armazenamento e SO ---
    @Rule(Fact(objetivo='Jogosleves'))
    def extras_jogosleves(self):
        self.declare(Fact(ram_cap='16GB'))
        self.declare(Fact(armazenamento='SSD 500GB'))
        self.declare(Fact(so='Windows 11'))

    @Rule(Fact(objetivo='Jogosaaa'))
    def extras_jogosaaa(self):
        self.declare(Fact(ram_cap='32GB'))
        self.declare(Fact(armazenamento='SSD 1TB'))
        self.declare(Fact(so='Windows 11'))

    @Rule(Fact(objetivo='Servidor'))
    def extras_servidor(self):
        self.declare(Fact(ram_cap='64GB'))
        self.declare(Fact(armazenamento='SSD 2TB'))
        self.declare(Fact(so='Linux'))

    # --- TELA DE SAÍDA ---
    # O MATCH captura todos os fatos gerados pelas regras anteriores
    @Rule(
        Fact(cpu=MATCH.cpu),
        Fact(placa_mae=MATCH.placa_mae),
        Fact(ram_tipo=MATCH.ram_tipo),
        Fact(gpu=MATCH.gpu),
        Fact(fonte=MATCH.fonte),
        Fact(ram_cap=MATCH.ram_cap),
        Fact(armazenamento=MATCH.armazenamento),
        Fact(so=MATCH.so)
    )
    def exibir_resultado(self, cpu, placa_mae, ram_tipo, gpu, fonte, ram_cap, armazenamento, so):
        print("=== PC MONTADO COM SUCESSO ===")
        print(f"Processador: {cpu}")
        print(f"Placa-Mãe: {placa_mae}")
        print(f"Memória RAM: {ram_cap} {ram_tipo}")
        print(f"Placa de Vídeo: {gpu}")
        print(f"Armazenamento: {armazenamento}")
        print(f"Fonte de Alimentação: {fonte}")
        print(f"Sistema Operacional Recomendado: {so}")
        print("==============================\n")


if __name__== "__main__":
    engine  = PC_Ideal()
    engine.reset()
    engine.run()