# MRE-901 Deep Learning with TensorFlow

Welcome to **MRE-901 Deep Learning with TensorFlow**, a comprehensive course designed to equip you with the foundational and advanced concepts of deep learning using one of the most powerful frameworks, TensorFlow. This course covers key topics such as neural network architectures, convolutional neural networks (CNNs), recurrent neural networks (RNNs), and generative adversarial networks (GANs), along with hands-on implementation using TensorFlow and Keras. Through a blend of theoretical lessons and practical projects, you will gain proficiency in building, training, and optimizing deep learning models for real-world applications. Whether you're a beginner or an experienced practitioner, this course will enhance your skills in deploying scalable AI solutions. Join us to explore the cutting-edge advancements in deep learning and harness the power of TensorFlow for intelligent system design.

## Learning paths

[Lesson 1 Introduction to Deep Learning](Lesson_01/Readme.md)

[Lesson 2 An Introduction to TensorFlow](Lesson_02/Readme.md)


### TensorFlow Glossary

| Term | Definition | Example/Notes |
|------|------------|---------------|
| **Tensor** | Multi-dimensional array with uniform type (dtype) | `tf.constant([[1, 2], [3, 4]])` |
| **Graph** | Computational dataflow structure (nodes=operations, edges=tensors) | Optimized before execution in TF1.x |
| **Eager Execution** | Immediate operation evaluation (default in TF2.x) | Debug like regular Python code |
| **Autodiff** | Automatic differentiation via `GradientTape` | Essential for backpropagation |
| **Keras API** | High-level neural networks API | `tf.keras.Sequential()` |
| **Layer** | Processing unit transforming inputs | `Dense`, `Conv2D`, `LSTM` |
| **Activation Function** | Non-linear function applied to outputs | `ReLU`, `sigmoid`, `softmax` |
| **Loss Function** | Measures model error during training | `MSE`, `binary_crossentropy` |
| **Optimizer** | Updates weights to minimize loss | `Adam`, `SGD`, learning rate tuning |
| **Dataset API** | Efficient input pipeline for data | `.map()`, `.batch()`, `.prefetch()` |
| **TFRecord** | Binary format for efficient data storage | Optimized for large datasets |
| **Feature Columns** | Structured data preprocessing | `numeric_column`, `embedding_column` |
| **Fit** | Training method for models | `model.fit(x_train, y_train)` |
| **Callback** | Customizes training behavior | `EarlyStopping`, `ModelCheckpoint` |
| **Metric** | Performance measurement | `Accuracy`, `AUC` (not used for training) |
| **SavedModel** | Universal serialization format | `tf.saved_model.save()` |
| **TF Serving** | Production model serving system | Supports versioning |
| **TFLite** | Lightweight format for mobile | Quantization support |
| **Distribution Strategy** | Multi-GPU/TPU training API | `MirroredStrategy` |
| **TPU** | Google's custom ML accelerator | Available in Colab/Cloud |
| **XLA** | Compiler for linear algebra ops | Improves execution speed |
| **TensorBoard** | Visualization toolkit | Loss curves, histograms |
| **TFX** | Production ML pipeline platform | Includes data validation |
| **Embedding** | Learned dense representations | Word embeddings in NLP |
| **Attention** | Focus mechanism for inputs | `MultiHeadAttention` |
| **Transfer Learning** | Reusing pre-trained models | Fine-tuning `ResNet` |
| **Gradient Tape** | Records ops for autodiff | Custom training loops |
| **Profiler** | Performance analysis tool | GPU utilization metrics |
| **Mixed Precision** | Combined float16/float32 training | Faster computation |

### Key Categories

1. **Core Concepts**: Tensor, Graph, Eager Execution  
2. **Model Building**: Keras, Layers, Activations  
3. **Training**: Loss, Optimizers, Metrics  
4. **Data**: Dataset API, TFRecord  
5. **Deployment**: SavedModel, TFLite  
6. **Advanced**: TPU, XLA, Distribution Strategies


## Specialized Learning for Industry Professionals

[Deep Learning (MIT)](https://www.youtube.com/watch?v=alfdI7S6wCY&list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI)

[Introduction to Deep Learning](https://www.youtube.com/watch?v=AhE8RhPGH1A)

[Transformers, the tech behind LLMs | Deep Learning](https://www.youtube.com/watch?v=wjZofJX0v4M&t=27s)

