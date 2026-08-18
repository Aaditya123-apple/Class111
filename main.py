import statistics

from stats_utils import (
    describe,
    plot_distribution,
    read_scores,
    sampling_distribution_means,
    standard_deviation_bounds,
)

population = read_scores("maths.csv")

#plotting the graph
plot_distribution(population, "Math Scores")

#calculating the mean and standard deviation of the population data
describe(population, "population")

##  code to find the mean of 100 data points 1000 times
mean_list = sampling_distribution_means(population, sample_size=100, repetitions=1000)

## calculating mean and standard_deviation of the sampling distribution.
mean, std_deviation = describe(mean_list, "sampling distribution")

#plotting the mean of the sampling
plot_distribution(mean_list, "student marks", [("MEAN", mean)], line_height=0.20)

#finding the standard deviation starting and ending values
sd_bounds = standard_deviation_bounds(mean, std_deviation)

# comparing each sample group against the sampling distribution
for index, (csv_path, (_, sd_end)) in enumerate(
    zip(["data1.csv", "data2.csv", "data3.csv"], sd_bounds), start=1
):
    sample = read_scores(csv_path)
    mean_of_sample = statistics.mean(sample)
    print("Mean of sample" + str(index) + ":- ", mean_of_sample)
    plot_distribution(
        mean_list,
        "student marks",
        [
            ("MEAN", mean),
            ("MEAN OF SAMPLE " + str(index), mean_of_sample),
            ("STANDARD DEVIATION " + str(index) + " END", sd_end),
        ],
    )
