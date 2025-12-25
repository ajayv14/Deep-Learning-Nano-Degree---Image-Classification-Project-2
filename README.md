# Image Classification Project (Udacity Deep Learning Nanodegree)

**Overview**

This repository contains the Image Classification project for the Udacity Deep Learning Nanodegree. The goal is to implement and evaluate components of a convolutional neural network using TensorFlow (TF 1.x API as used in the notebooks).

## 📚 Contents

- `dlnd_image_classification .ipynb` — Jupyter notebook with project instructions and exercises
- `helper.py` — helper utilities used by the notebook
- `problem_unittests.py` — unit tests to validate your solutions

---

## ⚙️ Setup (macOS / Linux)

1. (Optional) Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install project dependencies:

```bash
pip install -r requirements.txt
```

3. Launch Jupyter and open the notebook:

```bash
jupyter notebook "dlnd_image_classification .ipynb"
```

4. Run the unit tests to verify your implementations:

```bash
python problem_unittests.py
```

---

## 🚨 Notes on TensorFlow version

This project uses TensorFlow 1.x constructs (`tf.placeholder`, `tf.Session`). To run with modern pip-installable TensorFlow, the project is now compatible with **TensorFlow 2.x** using the `tf.compat.v1` API. Install a TF 2.x release and use the compatibility shim.

Add the following at the top of your notebook or modules that use TF 1.x features:

```python
import tensorflow.compat.v1 as tf
try:
    tf.disable_v2_behavior()
except Exception:
    pass
```

If you absolutely must run with TensorFlow 1.15, consider using `conda` or Docker to obtain an older runtime (see notes below).

---

## 💡 Tips

- Work through the notebook cells sequentially.
- Use the unit tests in `problem_unittests.py` while developing — they provide quick feedback on the functions you implement.

---

## 🧾 License & Attribution

This repository contains student project code and references to Udacity materials. Use and modify for personal learning and development.

---

If you'd like, I can also add a short CONTRIBUTING section or CI configuration to run the unit tests automatically. ✅
