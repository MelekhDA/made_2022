import pandas as pd

IS_TRAIN = 'is_train'
TARGET = 'target'
RANDOM_STATE = 42


def get_full_df(
        df_train: pd.DataFrame,
        df_test: pd.DataFrame,
        key: str = IS_TRAIN
) -> pd.DataFrame:
    """
    Get full dataframe with column <key> to determine train/test

    :param df_train: the first dataframe with train data
    :param df_test: the second dataframe with train data
    :param key: name of new column

    :return: full dataframe
    """
    df_train_new, df_test_new = df_train.copy(), df_test.copy()

    df_train_new = df_train[df_test.columns]
    df_train_new[key], df_test_new[key] = 1, 0

    df = pd.concat([df_train_new, df_test_new])

    return df


def create_train_negative(
        df_train: pd.DataFrame,
        random_state: RANDOM_STATE,
        target: str = TARGET
) -> pd.DataFrame:
    """
    Create dataframe with negative sampling

    :param df_train: dataframe
    :param random_state: random_state for random operations
    :param target: column name for target

    :return: dataframe with negative sampling
    """

    print(df_train.shape)

    df_train_0 = df_train[df_train['target'] == 0]
    df_train_1 = df_train[df_train['target'] == 1]

    n = df_train_1.shape[0]
    df_train_0_neg_sample = df_train_0.sample(n, random_state=random_state)

    df_train_neg = pd.concat([df_train_0_neg_sample, df_train_1], ignore_index=True)
    df_train_neg = df_train_neg.sample(frac=1, random_state=random_state, ignore_index=True)

    print(df_train.shape, df_train_neg.shape)
    print(df_train_neg[target].value_counts())

    return df_train_neg
