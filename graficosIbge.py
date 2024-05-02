import matplotlib.pyplot as plt

# Dados
anos = ['1940', '2022']
expectativa_total = [45.5, 75.5]
expectativa_homem = [42.9, 72.0]
expectativa_mulher = [expectativa_total[i] - expectativa_homem[i] for i in range(len(anos))]

# Cores para os setores
cores = ['#ff9999', '#66b3ff']

# Criar gráfico de setores para 1940
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.pie([expectativa_homem[0], expectativa_mulher[0]], labels=['Homem', 'Mulher'],
        autopct='%1.1f%%', startangle=90, colors=cores)
plt.title(f'Expectativa de Vida ao Nascer - {anos[0]}')

# Criar gráfico de setores para 2022
plt.subplot(1, 2, 2)
plt.pie([expectativa_homem[1], expectativa_mulher[1]], labels=['Homem', 'Mulher'],
        autopct='%1.1f%%', startangle=90, colors=cores)
plt.title(f'Expectativa de Vida ao Nascer - {anos[1]}')

# Ajustar o layout e mostrar o gráfico
plt.tight_layout()
plt.show()
