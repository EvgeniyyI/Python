import pandas as pd
import matplotlib.pyplot as plt


def task2():
    df = pd.read_csv('test.csv')

    df = df.sample(n=1000)

    print("Проверка данных на пропуски:")
    print(df.isnull().sum())

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    df['Rooms'].plot(kind='hist', ax=axes[0], title="Гистограмма")
    df['Rooms'].plot(kind='box', ax=axes[1], logy=True, title="Ящик с усами")
    plt.show()

    df['Rooms'].fillna(df['Rooms'].mean(), inplace=True)

    room_counts = df['Rooms'].value_counts()
    print("\nКоличество квартир в зависимости от количества комнат:")
    print(room_counts)

    pivot_table = pd.pivot_table(df, index='DistrictId', columns='Rooms', values='Id', aggfunc='count')

    df.to_csv('Ivanov.csv', index=False)


task2()
