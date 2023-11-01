#Binning
import statistics

def equal_frequency_binning(data, num_bins):
    sorted_data = sorted(data)
    n = len(data)
    bin_size = n // num_bins
    bins = []

    for i in range(0, n, bin_size):
         bin_values = sorted_data[i:i + bin_size]
         bins.append(bin_values)

         return bins

def bin_means_smoothing(bins):
    smoothed_bins = []

    for bin_values in bins:
            bin_mean = sum(bin_values) / len(bin_values)
            smoothed_bin = [bin_mean] * len(bin_values)
            smoothed_bins.append(smoothed_bin)

    return smoothed_bins

def bin_medians_smoothing(bins):
    smoothed_bins = []

    for bin_values in bins:
            bin_median = statistics.median(bin_values)
            smoothed_bin = [bin_median] * len(bin_values)
            smoothed_bins.append(smoothed_bin)

    return smoothed_bins

def bin_boundaries_smoothing(bins):
    smoothed_bins = []

    for bin_values in bins:
        bin_min = min(bin_values)
        bin_max = max(bin_values)
        smoothed_bin = [bin_min] * (len(bin_values) // 2) + [bin_max] * (len(bin_values) - len(bin_values) // 2)
        smoothed_bins.append(smoothed_bin)

    return smoothed_bins



data = [4, 8, 15, 21, 21, 24, 25, 28, 34]
num_bins = int(input("Enter the number of bins: "))

if num_bins <= 0:
    print("Number of bins should be greater than 0.")
else:
    bins = equal_frequency_binning(data,num_bins)
    mean_smoothed_bins = bin_means_smoothing(bins)
    median_smoothed_bins = bin_medians_smoothing(bins)
    boundary_smoothed_bins = bin_boundaries_smoothing(bins)

    print("\nOriginal Bins:")
    for i, bin_values in enumerate(bins):
        print(f"Bin {i + 1}:{bin_values}")

    print("\nSmoothed Bins by Means:")
    for i, smoothed_bin in enumerate(mean_smoothed_bins):
        print(f"Bin {i + 1}: {smoothed_bin}")

    print("\nSmoothed Bins by Medians:")
    for i, smoothed_bin in enumerate(median_smoothed_bins):
        print(f"Bin {i + 1}: {smoothed_bin}")

    print("\nSmoothed Bins by Boundaries:")
    for i, smoothed_bin in enumerate(boundary_smoothed_bins):
        print(f"Bin {i + 1}: {smoothed_bin}")
