import random
import statistics
import sys
from pathlib import Path

import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

DATA_DIR = Path(__file__).resolve().parent
SCORE_COLUMN = "Math_score"


def load_scores(filename, column=SCORE_COLUMN):
    """Read a numeric column from a CSV file, raising a clear error on bad input."""
    path = DATA_DIR / filename
    try:
        df = pd.read_csv(path)
    except FileNotFoundError as error:
        raise FileNotFoundError(f"Data file not found: {path}") from error
    except pd.errors.EmptyDataError as error:
        raise ValueError(f"Data file is empty: {path}") from error
    except pd.errors.ParserError as error:
        raise ValueError(f"Could not parse CSV file {path}: {error}") from error

    if column not in df.columns:
        raise ValueError(
            f"Column {column!r} missing from {path}; found columns: {list(df.columns)}"
        )

    scores = pd.to_numeric(df[column], errors="coerce")
    invalid_count = int(scores.isna().sum())
    if invalid_count:
        raise ValueError(
            f"Column {column!r} in {path} has {invalid_count} non-numeric value(s)"
        )
    if len(scores) < 2:
        raise ValueError(
            f"Column {column!r} in {path} needs at least 2 values to compute "
            f"a standard deviation, found {len(scores)}"
        )
    return scores.tolist()


def random_set_of_mean(data, counter):
    """Mean of `counter` values sampled with replacement from `data`."""
    if counter < 1:
        raise ValueError(f"counter must be at least 1, got {counter}")
    if not data:
        raise ValueError("cannot sample from an empty dataset")
    dataset = [data[random.randint(0, len(data) - 1)] for _ in range(counter)]
    return statistics.mean(dataset)


def plot_sample(mean_list, population_mean, sample_mean, sd_end, sample_label):
    fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
    fig.add_trace(go.Scatter(x=[population_mean, population_mean], y=[0, 0.17], mode="lines", name="MEAN"))
    fig.add_trace(go.Scatter(x=[sample_mean, sample_mean], y=[0, 0.17], mode="lines", name=f"MEAN OF {sample_label}"))
    fig.add_trace(go.Scatter(x=[sd_end, sd_end], y=[0, 0.17], mode="lines", name=f"{sample_label} STANDARD DEVIATION END"))
    fig.show()


def main():
    population = load_scores("maths.csv")

    #plotting the graph
    fig = ff.create_distplot([population], ["Math Scores"], show_hist=False)
    fig.show()

    #calculating the mean and standard deviation of the population data
    print("mean of population:- ", statistics.mean(population))
    print("Standard deviation of population:- ", statistics.stdev(population))

    # mean of 100 data points, 1000 times
    mean_list = [random_set_of_mean(population, 100) for _ in range(1000)]

    ## calculating mean and standard_deviation of the sampling distribution.
    mean = statistics.mean(mean_list)
    std_deviation = statistics.stdev(mean_list)
    print("mean of sampling distribution:- ", mean)
    print("Standard deviation of sampling distribution:- ", std_deviation)

    #plotting the mean of the sampling
    fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.20], mode="lines", name="MEAN"))
    fig.show()

    #finding the standard deviation ending values
    first_sd_end = mean + std_deviation
    second_sd_end = mean + 2 * std_deviation
    third_sd_end = mean + 3 * std_deviation

    for index, (filename, sd_end) in enumerate(
        (("data1.csv", first_sd_end), ("data2.csv", second_sd_end), ("data3.csv", third_sd_end)),
        start=1,
    ):
        sample = load_scores(filename)
        sample_mean = statistics.mean(sample)
        print(f"Mean of sample{index}:- ", sample_mean)
        plot_sample(mean_list, mean, sample_mean, sd_end, f"SAMPLE {index}")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, statistics.StatisticsError) as error:
        print(f"error: {error}", file=sys.stderr)
        sys.exit(1)
