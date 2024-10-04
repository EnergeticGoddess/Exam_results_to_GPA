import pandas as pd
import matplotlib.pyplot as plt

# Открываем файл для чтения
with open('text.txt', 'r') as file:
    # Читаем все строки из файла и сохраняем их в список
    raw_data = file.read()

raw_data = raw_data.split('\t')
for i in range(len(raw_data)):
    if i % 10 == 1 or i % 10 == 3 or i % 10 == 4 or i % 10 == 5:
        raw_data[i] = 'k'
    if i % 10 == 6:
        raw_data[i] = raw_data[i][-2:] 

value_to_remove = 'k'
data = list(filter(lambda item:  item != value_to_remove, raw_data))

for i in range(len(data)):
    if i % 6 == 0:
        data[i] =  data[i].replace('\n', '')

chunks = [data[i:i + 6] for i in range(0, len(data), 6)]
df = pd.DataFrame(chunks, columns=[
    'id', 'Prior', 'Exam', 'IA', 'Sum', 'Avg.grade'
])
df.set_index('id', inplace=True)
df['IA'].replace('', 0, inplace=True)
df['Avg.grade'].replace('', 'NaN', inplace=True)
df['Avg.grade'] = df['Avg.grade'].replace({',': '.'}, regex=True)
print(df['Avg.grade'])
df['Exam'] = df['Exam'].astype(int)
df['IA'] = df['IA'].astype(int)
df['Sum'] = df['Sum'].astype(int)
df['Avg.grade'] = df['Avg.grade'].astype(float)

print(df)

print(df['Exam'].mean())
print(df['Exam'].mode())
print(df['Exam'].median())
print((df['Sum'] > 79).sum())
print(107/455)

hist, bin_edges = pd.cut(df['Exam'], bins=range(0, 100), include_lowest=False, right=True, retbins=True)
frequency = hist.value_counts().sort_index()
relative_frequency = frequency
filtered_bin_edges = bin_edges[:-1][relative_frequency > 0]
filtered_relative_frequency = relative_frequency[relative_frequency > 0]
plt.plot(filtered_bin_edges, filtered_relative_frequency, marker='o', linestyle='-')
plt.xticks(range(0, 100, 5)) 
plt.title('Полигон')
plt.xlabel('Результат экзамена')
plt.ylabel('Частота')
plt.show()

hist, bin_edges = pd.cut(df['IA'], bins=range(0, 50), include_lowest=True, right=True, retbins=True)
frequency = hist.value_counts().sort_index()
relative_frequency = frequency
filtered_bin_edges = bin_edges[:-1][relative_frequency > 0]
filtered_relative_frequency = relative_frequency[relative_frequency > 0]
plt.plot(filtered_bin_edges, filtered_relative_frequency, marker='o', linestyle='-')
plt.xticks(range(0, 50, 5)) 
plt.title('Полигон')
plt.xlabel('Количество ИД')
plt.ylabel('Частота')
plt.show()

print(df['IA'].mean())
print(df['IA'].median())
print((df['IA'] > 26).sum())
print(107/455)