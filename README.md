# Sketch2Struct 🏗️  
**Automated Floor Plan Structural Reconstruction using Custom-Modified Sobel Filtering**

---

## 📌 Overview

**Sketch2Struct** is a computer vision–based system designed to automatically convert messy hand-drawn or digitally sketched floor plans into clean, structured architectural layouts.

The core contribution of this project is a **custom-modified Sobel operator combined with gradient-orientation modeling**, enabling robust detection, classification, and straightening of architectural wall structures. The pipeline performs noise-aware preprocessing, directional gradient extraction, orientation-based wall classification, and morphological line reconstruction to generate geometrically consistent floor plans.

This approach allows reliable **sketch-to-structure transformation**, making the system suitable for architectural digitization, indoor mapping, robotic navigation, and CAD preprocessing workflows.

---

## 🎯 Problem Statement

Hand-drawn and digital sketch floor plans typically suffer from:
- Irregular and shaky lines  
- Noise and artifacts  
- Uneven thickness  
- Broken wall segments  
- Distorted geometry  

Traditional edge detection techniques highlight raw edges but fail to preserve **structural continuity**, producing fragmented and noisy outputs unsuitable for architectural reconstruction.

**Sketch2Struct** addresses this challenge by introducing a **custom-modified Sobel-based directional filtering framework** combined with **gradient orientation modeling** and **directional morphological reconstruction**, enabling robust extraction and straightening of architectural wall structures.

---

## 🚀 Key Features

- Noise-robust preprocessing pipeline  
- **Custom-modified Sobel directional filtering**  
- Gradient orientation ratio-based wall classification  
- Direction-aware morphological line reconstruction  
- Structural wall straightening  
- Clean architectural output generation  

---

## 🔬 Key Technical Contribution

The primary innovation of Sketch2Struct lies in its **custom-modified Sobel-based directional edge detection framework**.

Instead of relying on conventional edge magnitude computation, the system:

- Separates horizontal and vertical gradient components  
- Applies **orientation ratio modeling** to identify dominant wall directions  
- Suppresses ambiguous gradient responses  
- Performs **directional morphological reconstruction** to generate continuous and straight wall segments  

This results in significantly improved **wall continuity, geometric consistency, and architectural clarity** compared to standard edge detection pipelines.

---

## 🧠 Methodology / Pipeline
