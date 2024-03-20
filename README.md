## FTIR Data Plotting with User-Annotated Points

This Python script allows you to plot FTIR data from a text file and interactively add user-defined annotations with labels and descriptions.

**Data File Structure:**

The script expects the data to be in a text file with the following format:

```
x_value y_value
...
```

- Each line represents a data point.
- `x_value`: The wavenumber (cm-1) on the x-axis.
- `y_value`: The intensity (a.u.) on the y-axis.

**Instructions:**

1. **Save the script as a Python file (e.g., `ftir_plot.py`).**
2. **Place your data file (e.g., `22MS140.txt`) in the same directory.**
3. **Run the script from your terminal using `python ftir_plot.py`**

**Code Breakdown:**

1. **Import libraries:**
   - `matplotlib.pyplot` is imported as `plt` for plotting functionalities.

2. **`read_data` function:**
   - This function takes the filename as input and reads the data line by line.
   - It splits each line based on whitespace (usually space or tab) and converts the first element (wavenumber) and second element (intensity) into floats.
   - Finally, it returns two lists: `x_data` containing wavenumbers and `y_data` containing intensities.

3. **Read data from the text file:**
   - The script calls the `read_data` function with the filename to get the `x_data` and `y_data` lists.

4. **User Input for Annotations:**
   - The script enters a loop to get user input for the data points they want to annotate.
   - Users can enter 'q' to quit the loop.
   - For each point, the user provides the x-coordinate and y-coordinate.
   - Optionally, the script finds the closest data point in the dataset based on the x-coordinate (commented out by default).
   - Users enter a label and a few words describing the data point for annotation.

5. **Plot the data:**
   - The script uses `plt.plot(x_data, y_data)` to create the line plot for the FTIR data.

6. **Set labels and title:**
   - The script sets informative labels for the x-axis ("Wavenumber (cm-1)"), y-axis ("Intensity (a.u.)"), and the plot title ("FTIR Data - filename").

7. **Add annotations:**
   - The loop iterates through the user-provided points and their corresponding labels and descriptions.
   - It uses `plt.annotate` to add text annotations at the specified points.
   - The annotation text includes the label, description, and data point value (x-coordinate and closest y-value, if applicable).
   - The offset is adjusted with `xytext` to position the annotation text slightly below the point for better readability.

8. **Plotting marker (optional):**
   - The script uses `plt.scatter` to plot a red circle marker at each user-specified annotated point (commented out by default).

9. **Ensure plot elements are drawn correctly:**
   - The script calls `plt.legend()` to display a legend if needed (may obscure annotations otherwise).
   - `plt.tight_layout()` adjusts the spacing between plot elements to avoid overlapping content.

10. **Show the plot with grid:**
   - The script displays the final plot with a grid using `plt.grid(True)`.
   - Additionally, it inverts the x-axis using `plt.gca().invert_xaxis()`  for typical FTIR data visualization (uncomment if needed).

**Customization:**

- You can uncomment the commented-out sections to enable features like finding the closest data point and plotting markers for annotated points.
- Feel free to modify the plot customization options like colors, markers, and labels based on your preferences.
