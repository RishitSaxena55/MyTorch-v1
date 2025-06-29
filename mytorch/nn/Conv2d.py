import numpy as np
from resampling import *


class Conv2d_stride1():
    def __init__(self, in_channels, out_channels,
                 kernel_size, weight_init_fn=None, bias_init_fn=None):

        # Do not modify this method

        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size

        if weight_init_fn is None:
            self.W = np.random.normal(
                0, 1.0, (out_channels, in_channels, kernel_size, kernel_size))
        else:
            self.W = weight_init_fn(
                out_channels,
                in_channels,
                kernel_size,
                kernel_size)

        if bias_init_fn is None:
            self.b = np.zeros(out_channels)
        else:
            self.b = bias_init_fn(out_channels)

        self.dLdW = np.zeros(self.W.shape)
        self.dLdb = np.zeros(self.b.shape)

    def forward(self, A):
        """
        Argument:
            A (np.array): (batch_size, in_channels, input_height, input_width)
        Return:
            Z (np.array): (batch_size, out_channels, output_height, output_width)
        """
        self.A = A
        (batch_size, in_channels, input_height, input_width) = A.shape
        output_height = input_height - self.kernel_size + 1
        output_width = input_width - self.kernel_size + 1

        Z = np.zeros((batch_size, self.out_channels, output_height, output_width))  # TODO

        for i in range(input_width - self.kernel_size + 1):
            for j in range(input_height - self.kernel_size + 1):
                sliced_A = A[:, :, j:j + self.kernel_size, i:i + self.kernel_size]
                Z[:, :, j, i] = np.tensordot(sliced_A, self.W, ((1, 2, 3), (1, 2, 3))) + self.b[None, :]

        return Z

    def backward(self, dLdZ):
        """
        Argument:
            dLdZ (np.array): (batch_size, out_channels, output_height, output_width)
        Return:
            dLdA (np.array): (batch_size, in_channels, input_height, input_width)
        """
        (batch_size, in_channels, input_height, input_width) = self.A.shape
        (batch_size, out_channels, output_height, output_width) = dLdZ.shape

        self.dLdW = np.zeros_like(self.W)  # TODO
        for i in range(self.kernel_size):
            for j in range(self.kernel_size):
                A_slice = self.A[:, :, j:j + output_height, i:output_width]
                self.dLdW[:, :, j, i] = np.tensordot(dLdZ, A_slice, axes=([0, 2, 3], [0, 2, 3]))

        self.dLdb = np.sum(dLdZ, axis=(0, 2, 3))  # TODO

        dLdA = np.zeros_like(self.A)  # TODO
        dLdZ_padded = np.pad(dLdZ, pad_width=((0, 0), (0, 0), (self.kernel_size - 1, self.kernel_size - 1), (self.kernel_size-1, self.kernel_size-1)))
        flipped_W = np.flip(self.W, (2, 3))
        for i in range(input_width):
            for j in range(input_height):
                dLdZ_padded_slice = dLdZ_padded[:, :, j:j + self.kernel_size, i:i + self.kernel_size]
                dLdA[:, :, j, i] = np.tensordot(dLdZ_padded_slice, flipped_W, axes=([1, 2, 3], [0, 2, 3]))

        return dLdA


class Conv2d():
    def __init__(self, in_channels, out_channels, kernel_size, stride, padding=0,
                 weight_init_fn=None, bias_init_fn=None):
        # Do not modify the variable names
        self.stride = stride
        self.pad = padding

        # Initialize Conv2d() and Downsample2d() isntance
        self.conv2d_stride1 = Conv2d_stride1(in_channels, out_channels,
                                             kernel_size, weight_init_fn, bias_init_fn)  # TODO
        self.downsample2d = Downsample2d(self.stride)  # TODO

    def forward(self, A):
        """
        Argument:
            A (np.array): (batch_size, in_channels, input_height, input_width)
        Return:
            Z (np.array): (batch_size, out_channels, output_height, output_width)
        """

        # Pad the input appropriately using np.pad() function
        # TODO
        A = np.pad(A, ((0, 0), (0, 0), (self.pad, self.pad), (self.pad, self.pad)), mode="constant")

        # Call Conv2d_stride1
        # TODO
        Z = self.conv2d_stride1.forward(A)

        # downsample
        Z = self.downsample2d.forward(Z)  # TODO

        return Z

    def backward(self, dLdZ):
        """
        Argument:
            dLdZ (np.array): (batch_size, out_channels, output_height, output_width)
        Return:
            dLdA (np.array): (batch_size, in_channels, input_height, input_width)
        """

        # Call downsample1d backward
        # TODO
        dLdZ = self.downsample2d.backward(dLdZ)

        # Call Conv1d_stride1 backward
        dLdA = self.conv2d_stride1.backward(dLdZ)  # TODO

        # Unpad the gradient
        # TODO
        if self.pad:
            dLdA = dLdA[:, :, self.pad:-self.pad, self.pad:-self.pad]

        return dLdA
