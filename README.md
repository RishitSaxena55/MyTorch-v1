# 🔦 MyTorch: A Minimal PyTorch-like Deep Learning Library

Welcome to **MyTorch**, a minimalist deep learning library implemented from scratch.

This project is designed to replicate core features of PyTorch's `nn.Module` and autograd systems, providing a hands-on understanding of how deep learning libraries work under the hood.

---

## 📁 Project Structure


- ├── hw1p1_autograder.py # Autograder to test the implementation
- ├── mytorch/
- │ ├── init.py
- │ ├── nn/
- │ │ ├── init.py
- │ │ ├── linear.py # Custom Linear Layer
- │ │ ├── activation.py # Custom ReLU, Sigmoid, etc.
- │ │ ├── loss.py # Custom CrossEntropyLoss
- │ └── util.py # Utility functions (e.g., one-hot encoder)
- └── models/
- └── mlp0.py # Example MLP model built using MyTorch
- ├── requirements.txt

---


---

## 🚀 Features Implemented

✅ Custom implementation of:
- `Linear` layer with forward and backward pass  
- `ReLU` activation function  
- `Sigmoid` activation function
- `Tanh` activation function
- `CrossEntropyLoss` and `Mean Squared Error` loss functions 
- Backpropagation using analytical gradients(`Stochastic Gradient Descent (SGD)`)
- Simple Multi-layer Perceptron (MLP) network (`MLP0`, `MLP1`, `MLP2`, `MLP4`)
- Regularization(`Batch Normalization`)
- Unit tests and autograder support  

---

## 🛠️ How to Use

1. **Clone the Repository**

```bash
git clone https://github.com/RishitSaxena55/MyTorch-v1.git
cd MyTorch-v1
