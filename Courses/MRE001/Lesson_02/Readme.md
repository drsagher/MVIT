# Lesson 2 An Introduction to TensorFlow

[TensorFlow](https://www.tensorflow.org/) is an open-source, versatile deep learning framework developed by Google, designed to facilitate the development, training, and deployment of machine learning models, particularly neural networks, across a wide range of platforms and applications. Initially released in 2015, TensorFlow provides a comprehensive ecosystem for building models using high-level APIs like [**Keras**](https://keras.io/) for rapid prototyping, as well as low-level APIs for fine-grained control over neural network operations. It supports a variety of architectures, including Multi-Layer Perceptrons (MLPs), Convolutional Neural Networks (CNNs), Recurrent Neural Networks (RNNs), and Transformers, making it suitable for tasks like image classification, natural language processing, and time-series analysis. TensorFlow’s core is built around **tensors** (multi-dimensional arrays) and a **computation graph** that enables efficient execution of mathematical operations, optimized for parallel processing on GPUs and TPUs. It supports **automatic differentiation** for backpropagation, enabling gradient-based optimization techniques like Adam or Stochastic Gradient Descent. TensorFlow also offers **TensorFlow Extended (TFX)** for end-to-end MLOps pipelines, **TensorFlow Lite** for mobile and edge device deployment, and **TensorFlow Serving** for production-grade model serving. With robust support for distributed training via tools like [**Horovod**](https://horovod.ai/), cross-platform compatibility (Windows, macOS, Linux, and cloud platforms like AWS, GCP), and integration with libraries like [**NumPy**](https://numpy.org/) and [**Pandas**](https://pandas.pydata.org/), TensorFlow is widely used in academia and industry. Its active community, extensive documentation, and pre-trained models (e.g., via TensorFlow Hub) make it accessible to beginners while providing the scalability needed for enterprise-level applications.

## First Look at a Neural Network 
A neural network (NN) is a biologically inspired computational model designed to recognize patterns and make decisions based on input data. At its most basic level, a neural network consists of three fundamental components:  
1. **Input Layer** – The entry point for raw data (e.g., pixels in an image, words in a text), where each input node represents a feature.  
2. **Hidden Layers** – Intermediate layers where computation occurs, each comprising **neurons** (or nodes) that apply a weighted sum of inputs followed by a **nonlinear activation function** (e.g., ReLU, Sigmoid) to introduce complexity and enable learning.  
3. **Output Layer** – Produces the final prediction (e.g., class probabilities in classification, a continuous value in regression).  

<img src="nn2.PNG"/>

The network **learns** by adjusting weights via **backpropagation**, where errors from predictions are propagated backward, and optimization algorithms (e.g., **SGD, Adam**) minimize a **loss function** (e.g., cross-entropy, MSE). A simple **feedforward neural network (FNN)** processes data in one direction, while more advanced architectures like **CNNs** (for spatial data) and **RNNs** (for sequential data) introduce specialized layers (e.g., convolutions, recurrent cells).  

Key concepts in a first encounter include:  
- **Forward Pass**: Data flows from input to output, generating predictions.  
- **Training Loop**: Iterative weight updates using batches of data (**mini-batch gradient descent**).  
- **Overfitting Prevention**: Techniques like **dropout** and **L2 regularization**.  

Neural networks form the backbone of deep learning, enabling tasks like image recognition, machine translation, and game-playing AI. Their power lies in **hierarchical feature learning**—transforming raw input into abstract representations through successive layers.


## Data Representations for Neural Networks

Neural networks process data in structured numerical formats, requiring careful preprocessing to ensure compatibility with model architectures. The choice of representation significantly impacts learning efficiency and performance. Below are the key data types and their typical encodings:

**1. Structured Data (Tabular)**
- **Format**: Tables (CSV, DataFrames) with rows as samples and columns as features.
- **Preprocessing**:
  - **Numerical Features**: Scaled (MinMax, Standard) to normalize ranges.
  - **Categorical Features**: Encoded via one-hot or embeddings (high-cardinality).
  - **Missing Values**: Imputed (mean/median) or masked.
- **Example**: Predicting house prices from square footage, bedrooms, and location.

**2. Images**
- **Format**: Grids of pixels (height × width × channels).
  - Grayscale: 1 channel (e.g., MNIST).
  - RGB: 3 channels (e.g., CIFAR-10).
- **Preprocessing**:
  - Normalization (e.g., pixel values rescaled to [0, 1] or [-1, 1]).
  - Augmentation (rotation, flipping) for robustness.
- **Representation**: 4D tensors (batch_size × height × width × channels) for CNNs.

**3. Text**
- **Format**: Sequences of tokens (words, characters, subwords).
- **Preprocessing**:
  - **Tokenization**: Splitting text into units (e.g., BPE for GPT).
  - **Vectorization**:
    - **Bag-of-Words (BoW)**: Count-based (sparse).
    - **Embeddings**: Dense vectors (Word2Vec, GloVe, BERT).
    - **Sequence Encoding**: RNNs/Transformers use integer indices (vocabulary mapping).
- **Representation**:
  - 2D tensors (batch_size × sequence_length) for embeddings.
  - 3D for attention masks (Transformer models).

**4. Time Series/Sensor Data**
- **Format**: Ordered sequences (timestamp × features).
- **Preprocessing**:
  - Normalization (per-feature scaling).
  - Windowing (rolling windows for RNNs/CNNs).
  - Handling missing timestamps (interpolation).
- **Representation**: 3D tensors (batch_size × timesteps × features).

**5. Audio**
- **Format**: Waveforms (time-domain) or spectrograms (frequency-domain).
- **Preprocessing**:
  - **Waveforms**: Sample-rate normalization, padding/trimming.
  - **Spectrograms**: STFT/Mel-spectrograms for CNNs (2D time-frequency plots).
- **Representation**:
  - Waveforms: 2D (batch_size × samples).
  - Spectrograms: 3D (batch_size × frequency_bins × time_steps).

**6. Graph Data**
- **Format**: Nodes + edges (e.g., social networks, molecules).
- **Preprocessing**:
  - **Node Features**: Numeric attributes or embeddings.
  - **Adjacency Matrix**: Sparse/dense connectivity.
- **Representation**:
  - Graph Neural Networks (GNNs) use tuples of (node_features, edge_index).

**7. Multimodal Data**
- **Format**: Combined inputs (e.g., image + text, video + audio).
- **Preprocessing**:
  - Aligning modalities (temporal synchronization for video-audio).
  - Fusion strategies (early/late fusion, cross-attention).
- **Example**: Video captioning (frames + speech).

**Key Considerations**
- **Dimensionality**: Higher dimensions (e.g., 3D medical images) require memory-efficient representations.
- **Sparsity**: Text/graphs often use sparse formats (COO, CSR) for efficiency.
- **Normalization**: Critical for stable training (avoids exploding gradients).

**Tools for Representation**
- **Libraries**: `TensorFlow` (tf.data), `PyTorch` (Dataset), `scikit-learn` (preprocessing).
- **Embeddings**: Pretrained (BERT, ResNet) or learned end-to-end.

By tailoring data representations to the problem domain, neural networks can effectively learn hierarchical patterns, enabling state-of-the-art performance across diverse tasks.
