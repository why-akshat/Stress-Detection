Audio Based Stress Detection using DAIC-WOZ Dataset

1.	**Overview**
This machine learning model aims to detect stress levels based on input data. It utilizes various neural network architectures such as Deep Neural Networks (DNN), Convolutional Neural Networks (CNN), and Long Short-Term Memory networks (LSTM) for stress detection.

3.	**Model Architecture**
The model consists of three different architectures:
**a.	Deep Neural Network (DNN)**
i.	**Layers:**
1.	Input Layer (193 features)
2.	Dense Layer (64 units, ReLU activation)
3.	Dense Layer (32 units, ReLU activation)
4.	Output Layer (1 unit, Sigmoid activation)
**b.	Convolutional Neural Network (CNN)
i.	Layers:**
1.	Conv1D Layer (128 filters, kernel size 8, ReLU activation)
2.	MaxPooling1D Layer (pool size 2)
3.	Conv1D Layer (64 filters, kernel size 8, ReLU activation)
4.	MaxPooling1D Layer (pool size 2)
5.	Flatten Layer
6.	Output Layer (1 unit, Sigmoid activation)
**c.	Long Short-Term Memory network (LSTM)
i.	Layers:**
1.	LSTM Layer (128 units)
2.	Dense Layer (64 units, ReLU activation)
3.	Dense Layer (32 units, ReLU activation)
4.	Output Layer (1 unit, Sigmoid activation)

**3.	Usage Instructions:**
a.	Prerequisites:
i.	Python (3.x recommended)
ii.	Required libraries: TensorFlow, pandas, numpy, matplotlib, sklearn
b.	Steps:
i.	Set Up Environment:
1.	Ensure Python is installed. If not, download and install Python (3.x) from [Python's official website](https://www.python.org/downloads/).
ii.	Install Required Libraries:
1.	Open the terminal or command prompt.
2.	Navigate to the project directory.
3.	Run `pip install -r requirements.txt` to install necessary libraries.
iii.	Prepare the Data:
1.	Ensure the dataset is available or use your own dataset.
2.	Modify the file paths in the code (`data_analysis.ipynb` and `stress_detection.ipynb`) to point to your dataset if necessary.
iv.	Run Data Analysis:
1.	Open `data_analysis.ipynb` using Jupyter Notebook or any compatible IDE.
2.	Execute each cell sequentially to extract audio features from the test audio file.
v.	Run Stress Detection:
1.	Open `stress_detection.ipynb` using Jupyter Notebook or any compatible IDE.
2.	Ensure that the extracted features from the previous step are accessible to `stress_detection.ipynb`.
3.	Run each cell sequentially in `stress_detection.ipynb` to perform data preprocessing, model training, and evaluation.
vi.	Customization and Experimentation:
1.	Tweak hyperparameters, modify architectures, or adjust data preprocessing steps for experimentation and customization.

4.	Notes :
a.	The provided code in the notebooks (`data_analysis.ipynb` and `stress_detection.ipynb`) demonstrates the entire workflow from data preprocessing to model evaluation.
b.	Customization and fine-tuning of hyperparameters may be required for specific use cases.
