import random
import statistics

import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go


def read_scores(csv_path, column="Math_score"):
    return pd.read_csv(csv_path)[column].tolist()


def describe(data, label):
    mean = statistics.mean(data)
    std_deviation = statistics.stdev(data)
    print("mean of " + label + ":- ", mean)
    print("Standard deviation of " + label + ":- ", std_deviation)
    return mean, std_deviation


def random_set_of_mean(data, counter):
    dataset = []
    for _ in range(0, counter):
        random_index = random.randint(0, len(data) - 1)
        dataset.append(data[random_index])
    return statistics.mean(dataset)


def sampling_distribution_means(data, sample_size=100, repetitions=1000):
    return [random_set_of_mean(data, sample_size) for _ in range(0, repetitions)]


def standard_deviation_bounds(mean, std_deviation, deviations=3):
    return [
        (mean - i * std_deviation, mean + i * std_deviation)
        for i in range(1, deviations + 1)
    ]


def plot_distribution(data, label, lines=(), line_height=0.17, show_hist=False):
    fig = ff.create_distplot([data], [label], show_hist=show_hist)
    for name, x in lines:
        fig.add_trace(
            go.Scatter(
                x=[x, x], y=[0, line_height], mode="lines", name=name
            )
        )
    fig.show()
    return fig
