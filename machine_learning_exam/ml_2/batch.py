def batch_split(collect: list, n: int) -> list:
    """
    n-sized batch from collect

    :param collect: list of objects
    :param n: number of batch

    :return: list of batch (list)
    """

    collect_batch = [collect[i:i + n] for i in range(0, len(collect), n)]

    return collect_batch
