# lyceum-test
This is a test of the product of lyceum, a cloud computing company.

# Problems encountered
## Output streaming
When waiting for my code to compute, the process "Running" was not explicit. 

## Computing between the CPU/GPU/automatic selection (using mnist.py)
While computing the mnist.py code (copied from the "get started page")
- (SUCCESS) using the CPU was working
- (FAILED) using the GPU crashed - nvlink_path: Couldn't find a suitable version of nvlink.
- (FAILED) using the automatic selection gave a http 500 with detail "All connection attempts failed" 

While computing the image-classification.py code
- (FAILED) using the automatic selection gave a http 500 with detail "All connection attempts failed"

While computing the nlp-project.ipynb (different results !)
- (FAILED) The Notebook was running cell after cell which allows to display results properly. However, i couldn't do a "pip install" which is the basic of use of a notebook.

## Many broken links in the documentation/website
- menu bar of the main website
- doc : get started page
- doc : too many 404 redirect


# Questions
## 1. Name one feature that we should build next ?


## 2. What do you not like about the product ?


## 3. Did anything not work as you'd expect ?

