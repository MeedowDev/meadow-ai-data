import rasterio
import numpy as np


def validate_raster(file_path):
    with rasterio.open(file_path) as dataset:
        band = dataset.read(1)  # Read first band
        
        # Mask NoData values
        nodata_value = dataset.nodata
        if nodata_value is not None:
            band = np.where(band == nodata_value, np.nan, band)

        # Compute statistics
        mean_val = np.nanmean(band)
        max_val = np.nanmax(band)
        min_val = np.nanmin(band)
        std_dev = np.nanstd(band)
        nodata_count = np.sum(np.isnan(band))
        
        print(f"📌 Raster: {file_path}")
        print(f"➡️ Mean Value: {mean_val:.4f}")
        print(f"➡️ Max Value: {max_val:.4f}")
        print(f"➡️ Min Value: {min_val:.4f}")
        print(f"➡️ Standard Deviation: {std_dev:.4f}")
        print(f"➡️ NoData Count: {nodata_count}")

        # Optional: Compute histogram
        hist, bin_edges = np.histogram(band[~np.isnan(band)], bins=20)
        print("\n📊 Histogram:")
        for i in range(len(hist)):
            print(f"{bin_edges[i]:.2f} - {bin_edges[i+1]:.2f}: {hist[i]} pixels")

# Example usage
validate_raster('mean_rainfall_2013-2023-UCSB.tif')
validate_raster('mean_rainfall.tif')