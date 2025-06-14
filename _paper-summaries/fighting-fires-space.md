---
title: "Fighting Fires from Space: Leveraging Vision Transformers for Enhanced Wildfire Detection and Characterization"
layout: single
author_profile: true
share: true
---

# Fighting Fires from Space: Leveraging Vision Transformers for Enhanced Wildfire Detection and Characterization

## Paper Details
- **Authors**: 
  - Aman Agarwal (Indiana University)
  - James H. Gearon (Indiana University)
  - Raksha Rank (Indiana University)
  - Etienne Chenevert (Indiana University)
- **Journal**: arXiv
- **Year**: 2025
- **DOI**: [arXiv:2504.13776](https://arxiv.org/abs/2504.13776)
- **Keywords**: CNN, Transformers, Wildfire

## Study Overview

### Research Objectives
1. Evaluate Vision Transformers (ViT) against specialized CNNs for wildfire detection
2. Implement and compare multiple deep learning architectures:
   - Traditional CNNs
   - Vision Transformers
   - UNet variants
   - Hybrid approaches

### Methods
1. **Dataset**
   - Landsat-8 Operational Land Imager (OLI) imagery
   - ~200 GB compressed data
   - 7600 × 7600 pixel resolution
   - 16-bit information
   - 11 spectral bands
   - Ground truth masks from:
     - Mathematical models
     - Manual annotation

2. **Model Architectures**
   - **Vision Transformers (ViT)**
     - Efficient training
     - Global context awareness
     - PyTorch implementation
     - NVIDIA V100 GPU

   - **Convolutional Neural Networks (CNN)**
     - Baseline comparison
     - Traditional architecture
     - PyTorch implementation

   - **UNet Variants**
     - Classic UNet:
       - Strided convolutions
       - Dilated convolutions
       - Four stages
       - Skip connections
     - Swin-Unet:
       - Shifted windows
       - Self-attention on patches
     - TransUNet:
       - ViT encoder
       - CNN fusion
       - Global context integration

3. **Training Approach**
   - AdamW optimizer
   - Dice Similarity Coefficient (DSC) loss
   - Data augmentation:
     - Random flipping
     - Rotation (50% probability)
     - Shear (20% probability)
     - Erase (20% probability)

## Key Findings

### Model Performance
1. **Vision Transformers**
   - Outperformed baseline CNN by 0.92%
   - Demonstrated potential for global context
   - Limited by pre-training on general images

2. **UNet Architecture**
   - Achieved 93.58% IoU
   - 4.58% improvement over baseline
   - Best performance in:
     - Precision
     - Intersection over Union (IoU)

3. **Comparative Analysis**
   - Swin-Unet outperformed TransUNet
   - Custom UNet exceeded all models in:
     - Precision
     - IoU metrics
   - Better than Pereira et al. (2021) models

## Impact & Applications

### Scientific Implications
- Novel comparison of ViT and CNN architectures
- Insights into model performance for remote sensing
- Understanding of:
   - Global vs. local context
   - Pre-training limitations
   - Architecture trade-offs

### Practical Applications
- Enhanced wildfire detection
- Improved early warning systems
- Better resource allocation
- More accurate fire mapping
- Real-time monitoring capabilities

## Technical Details

### Model Architecture
1. **UNet Modifications**
   - Strided convolutions for downsampling
   - Dilated convolutions (rates: 1, 1, 2, 3)
   - Four-stage architecture
   - Encoder-decoder skip connections

2. **Training Parameters**
   - Hardware: NVIDIA V100 GPU
   - Optimizer: AdamW
   - Loss Function: Dice Similarity Coefficient
   - Augmentation Strategy:
     - Flipping
     - Rotation
     - Shear
     - Erase

3. **Performance Metrics**
   - Intersection over Union (IoU)
   - Precision
   - Model comparison statistics

## Related Papers
- [Rules of River Avulsion Change Downstream](/paper-summaries/rules-of-river-avulsion/) (Gearon et al., 2024)
- [River Avulsion Precursors Encoded in Alluvial Ridge Geometry](/paper-summaries/river-avulsion-precursors/) (Gearon & Edmonds, 2025)
- [The Supply-Generated Sequence](/paper-summaries/supply-generated-sequence/) (Gearon et al., 2022)

## Further Reading
*[Note: This section can include links to related resources, datasets, or code repositories]*

## Visual Summary
*[Note: We can add key figures from the paper here, with proper attribution]*

## Key Concepts
### For Non-Specialists
- **Vision Transformer (ViT)**: A type of AI model that processes images
- **CNN**: A traditional AI model for image analysis
- **UNet**: A specific AI architecture for detailed image analysis
- **IoU**: A measure of how well the model identifies wildfires
- **Data Augmentation**: Creating variations of training data

### Technical Terms
- **AdamW**: An optimization algorithm for training AI models
- **Dice Similarity Coefficient**: A measure of model accuracy
- **Dilated Convolution**: A technique for capturing larger image areas
- **Strided Convolution**: A method for reducing image size
- **Self-attention**: A mechanism for understanding image relationships 