# region LinearRegression
def linear_regression():
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import r2_score

    realEstate = pd.read_csv("E:/PyCharm/Practice/Datasets/bears.csv")
    X = realEstate.iloc[:, :-1].values
    y = realEstate.iloc[:, 8].values

    sns.heatmap(realEstate.corr())
    plt.show()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    regression = LinearRegression()
    regression.fit(X_train, y_train)
    y_pred = regression.predict(X_test)

    print(r2_score(y_test, y_pred))
# endregion

# region LogisticRegression



# endregion

